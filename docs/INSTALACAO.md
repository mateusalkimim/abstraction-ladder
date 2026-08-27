<!-- idioma: linha gerada por i18n.py -->
*[Read this in English](INSTALACAO.en.md)*

# Instalação

Não há instalação para **usar**: `index.html` é uma página autocontida, abre
offline em qualquer navegador moderno.

## Usar

**Windows** — baixe (Code → Download ZIP, ou `git clone`), extraia, e dê duplo
clique em `index.html`.

**Linux** — `git clone … && cd abstraction-ladder && xdg-open index.html`

**macOS** — o mesmo, com `open index.html`.

**Sem baixar** — <https://mateusalkimim.github.io/abstraction-ladder/>

## Regerar a página

Só quem for **editar** o mapa precisa disto. Python 3, biblioteca padrão, nenhum
pacote.

```bash
python3 gerar_escada.py
```

O `index.html` é **derivado** de `degraus.py`. Editá-lo à mão é o defeito: a
próxima geração apaga.

## Acrescentar uma aresta

Uma aresta só entra **depois de lida**. O procedimento é:

1. abra o capítulo na fonte e encontre a frase em que o autor diz de que a peça
   é feita;
2. acrescente o degrau em `DEGRAUS`, se ele ainda não existir;
3. acrescente a aresta em `ARESTAS`, com a **citação literal**, a fonte e o
   capítulo;
4. remova a linha correspondente de `NAO_LIDO`;
5. `python3 gerar_escada.py`.

O gerador **aborta** se a citação estiver vazia ou se a aresta apontar para um
degrau que não existe. Isso é proposital: seta sem warrant não é desenhada.

Confira que ele ainda aborta, apagando uma citação de propósito e rodando de
novo — é o controle negativo, e vale a mesma regra do resto da casa: portão que
nunca reprovou não vale nada.
