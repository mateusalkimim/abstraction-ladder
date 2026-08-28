<!-- idioma: linha gerada por i18n.py -->
> [!NOTE]
> ### 🌍 **[Read this page in English →](README.md)**

# A escada de abstrações — `abstraction-ladder`

**Um mapa da computação que só admite o que alguém leu — e que constrói na sua
frente o que afirma.** Do eletroímã ao paradigma de programação, um degrau por
vez. Cada degrau responde **o que é**, **por que existe**, **onde aparece** e
**onde se trava**; cada seta abre a frase do livro que a sustenta; e cinco das
passagens você não precisa aceitar de palavra, porque elas **montam a peça aqui
na tela**.

A garantia é estrutural, não é convenção que se pode esquecer: **o gerador
aborta** se uma aresta vier sem citação, ou se um campo alegar fonte e não
trouxer a passagem.

No ar em <https://mateusalkimim.github.io/abstraction-ladder/> — em
[inglês](https://mateusalkimim.github.io/abstraction-ladder/en/) e em
[português](https://mateusalkimim.github.io/abstraction-ladder/pt/).

## As três camadas

**O mapa.** Um SVG gerado, que sobe: o eletroímã é o chão, o paradigma é o topo,
e duas réguas marcam onde o assunto muda de matéria — a dourada, onde ele **deixa de ser eletricidade e passa a ser lógica**; a roxa, onde **deixa de ser
circuito e passa a ser linguagem**. A cor do nó diz o regime (física, combinacional,
sequencial, arquitetura) e a chave fica na mesma tela. As arestas que ninguém
leu estão **desenhadas**, tracejadas, subindo para fora do mapa — porque mapa
que esconde o que falta mente sobre o próprio tamanho.

**Os quatro campos.** 52 deles, 4 por degrau, e **nenhum saiu de um modelo**.
Cada um carrega o seu próprio selo de procedência:

| selo | quantos | o que significa |
|---|---|---|
| `citação` | 15 | tradução fiel de uma passagem, e a passagem abre ao lado |
| `síntese` | 12 | resumo de passagem citada — a passagem abre junto, para você conferir se o resumo é honesto |
| `ofício · ratificado` | 17 | julgamento de quem ensina, que nenhum livro escreve — **ratificado em 2026-08-27**, e cada campo estampa a data |
| `ofício · proposta` | 8 | os mesmos, nos quatro degraus que entraram **depois** da ratificação. Ratificação não se estende por analogia a texto que ninguém leu |

Os **13 campos "o que é" são todos citação do livro**: nenhum conceito desta
escada foi definido por mim. Não existe selo para *"um modelo escreveu"*, e é de
propósito.

**Os instrumentos.** Cinco, em `canvas` e aritmética — sem biblioteca, sem rede,
sem servidor. E eles não ilustram: **eles são o warrant da aresta**. Quando a
escada diz *"porta lógica ← dois relés em série"*, o instrumento liga os dois
relés e monta a tabela-verdade na sua frente, sem o livro na mão.

| instrumento | a aresta que ele prova |
|---|---|
| dois relés viram uma porta | relé → porta lógica |
| duas portas viram uma conta | porta lógica → somador |
| o circuito que lembra | porta lógica → flip-flop de nível |
| nível × borda, no mesmo relógio | flip-flop de nível → flip-flop de borda |
| a contagem aparece sozinha | flip-flop de borda → contador |

A citação continua ali, como segunda testemunha. Mas deixou de ser a única coisa
que sustenta a seta — e essa é a diferença entre pedir que você acredite num
livro que talvez não tenha em mãos, e mostrar.

## Início rápido

```bash
git clone https://github.com/mateusalkimim/abstraction-ladder.git
cd abstraction-ladder
xdg-open index.html          # no Windows, duplo clique
```

Ou <https://mateusalkimim.github.io/abstraction-ladder/>. Para regerar a página
(só Python 3, biblioteca padrão):

```bash
python3 gerar_escada.py      # pt/index.html, a matriz
python3 gerar_en.py          # en/index.html, derivado da tabela de tradução
```

Passo a passo em [`docs/INSTALACAO.md`](docs/INSTALACAO.md).

## O que tem aqui

```
index.html            a porta — encaminha por idioma
pt/index.html         a página, em português — GERADA, não editar à mão
en/index.html         a mesma página em inglês — DERIVADA de pt/ + traducao/

degraus.py            os degraus, as arestas e as CITAÇÕES que as sustentam
conceitos.py          os quatro campos de cada degrau, com procedência por campo
mapa.py               o SVG do mapa, citando a norma de diagramas que o rege
instrumentos.js       os cinco instrumentos
gerar_escada.py       o gerador, que aborta se faltar warrant

conferir_citacoes.py     confere cada citação contra o livro, trecho a trecho
conferir_mapa.py         geometria do mapa: cruzamento, aresta atravessando nó
conferir_pagina.py       mede a TELA em três resoluções
conferir_instrumentos.py APERTA cada botão e confere que o desenho mudou
conferir_idioma.py       cada página está no idioma da pasta em que mora

i18n.py, gerar_en.py, gerar_porta.py   a máquina bilíngue, para quem clonar
traducao/             a tabela pt→en, chaveada por hash do original
pharo/                por que um mapa pequeno e lido vence um grande e gerado
docs/INSTALACAO.md    passo a passo
LICENSE               MIT, para o código
LICENSE-CONTENT       CC BY-SA 4.0, para o conteúdo
```

## Os portões

Nenhum deles é promessa: todos têm **controle negativo** — plantam o defeito que
deveriam achar e falham se não acharem. Um portão que nunca reprovou não provou
nada.

- **`conferir_citacoes.py`** — cada citação conferida contra o livro, caractere a
  caractere. Hoje: **67 conferem, 0 reprovam, 0 sem a fonte no acervo** — o SICP foi
  dissecado em 27/08/2026 e as duas citações que antes eram inverificáveis
  passaram a conferir. Ele **nunca devolve "ok" por ausência de prova**: sem o
  livro à mão, sai com erro;
- **`conferir_mapa.py`** — mede o que a norma de diagramas manda em vez de
  prometer. Pegou um arco que raspava a caixa de um nó, e uma chave de cor que
  caía cinco pixels fora do quadro;
- **`conferir_instrumentos.py`** — o único que acha uma classe inteira de
  defeito: ele **clica**. Na primeira tradução desta página, `"[data-acao]"`
  virou `"[data-action]"` — tradução impecável de um seletor CSS. Os cinco
  instrumentos ficaram sem ouvinte e todos os botões mudos, com o HTML íntegro,
  o console limpo e **todos os outros portões em verde**. Nenhuma sonda de texto
  acha isso.

## O lugar no ciclo maior

É o primeiro pedaço de um mapa maior da computação, organizado por dois eixos:
**substância** (pixel · tensor · estado, cada uma virando um órgão de silício —
GPU · GPU/NPU · CPU) e **profundidade** (esta escada). Só o segundo eixo tem
warrant hoje, e por isso só ele está publicado.

A máquina veio do
[math-prerequisite-map](https://github.com/mateusalkimim/math-prerequisite-map):
nós, arestas com warrant declarado, e a página gerada da fonte. O espírito dos
instrumentos veio do
[seeing-calculus](https://github.com/mateusalkimim/seeing-calculus), e é o mesmo
contrato: eles não ilustram o que um texto já disse, eles deixam a afirmação ser
conferida.

## Proveniência e garantias

- **As arestas vêm de dois livros**, lidos: Petzold, *Code* (2ª ed.) e
  Abelson & Sussman, *SICP* (2ª ed.). As citações aparecem sob direito de
  citação, com fonte e capítulo, e pertencem aos seus autores.
- **13 arestas entre degraus, sustentadas por 15 citações**, e **24 construções
  verificadas** — peças feitas de peças da mesma camada.
- **Uma aresta tem duas testemunhas independentes** — `registrador → máquina de
  registradores`. Petzold constrói a máquina a partir de portas; SICP a define
  como caminhos de dados mais controlador e declara que seu diagrama corresponde
  a *"uma máquina que poderia ser construída de componentes elétricos"*. Os dois
  chegam de lados opostos ao mesmo objeto.
- **Como as arestas entram, desde 27/08/2026.** Um modelo local varre o capítulo
  e **propõe** candidatos — ele é garimpeiro, nunca autor. Cada candidato carrega
  a frase que o sustentaria, e um portão confere essa frase **caractere a
  caractere** contra o original em inglês; o que não bate morre ali, sem custar
  leitura humana. O que sobrevive tem a citação provada e **ainda não é aresta**:
  vai para julgamento humano, item a item, e só então sobe. Na primeira rodada
  foram 48 propostos → 46 passaram no portão → **34 aceitos por mim** (27 direto e
  7 depois de corrigir um rótulo circular, anafórico ou duplicado — a citação
  segue intacta), e **12 descartadas**, cada decisão registrada com o motivo.
- **A regra que isso preserva**: toda citação verificada contra a fonte, toda
  interpretação aceita por um humano. O modelo pode achar; ele não pode afirmar.
- **O que o portão não pega**, e por isso o julgamento humano continua: citação
  real que não sustenta a aresta. Das 46 verificadas, 11 caíram exatamente aí —
  `CPU ← Intel 8080` é instância, não composição; `ULA ← operações aritméticas` é
  função, não peças; e uma trazia como warrant a frase *"Much of this module
  should look familiar:"*, que não afirma nada.
- **A tradução também tem dono.** O inglês é derivado do português por um modelo
  local, bloco a bloco, com a tabela chaveada por hash do original. Onde a
  máquina não decidiu, decidiu uma pessoa, e **a decisão está escrita na tabela**
  — inclusive por quê. Exemplo: os quatro rótulos de campo saíram em seis
  variantes, e `onde se trava` virou *"where it locks"* em sete dos nove degraus.
  Ali "travar" é o aluno empacar, não uma fechadura.
- Sem rede, sem telemetria, sem dependência. A página abre offline.
- Os livros **não estão** neste repositório: são obra de terceiro e ficam fora.

## Por que assim

Um mapa de computação gerado por modelo custa uma tarde e parece completo. O
problema aparece depois: no mapa irmão desta casa, os verbetes foram escritos por
um modelo local e um deles afirma, publicado até hoje, que dois conjuntos com os
mesmos elementos podem ser diferentes. É falso, e passou porque ninguém leu.

Esta página tem **os mesmos quatro campos daquele mapa**, e é por isso que a
diferença importa. Aqui nenhum deles saiu de um modelo: os que descrevem a peça
saíram do próprio Petzold — que é professor, e já responde *o que é* e *por que
existe* em prosa, com capítulo —, e a passagem vai junto de cada campo. Os que
dizem **onde o aluno trava** nenhum livro escreve: são ofício de quem ensina, e
entram pelo rito da casa — proposta primeiro, ratificação depois. Os 17 foram
ratificados em **27/08/2026**, e cada um estampa a data. Ela não é enfeite: diz
**a partir de quando alguém responde pelo texto**, e um campo que mudar depois
dela volta a ser proposta até ser relido.

Aqui a ordem se inverteu — o portão da leitura humana vem **antes** do conteúdo —
e o preço é este mapa pequeno. A aposta é que treze arestas conferíveis valem mais
que sessenta que não.

O funil não afrouxa essa ordem: ele só barateia o **achar**. O julgamento continua
sendo humano, e a prova continua sendo a frase no livro — agora com um instrumento
ao lado, quando a peça pode ser construída.

## Estado, e o que falta

- **as dez que faltavam foram lidas em 27/08/2026**, e o resultado está na
  página com o motivo de cada uma. Todas as dez passaram no portão da citação
  literal; **três sobreviveram ao julgamento** e viraram aresta (ULA, assembler,
  avaliador→paradigma), uma **já estava no repositório** e a linha sobrava, duas
  foram **reescritas** porque nomeavam o nó de origem errado, uma foi
  **rebaixada** a nota (contraste não é aresta) e três seguem sem sustentação.
  Passar no portão não é sustentar a aresta, e é aí que a diferença aparece;
- **8 campos de ofício em proposta**, nos quatro degraus novos, aguardando
  leitura e ratificação;
- **8 construções verificadas que ainda não pousaram em degrau nenhum** (RAM,
  PSW, oscilador, transistor, decodificador de sete segmentos). A da ULA pousou
  em 27/08/2026, quando a ULA virou degrau. A citação
  está provada; o degrau abaixo delas é que não foi lido. Ficam à vista, em seção
  própria, em vez de entrar na escada por conveniência;
- **quatro degraus ainda não têm instrumento** — eletroímã, relé, registrador e
  máquina de registradores. Os dois de baixo são física, e o de cima é grande
  demais para um `canvas`;
- **a escada tem um fim medido.** Do capítulo 5 ao 20 de Petzold, uma só proposta
  não sustentava; dos capítulos 21 ao 24, oito de onze. É onde o livro para de
  construir e passa a descrever um chip que já existe — e é por isso que os
  degraus provados param antes do 8080;
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
