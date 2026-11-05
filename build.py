"""Build a static portfolio from read-only assignment files (standard library only)."""
from __future__ import annotations

import builtins
import hashlib
import html
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tokenize
import zipfile

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent
CATALOG = json.loads((HERE / "catalog.json").read_text())
PROJECTS = CATALOG["projects"]
WEEKS = CATALOG["weeks"]
PROJECT_COUNT = len(PROJECTS)
WEEK_COUNT = len(WEEKS)
DEMO_COUNT = sum(bool(p.get("demo")) for p in PROJECTS)
esc = html.escape


def write(relative, text):
    target = HERE / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def highlight(code):
    """Tokenize Python correctly, including multiline comments and string literals."""
    lines = code.splitlines()
    parts = [[] for _ in lines]
    cursor = [0 for _ in lines]
    keywords = set("False None True and as assert async await break class continue def del elif else except finally for from global if import in is lambda nonlocal not or pass raise return try while with yield".split())
    builtins_names = set(dir(builtins))
    for token in tokenize.generate_tokens(io.StringIO(code).readline):
        category = None
        if token.type == tokenize.STRING:
            category = "string"
        elif token.type == tokenize.COMMENT:
            category = "comment"
        elif token.type == tokenize.NUMBER:
            category = "number"
        elif token.type == tokenize.NAME:
            category = "keyword" if token.string in keywords else "builtin" if token.string in builtins_names else None
        if not category:
            continue
        start, end = token.start, token.end
        for row in range(start[0] - 1, min(end[0], len(lines))):
            left = start[1] if row == start[0] - 1 else 0
            right = end[1] if row == end[0] - 1 else len(lines[row])
            parts[row].append(esc(lines[row][cursor[row]:left]))
            parts[row].append(f'<span class="tok-{category}">{esc(lines[row][left:right])}</span>')
            cursor[row] = right
    return ["".join(items) + esc(lines[row][cursor[row]:]) for row, items in enumerate(parts)]


HARNESS = '''import builtins, json, runpy, sys, time
answers = iter(json.loads(sys.argv[2]))
def sample_input(prompt=""):
    answer = next(answers)
    print(prompt + answer)
    return answer
builtins.input = sample_input
time.sleep = lambda *_args, **_kwargs: None
runpy.run_path(sys.argv[1], run_name="__main__")
'''


def sample(project):
    result = subprocess.run(
        [sys.executable, "-B", "-c", HARNESS, str(SOURCE / project["path"]), json.dumps(project["inputs"])],
        text=True, capture_output=True, timeout=5,
    )
    if result.returncode:
        raise RuntimeError(f"Sample failed for {project['path']}: {result.stderr}")
    return result.stdout.rstrip() or "[This original file produces no console output.]"


def chips(skills):
    return '<div class="tags">' + "".join(f'<span>{esc(s)}</span>' for s in skills) + '</div>'


def layout(title, description, body, base="", active=0, project=None):
    nav = "".join(
        f'<a class="week-nav {"current" if active == w["number"] else ""}" href="{base}weeks/week-{w["number"]}.html"'
        f'{" aria-current=\"page\"" if active == w["number"] else ""}>'
        f'<span class="nav-number">0{w["number"]}</span><span>Week {w["number"]}<small>{esc(w["title"])}</small></span></a>'
        for w in WEEKS
    )
    data = ''
    if project:
        payload = json.dumps(project, ensure_ascii=False).replace('<', '\\u003c')
        data = f'<script id="project-data" type="application/json">{payload}</script><script defer src="{base}assets/demos.js"></script>'
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description, quote=True)}"><meta name="color-scheme" content="light dark">
  <title>{esc(title)} · Spencer's Python Notebook</title>
  <link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{base}assets/styles.css">
  <script defer src="{base}assets/app.js"></script>{data}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<div class="site-shell">
<aside class="sidebar">
  <a class="brand" href="{base}index.html"><span class="brand-mark" aria-hidden="true">s<span>.</span></span><span>THE PYTHON<br>NOTEBOOK<small>SPENCER SMITH / CSE 110</small></span></a>
  <nav aria-label="Portfolio"><a class="overview-link {"current" if not active else ""}" href="{base}index.html">⌂ <span>The collection</span><span class="nav-count">{PROJECT_COUNT}</span></a>
  <p class="nav-label">{WEEK_COUNT} WEEKS OF BUILDING</p>{nav}</nav>
  <div class="sidebar-bottom"><p>From a first hello<br>to a little adventure.</p><a href="{base}downloads/python-assignments.zip" download>Download all Python files <span aria-hidden="true">↙</span></a></div>
</aside>
<div class="workspace">
<header class="topbar"><span><span class="status-dot"></span> A programming learning journal</span><div><span class="reading-progress" aria-live="polite">0 / {PROJECT_COUNT} explored</span><button class="theme-button" type="button" data-theme-toggle aria-label="Switch to dark theme">◐ <span>Dark mode</span></button></div></header>
<main id="main" tabindex="-1">{body}</main>
<footer class="site-footer"><p>Built one idea at a time.<br><span>Spencer Smith · CSE 110 · Weeks 01–{WEEK_COUNT:02d}</span></p><a href="{base}index.html">Back to the collection <span aria-hidden="true">↗</span></a></footer>
</div></div>
<div class="toast" role="status" aria-live="polite"></div>
</body></html>'''


def card(p, base="", compact=False):
    skills = " ".join(p["skills"])
    mode = "Interactive" if p.get("demo") else "Source notes"
    return f'''<article class="project-card {"compact" if compact else ""}" data-project-id="{p['id']}" data-week="{p['week']}" data-kind="{p['kind']}" data-search="{esc((p['title']+' '+p['summary']+' '+skills+' '+p['path']).lower(), quote=True)}">
<div class="card-meta"><span>W{p['week']:02d} <span class="meta-divider">/</span> {p['kind']}</span><span class="read-indicator" aria-label="Not yet explored">○</span></div>
<h3><a href="{base}projects/{p['id']}.html">{esc(p['title'])}</a></h3><p>{esc(p['summary'])}</p>
{chips(p['skills'][:3])}<div class="card-bottom"><span><span class="mini-dot"></span>{mode}</span><a href="{base}projects/{p['id']}.html" aria-label="Explore {esc(p['title'], quote=True)}">Explore <span aria-hidden="true">↗</span></a></div></article>'''


def home():
    featured = [next(p for p in PROJECTS if p['id'] == i) for i in ['week7-prove', 'week6-provept2', 'week3-prove']]
    f_cards = ''
    arts = [
        '<div class="feature-art word-art" aria-hidden="true"><span class="tiny-label">ONE WORD. A FEW GOOD GUESSES.</span><div class="letter-row"><span>M</span><span>_</span><span>_</span><span>I</span><span>_</span><span>_</span></div><span class="art-foot">while guess != secret_word:</span></div>',
        '<div class="feature-art forest-art" aria-hidden="true"><span class="tiny-label">WHISPERING WOODS / FIELD NOTES</span><div class="forest-scene"><i></i><i></i><i></i><span>✦</span><i></i><i></i></div><span class="art-foot">Pack a bag. Pick a friend. Find Eevee.</span></div>',
        '<div class="feature-art receipt-art" aria-hidden="true"><span class="tiny-label">THE EVERYDAY MATH DEPARTMENT</span><div class="receipt"><span>2 × CHILD\u2002$10.00</span><span>2 × ADULT\u2002$20.00</span><span>4 × DRINK\u2002$8.00</span><strong>TOTAL\u2002$40.28</strong></div></div>'
    ]
    for p, art in zip(featured, arts):
        f_cards += f'<a class="feature-card" href="projects/{p["id"]}.html">{art}<div class="feature-info"><span class="eyebrow">WEEK 0{p["week"]} / FEATURED PROJECT</span><h3>{esc(p["title"])}</h3><p>{esc(p["summary"])}</p><span class="feature-cta">Take a look <span aria-hidden="true">↗</span></span></div></a>'
    week_options = ''.join(f'<option value="{w["number"]}">Week {w["number"]}</option>' for w in WEEKS)
    cards = ''.join(card(p) for p in PROJECTS)
    body = f'''<section class="hero"><div><p class="eyebrow">A COLLECTION OF SMALL DISCOVERIES</p><h1>Small programs.<br><em>Bigger possibilities.</em></h1><p class="hero-description">{WEEK_COUNT} weeks of learning Python, from a first line of code to stories, calculators, and games. Come see how each idea works.</p><div class="hero-actions"><a class="button primary" href="#collection">Explore the assignments <span aria-hidden="true">↓</span></a><button class="text-button" type="button" data-surprise>Surprise me ↗</button></div><div class="hero-stats"><span><strong>{WEEK_COUNT:02d}</strong> weeks of learning</span><span><strong>{PROJECT_COUNT}</strong> original Python files</span><span><strong>{DEMO_COUNT}</strong> browser explorations</span></div></div><div class="hero-note"><span class="note-pin" aria-hidden="true"></span><p class="handwritten">It starts with a question.</p><div class="mini-terminal"><div><i></i><i></i><i></i><span>hello.py</span></div><pre><span class="tok-builtin">name</span> = <span class="tok-builtin">input</span>(<span class="tok-string">"Your name? "</span>)
<span class="tok-builtin">print</span>(<span class="tok-string">f"Hello, {{name}}!"</span>)

<span class="terminal-comment"># A little input. A little possibility.</span></pre></div><p class="note-caption">Read it. Try it. See what changes.</p></div></section>
<section class="featured-section" aria-labelledby="featured-heading"><div class="section-heading"><div><p class="eyebrow">A FEW GOOD PLACES TO START</p><h2 id="featured-heading">Made to be explored.</h2></div><p>Play a game. Change a number.<br>Find the code behind it.</p></div><div class="featured-grid">{f_cards}</div></section>
<section class="collection-section" id="collection" aria-labelledby="collection-heading"><div class="section-heading"><div><p class="eyebrow">THE COMPLETE NOTEBOOK</p><h2 id="collection-heading">One week at a time.</h2></div><a class="subtle-link" href="downloads/python-assignments.zip" download>All original files ↙</a></div>
<div class="filter-bar"><label class="search-field"><span aria-hidden="true">⌕</span><span class="sr-only">Search assignments by name, skill, or filename</span><input id="search" type="search" placeholder="Search a project, a skill, an idea…" autocomplete="off"></label><label><span class="sr-only">Filter by week</span><select id="week-filter"><option value="">Every week</option>{week_options}</select></label><label><span class="sr-only">Filter by assignment type</span><select id="kind-filter"><option value="">Every type</option><option>Prepare</option><option>Prove</option><option>Teach</option><option>Practice</option><option>Lesson</option></select></label></div>
<div class="collection-meta"><p id="result-count" role="status">{PROJECT_COUNT} assignments to explore</p><button type="button" class="text-button" id="clear-filters">Reset filters</button></div>
<div class="project-grid">{cards}</div><div class="empty-state" hidden><span aria-hidden="true">⌕</span><h3>No matching pages yet.</h3><p>Try a broader word, another week, or reset your filters.</p></div></section>
<section class="about-strip"><div class="about-monogram" aria-hidden="true">SS</div><div><p class="eyebrow">ABOUT THIS COLLECTION</p><h2>A record of learning, as it happened.</h2><p>These are my CSE 110 assignments, including the small exercises, class notes, and work in progress. Each page explains the idea, shows a real sample run, and keeps the original Python close by.</p></div><a class="subtle-link" href="weeks/week-1.html">Start at the beginning ↗</a></section>'''
    write('index.html', layout('The collection', f'Explore Spencer Smith’s {PROJECT_COUNT} Python assignments from CSE 110 Weeks 1–{WEEK_COUNT}, with explanations, original source, and interactive browser demos.', body))


def week_page(w):
    n = w['number']
    projects = [p for p in PROJECTS if p['week'] == n]
    previous = f'<a href="week-{n-1}.html">← Week {n-1}</a>' if n > 1 else '<a href="../index.html">← The collection</a>'
    following = f'<a href="week-{n+1}.html">Week {n+1} →</a>' if n < 7 else '<a href="../index.html">The collection →</a>'
    body = f'''<div class="breadcrumbs"><a href="../index.html">The collection</a><span>/</span><span>Week {n}</span></div><section class="week-hero"><p class="eyebrow">CHAPTER 0{n} / {len(projects)} PYTHON FILES</p><h1>{esc(w['title'])}<span class="heading-dot">.</span></h1><p class="hero-description">{esc(w['summary'])}</p>{chips(w['concepts'])}</section><div class="section-heading"><h2>Inside this week</h2><span class="muted">Small steps, real programs.</span></div><div class="project-grid week-projects">{''.join(card(p, '../') for p in projects)}</div><nav class="page-pagination" aria-label="Weeks">{previous}{following}</nav>'''
    write(f'weeks/week-{n}.html', layout(f'Week {n}: {w["title"]}', w['summary'], body, '../', n))


def project_page(p):
    code = p['source']
    lines = highlight(code)
    important = next((i for i, line in enumerate(code.splitlines(), 1) if p['highlight'] in line), 1)
    line_html = ''.join(f'<span class="code-line {"important-line" if i == important else ""}" id="line-{i}"><span class="line-number" aria-hidden="true">{i}</span><span class="line-text">{line or " "}</span></span>' for i, line in enumerate(lines, 1))
    steps = ''.join(f'<li><span class="step-number">0{i}</span><div><h3>{esc(title)}</h3><p>{esc(text)}</p></div></li>' for i, (title,text) in enumerate(p['steps'], 1))
    demo = '<div id="demo-root"><p class="muted">Loading the browser exploration…</p></div><noscript><p>Enable JavaScript to try the interactive version. The sample run, explanation, and Python code below are available without it.</p></noscript>' if p.get('demo') else f'<div class="notes-only"><span aria-hidden="true">{{ }}</span><h3>Original source, ready to run.</h3><p>{esc(p["note"])}</p></div>'
    example = esc(p['sample'])
    index = PROJECTS.index(p)
    previous = f'<a href="{PROJECTS[index-1]["id"]}.html">← {esc(PROJECTS[index-1]["title"])}</a>' if index else '<a href="../index.html">← The collection</a>'
    following = f'<a href="{PROJECTS[index+1]["id"]}.html">{esc(PROJECTS[index+1]["title"])} →</a>' if index+1 < len(PROJECTS) else '<a href="../index.html">The collection →</a>'
    extra = '<a class="button secondary" href="../games/rescue-eevee/index.html" target="_blank" rel="noopener">Open illustrated game ↗</a>' if p['demo'] == 'eevee' else ''
    body = f'''<div class="breadcrumbs"><a href="../index.html">The collection</a><span>/</span><a href="../weeks/week-{p['week']}.html">Week {p['week']}</a><span>/</span><span>{esc(p['kind'])}</span></div>
<section class="project-hero"><p class="eyebrow">WEEK 0{p['week']} / {p['kind'].upper()}</p><h1>{esc(p['title'])}</h1><p class="hero-description">{esc(p['summary'])}</p>{chips(p['skills'])}</section>
<nav class="project-jumps" aria-label="On this project page"><a href="#try">Try it</a><a href="#example">Sample run</a><a href="#how">How it works</a><a href="#source">Python code</a></nav>
<div class="project-layout"><div class="project-content"><section class="demo-section" id="try"><div class="section-heading"><div><p class="eyebrow">GET A FEEL FOR IT</p><h2>{'Try it for yourself.' if p.get('demo') else 'A work in progress.'}</h2></div>{extra}</div>{demo}</section>
<section class="detail-section" id="example"><p class="eyebrow">STRAIGHT FROM THE PYTHON FILE</p><h2>A real sample run.</h2><p class="section-intro">Recorded from the original program. Answers are shown alongside the prompts.</p><div class="output-window"><div class="window-bar"><span><i></i><i></i><i></i></span><span>{esc(p['path'])}</span><span>PYTHON</span></div><pre class="sample-output" tabindex="0" aria-label="Original Python sample output">{example}</pre></div><details class="input-details"><summary>{len(p['inputs'])} sample input{'s' if len(p['inputs']) != 1 else ''}, in order</summary><ol>{''.join(f'<li><code>{esc(a)}</code></li>' for a in p['inputs']) or '<li>This program does not ask for input.</li>'}</ol></details></section>
<section class="detail-section" id="how"><p class="eyebrow">THE IDEA BEHIND THE INTERACTION</p><h2>How it works.</h2><ol class="walkthrough">{steps}</ol><div class="code-insight"><span class="eyebrow">LOOK CLOSER / LINE {important}</span><code>{esc(code.splitlines()[important-1].strip())}</code><p>{esc(p['explanation'])}</p><a href="#source" data-open-source>Find it in the code ↓</a></div></section>
<section class="detail-section"><details class="source-details" id="source"><summary><span><span class="eyebrow">THE ORIGINAL, LINE BY LINE</span><span class="source-title">Read the Python code</span></span><span class="source-line-count">{len(lines)} lines <span aria-hidden="true">＋</span></span></summary><div class="source-toolbar"><span>{esc(p['path'])}</span><div><button type="button" class="text-button" data-copy-code>Copy code</button><a href="../source/{p['path']}" download>Download .py ↙</a></div></div><pre class="code-view" tabindex="0" aria-label="Python source code"><code>{line_html}</code></pre></details></section></div>
<aside class="project-facts"><span class="eyebrow">IN THIS NOTEBOOK</span><h2>One small idea.<br>Something to build on.</h2><dl><dt>Week</dt><dd>0{p['week']}</dd><dt>Assignment</dt><dd>{esc(p['kind'])}</dd><dt>Original file</dt><dd><code>{esc(p['path'])}</code></dd><dt>Language</dt><dd>Python</dd></dl><div class="project-note"><span class="eyebrow">A NOTE AS YOU EXPLORE</span><p>{esc(p['note'])}</p></div><button type="button" class="button secondary read-button" data-mark-read="{p['id']}" aria-pressed="false">○ Mark as explored</button><p class="storage-note">Your checklist stays in this browser.</p></aside></div>
<nav class="page-pagination" aria-label="Assignments">{previous}{following}</nav>'''
    payload = {key:p[key] for key in ['id','demo','title','week','inputs','source','note']}
    write(f'projects/{p["id"]}.html', layout(p['title'], p['summary'], body, '../', p['week'], payload))


def main():
    expected = {p['path'] for p in PROJECTS}
    assert len(expected) == len(PROJECTS) and all((SOURCE / path).is_file() for path in expected), 'Catalog paths must be unique and point to source files.'
    assert len({p['id'] for p in PROJECTS}) == len(PROJECTS)
    manifest = {}
    for p in PROJECTS:
        source = SOURCE / p['path']
        original = source.read_bytes()
        p['week'] = int(p['path'][4])
        p['source'] = original.decode('utf-8').replace('\r\n', '\n')
        p['sample'] = sample(p)
        target = HERE / 'source' / p['path']
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        manifest[p['path']] = hashlib.sha256(original).hexdigest()
    shutil.copytree(SOURCE / 'week6/browser-game/dist', HERE / 'games/rescue-eevee', dirs_exist_ok=True)
    # This small banner is added to the COPY only; original game assets stay untouched.
    game = HERE / 'games/rescue-eevee/index.html'
    content = game.read_text()
    content = content.replace('<body>', '<body><a href="../../projects/week6-provept2.html" style="display:block;padding:12px 24px;background:#173c2e;color:#fff;font:600 14px system-ui;text-decoration:none">← Back to Spencer’s Python Notebook</a>', 1)
    game.write_text(content)
    home()
    for w in WEEKS:
        week_page(w)
    for p in PROJECTS:
        project_page(p)
    (HERE / 'downloads').mkdir(exist_ok=True)
    with zipfile.ZipFile(HERE / 'downloads/python-assignments.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        for p in PROJECTS:
            archive.write(SOURCE / p['path'], p['path'])
    write('source-manifest.json', json.dumps(manifest, indent=2) + '\n')
    # Confirm generation has not changed any original assignment.
    for path, checksum in manifest.items():
        assert hashlib.sha256((SOURCE / path).read_bytes()).hexdigest() == checksum
    print(f'Built 1 collection, {len(WEEKS)} week pages, {len(PROJECTS)} project pages, and a copied illustrated game.')
    print(f'Open: {HERE / "index.html"}')


if __name__ == '__main__':
    main()
