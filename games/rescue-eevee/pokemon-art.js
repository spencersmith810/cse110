// Small SVG drawings: each shape is a path, ellipse, or circle you can edit.
function pokemonArt(species) {
  const drawings = {
    pikachu: `<path d="M121 119l27-23-10-17 29-23-9 37 14 13-40 26" fill="#f5ce51"/>
      <ellipse cx="88" cy="126" rx="33" ry="36" fill="#f5ce51"/>
      <path d="M64 65Q39 12 48 8Q73 26 77 61M97 61Q108 15 125 12Q132 31 111 74" fill="#f5ce51"/>
      <path d="M48 8Q44 19 49 33L60 27Z M125 12Q114 15 110 28L125 34Z" fill="#493c34"/>
      <ellipse cx="88" cy="85" rx="40" ry="32" fill="#f5ce51"/>
      <circle cx="57" cy="95" r="8" fill="#e77e58"/><circle cx="119" cy="95" r="8" fill="#e77e58"/>
      <path d="M64 125l-10 13M111 125l10 13M66 155l-9 4M109 155l9 4"/>`,
    charmander: `<path d="M112 140Q154 153 148 102" fill="none" stroke="#dc9159" stroke-width="17"/>
      <path class="tail-flame" d="M147 111Q125 99 144 75L149 59Q169 86 162 101Z" fill="#ed8350"/>
      <path d="M148 105Q139 96 150 82Q158 95 154 103Z" fill="#ffe090" stroke="none"/>
      <ellipse cx="86" cy="126" rx="31" ry="35" fill="#df985f"/>
      <ellipse cx="86" cy="134" rx="20" ry="24" fill="#f6dba0" stroke="none"/>
      <path d="M56 129l-13 6M115 129l12 6M66 155l-11 4M104 155l10 4"/>
      <path d="M54 88Q49 44 82 43Q118 41 121 82Q124 113 88 114Q56 115 54 88Z" fill="#df985f"/>`,
    bulbasaur: `<path d="M71 91Q42 47 83 33L102 17Q105 41 130 47Q152 75 115 99Z" fill="#739663"/>
      <path d="M102 26Q91 53 101 85M75 48Q85 63 86 87M125 49Q113 68 112 87" fill="none" stroke="#4f7652"/>
      <ellipse cx="99" cy="125" rx="49" ry="29" fill="#88b5a0"/>
      <path d="M63 130v25h15l6-18M112 139l4 16h15l4-28" fill="#88b5a0"/>
      <path d="M37 87L39 58L60 72Q81 64 101 74L119 62L117 92Q127 128 80 131Q34 131 37 87Z" fill="#91bfa9"/>
      <path d="M53 80l9-4 5 11-10 4ZM95 115l10-5 6 8-10 4ZM137 118l-12-7-4 12Z" fill="#508e79" stroke="none"/>`,
    jolteon: `<path d="M110 118l24-25-3 22 25-5-22 22 15 7-32 8" fill="#efcf4e"/>
      <path d="M60 120l-8 37h17l14-24 16 24h18l-7-39Z" fill="#efcf4e"/>
      <path d="M55 103l-16 10 16 5-8 18 22-6 14 17 11-18 22 7-4-19 18-9-20-10Z" fill="#fff5d9"/>
      <path d="M58 72L34 16l28 15 14 33M99 66l24-51 13 6-20 57" fill="#efcf4e"/>
      <path d="M56 58L44 31l16 10 5 19M109 59l17-29-7 30" fill="#665044" stroke="none"/>
      <path d="M48 87l-10-7 13-8-2-15 20 9 17-12 12 12 21-6-3 17 15 10-12 12 5 13-24-2-13 12-19-11-19 2Z" fill="#f5d650"/>`,
    flareon: `<path d="M109 133Q161 146 160 107l10-11-12-3 5-18-22 5-6-12-7 20Q106 104 109 133Z" fill="#f4dca0"/>
      <ellipse cx="86" cy="132" rx="32" ry="27" fill="#d98250"/>
      <path d="M62 143l-7 16h18l8-13M100 146l3 13h17l-8-17" fill="#d98250"/>
      <path d="M56 101l-13 14 10 7-4 13 20-2 16 14 16-13 20 2-4-15 12-10-20-12Z" fill="#f4dca0"/>
      <path d="M61 73Q35 56 37 23Q68 28 75 67M99 67Q111 28 136 23Q140 54 113 77" fill="#d98250"/>
      <path d="M60 62Q46 46 46 36l20 28M108 64l20-27q1 15-14 29" fill="#665044" stroke="none"/>
      <path d="M49 88Q49 63 85 64Q121 63 122 89Q127 117 87 119Q47 117 49 88Z" fill="#e3935b"/>
      <path d="M72 66l-9-9 12-2-1-14 12 7 10-12 2 17 13 7-14 11Z" fill="#f4dca0"/>`,
    leafeon: `<path d="M110 137Q156 142 159 84Q120 88 113 117Z" fill="#83a264"/>
      <path d="M116 132l33-33" fill="none" stroke="#587e52"/>
      <ellipse cx="86" cy="131" rx="31" ry="27" fill="#e4d6ab"/>
      <path d="M61 142l-6 17h17l9-14M99 145l4 14h17l-8-17" fill="#e4d6ab"/>
      <path d="M57 151l-8-9 14 2 2 13M107 152l10-11 4 14" fill="#83a264"/>
      <path d="M61 76Q29 61 34 22Q68 26 77 66M99 68Q111 29 140 20Q144 56 112 79" fill="#83a264"/>
      <path d="M46 38l21 29M128 36l-21 32" fill="none" stroke="#587e52"/>
      <path d="M49 89Q48 64 85 65Q121 64 123 90Q125 118 87 120Q48 118 49 89Z" fill="#e4d6ab"/>
      <path d="M79 70Q69 44 93 29Q105 54 88 75Z" fill="#83a264"/>
      <path d="M84 65l7-24" fill="none" stroke="#587e52"/>
      <path d="M59 118l-13 8 20 4M109 117l17 9-18 4" fill="#83a264"/>`,
    eevee: `<path d="M112 129Q166 138 157 88Q126 87 112 112" fill="#b98559"/>
      <path d="M157 88Q163 109 151 120l-8-12-13 1Q138 91 157 88Z" fill="#f4dfb1"/>
      <ellipse cx="87" cy="133" rx="31" ry="29" fill="#b98559"/>
      <path d="M65 146l-5 13h16l6-10M100 148l3 11h15l-6-16" fill="#b98559"/>
      <path d="M53 105l-8 13 14 4 1 17 18-8 12 12 11-14 17 4-1-19-9-10Z" fill="#f4dfb1"/>
      <path d="M59 76Q28 47 36 17Q64 24 74 66M97 68Q107 27 139 17Q143 51 111 79" fill="#b98559"/>
      <path d="M60 61Q41 43 44 29Q60 37 65 61M106 62Q116 36 130 29Q130 47 112 65" fill="#665044" stroke="none"/>
      <path d="M49 87Q49 61 84 63Q117 61 123 88Q128 116 87 118Q47 116 49 87Z" fill="#bd9065"/>`
  };
  const faceY = species === 'bulbasaur' ? 99 : 86;
  return `<svg class="pokemon-drawing pokemon-${species}" viewBox="0 0 180 180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
    <ellipse cx="91" cy="166" rx="49" ry="7" fill="#244837" opacity=".12"/>
    <g class="pokemon-body" stroke="#574738" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
      ${drawings[species] || drawings.eevee}
      <g class="pokemon-eyes" fill="#352e29" stroke="none"><ellipse cx="71" cy="${faceY}" rx="5" ry="8"/><ellipse cx="103" cy="${faceY}" rx="5" ry="8"/>
      <g fill="#fff9e8"><circle cx="70" cy="${faceY - 3}" r="2"/><circle cx="102" cy="${faceY - 3}" r="2"/></g></g>
      <path d="M82 ${faceY + 9}l5 3 5-3" fill="#574738"/>
      <path d="M78 ${faceY + 17}q9 8 18 0" fill="none" stroke-width="2"/>
    </g></svg>`;
}

// This scene changes with the same state that drives the story and journal.
function pokemonScene() {
  const rescued = state.step >= 3;
  const evolution = endingEvolution();
  const companion = evolution ? evolution.toLowerCase() : 'eevee';
  const location = state.partner === 'pikachu' ? 'river' : state.partner === 'charmander' ? 'cave' : 'woods';
  return `<div class="pokemon-scene scene-${location} ${rescued ? 'is-rescued' : ''} ${evolution ? 'is-evolved' : ''}" role="img" aria-label="${escapeHTML(partnerName())} and ${evolution || 'Eevee'} ${rescued ? 'celebrating a safe rescue' : 'on the adventure'}">
    <span class="scene-sun" aria-hidden="true"></span><span class="scene-hill" aria-hidden="true"></span>
    <div class="scene-partner">${pokemonArt(state.partner)}</div><span class="scene-friendship" aria-hidden="true">${rescued ? '♥' : '✦'}</span>
    <div class="scene-eevee">${pokemonArt(companion)}</div>
    <span class="scene-caption">${evolution ? 'EEVEE EVOLVED INTO ' + evolution.toUpperCase() : rescued ? 'SAFE & SOUND · THANKS TO YOU' : 'EXPLORING WITH ' + escapeHTML(partnerName().toUpperCase())}</span></div>`;
}
