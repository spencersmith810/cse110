"""Check generated page links and byte-for-byte copies using the standard library."""
from hashlib import sha256
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parent


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.links = []
        self.errors = []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if 'id' in attributes:
            name = attributes['id']
            if name in self.ids:
                self.errors.append(f'{self.path.name}: duplicate ID {name}')
            self.ids.add(name)
        for attribute in ('href', 'src'):
            if attribute in attributes:
                self.links.append(attributes[attribute])


def main():
    pages = {path.resolve(): Page(path) for path in ROOT.rglob('*.html')}
    errors = [message for page in pages.values() for message in page.errors]
    checked = 0
    for path, page in pages.items():
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            destination = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not destination.is_relative_to(ROOT):
                errors.append(f'{path.name}: link escapes portfolio: {link}')
                continue
            if destination.is_dir():
                destination /= 'index.html'
            if not destination.exists():
                errors.append(f'{path.name}: missing link: {link}')
            elif url.fragment and destination in pages and unquote(url.fragment) not in pages[destination].ids:
                errors.append(f'{path.name}: missing anchor: {link}')
            checked += 1
    catalog = json.loads((ROOT / 'catalog.json').read_text())
    manifest = json.loads((ROOT / 'source-manifest.json').read_text())
    assert len(catalog['projects']) == 27
    assert len(list((ROOT / 'projects').glob('*.html'))) == 27
    assert len(list((ROOT / 'weeks').glob('*.html'))) == 7
    with zipfile.ZipFile(ROOT / 'downloads/python-assignments.zip') as archive:
        assert set(archive.namelist()) == set(manifest)
        for name, checksum in manifest.items():
            copied = (ROOT / 'source' / name).read_bytes()
            assert sha256(copied).hexdigest() == checksum, f'Changed source copy: {name}'
            assert archive.read(name) == copied, f'Archive mismatch: {name}'
            original = ROOT.parent / name
            if original.exists():
                assert original.read_bytes() == copied, f'Original mismatch: {name}'
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(pages)} HTML pages, {checked} local links and assets, 27 exact source copies, and the downloadable archive.')


if __name__ == '__main__':
    main()
