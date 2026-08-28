# -*- coding: utf-8 -*-
"""O mapa da escada, em SVG — gerado, nunca desenhado à mão.

Regras aplicadas, com o parágrafo da norma que as manda (norma-de-diagramas.md
da Hipátia, estado PROPOSTA):

  §1.1  Cruzamento de aresta é o defeito nº 1, e ganha de qualquer outra regra
        desta norma. Este layout tem ZERO cruzamentos, e o `conferir_mapa.py`
        mede isso — não é promessa, é portão.
  §1.2  Direção declarada UMA vez e não misturada: aqui é de baixo para cima.
        O eletroímã é o chão; a máquina é o topo. (A página antiga dizia "de
        baixo para cima" no título e renderizava de cima para baixo.)
  §1.3  Teto de cinco formas, e forma só entra com significado atribuído. Aqui
        usa-se UMA forma para todos os nós: o que distingue é a cor, e o
        argumento da própria §1.3 é que vocabulário menor é menos coisa para o
        leitor decorar antes de ler.
  §1.4  O rótulo mora DENTRO do nó.
  §2    A cor carrega domínio (o regime do degrau), e por isso a CHAVE vai na
        mesma tela — sem ela a cor vira enfeite. A norma é explícita: "cor
        semântica exige a chave na mesma tela".
  §4    SVG com `width:100%` escala pela largura e, em tela baixa, corta os
        dois extremos em silêncio. Daí o `max-height` em vh no CSS, e a medida
        em mais de uma resolução.

O que a cor diz (o regime), e é a tese da escada desenhada:
  física        — ainda é eletricidade e ferro
  combinacional — a saída depende só das entradas DE AGORA
  sequencial    — a saída depende também do que veio ANTES (o degrau que lembra)
  arquitetura   — peças em sequência sob um controlador

A régua horizontal entre o nível 0 e o 1 é a afirmação mais forte do mapa: é
onde o assunto deixa de ser eletricidade e passa a ser lógica. Ela é desenhada
porque é conteúdo, não enfeite.
"""
import degraus as D

# --- geometria --------------------------------------------------------------
LARG, NO_W, NO_H = 1090, 200, 56
FAIXA = {"L": 200, "C": 470, "R": 740}
LINHA = 104          # altura de um nível
TOPO  = 196          # y do nível 5 (abaixo da fronteira de cima)

def y_de(nivel):     # nível 5 no topo, -1 embaixo — §1.2, direção declarada
    return TOPO + (5 - nivel) * LINHA

# faixa horizontal de cada degrau, escolhida para não cruzar nenhuma aresta
COLUNA = {
    "eletroima": "C", "rele": "C", "porta": "C",
    "somador": "L", "flipflop": "R", "flipflop_b": "R",
    "registrador": "C", "contador": "R", "maquina": "C",
}
REGIME = {
    "eletroima": "fisica", "rele": "fisica",
    "porta": "comb", "somador": "comb",
    "flipflop": "seq", "flipflop_b": "seq", "contador": "seq",
    "registrador": "seq", "maquina": "arq",
}
COR = {
    "fisica": ("#3a2418", "#c1704f", "#e6b499"),
    "comb":   ("#14263f", "#5b8fc9", "#bcd4ec"),
    "seq":    ("#10312e", "#4fb3a5", "#a8e0d7"),
    "arq":    ("#33280f", "#c9a266", "#f0dcb4"),
}
NOME_REGIME = {
    "fisica": "física — ainda é eletricidade e ferro",
    "comb":   "combinacional — a saída depende só das entradas de agora",
    "seq":    "sequencial — a saída depende também do que veio antes",
    "arq":    "arquitetura — peças em sequência, sob um controlador",
}

# fronteira: o que se sabe que existe e ninguém leu. Desenhada, não escondida.
FRONTEIRA_CIMA = [
    ("sistema operacional", "L"), ("instrução", "C"), ("assembler", "R"),
]
FRONTEIRA_ULA  = ("ULA", "L")          # acima do somador
FRONTEIRA_RAM  = ("memória (RAM)", "C") # ao lado do registrador... ver abaixo
FRONTEIRA_BAIXO = ("corrente e ferro", "C")

def _no(x, y, rot, nivel, regime, alvo):
    fundo, borda, texto = COR[regime]
    x0, y0 = x - NO_W // 2, y - NO_H // 2
    linhas = _quebrar(rot)
    dy = -5 if len(linhas) > 1 else 5
    tspans = "".join(
        f'<tspan x="{x}" dy="{0 if i == 0 else 17}">{l}</tspan>'
        for i, l in enumerate(linhas))
    return f'''<a href="#{alvo}" class="no">
<rect x="{x0}" y="{y0}" width="{NO_W}" height="{NO_H}" rx="7"
      fill="{fundo}" stroke="{borda}" stroke-width="1.6"/>
<text x="{x}" y="{y + dy}" text-anchor="middle" fill="{texto}"
      font-family="Cormorant,Georgia,serif" font-size="17.5">{tspans}</text>
<text x="{x0 + 9}" y="{y0 + 15}" fill="{borda}" font-family="Inter,sans-serif"
      font-size="10" opacity=".75">{nivel}</text>
</a>'''

def _fantasma(x, y, rot):
    x0, y0 = x - NO_W // 2, y - 21
    return (f'<rect x="{x0}" y="{y0}" width="{NO_W}" height="42" rx="7" '
            f'fill="none" stroke="#33465f" stroke-width="1.3" '
            f'stroke-dasharray="5 4"/>'
            f'<text x="{x}" y="{y + 5}" text-anchor="middle" fill="#6b7a90" '
            f'font-family="Inter,sans-serif" font-size="12.5">{rot}</text>')

def _quebrar(rot):
    if len(rot) <= 22: return [rot]
    p = rot.split()
    meio = len(rot) // 2; melhor, corte = 1e9, 1
    for i in range(1, len(p)):
        d = abs(len(" ".join(p[:i])) - meio)
        if d < melhor: melhor, corte = d, i
    return [" ".join(p[:corte]), " ".join(p[corte:])]

def _aresta(de, para, lida=True, dupla=False):
    """Sobe do topo do nó de baixo até a base do nó de cima."""
    x1, y1 = FAIXA[COLUNA[de]], y_de(_niv(de)) - NO_H // 2
    x2, y2 = FAIXA[COLUNA[para]], y_de(_niv(para)) + NO_H // 2
    cor = "#6fbf6a" if lida else "#33465f"
    tra = '' if lida else ' stroke-dasharray="5 4"'
    if abs(_niv(para) - _niv(de)) > 1 and x1 != x2:
        # A que pula nível: arco por FORA. A folga NÃO é chutada — é a borda
        # direita do nó mais largo desta faixa mais uma margem, senão o arco
        # raspa a caixa de quem está no meio do caminho. Foi o que aconteceu
        # na 1ª versão, e quem viu foi o conferir_mapa.py, não eu.
        cx = max(x1, x2) + NO_W // 2 + 130
        d = f"M{x1},{y1} C{cx},{y1 - 30} {cx},{y2 + 30} {x2},{y2}"
    elif x1 == x2:
        d = f"M{x1},{y1} L{x2},{y2}"
    else:
        my = (y1 + y2) / 2
        d = f"M{x1},{y1} C{x1},{my} {x2},{my} {x2},{y2}"
    saida = (f'<path d="{d}" fill="none" stroke="{cor}" stroke-width="1.7"{tra} '
             f'marker-end="url(#ponta{"" if lida else "F"})"/>')
    if dupla:  # segunda testemunha: duas fontes independentes sustentam a seta
        saida += (f'<path d="{d}" fill="none" stroke="{cor}" stroke-width="4.6" '
                  f'opacity=".22"/>')
    return saida

_NIV = {d[0]: d[2] for d in D.DEGRAUS}
_ROT = {d[0]: d[1] for d in D.DEGRAUS}
def _niv(k): return _NIV[k]


def desenhar():
    ybase_chave = y_de(-1) + LINHA + 44
    alt = ybase_chave + 46   # a chave TERMINA dentro do quadro
    p = []
    p.append(f'<svg viewBox="0 0 {LARG} {alt}" xmlns="http://www.w3.org/2000/svg" '
             f'role="img" aria-label="Mapa da escada de abstrações, do eletroímã '
             f'à máquina de registradores">')
    p.append('''<defs>
<marker id="ponta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6"
        markerHeight="6" orient="auto-start-reverse">
  <path d="M0,1 L9,5 L0,9 z" fill="#6fbf6a"/></marker>
<marker id="pontaF" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6"
        markerHeight="6" orient="auto-start-reverse">
  <path d="M0,1 L9,5 L0,9 z" fill="#33465f"/></marker>
</defs>''')

    # --- a régua: onde o assunto deixa de ser eletricidade -------------------
    yr = (y_de(1) + y_de(0)) / 2
    p.append(f'<line x1="46" y1="{yr}" x2="{LARG-46}" y2="{yr}" stroke="#c9a266" '
             f'stroke-width="1" stroke-dasharray="2 5" opacity=".65"/>')
    p.append(f'<text x="{LARG-50}" y="{yr-9}" text-anchor="end" fill="#c9a266" '
             f'font-family="Inter,sans-serif" font-size="11.5" opacity=".9">'
             f'daqui para cima o assunto é lógica, não eletricidade</text>')

    # --- fronteira de cima: a estrada continua ------------------------------
    for rot, col in FRONTEIRA_CIMA:
        p.append(_fantasma(FAIXA[col], 74, rot))
    p.append(f'<text x="50" y="30" fill="#6b7a90" font-family="Inter,sans-serif" '
             f'font-size="11.5">não lido — a estrada continua, e o mapa não '
             f'esconde isso</text>')
    xm, ym = FAIXA["C"], y_de(5) - NO_H // 2
    for col in ("L", "C", "R"):
        xd, yd = FAIXA[col], 74 + 21 + 8
        d = (f"M{xm},{ym} L{xd},{yd}" if col == "C"
             else f"M{xm},{ym} C{xm},{ym-40} {xd},{yd+44} {xd},{yd}")
        p.append(f'<path d="{d}" fill="none" stroke="#33465f" stroke-width="1.4" '
                 f'stroke-dasharray="5 4" marker-end="url(#pontaF)"/>')
    # ULA sobre o somador, RAM sobre o registrador: as duas pontas que a
    # bibliografia sustenta e ninguém abriu
    p.append(_fantasma(FAIXA["L"], y_de(3), "ULA"))
    p.append(f'<path d="M{FAIXA["L"]},{y_de(2)-NO_H//2} L{FAIXA["L"]},{y_de(3)+21}" '
             f'fill="none" stroke="#33465f" stroke-width="1.4" '
             f'stroke-dasharray="5 4" marker-end="url(#pontaF)"/>')
    p.append(_fantasma(FAIXA["C"], y_de(-1) + LINHA, "corrente e ferro"))
    p.append(f'<path d="M{FAIXA["C"]},{y_de(-1)+LINHA-21} L{FAIXA["C"]},'
             f'{y_de(-1)+NO_H//2}" fill="none" stroke="#33465f" stroke-width="1.4" '
             f'stroke-dasharray="5 4" marker-end="url(#pontaF)"/>')

    # --- arestas lidas ------------------------------------------------------
    vistas, dupla = set(), set(D.SEGUNDA_TESTEMUNHA)
    for a in D.ARESTAS:
        if (a[0], a[1]) in vistas: continue
        vistas.add((a[0], a[1]))
        p.append(_aresta(a[0], a[1], lida=True, dupla=(a[0], a[1]) in dupla))

    # --- nós ----------------------------------------------------------------
    for k, rot, niv, _diz in D.DEGRAUS:
        p.append(_no(FAIXA[COLUNA[k]], y_de(niv), rot, f"nível {niv}",
                     REGIME[k], k))

    # --- a chave, na MESMA tela (§2) ---------------------------------------
    ybase = ybase_chave
    p.append(f'<text x="50" y="{ybase}" fill="#5b6b86" '
             f'font-family="Inter,sans-serif" font-size="11.5">a cor diz o '
             f'regime · a seta cheia tem citação conferida · a tracejada é o '
             f'que ninguém leu</text>')
    x = 50
    for reg in ("fisica", "comb", "seq", "arq"):
        fundo, borda, _t = COR[reg]
        p.append(f'<rect x="{x}" y="{ybase+13}" width="13" height="13" rx="3" '
                 f'fill="{fundo}" stroke="{borda}" stroke-width="1.4"/>')
        p.append(f'<text x="{x+19}" y="{ybase+24}" fill="#8a94a4" '
                 f'font-family="Inter,sans-serif" font-size="11">'
                 f'{NOME_REGIME[reg].split(" — ")[0]}</text>')
        x += 26 + len(NOME_REGIME[reg].split(" — ")[0]) * 6.4
    p.append("</svg>")
    return "\n".join(x for x in p if x)


if __name__ == "__main__":
    print(desenhar()[:400])
