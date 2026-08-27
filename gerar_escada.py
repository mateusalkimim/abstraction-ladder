#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o index.html a partir de degraus.py. A página é DERIVADA.

Cada seta da escada abre a **citação que a sustenta**. É a regra do
repositório, e o gerador a impõe: aresta sem citação não é desenhada — ela
aborta a geração, porque publicar uma seta sem warrant é exatamente o defeito
que este mapa existe para não ter.

Roda:  python3 gerar_escada.py
"""
import html, os, sys
import degraus as D

AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(AQUI, "index.html")

CSS = """
  :root{ --fundo:#0a1424; --creme:#e8e2d6; --fraco:#5b6b86; --ouro:#c9a266;
         --cartao:#0d1c30; --borda:#1e3050; --lido:#6fbf6a; --falta:#8a94a4; }
  *{box-sizing:border-box}
  body{margin:0;background:var(--fundo);color:var(--creme);
       font-family:Inter,-apple-system,"Segoe UI",system-ui,sans-serif;
       padding:44px 26px 60px;line-height:1.6}
  .caixa{max-width:940px;margin:0 auto}
  h1{font-family:Cormorant,Georgia,serif;font-weight:600;font-size:44px;margin:0 0 6px}
  .lede{color:#b9c4d4;font-size:16px;max-width:740px;margin:0 0 4px}
  .nota{color:var(--fraco);font-size:13.5px;max-width:740px;margin:12px 0 0}
  h2{font-family:Cormorant,Georgia,serif;font-size:25px;margin:44px 0 10px;font-weight:600}
  .escada{margin:22px 0 0}
  .degrau{background:var(--cartao);border:1px solid var(--borda);border-radius:6px;
          padding:14px 18px;margin:0}
  .nome{font-family:Cormorant,Georgia,serif;font-size:22px;font-weight:600}
  .nivel{color:var(--fraco);font-size:12px;float:right;font-variant-numeric:tabular-nums}
  .diz{color:#9fadc0;font-size:13.5px;margin-top:4px}
  details.seta{margin:0;padding:0 0 0 26px;border-left:2px solid var(--lido)}
  details.seta>summary{cursor:pointer;color:var(--lido);font-size:13px;
          padding:9px 0;list-style:none}
  details.seta>summary::before{content:"▲  ";}
  details.seta[open]>summary{color:var(--creme)}
  blockquote{margin:2px 0 12px;padding:12px 16px;background:#132440;
             border-left:3px solid var(--ouro);border-radius:0 5px 5px 0;
             color:#cfd6e2;font-size:13.5px}
  blockquote cite{display:block;margin-top:8px;color:var(--fraco);font-size:12px;
                  font-style:normal}
  .duas{color:var(--ouro);font-size:12.5px;margin:-6px 0 12px 26px}
  ul.falta{list-style:none;padding:0;margin:14px 0 0}
  ul.falta li{background:var(--cartao);border:1px dashed #33465f;border-radius:5px;
              padding:9px 14px;margin:0 0 7px;color:var(--falta);font-size:13.5px}
  ul.falta li b{color:#b9c4d4}
  ul.falta li span{float:right;font-size:12px;color:var(--fraco)}
  footer{margin-top:52px;padding-top:18px;border-top:1px solid var(--borda);
         color:var(--fraco);font-size:13px}
  footer a{color:var(--ouro)}
  code{background:#132440;padding:1px 6px;border-radius:3px;font-size:13px;color:var(--ouro)}
"""


def main():
    nos = {i: (nome, nivel, diz) for i, nome, nivel, diz in D.DEGRAUS}
    ordem = [i for i, _, _, _ in D.DEGRAUS]

    for de, para, classe, fonte, ref, cit in D.ARESTAS:
        if not cit.strip():
            print(f"ABORTADO: a aresta {de}→{para} não tem citação. "
                  f"Seta sem warrant não é desenhada.", file=sys.stderr)
            return 1
        if de not in nos or para not in nos:
            print(f"ABORTADO: a aresta {de}→{para} cita degrau inexistente.", file=sys.stderr)
            return 1

    entrada = {}
    for de, para, classe, fonte, ref, cit in D.ARESTAS:
        entrada.setdefault(para, []).append((de, classe, fonte, ref, cit))

    partes = []
    for i in ordem:
        nome, nivel, diz = nos[i]
        for de, classe, fonte, ref, cit in entrada.get(i, []):
            partes.append(
                f'<details class="seta"><summary>é feito de '
                f'<b>{html.escape(nos[de][0])}</b> — {classe}, e a fonte diz:</summary>'
                f'<blockquote>“{cit}”<cite>{D.FONTES[fonte]} · {html.escape(ref)}</cite>'
                f'</blockquote>')
            seg = D.SEGUNDA_TESTEMUNHA.get((de, i))
            if seg:
                f2, r2, c2 = seg
                partes.append(
                    f'<blockquote>“{c2}”<cite>{D.FONTES[f2]} · {html.escape(r2)}</cite>'
                    f'</blockquote>'
                    f'<p class="duas">Duas testemunhas independentes, chegando de lados '
                    f'opostos da escada — uma construindo a máquina, a outra definindo-a.</p>')
            partes.append('</details>')
        partes.append(
            f'<div class="degrau"><span class="nivel">nível {nivel}</span>'
            f'<div class="nome">{html.escape(nome)}</div>'
            f'<div class="diz">{diz}</div></div>')

    falta = "\n".join(
        f'  <li><b>{html.escape(a)}</b><span>{html.escape(f)}</span></li>'
        for a, f in D.NAO_LIDO)

    pag = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>A escada de abstrações — só o que foi lido</title>
<style>{CSS}</style>
</head>
<body>
<div class="caixa">

<h1>A escada de abstrações</h1>
<p class="lede">Do relé à máquina de registradores, um degrau de cada vez — e
<b>cada seta abre a frase que a sustenta</b>, copiada do livro, com capítulo.</p>
<p class="lede">Este mapa começa quase vazio de propósito. Ele só admite o que
alguém <b>leu</b>: nada entra por plausibilidade, por consenso, nem porque um
modelo escreveu. <b>{len(D.ARESTAS)} arestas lidas</b> contra
<b>{len(D.NAO_LIDO)} que se sabe existirem e ainda não foram abertas</b>, listadas
no fim — porque mapa que esconde o que falta mente sobre o próprio tamanho.</p>

<h2>Os degraus, de baixo para cima</h2>
<div class="escada">
{chr(10).join(reversed(partes))}
</div>

<h2>O que falta ler</h2>
<p class="nota">Cada linha aqui é uma aresta que a bibliografia sustenta e que
ninguém abriu ainda. Elas entram quando forem lidas, com a citação — não antes.</p>
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
<p class="nota">Aqui a ordem se inverteu: o portão da leitura humana vem
<b>antes</b> do conteúdo, e o preço é este mapa pequeno. A aposta é que seis
arestas que se pode conferir valem mais que sessenta que não.</p>

<footer>
<b>A escada de abstrações</b> — Mateus Alkimim · código <b>MIT</b>, conteúdo
<a href="https://creativecommons.org/licenses/by-sa/4.0/deed.pt-br">CC BY-SA 4.0</a>.<br>
As citações pertencem aos seus autores e aparecem sob direito de citação, com
fonte e capítulo.
</footer>

</div>
</body>
</html>
"""
    open(SAIDA, "w", encoding="utf-8").write(pag)
    print(f"index.html gerado — {len(D.ARESTAS)} arestas com citação, "
          f"{len(D.DEGRAUS)} degraus, {len(D.NAO_LIDO)} por ler")
    return 0


if __name__ == "__main__":
    sys.exit(main())
