<!-- idioma: linha gerada por i18n.py -->
*[Leia em português](INSTALACAO.md)*

# Installation

There is no installation to **use**: `index.html` is a self-contained page, opens offline in any modern browser.

## Use

**Windows** — download (Code → Download ZIP, or `git clone`), extract, and double-click on `index.html`.

**Linux** — `git clone … && cd abstraction-ladder && xdg-open index.html`

**macOS** — the same, with `open index.html`.

**Without downloading** — <https://mateusalkimim.github.io/abstraction-ladder/>

## Regenerate the Page

Only those who are **editing** the map need this. Python 3, standard library, no package.

```bash
python3 gerar_escada.py
```

The `index.html` is **derived** from `steps.py`. Editing it by hand is a mistake: the next generation will overwrite it.

## Add an Edge

An edge only enters **after being read**. The procedure is:

1. Open the chapter in the source and find the sentence where the author says what the piece is made of;  
2. Add the step in `STEPS`, if it does not already exist;  
3. Add the edge in `EDGES`, with the **literal quote**, the source, and the chapter;  
4. Remove the corresponding line from `UNREAD`;  
5. `python3 generate_staircase.py`.

The generator **aborts** if the citation is empty or if the edge points to a step that does not exist. This is intentional: an arrow without warrant is not drawn.

Check that it still aborts, by deleting a citation on purpose and running again — this is the negative control, and the same rule applies to the rest of the house: a gate that never failed is worthless.