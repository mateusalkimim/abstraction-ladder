#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o index.html a partir de degraus.py, conceitos.py e mapa.py.
A página é DERIVADA — não se edita à mão.

O que esta página é, depois da reforma de 2026-08-27
----------------------------------------------------
Ela era um livro-razão de proveniência: uma pilha de cartões, cada seta abrindo
a citação que a sustenta. Honesta e rastreável, e fria — porque a unidade dela
era a CITAÇÃO, não o conceito. Media-se: 9 peças com uma linha de definição e
**33 nomeadas sem nenhuma**. Quem não sabia o que é um latch não descobria ali.

Agora ela tem três camadas, e cada uma responde a uma pergunta diferente:

  o MAPA         — onde a peça mora, e o que muda de regime quando se sobe
  os QUATRO CAMPOS — o que é · por que existe · onde aparece · onde se trava
  o INSTRUMENTO  — a aresta, conferível no navegador, sem o livro na mão

A terceira é a novidade que muda o argumento. Antes, a seta "porta lógica ←
dois relés em série" pedia que você acreditasse numa frase de um livro que você
não tem. Agora o instrumento liga os dois relés e monta a tabela-verdade na sua
frente: a citação continua, como segunda testemunha, mas deixou de ser a única
coisa que sustenta a seta.

A REGRA QUE NÃO MUDOU, e que aborta a geração
----------------------------------------------
Aresta sem citação não é desenhada — ela derruba o build. Publicar seta sem
warrant é exatamente o defeito que este mapa existe para não ter. A reforma
ampliou o alcance da regra: agora **campo sem procedência também aborta**.

Roda:  python3 gerar_escada.py
"""
import html, os, sys
import degraus as D
import conceitos as CO
import mapa as MAPA

AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(AQUI, "pt" if os.path.isdir(os.path.join(AQUI, "pt")) else "",
                     "index.html")

# Instrumento por degrau: cada um PROVA a aresta que entra naquele degrau.
INSTRUMENTOS = {
    "porta": ("rele-vira-porta", "Dois relés viram uma porta",
              "Ligue os dois e veja: <b>em série</b> a lâmpada só acende com os "
              "dois acionados — que é o E de Boole, feito de metal. A "
              "tabela-verdade não vem pronta; ela se preenche conforme você "
              "visita as combinações, e enquanto faltar linha o instrumento diz "
              "quantas faltam.",
              [("mode", "em série"), ("inA", "relé A"), ("inB", "relé B")], 230),
    "somador": ("portas-viram-conta", "Duas portas viram uma conta",
              "O XOR dá a soma, o AND dá o vai-um. A conta em binário aparece ao "
              "lado para você conferir que não é coincidência — e o caso que "
              "interessa é <b>1 + 1</b>.",
              [("inA", "A"), ("inB", "B")], 220),
    "flipflop": ("circuito-que-lembra", "O circuito que lembra",
              "Aperte <b>S</b>, solte. Aperte <b>R</b>, solte. Nos dois casos a "
              "entrada volta a ser (0,0) — e a saída é diferente. É essa a "
              "definição de lembrar, e é a coisa que nenhuma porta sozinha faz.",
              [("setS", "S — segurar"), ("setR", "R — segurar")], 240),
    "flipflop_b": ("nivel-x-borda", "Nível × borda, no mesmo relógio",
              "Os dois circuitos, o mesmo dado, o mesmo relógio. A faixa clara é "
              "o tempo em que o relógio está alto: o de <b>nível</b> copia o dado "
              "durante toda ela — ele <b>vaza</b>. O de <b>borda</b> copia só na "
              "linha pontilhada. Esta é a passagem em que quase todo mundo trava, "
              "e em prosa os dois soam iguais.",
              [("playpause", "pausar"), ("restart", "reiniciar")], 260),
    "contador": ("contagem-aparece", "A contagem aparece sozinha",
              "Dê pulsos e olhe as ondas: cada estágio vira na <b>metade</b> da "
              "frequência do anterior. Ninguém projetou a contagem binária — ela "
              "é a fiação. Se você está procurando a peça que “faz a conta”, ela "
              "não existe.",
              [("step", "um pulso"), ("autorun", "automático"), ("clear", "zerar")], 250),
}

# O valor de `data-acao` e IDENTIFICADOR e por isso e token neutro, nunca uma
# palavra que tambem aparece na tela. "reiniciar" e "zerar" eram as duas
# coisas ao mesmo tempo, e no ingles a mesma cadeia teria de ser traduzida
# como rotulo e preservada como gancho — o que nenhuma tabela resolve.
MARCA_CLASSE = {
    "a": ("citação", "lido"),
    "b": ("síntese", "lido"),
    "d": ("ofício · ratificado", "oficio"),
    # um campo de ofício SEM data de ratificação volta a ser proposta — é o que
    # torna a data uma medida e não um carimbo
    "d?": ("ofício · proposta", "oficio"),
}

CSS = """
  :root{ --fundo:#0a1424; --creme:#e8e2d6; --fraco:#5b6b86; --ouro:#c9a266;
         --cartao:#0d1c30; --borda:#1e3050; --lido:#6fbf6a; --falta:#8a94a4;
         --fisica:#c1704f; --comb:#5b8fc9; --seq:#4fb3a5; --lingua:#a883c9; }
  *{box-sizing:border-box}
  body{margin:0;background:var(--fundo);color:var(--creme);
       font-family:Inter,-apple-system,"Segoe UI",system-ui,sans-serif;
       padding:44px 26px 60px;line-height:1.6}
  .caixa{max-width:980px;margin:0 auto}
  h1{font-family:Cormorant,Georgia,serif;font-weight:600;font-size:44px;margin:0 0 6px}
  .lede{color:#b9c4d4;font-size:16px;max-width:760px;margin:0 0 4px}
  .nota{color:var(--fraco);font-size:13.5px;max-width:760px;margin:12px 0 0}
  h2{font-family:Cormorant,Georgia,serif;font-size:25px;margin:52px 0 10px;font-weight:600}
  h3{font-family:Cormorant,Georgia,serif;font-size:23px;font-weight:600;margin:0}

  /* --- o mapa. §4 da norma-de-diagramas: SVG com width:100% escala pela
     largura e, em tela baixa, corta os dois extremos em silêncio. Daí o
     max-height em vh — e a medida em mais de uma resolução. --- */
  .mapa{margin:26px 0 0;background:var(--cartao);border:1px solid var(--borda);
        border-radius:8px;padding:18px 14px}
  .mapa svg{width:100%;height:auto;max-height:82vh;display:block}
  /* No telefone o mapa espremido a 308px fica ilegivel — medido. Em vez de
     encolher, ele mantem largura minima e ROLA na propria caixa; o corpo da
     pagina nunca rola na horizontal. */
  @media (max-width:820px){
    .mapa{overflow-x:auto;-webkit-overflow-scrolling:touch}
    .mapa svg{min-width:720px;max-height:none}
    .mapa::after{content:"↔ arraste o mapa para o lado";display:block;
      color:var(--fraco);font-size:11.5px;padding:8px 2px 0}
  }
  .mapa a.no{cursor:pointer}
  .mapa a.no:hover rect{stroke-width:2.6}

  /* --- cartão de degrau --- */
  .degrau{background:var(--cartao);border:1px solid var(--borda);border-radius:7px;
          padding:16px 20px 14px;margin:0 0 16px;scroll-margin-top:18px}
  .degrau header{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}
  .nivel{color:var(--fraco);font-size:12px;font-variant-numeric:tabular-nums;
         margin-left:auto}
  .regime{font-size:11px;padding:2px 9px;border-radius:11px;border:1px solid}
  .r-fisica{color:var(--fisica);border-color:var(--fisica)}
  .r-comb{color:var(--comb);border-color:var(--comb)}
  .r-seq{color:var(--seq);border-color:var(--seq)}
  .r-arq{color:var(--ouro);border-color:var(--ouro)}
  .r-lingua{color:#a883c9;border-color:#a883c9}

  .campos{margin:14px 0 0;display:grid;gap:11px}
  @media (min-width:760px){ .campos{grid-template-columns:1fr 1fr;gap:11px 26px} }
  .campo{border-top:1px solid #16283f;padding-top:9px}
  .campo dt{font-size:11.5px;color:var(--ouro);letter-spacing:.04em;
            text-transform:lowercase;margin:0 0 3px}
  .campo dd{margin:0;font-size:13.5px;color:#c3ccda}
  .selo{display:inline-block;font-size:10.5px;padding:1px 7px;border-radius:9px;
        margin-left:6px;vertical-align:1px;white-space:nowrap}
  .selo.lido{color:var(--lido);border:1px solid rgba(111,191,106,.45)}
  .selo.oficio{color:var(--ouro);border:1px solid rgba(201,162,102,.45)}
  details.proc>summary{cursor:pointer;color:var(--fraco);font-size:11.5px;
        padding:5px 0 0;list-style:none}
  details.proc>summary::before{content:"· ";color:var(--ouro)}

  /* --- instrumento --- */
  .instr{margin:16px 0 4px;border:1px solid #23405e;border-radius:7px;
         background:#0a1a2e;padding:14px 16px 12px}
  .instr h4{margin:0 0 4px;font-family:Cormorant,Georgia,serif;font-size:19px;
            font-weight:600;color:var(--creme)}
  .instr .comoler{color:#9fadc0;font-size:13px;margin:0 0 12px}
  .instr canvas{width:100%;display:block;background:#0d1c30;border-radius:5px;
                border:1px solid #16283f}
  .botoes{display:flex;gap:8px;flex-wrap:wrap;margin:11px 0 0}
  .botoes button{background:#17293f;color:#b9c4d4;border:1px solid #2b4767;
        border-radius:5px;padding:6px 13px;font-size:12.5px;
        font-family:inherit;cursor:pointer}
  .botoes button:hover{border-color:var(--ouro);color:var(--creme)}
  .botoes button.on{background:#1d3a2a;border-color:var(--lido);color:#cfe8cd}
  .prova{color:var(--fraco);font-size:11.5px;margin:9px 0 0}
  .aviso{color:var(--fisica);font-size:12px}

  details.seta{margin:12px 0 0;padding:0 0 0 26px;border-left:2px solid var(--lido)}
  details.seta>summary{cursor:pointer;color:var(--lido);font-size:13px;
          padding:7px 0;list-style:none}
  details.seta>summary::before{content:"▲  ";}
  details.seta[open]>summary{color:var(--creme)}
  blockquote{margin:2px 0 12px;padding:12px 16px;background:#132440;
             border-left:3px solid var(--ouro);border-radius:0 5px 5px 0;
             color:#cfd6e2;font-size:13.5px}
  blockquote cite{display:block;margin-top:8px;color:var(--fraco);font-size:12px;
                  font-style:normal}
  .duas{color:var(--ouro);font-size:12.5px;margin:-6px 0 12px 26px}
  .pordentro{margin:12px 0 2px;padding-top:10px;border-top:1px dashed #24395c;
             color:var(--fraco);font-size:12.5px}
  .pordentro b{color:#9fadc0}
  details.dentro>summary{cursor:pointer;color:#9fadc0;font-size:13px;padding:6px 0;
             list-style:none}
  details.dentro>summary::before{content:"· ";color:var(--ouro)}
  details.dentro>summary span{color:var(--fraco)}
  ul.soltas{list-style:none;padding:0;margin:14px 0 0}
  ul.soltas li{background:var(--cartao);border:1px solid var(--borda);border-radius:5px;
             padding:11px 15px;margin:0 0 8px;font-size:13.5px}
  ul.falta{list-style:none;padding:0;margin:14px 0 0}
  ul.falta li{background:var(--cartao);border:1px dashed #33465f;border-radius:5px;
              padding:9px 14px;margin:0 0 7px;color:var(--falta);font-size:13.5px}
  ul.falta li b{color:#b9c4d4}
  ul.falta li span{float:right;font-size:12px;color:var(--fraco)}
  .estado{display:inline-block;font-size:11px;padding:1px 8px;border-radius:9px;
          margin:6px 0 0;border:1px solid}
  .e-nao-sustenta{color:#c1704f;border-color:#c1704f}
  .e-reescrita{color:var(--lido);border-color:var(--lido)}
  .e-nao-achada{color:var(--fraco);border-color:#33465f}
  .e-nao-aresta{color:#a883c9;border-color:#a883c9}
  .porque{color:#8d99ab;font-size:12.5px;margin:7px 0 0;line-height:1.55}
  .comolerpag{background:var(--cartao);border:1px solid var(--borda);
        border-radius:7px;padding:15px 20px;margin:22px 0 0;font-size:13.5px;
        color:#b0bbcb}
  .comolerpag b{color:var(--creme)}
  footer{margin-top:52px;padding-top:18px;border-top:1px solid var(--borda);
         color:var(--fraco);font-size:13px}
  footer a{color:var(--ouro)}
  code{background:#132440;padding:1px 6px;border-radius:3px;font-size:13px;color:var(--ouro)}
"""

NOME_REGIME_CURTO = {"fisica":"física","comb":"combinacional","seq":"sequencial",
                     "arq":"arquitetura","lingua":"linguagem"}


def campos_de(chave):
    """Os quatro campos do degrau, cada um com a sua procedência à mostra."""
    c = CO.CONCEITOS[chave]
    fora = []
    for campo, rotulo in CO.CAMPOS:
        texto, classe, ref, cit, ratificado = c[campo]
        marca, css = MARCA_CLASSE[classe if classe != "d" or ratificado else "d?"]
        proc = ""
        if cit:
            proc = (f'<details class="proc"><summary>a passagem que sustenta'
                    f'</summary><blockquote>“{cit}”'
                    f'<cite>{D.FONTES["petzold" if "SICP" not in (ref or "") else "sicp"]}'
                    f' · {html.escape(ref)}</cite></blockquote></details>')
        elif ratificado:
            proc = ('<details class="proc"><summary>de onde vem este campo'
                    '</summary><blockquote>Nenhum livro escreve onde o aluno '
                    'trava; isso vem da sala de aula. Este campo é julgamento '
                    'didático do autor, <b>ratificado em '
                    f'{ratificado}</b> — o rito da casa é proposta mais '
                    'ratificação, e conteúdo não é diferente de norma. A data '
                    'diz a partir de quando alguém responde pelo texto; se ele '
                    'mudar, volta a ser proposta até ser relido. Ele não foi '
                    'escrito por modelo.</blockquote></details>')
        else:
            proc = ('<details class="proc"><summary>de onde vem este campo'
                    '</summary><blockquote>Nenhum livro escreve onde o aluno '
                    'trava; isso vem da sala de aula. Este campo é julgamento '
                    'didático do autor e está em <b>PROPOSTA</b> — o rito da '
                    'casa é proposta mais ratificação, e conteúdo não é '
                    'diferente de norma. Ele não foi escrito por modelo.'
                    '</blockquote></details>')
        fora.append(
            f'<div class="campo"><dt>{rotulo}<span class="selo {css}">{marca}'
            f'</span></dt><dd>{texto}{proc}</dd></div>')
    return '<dl class="campos">' + "".join(fora) + '</dl>'


def instrumento_de(chave):
    if chave not in INSTRUMENTOS:
        return ""
    ident, titulo, comoler, botoes, alt = INSTRUMENTOS[chave]
    bs = "".join(f'<button data-acao="{a}">{html.escape(r)}</button>'
                 for a, r in botoes)
    return (f'<div class="instr" id="i-{ident}">'
            f'<h4>{titulo}</h4><p class="comoler">{comoler}</p>'
            f'<canvas data-h="{alt}"></canvas>'
            f'<div class="botoes">{bs}</div>'
            f'<p class="prova">Este instrumento <b>é</b> o warrant da seta '
            f'abaixo: ele constrói a peça no navegador, sem o livro na mão. '
            f'A citação continua ali, como segunda testemunha.</p></div>')


def main():
    nos = {i: (nome, nivel, diz) for i, nome, nivel, diz in D.DEGRAUS}

    # --- os portões que abortam ---------------------------------------------
    for de, para, classe, fonte, ref, cit in D.ARESTAS:
        if not cit.strip():
            print(f"ABORTADO: a aresta {de}→{para} não tem citação. "
                  f"Seta sem warrant não é desenhada.", file=sys.stderr)
            return 1
        if de not in nos or para not in nos:
            print(f"ABORTADO: a aresta {de}→{para} cita degrau inexistente.",
                  file=sys.stderr)
            return 1
    for degrau, peca, feita, fonte, ref, cit in D.CONSTRUCAO:
        if not cit.strip():
            print(f"ABORTADO: a construção {peca} não tem citação.", file=sys.stderr)
            return 1
        if degrau is not None and degrau not in nos:
            print(f"ABORTADO: a construção {peca} cita degrau inexistente "
                  f"{degrau!r}.", file=sys.stderr)
            return 1
    # portão novo: campo sem procedência aborta igual a aresta sem citação
    for chave in nos:
        if chave not in CO.CONCEITOS:
            print(f"ABORTADO: o degrau {chave!r} não tem os quatro campos.",
                  file=sys.stderr)
            return 1
        for campo, _rot in CO.CAMPOS:
            if campo not in CO.CONCEITOS[chave]:
                print(f"ABORTADO: {chave}.{campo} não existe.", file=sys.stderr)
                return 1
            texto, classe, ref, cit, ratificado = CO.CONCEITOS[chave][campo]
            if not texto.strip():
                print(f"ABORTADO: {chave}.{campo} está vazio.", file=sys.stderr)
                return 1
            if classe in ("a", "b") and not (cit or "").strip():
                print(f"ABORTADO: {chave}.{campo} diz ser {classe!r} e não traz "
                      f"a passagem. Classe sem passagem é alegação.",
                      file=sys.stderr)
                return 1

    dentro, entrada = {}, {}
    for degrau, peca, feita, fonte, ref, cit in D.CONSTRUCAO:
        dentro.setdefault(degrau, []).append((peca, feita, fonte, ref, cit))
    for de, para, classe, fonte, ref, cit in D.ARESTAS:
        entrada.setdefault(para, []).append((de, classe, fonte, ref, cit))

    # --- os cartões, de baixo para cima (a MESMA direção do mapa, §1.2) ------
    partes = []
    for chave, nome, nivel, diz in D.DEGRAUS:
        setas = []
        for de, classe, fonte, ref, cit in entrada.get(chave, []):
            setas.append(
                f'<details class="seta"><summary>é feito de '
                f'<b>{html.escape(nos[de][0])}</b> — {classe}, e a fonte diz:</summary>'
                f'<blockquote>“{cit}”<cite>{D.FONTES[fonte]} · {html.escape(ref)}</cite>'
                f'</blockquote>')
            seg = D.SEGUNDA_TESTEMUNHA.get((de, chave))
            if seg:
                f2, r2, c2 = seg
                setas.append(
                    f'<blockquote>“{c2}”<cite>{D.FONTES[f2]} · {html.escape(r2)}</cite>'
                    f'</blockquote><p class="duas">Duas testemunhas independentes, '
                    f'chegando de lados opostos da escada — uma construindo a '
                    f'máquina, a outra definindo-a.</p>')
            setas.append('</details>')
        dd = "".join(
            f'<details class="dentro"><summary>{html.escape(pc)} '
            f'<span>&larr; {html.escape(ft)}</span></summary>'
            f'<blockquote>“{ct}”<cite>{D.FONTES[fo]} · {html.escape(rf)}</cite>'
            f'</blockquote></details>'
            for pc, ft, fo, rf, ct in dentro.get(chave, []))
        if dd:
            dd = ('<div class="pordentro"><b>por dentro</b> — peças da mesma camada, '
                  'com a frase que sustenta cada uma:' + dd + '</div>')
        reg = MAPA.REGIME[chave]
        partes.append(
            f'<article class="degrau" id="{chave}">'
            f'<header><h3 class="nome">{html.escape(nome)}</h3>'
            f'<span class="regime r-{reg}">{NOME_REGIME_CURTO[reg]}</span>'
            f'<span class="nivel">nível {nivel}</span></header>'
            f'{campos_de(chave)}'
            f'{instrumento_de(chave)}'
            f'{"".join(setas)}{dd}</article>')

    soltas = "\n".join(
        f'  <li><b>{html.escape(pc)}</b> &larr; {html.escape(ft)}'
        f'<blockquote>“{ct}”<cite>{D.FONTES[fo]} · {html.escape(rf)}</cite>'
        f'</blockquote></li>'
        for pc, ft, fo, rf, ct in dentro.get(None, []))
    ESTADO = {
        "lida, não sustenta":   ("lida — a frase não sustenta", "nao-sustenta"),
        "lida, reescrita":      ("lida — reescrita, pronta para entrar", "reescrita"),
        "procurada, não achada":("procurada — nenhuma frase encontrada", "nao-achada"),
        "lida, não é aresta":   ("lida — não é aresta, é contraste", "nao-aresta"),
    }
    falta = "\n".join(
        f'  <li><b>{html.escape(a)}</b><span>{html.escape(f)}</span>'
        f'<div class="estado e-{ESTADO[e][1]}">{ESTADO[e][0]}</div>'
        f'<div class="porque">{motivo}</div></li>'
        for a, f, e, motivo in D.NAO_LIDO)
    js = open(os.path.join(AQUI, "instrumentos.js"), encoding="utf-8").read()
    n_inst = len(INSTRUMENTOS)

    pag = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>A escada de abstrações — do eletroímã à máquina</title>
<style>{CSS}</style>
</head>
<body>
<div class="caixa">

<h1>A escada de abstrações</h1>
<p class="lede">Do eletroímã ao paradigma de programação, um degrau de cada vez.
Cada degrau responde <b>o que é</b>, <b>por que existe</b>, <b>onde aparece</b> e
<b>onde se trava</b> — e {n_inst} das passagens você não precisa aceitar de
palavra: elas <b>montam a peça aqui na tela</b>.</p>
<p class="lede">O mapa começa quase vazio de propósito. Ele só admite o que
alguém <b>leu</b>: nada entra por plausibilidade, por consenso, nem porque um
modelo escreveu.</p>

<div class="mapa">
{MAPA.desenhar()}
</div>

<div class="comolerpag">
<b>Como ler.</b> O mapa sobe: o eletroímã é o chão, a máquina é o topo — e a
linha pontilhada dourada marca o lugar em que o assunto <b>deixa de ser
eletricidade e passa a ser lógica</b>. A cor do nó diz o regime; a chave está
logo abaixo dele. Seta cheia tem citação conferida contra o livro; seta
tracejada é o que ninguém leu ainda, e ela está desenhada porque
<b>mapa que esconde o que falta mente sobre o próprio tamanho</b>.<br><br>
Dentro de cada degrau, os quatro campos vêm com um <b>selo de procedência</b>:
<span class="selo lido">citação</span> quando o texto é do livro,
<span class="selo lido">síntese</span> quando é resumo de passagem citada — e a
passagem abre ao lado, para você conferir se o resumo é honesto —, e
<span class="selo oficio">ofício · ratificado</span> quando é julgamento de quem
ensina, que nenhum livro escreve — e cada um traz <b>a data em que o autor
respondeu por ele</b>, porque campo que mudar depois dela volta a ser proposta.
<b>Não existe selo para “um modelo escreveu”</b>, e é de propósito: veja a
última seção.
</div>

<h2>Os degraus, de baixo para cima</h2>
<div class="escada">
{chr(10).join(partes)}
</div>

<h2>Verificado, ainda fora da escada</h2>
<p class="nota">Estas {len(dentro.get(None, []))} construções passaram no portão da
citação literal, mas o degrau em que elas pousam ainda não foi lido — então elas
esperam aqui, à vista, em vez de entrar na escada por conveniência.</p>
<ul class="soltas">
{soltas}
</ul>

<h2>O que falta, e por quê</h2>
<p class="nota">Esta lista mudou em 27/08/2026. Antes ela dizia só <i>“ninguém
abriu ainda”</i>. As dez foram lidas, e a leitura mostrou que <b>“não lido” e
“lido e não sustenta” são estados diferentes</b> — e que esconder a diferença é
a mesma mentira que esconder a lista inteira. Das dez: <b>três viraram aresta</b>,
<b>uma já estava no repositório</b> (a linha sobrava), e estas seis ficaram, cada
uma com o motivo. Nenhuma delas reprovou no portão da citação literal: todas as
dez passaram caractere a caractere. <b>Passar no portão não é sustentar a
aresta</b>, e é exatamente aqui que a diferença aparece.</p>
<ul class="falta">
{falta}
</ul>

<h2>Por que assim</h2>
<p class="nota">Um mapa de computação gerado por modelo custa uma tarde e
parece completo. O problema aparece depois: no mapa irmão desta casa, o
<a href="https://github.com/mateusalkimim/math-prerequisite-map">math-prerequisite-map</a>,
os verbetes foram escritos por um modelo local e um deles afirma, no ar até
hoje, que dois conjuntos com os mesmos elementos podem ser diferentes. É falso,
e passou porque ninguém leu.</p>
<p class="nota">Esta página tem os mesmos quatro campos daquele mapa, e é por
isso que a diferença importa: aqui <b>nenhum deles saiu de um modelo</b>. Os que
descrevem a peça saíram do próprio Petzold, que é professor e já responde “o que
é” e “por que existe” em prosa, com capítulo — a passagem vai junto de cada
campo. Os que dizem <b>onde o aluno trava</b> nenhum livro escreve: são
julgamento de quem ensina, entram marcados como <b>proposta</b> e esperam
ratificação.</p>
<p class="nota">As arestas novas entram por um funil: um modelo local <b>propõe</b>
candidatos, um portão confere a frase caractere a caractere contra o livro, e o
que sobrevive só vira aresta depois de <b>julgamento humano</b>. Na primeira
rodada: 48 propostos, 46 passaram no portão, 34 aceitos. O modelo pode achar;
ele não pode afirmar.</p>
<p class="nota">E os {n_inst} instrumentos existem porque citação é warrant de
segunda mão: ela pede que você acredite num livro que talvez não tenha em mãos.
O instrumento constrói a peça na sua frente. Quando os dois concordam, a seta
está sustentada por uma fonte publicada <b>e</b> por uma coisa que roda —
é o padrão mais alto que esta casa consegue.</p>

<footer>
<b>A escada de abstrações</b> — Mateus Alkimim · código <b>MIT</b>, conteúdo
<a href="https://creativecommons.org/licenses/by-sa/4.0/deed.pt-br">CC BY-SA 4.0</a>.<br>
As citações pertencem aos seus autores e aparecem sob direito de citação, com
fonte e capítulo.
</footer>

</div>
<script>{js}</script>
</body>
</html>
"""
    open(SAIDA, "w", encoding="utf-8").write(pag)
    print(f"index.html gerado — {len(D.DEGRAUS)} degraus, "
          f"{len(D.DEGRAUS)*4} campos com procedência, {n_inst} instrumentos, "
          f"{len(D.ARESTAS)} arestas com citação, {len(D.NAO_LIDO)} por ler")
    return 0


if __name__ == "__main__":
    sys.exit(main())
