/* Browser adaptations of the course exercises. The original Python is shown separately. */
(() => {
  'use strict';
  const data = document.querySelector('#project-data');
  if (!data) return;
  const project = JSON.parse(data.textContent);
  const root = document.querySelector('#demo-root');
  if (!root) return;
  const escape = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const capitalize = value => value ? value[0].toUpperCase() + value.slice(1).toLowerCase() : '';
  const title = value => value.toLowerCase().replace(/(^|[^a-z])([a-z])/g, (_, prefix, letter) => prefix + letter.toUpperCase());
  const money = value => '$' + value.toFixed(2);
  const decimal = value => Number.isInteger(value) ? value.toFixed(1) : String(value);
  // Python rounds the exact stored float using ties-to-even. Integer arithmetic
  // avoids changing the tie when multiplying a floating-point value by 100.
  const roundMoney = value => {
    if (!Number.isFinite(value) || value === 0) return value;
    const view = new DataView(new ArrayBuffer(8));
    view.setFloat64(0, Math.abs(value));
    const bits = view.getBigUint64(0);
    const storedExponent = Number((bits >> 52n) & 0x7ffn);
    const exponent = (storedExponent || 1) - 1023 - 52;
    const fraction = bits & ((1n << 52n) - 1n);
    let numerator = (storedExponent ? (1n << 52n) + fraction : fraction) * 100n;
    let denominator = 1n;
    if (exponent < 0) denominator <<= BigInt(-exponent);
    else numerator <<= BigInt(exponent);
    let cents = numerator / denominator;
    const twiceRemainder = (numerator % denominator) * 2n;
    if (twiceRemainder > denominator || (twiceRemainder === denominator && cents % 2n !== 0n)) cents++;
    return Math.sign(value) * Number(cents) / 100;
  };
  const field = (key, label, value, type = 'text', settings = {}) => ({key,label,value,type,...settings});
  const number = (key, label, value, settings = {}) => field(key,label,value,'number',{step:'any',...settings});
  const select = (key, label, value, options) => field(key,label,value,'select',{options});
  function result({label='Result', value='', copy='', extra=''}) {
    return `<p class="result-label">${escape(label)}</p>${value !== '' ? `<div class="result-value">${escape(value)}</div>` : ''}${copy ? `<p class="result-copy">${escape(copy)}</p>` : ''}${extra}`;
  }
  function rows(items) {
    return '<dl>' + items.map(([key,value]) => `<dt>${escape(key)}</dt><dd>${escape(value)}</dd>`).join('') + '</dl>';
  }
  function formDemo(fields, calculate, options = {}) {
    const caption = options.teaching ? 'ADDED TEACHING EXPLORATION · ORIGINAL FILE BELOW' : 'BROWSER ADAPTATION · TRY DIFFERENT INPUTS';
    root.innerHTML = `<div class="demo-panel"><div class="demo-caption">${caption}</div>${options.intro ? `<p class="demo-intro">${escape(options.intro)}</p>` : ''}<form class="demo-form"><div class="demo-fields">${fields.map(f => {
      const id = 'demo-' + f.key;
      let control;
      if (f.type === 'select') {
        control = `<select id="${id}" name="${f.key}">${f.options.map(option => {
          const [value,label] = Array.isArray(option) ? option : [option,capitalize(option)];
          return `<option value="${escape(value)}" ${String(f.value) === String(value) ? 'selected' : ''}>${escape(label)}</option>`;
        }).join('')}</select>`;
      } else {
        control = `<input id="${id}" name="${f.key}" type="${f.type}" value="${escape(f.value)}" ${f.min !== undefined ? `min="${f.min}"` : ''} ${f.max !== undefined ? `max="${f.max}"` : ''} ${f.step !== undefined ? `step="${f.step}"` : ''} ${f.optional ? '' : 'required'} ${f.type === 'text' ? 'maxlength="200"' : ''}>`;
      }
      return `<label class="demo-field" for="${id}">${escape(f.label)}${control}</label>`;
    }).join('')}</div><div class="demo-actions"><button class="button primary" type="submit">${escape(options.button || 'See what happens')} <span aria-hidden="true">↗</span></button><button class="text-button" type="reset">Reset example</button></div></form><div class="demo-result" role="status" aria-live="polite" aria-atomic="true"></div></div>`;
    const form = root.querySelector('form');
    const output = root.querySelector('.demo-result');
    function draw() {
      const values = {};
      for (const f of fields) {
        const input = form.elements.namedItem(f.key);
        if (!input.validity.valid) return;
        values[f.key] = ['number','range'].includes(f.type) ? Number(input.value) : input.value;
      }
      try { output.innerHTML = calculate(values); }
      catch { output.textContent = 'These inputs cannot produce a valid result. Try the example values.'; }
    }
    form.addEventListener('submit', event => { event.preventDefault(); if (form.reportValidity()) draw(); });
    form.addEventListener('reset', () => setTimeout(draw,0));
    if (options.live) form.addEventListener('input', draw);
    draw();
  }

  function meal(withTip) {
    const fields = [
      number('childPrice',"Child's meal price ($)",5,{min:0}), number('adultPrice',"Adult's meal price ($)",10,{min:0}),
      number('drinkPrice','Drink price ($)',2,{min:0}), number('children','Children',2,{min:0,step:1}),
      number('adults','Adults',2,{min:0,step:1}), number('drinks','Drinks',4,{min:0,step:1}),
      number('tax','Sales tax (%)',6,{min:0,max:100}), number('payment','Cash payment ($)',50,{min:0})
    ];
    if (withTip) fields.splice(7,0,select('tipChoice','Add a tip?','yes',['yes','no']),number('tip','Tip amount ($)',5,{min:0}));
    formDemo(fields, v => {
      const subtotal = v.childPrice * v.children + v.adultPrice * v.adults + v.drinkPrice * v.drinks;
      const tax = roundMoney(subtotal * (v.tax / 100));
      const tip = withTip && v.tipChoice === 'yes' ? v.tip : 0;
      const total = subtotal + tax + tip;
      const change = roundMoney(v.payment - total);
      return result({label:'Your receipt', extra: rows([
        [`${v.children} × child meals`,money(v.children * v.childPrice)],
        [`${v.adults} × adult meals`,money(v.adults * v.adultPrice)],
        [`${v.drinks} × drinks`,money(v.drinks * v.drinkPrice)],
        ['Subtotal',money(subtotal)],[`Tax (${v.tax}%)`,money(tax)],...(withTip ? [['Tip',money(tip)]] : [])
      ]) + `<div class="result-total"><span>Total</span><strong>${money(total)}</strong></div><p class="result-equation">${change < 0 ? `Still owed: ${money(-change)}` : `Your change: ${money(change)}`}</p>`});
    }, {button:'Calculate the bill'});
  }

  function wordGame() {
    const secret = 'mosiah';
    let guesses = 0;
    let finished = false;
    root.innerHTML = `<div class="demo-panel"><div class="demo-caption">BROWSER ADAPTATION · THE ORIGINAL SIX-LETTER SECRET</div><div class="word-game"><span class="word-counter">0 guesses so far</span><div class="letter-row" aria-label="Six unknown letters">${Array.from(secret,() => '<span class="absent">_</span>').join('')}</div><div class="word-key"><span><i class="exact"></i>UPPERCASE: exact place</span><span><i class="elsewhere"></i>lowercase: elsewhere</span><span><i></i>_: not present</span></div><form class="guess-form"><label class="sr-only" for="word-guess">Your guess</label><input id="word-guess" name="guess" type="text" placeholder="Try a six-letter word" autocomplete="off" autocapitalize="none" spellcheck="false" maxlength="100"><button class="button primary" type="submit">Guess ↗</button></form><p class="word-status" role="status" aria-live="polite">A new word is waiting. What is your first guess?</p><ol class="guess-history" aria-label="Guess history"></ol></div><div class="demo-bottom"><span>No guess limit. Every attempt counts.</span><button class="text-button" type="button" data-restart-word>Start over ↺</button></div></div>`;
    const form = root.querySelector('form');
    const input = form.elements.guess;
    const board = root.querySelector('.letter-row');
    const status = root.querySelector('.word-status');
    const counter = root.querySelector('.word-counter');
    const history = root.querySelector('.guess-history');
    form.addEventListener('submit', event => {
      event.preventDefault();
      if (finished) return;
      const guess = input.value.toLowerCase();
      guesses++;
      counter.textContent = `${guesses} guess${guesses === 1 ? '' : 'es'} so far`;
      const item = document.createElement('li');
      const label = document.createElement('span');
      label.textContent = guess || '(empty guess)';
      item.append(label);
      if (guess.length !== secret.length) {
        status.textContent = `The guess must have ${secret.length} letters. This attempt still counts.`;
        const hint = document.createElement('span'); hint.textContent = 'Wrong length'; item.append(hint);
      } else {
        const hint = [...guess].map((letter,index) => ({
          text: letter === secret[index] ? letter.toUpperCase() : secret.includes(letter) ? letter : '_',
          kind: letter === secret[index] ? 'exact' : secret.includes(letter) ? 'elsewhere' : 'absent'
        }));
        const tiles = hint.map(({text,kind}) => `<span class="${kind}">${escape(text)}</span>`).join('');
        board.innerHTML = tiles;
        board.setAttribute('aria-label', hint.map(h => `${h.text}: ${h.kind}`).join(', '));
        const hintRow = document.createElement('span'); hintRow.innerHTML = tiles; item.append(hintRow);
        if (guess === secret) {
          finished = true;
          status.textContent = `Congratulations! You guessed it in ${guesses} guess${guesses === 1 ? '' : 'es'}.`;
          form.querySelector('button').disabled = true; input.disabled = true;
        } else status.textContent = 'Your hint is ready. Use the letters to try again.';
      }
      history.prepend(item);
      input.value = '';
      if (!finished) input.focus();
    });
    root.querySelector('[data-restart-word]').addEventListener('click', () => { wordGame(); root.querySelector('input').focus(); });
  }

  function adventure() {
    let supplies = [];
    let partner = '';
    let node = 'pack';
    const endings = {
      build:'You built the bridge and offered Eevee a safe path across! It is SAVED!!!',
      call:'You called to Eevee, causing Eevee to jump across. Eevee landed in the water soaking you both! Eevee is saved!',
      offer:'You offered Psyduck a berry. It was grateful and helped you save Eevee!',
      wait:'Psyduck waddled away. You saved Eevee, but it took much longer.',
      sneak:"You quietly rescue Eevee, and Onix doesn't notice.",
      distract:'Onix wakes up! But he is kind and helps you get Eevee safely back!',
      lower:'You use your rope to bring Eevee safely up.',
      find:'A hidden trail leads you to Eevee. You also find a rare berry tree. SCORE!!',
      lift:'You lift the branch and free Eevee, but get super muddy!',
      vine:"Bulbasaur's vine frees Eevee and reveals a buried Poke Ball.",
      cut:'You use the knife to cut Eevee free! The knife scares off Eevee. You saved it but at what cost...',
      untangle:'Untangling takes much longer, but Eevee becomes your friend!'
    };
    const scenes = {
      pikachu:['A river on the way','Do you cross the stepping stones or follow the riverbank?',[['Cross','island'],['Follow','psyduck']]],
      island:['A small island','Eevee is stranded on an island. How will you help?',[['Build a bridge','build'],['Call to Eevee','call']]],
      psyduck:['An unexpected friend','A nervous Psyduck blocks the way to Eevee.',[['Offer a berry','offer','berry'],['Wait','wait']]],
      charmander:['A light in the woods','Charmander lights up a cave entrance.',[['Enter the cave','cave'],['Climb the hill','ledge']]],
      cave:['Let sleeping Onix lie?','Eevee is hiding behind a sleeping Onix.',[['Sneak past','sneak'],['Distract Onix','distract']]],
      ledge:['A narrow ledge','Eevee needs a way back up.',[['Lower a rope','lower','rope'],['Find another route','find']]],
      bulbasaur:['Tracks in the undergrowth','Bulbasaur discovers tracks near thick bushes.',[['Track the footprints','branch'],['Search the bushes','vines']]],
      branch:['A fallen branch',"Eevee's paw is caught under a branch!",[['Lift the branch','lift'],['Use Vine','vine']]],
      vines:['A thorny problem','Eevee is tangled in thorny vines.',[['Cut the vines','cut','knife'],['Untangle them','untangle']]]
    };
    function draw() {
      let content;
      if (node === 'pack') {
        content = `<h3>Pack a little possibility.</h3><p>Choose two different supplies for the adventure.</p><div class="choice-list">${['rope','berry','knife'].map(item => `<button type="button" data-supply="${item}" aria-pressed="${supplies.includes(item)}">${capitalize(item)} <span>${supplies.includes(item) ? '✓' : '+'}</span></button>`).join('')}</div><div class="demo-actions"><button class="button primary" data-continue ${supplies.length !== 2 ? 'disabled' : ''}>Choose your partner →</button></div>`;
      } else if (node === 'partner') {
        content = '<h3>Pick a partner.</h3><p>Each friend will lead you down a different path.</p><div class="choice-list">' + ['pikachu','charmander','bulbasaur'].map(p => `<button type="button" data-partner="${p}">${capitalize(p)} <span>→</span></button>`).join('') + '</div>';
      } else if (endings[node]) {
        content = `<p class="eyebrow">RESCUE COMPLETE</p><h3>Eevee is safe.</h3><p>${escape(endings[node])}</p><p>This is the Week 5 story. Continue to Week 6 to discover nicknames, trust, and evolution.</p><a class="subtle-link" href="week6-provept2.html">Explore the expanded adventure ↗</a>`;
      } else {
        const [heading,text,choices] = scenes[node];
        content = `<h3>${escape(heading)}</h3><p>${escape(text)}</p><div class="choice-list">${choices.map(([label,next,required]) => {
          const locked = required && !supplies.includes(required);
          return `<button type="button" data-next="${next}" ${locked ? 'disabled' : ''}>${escape(label)}${locked ? ` · requires ${required}` : ''}<span>${locked ? '⊘' : '→'}</span></button>`;
        }).join('')}</div>`;
      }
      root.innerHTML = `<div class="demo-panel"><div class="demo-caption">WEEK 5 BROWSER ADAPTATION · THE FIRST RESCUE</div><div class="adventure-scene" aria-live="polite">${content}</div><div class="inventory-bar">Bag: ${escape(supplies.join(', ') || 'nothing packed yet')}${partner ? ' · Partner: ' + capitalize(partner) : ''}</div><div class="demo-bottom"><span>Earlier choices open different paths.</span><button class="text-button" type="button" data-restart-adventure>Start over ↺</button></div></div>`;
      root.querySelectorAll('[data-supply]').forEach(button => button.addEventListener('click', () => {
        const value = button.dataset.supply;
        if (supplies.includes(value)) supplies = supplies.filter(i => i !== value);
        else if (supplies.length < 2) supplies.push(value);
        draw(); root.querySelector(`[data-supply="${value}"]`).focus();
      }));
      root.querySelector('[data-continue]')?.addEventListener('click', () => { node = 'partner'; draw(); focusHeading(); });
      root.querySelectorAll('[data-partner]').forEach(button => button.addEventListener('click', () => { partner = button.dataset.partner; node = partner; draw(); focusHeading(); }));
      root.querySelectorAll('[data-next]').forEach(button => button.addEventListener('click', () => { node = button.dataset.next; if (node === 'vine') supplies.push('Poke Ball'); draw(); focusHeading(); }));
      root.querySelector('[data-restart-adventure]').addEventListener('click', () => { supplies = []; partner = ''; node = 'pack'; draw(); focusHeading(); });
    }
    function focusHeading() { const heading = root.querySelector('h3'); heading.tabIndex = -1; heading.focus({preventScroll:true}); }
    draw();
  }

  function patience() {
    let stage = 'number';
    let count = 0;
    root.innerHTML = '<div class="demo-panel"><div class="demo-caption">BROWSER ADAPTATION · TWO WHILE LOOPS</div><div class="demo-form"><p class="result-label">First: a nonnegative number</p><form class="guess-form"><label class="sr-only" for="patient-answer">Please type a positive number</label><input id="patient-answer" type="number" step="1" required value="-3"><button class="button primary" type="submit">Answer →</button></form><p class="word-status" role="status">Try a negative number first, then zero or a positive number.</p><p class="result-equation" data-loop-count>0 answers submitted</p></div><div class="demo-bottom"><span>The condition is checked after each answer.</span><button class="text-button" data-reset-patience>Start over ↺</button></div></div>';
    const form = root.querySelector('form');
    const input = form.querySelector('input');
    const label = form.querySelector('label');
    const status = root.querySelector('.word-status');
    const heading = root.querySelector('.result-label');
    form.addEventListener('submit', event => {
      event.preventDefault(); count++;
      root.querySelector('[data-loop-count]').textContent = `${count} answer${count === 1 ? '' : 's'} submitted`;
      if (stage === 'number') {
        const value = Number(input.value);
        if (value < 0) { status.textContent = 'Sorry, that is a negative number. Please try again.'; input.select(); }
        else {
          stage = 'candy'; heading.textContent = 'Next: may I have a piece of candy?';
          status.textContent = `The number is: ${value}. Now answer the candy question.`;
          input.type = 'text'; input.value = ''; input.placeholder = 'Try yes, no, or another answer';
          input.removeAttribute('required'); label.textContent = 'May I have a piece of candy?'; input.focus();
        }
      } else if (stage === 'candy') {
        if (input.value.trim().toLowerCase() === 'yes') {
          stage = 'done'; heading.textContent = 'Both loops finished'; status.textContent = 'Thank you.';
          input.disabled = true; form.querySelector('button').disabled = true;
        } else { status.textContent = 'May I have a piece of candy?'; input.value = ''; input.focus(); }
      }
    });
    root.querySelector('[data-reset-patience]').addEventListener('click', () => { patience(); root.querySelector('input').focus(); });
  }

  switch (project.demo) {
    case 'word': wordGame(); break;
    case 'adventure': adventure(); break;
    case 'patience': patience(); break;
    case 'eevee':
      root.innerHTML = '<div class="demo-panel"><div class="demo-caption">THE ILLUSTRATED BROWSER ADAPTATION</div><div class="demo-link-panel"><p class="eyebrow">WHISPERING WOODS</p><h3>A small Pokémon. A big adventure.</h3><p>Pack two supplies, name your partner, and explore the woods. Your choices shape Eevee’s trust and its final evolution.</p><p>This is a copy of the browser game already included in your coursework, with a link back to this notebook.</p><a class="button primary" href="../games/rescue-eevee/index.html">Into the woods ↗</a></div></div>';
      break;
    case 'hello':
      root.innerHTML = '<div class="demo-panel"><div class="demo-caption">BROWSER ADAPTATION · ONE LINE OF OUTPUT</div><div class="demo-form"><p class="demo-intro">A single statement can start a whole collection.</p><div class="demo-actions"><button class="button primary" data-hello>Run Hello, world ↗</button></div></div><div class="demo-result" role="status" hidden></div></div>';
      root.querySelector('[data-hello]').addEventListener('click', () => { const output = root.querySelector('.demo-result'); output.hidden = false; output.innerHTML = result({value:'Hello World!',copy:'That is the complete output of the original program.'}); });
      break;
    case 'color':
      formDemo([select('permission','May I ask a question?','yes',['yes','no']),field('color','Your favorite color','BLUE')], v => result({label:'The conversation',copy:v.permission === 'yes' ? `I also really love ${v.color.toLowerCase()}! Thank you for answering!` : 'Well then, why are you here?'}));
      break;
    case 'basics':
      formDemo([field('name','Your name','Alex'),number('favorite','Favorite whole number',7,{step:1})], v => result({label:'Variables, one step at a time',copy:`5\n10.0\nbill\n${v.name}`,extra:`<p class="result-equation">Favorite number stored as an integer: ${v.favorite}. The original does not print this value.</p>`}));
      break;
    case 'name':
      formDemo([field('first','First name','spencer'),field('last','Last name','smith')], v => result({label:'Your introduction',value:`${capitalize(v.last)}, ${capitalize(v.first)} ${capitalize(v.last)}!`,copy:`It is really nice to meet you ${capitalize(v.first)}!`}));
      break;
    case 'story':
      formDemo([field('adjective','An adjective','sparkly'),field('animal','An animal','llama'),field('verb1','A verb','dance'),field('exclamation','An exclamation','wow'),field('verb2','Another verb','laugh'),field('verb3','One more verb','sing'),field('place','A place','bakery'),field('food','A food','cookies'),field('emotion','An emotion','relieved')], v => result({label:'Your story',copy:`I was in so much trouble the other day...\nIt all started when I saw a\n${v.adjective} ${v.animal} ${v.verb1} down the hall.\n${capitalize(v.exclamation)}!!" I yelled. But all I could do was to\n${v.verb2} over and over again. Miraculously,\nthat caused it to stop, but not before it tried to ${v.verb3}\nright in front of my family.\n\nAfter this eventful evening, I ran to the nearest ${v.place}.\nI bought some ${v.food} and finally started to feel ${v.emotion}.`}),{button:'Make my story'});
      break;
    case 'badge':
      formDemo([field('first','First name','Alex'),field('last','Last name','Rivera'),field('email','Email address','ALEX@EXAMPLE.COM','email'),field('phone','Phone (10 digits)','2085550123','text'),field('job','Job title','student developer'),field('id','School ID','11027'),field('candy','Favorite candy','chocolate'),field('drink','Favorite beverage','water'),field('movie','Favorite movie','Wall-E'),field('color','Favorite color','green')], v => result({label:'Your ID card',extra:`<p class="badge-name">${escape(v.last.toUpperCase())}, ${escape(capitalize(v.first))}</p><span class="badge-role">${escape(title(v.job))} · ID: ${escape(v.id)}</span><p class="badge-contact">${escape(v.email.toLowerCase())}<br>${escape(`(${v.phone.slice(0,3)})${v.phone.slice(3,6)}-${v.phone.slice(6)}`)}</p><div class="badge-favorites">${rows([['Candy',title(v.candy)],['Beverage',title(v.drink)],['Movie',title(v.movie)],['Color',title(v.color)]])}</div>`}),{button:'Create my badge',intro:'Use fictional details to experiment. Phone formatting follows the original string slices.'});
      break;
    case 'multiply':
      formDemo([number('value','A number to multiply',2)], v => result({value:decimal(v.value * 293884955),extra:`<p class="result-equation">${v.value} × 293,884,955</p>`}));
      break;
    case 'types':
      formDemo([field('dog',"Your dog's name",'churro'),field('favorite','Favorite number as text','7')], v => {
        const numeric = Number(v.favorite);
        return result({label:'The difference a type makes',extra: rows([['Original string',v.favorite],['String × 3',v.favorite.repeat(3)],['Numeric copy',Number.isFinite(numeric) ? decimal(numeric) : 'Not a valid number']]) + `<p class="result-equation">Hi ${escape(capitalize(v.dog))}, I hear your favorite number is ${Number.isFinite(numeric) ? numeric : '(not numeric)'}.</p>`});
      });
      break;
    case 'everyday':
      formDemo([number('age','Your age',20,{min:0}),number('dozens','Dozens of eggs',2,{min:0}),number('cookies','Number of cookies',12,{min:0}),number('people','People sharing',4,{min:.000001})], v => result({label:'Everyday arithmetic',extra:rows([['Age next birthday',decimal(v.age + 1)],['Eggs in total',decimal(v.dozens * 12)],['Cookies per person',decimal(v.cookies / v.people)]])}));
      break;
    case 'meal': meal(false); break;
    case 'meal-tip': meal(true); break;
    case 'download':
      formDemo([number('size','File size (MB)',250,{min:0}),number('speed','Download speed (MB/s)',10,{min:.000001})], v => result({value:`${decimal(v.size / v.speed)} seconds`,extra:`<p class="result-equation">${v.size} MB ÷ ${v.speed} MB/s</p>`}));
      break;
    case 'arithmetic':
      formDemo([number('left','First number',5),number('right','Second number',2,{min:.000001}),select('operation','Operation','/',[['/','/ · divide'],['//','// · floor divide'],['%','% · remainder'],['*','* · multiply'],['+','+ · add']])], v => {
        const answer = {'/':() => v.left / v.right,'//':() => Math.floor(v.left / v.right),'%':() => ((v.left % v.right) + v.right) % v.right,'*':() => v.left * v.right,'+':() => v.left + v.right}[v.operation]();
        return result({label:'Expression explorer',value:answer,extra:`<p class="result-equation">${v.left} ${escape(v.operation)} ${v.right} = ${answer}</p><p class="result-copy">In the original notes: a = 15, b = 1, c = 2, d = 2.5. These values are assigned but never printed.</p>`});
      },{teaching:true});
      break;
    case 'temperature':
      formDemo([field('fahrenheit','Fahrenheit · slide to explore',68,'range',{min:-40,max:212,step:1})], v => result({label:`${v.fahrenheit}° Fahrenheit`,value:`${((v.fahrenheit - 32) * 5 / 9).toFixed(1)}° Celsius`,extra:`<p class="result-equation">(${v.fahrenheit} − 32) × 5 ÷ 9</p>`}),{live:true,button:'Convert temperature'});
      break;
    case 'velocity':
      formDemo([number('mass','Mass (kg)',80,{min:.000001}),number('gravity','Gravity (m/s²)',9.8,{min:.000001}),number('time','Time (seconds)',10,{min:0}),number('density','Fluid density (kg/m³)',1.3,{min:.000001}),number('area','Cross-sectional area (m²)',.7,{min:.000001}),number('drag','Drag coefficient',.5,{min:.000001})], v => {
        const c = .5 * v.density * v.area * v.drag;
        const velocity = Math.sqrt(v.mass * v.gravity / c) * (1 - Math.exp(-Math.sqrt(v.mass * v.gravity * c) / v.mass * v.time));
        return result({label:`Velocity after ${v.time.toFixed(1)} seconds`,value:`${velocity.toFixed(3)} m/s`,extra:`<p class="result-equation">The inner value of c is: ${c.toFixed(3)}</p>`});
      },{button:'Calculate velocity'});
      break;
    case 'formatting':
      formDemo([number('mass','Mass (kg)',10),number('acceleration','Acceleration (m/s²)',9.8),number('square','Number for the square root',81,{min:0})], v => result({label:'A few ways to show a number',extra:rows([['Force (four decimals)',`${(v.mass * v.acceleration).toFixed(4)} Newtons`],['Square root (three decimals)',Math.sqrt(v.square).toFixed(3)],['Fixed expression: 100 + 5 × 23 − 12','203.00'],['Centered with asterisks','**100.00**']])}));
      break;
    case 'compare':
      formDemo([number('first','First number',8),number('second','Second number',3),field('animal','Favorite animal',' SHEEP ')], v => result({label:'Three comparisons and one animal',copy:`The first number is ${v.first > v.second ? '' : 'not '}greater\nThe numbers are ${v.first === v.second ? '' : 'not '}equal\nThe second number is ${v.second > v.first ? '' : 'not '}greater\n\n${v.animal.trim().toLowerCase() === 'sheep' ? 'We have the same favorite animal!' : 'This is not my favorite animal...'}`}));
      break;
    case 'grade':
      formDemo([number('grade','Percentage grade',89,{min:0,max:100}),number('passing','Passing percentage',70,{min:0,max:100})], v => {
        const bands = [[93,'A'],[90,'A−'],[87,'B+'],[83,'B'],[80,'B−'],[77,'C+'],[73,'C'],[70,'C−'],[67,'D+'],[60,'D'],[-Infinity,'F']];
        const letter = bands.find(([minimum]) => v.grade >= minimum)[1];
        return result({label:'Your letter grade',value:letter,copy:v.grade >= v.passing ? 'You passed the class!' : 'You failed... :( WOMP WOMP',extra:`<p class="result-equation">${v.grade}% compared with a ${v.passing}% passing mark.</p>`});
      },{button:'Check my grade'});
      break;
    case 'decisions':
      formDemo([number('a','Value of a',2),number('b','Value of b',3)], v => result({label:'What runs?',copy:`${v.a === v.b ? 'a == b\n' : ''}\n  outside of the if now`,extra:`<p class="result-equation">a == b is ${v.a === v.b ? 'True' : 'False'}. The final unindented print always runs.</p>`}),{teaching:true});
      break;
    case 'loan':
      formDemo([number('size','Loan-size rating (1–10)',6,{min:1,max:10,step:1}),number('credit','Credit-history rating (1–10)',8,{min:1,max:10,step:1}),number('income','Income rating (1–10)',6,{min:1,max:10,step:1}),number('down','Down-payment rating (1–10)',5,{min:1,max:10,step:1})], v => {
        let yes, reason;
        if (v.size >= 5) {
          if (v.credit >= 7 && v.income >= 7) { yes = true; reason = 'Large loan: credit and income are both at least 7.'; }
          else if (v.credit >= 7 || v.income >= 7) { yes = v.down >= 5; reason = 'Large loan: one strong rating needs a down-payment rating of at least 5.'; }
          else { yes = false; reason = 'Large loan: neither credit nor income reaches 7.'; }
        } else if (v.credit < 4) { yes = false; reason = 'Small loan: credit below 4 fails the first check.'; }
        else { yes = v.income >= 7 || v.down >= 7 || (v.income >= 4 && v.down >= 4); reason = 'Small loan: income or down payment must reach 7, or both must reach 4.'; }
        return result({label:'Fictional classroom decision',value:yes ? 'Yes' : 'No',copy:reason});
      },{button:'Follow the decision tree',intro:'Use fictional ratings to explore the assignment’s conditions.'});
      break;
    case 'ride':
      formDemo([number('age1','First rider age',16,{min:0,step:1}),number('height1','First rider height (inches)',55,{min:0}),select('passport1','First rider golden passport?','no',['no','yes']),select('second','Is there a second rider?','yes',['yes','no']),number('age2','Second rider age',14,{min:0,step:1}),number('height2','Second rider height (inches)',53,{min:0}),select('passport2','Second rider golden passport?','no',['no','yes'])], v => {
        const effective = (age,passport) => age >= 12 && age <= 17 && passport === 'yes' ? 18 : age;
        const a = effective(v.age1,v.passport1), b = effective(v.age2,v.passport2);
        let can = false, reason;
        if (v.second === 'no') { can = a >= 18 && v.height1 >= 62; reason = 'A solo rider needs effective age 18+ and height 62+ inches.'; }
        else if (v.height1 < 36 || v.height2 < 36) reason = 'Both riders must be at least 36 inches tall.';
        else if (a >= 18 || b >= 18) { can = true; reason = 'Both meet the height minimum, and one has effective age 18+.'; }
        else if (a >= 12 && b >= 12 && v.height1 >= 52 && v.height2 >= 52) { can = true; reason = 'Both riders are at least 12 years old and 52 inches tall.'; }
        else { can = (a >= 16 && b >= 14) || (b >= 16 && a >= 14); reason = can ? 'One rider is at least 16 and the other at least 14; both meet the height minimum.' : 'No allowed pair combination matches these ages and heights.'; }
        return result({label:'The assignment’s ride rules',value:can ? 'Welcome to the ride!' : 'Sorry, you may not ride.',copy:reason,extra:`<p class="result-equation">Effective age${v.second === 'yes' ? 's' : ''}: ${a}${v.second === 'yes' ? ' and ' + b : ''}. Passports affect ages 12–17 only.</p>`});
      },{button:'Check these riders',intro:'Second-rider fields are used only when “Is there a second rider?” is yes.'});
      break;
    case 'boolean':
      formDemo([number('credits','Completed credits',110,{min:0,step:1}),number('gpa','GPA',2,{min:0,max:4})], v => {
        const yes = v.credits >= 120 && v.gpa > 2;
        return result({label:'Added example: completing the placeholder',value:yes ? 'True' : 'False',copy:yes ? 'Both conditions pass.' : 'Graduation needs at least 120 credits AND a GPA above 2.0.',extra:`<p class="result-equation">can_graduate = credits >= 120 and gpa > 2.0</p><p class="result-copy">The original file leaves can_graduate as None. This exploration fills in the condition described by its comments.</p>`});
      },{teaching:true,button:'Evaluate the condition'});
      break;
    default:
      root.textContent = 'Explore the recorded sample and original code below.';
  }
})();
