# A escada de abstrações — `abstraction-ladder`

**Um mapa da computação que só admite o que alguém leu.** Do relé à máquina de
registradores, um degrau por vez — e **cada seta abre a frase que a sustenta**,
copiada do livro, com capítulo. Nada entra por plausibilidade, por consenso, nem
porque um modelo escreveu.

A garantia é essa, e ela é estrutural: **o gerador aborta se uma aresta vier sem
citação.** Não é convenção que se pode esquecer — a página não é escrita.

No ar em <https://mateusalkimim.github.io/abstraction-ladder/>.

Hoje: **6 arestas lidas** contra **10 que se sabe existirem e ainda não foram
abertas**, listadas na própria página. Mapa que esconde o que falta mente sobre o
próprio tamanho.

## Início rápido

```bash
git clone https://github.com/mateusalkimim/abstraction-ladder.git
cd abstraction-ladder
xdg-open index.html          # no Windows, duplo clique
```

Ou <https://mateusalkimim.github.io/abstraction-ladder/>. Para regerar a página
(só Python 3, biblioteca padrão):

```bash
python3 gerar_escada.py
```

Passo a passo em [`docs/INSTALACAO.md`](docs/INSTALACAO.md).

## O que tem aqui

```
index.html          a página — GERADA, não editar à mão
degraus.py          os degraus, as arestas e as CITAÇÕES que as sustentam
gerar_escada.py     o gerador, que aborta se faltar warrant
pharo/              por que um mapa pequeno e lido vence um grande e gerado
docs/INSTALACAO.md  passo a passo
LICENSE             MIT, para o código
LICENSE-CONTENT     CC BY-SA 4.0, para o conteúdo
```

## O lugar no ciclo maior

É o primeiro pedaço de um mapa maior da computação, organizado por dois eixos:
**substância** (pixel · tensor · estado, cada uma virando um órgão de silício —
GPU · GPU/NPU · CPU) e **profundidade** (esta escada). Só o segundo eixo tem
warrant hoje, e por isso só ele está publicado.

A máquina veio do
[math-prerequisite-map](https://github.com/mateusalkimim/math-prerequisite-map):
nós, arestas com warrant declarado, e a página gerada da fonte. O parente novo é o
[seeing-calculus](https://github.com/mateusalkimim/seeing-calculus).

## Proveniência e garantias

- **As arestas vêm de dois livros**, lidos: Petzold, *Code* (2ª ed.) e
  Abelson & Sussman, *SICP* (2ª ed.). As citações aparecem sob direito de
  citação, com fonte e capítulo, e pertencem aos seus autores.
- **Uma aresta tem duas testemunhas independentes** — `registrador → máquina de
  registradores`. Petzold constrói a máquina a partir de portas; SICP a define
  como caminhos de dados mais controlador e declara que seu diagrama corresponde
  a *"uma máquina que poderia ser construída de componentes elétricos"*. Os dois
  chegam de lados opostos ao mesmo objeto.
- **Nenhum verbete gerado por modelo.** As descrições dos degraus são minhas e
  curtas; onde não há leitura, não há texto.
- Sem rede, sem telemetria, sem dependência. A página abre offline.
- Os livros **não estão** neste repositório: são obra de terceiro e ficam fora.

## Por que assim

Um mapa de computação gerado por modelo custa uma tarde e parece completo. O
problema aparece depois: no mapa irmão desta casa, os verbetes foram escritos por
um modelo local e um deles afirma, publicado até hoje, que dois conjuntos com os
mesmos elementos podem ser diferentes. É falso, e passou porque ninguém leu.

Aqui a ordem se inverteu — o portão da leitura humana vem **antes** do conteúdo — e
o preço é este mapa pequeno. A aposta é que seis arestas conferíveis valem mais
que sessenta que não.

## Estado, e o que falta

- **10 arestas conhecidas e não lidas**, listadas na página com a referência de
  onde estão. Elas entram quando forem lidas, com a citação;
- **o eixo da substância** (pixel/tensor/estado → GPU/NPU/CPU) não tem nenhuma
  aresta ainda, embora a bibliografia exista no acervo;
- **as linguagens de programação** não estão aqui e não estarão até haver fonte:
  o acervo não tem livro de projeto ou comparação de linguagens. O que o SICP
  sustenta é classificação por **mecanismo** — interpretada × compilada, paradigma
  como variação do avaliador — e não por história ou adoção;
- **a tese de que a IA é a primeira camada que quebra o determinismo** é minha, sem
  livro atrás. Quando entrar, entra como warrant de classe `orientacao`, datado —
  nunca disfarçada de fato de livro.

## Licença

Código sob **MIT**. Conteúdo sob **CC BY-SA 4.0**. As citações dos livros
pertencem aos seus autores.
