<!-- idioma: linha gerada por i18n.py -->
> [!NOTE]
> ### 🇧🇷 **[Leia esta página em português →](README.pt-BR.md)**

# The ladder of abstractions — `abstraction-ladder`

**A map of computation that only admits what someone has read — and constructs in front of you what it claims.** From the electromagnet to the register machine, one step at a time. Each step answers **what it is**, **why it exists**, **where it appears**, and **where it breaks**; each arrow opens the sentence of the book that supports it; and five of the passages you do not need to accept at face value, because they **assemble the piece right here on the screen**.

The guarantee is structural, not a convention that can be forgotten: **the generator aborts** if an edge comes without citation, or if a field claims a source and does not bring the passage.

Live at <https://mateusalkimim.github.io/abstraction-ladder/> — in
[English](https://mateusalkimim.github.io/abstraction-ladder/en/) and in
[Portuguese](https://mateusalkimim.github.io/abstraction-ladder/pt/).

## The Three Layers

**The map.** An SVG generated, that ascends: the electromagnet is the ground, the  
machine is the top, and a golden ruler marks the place where the subject **leaves  
electricity and becomes logic**. The color of the node indicates the regime (physics,  
combinational, sequential, architecture) and the key is on the same screen. The  
edges that no one read are **drawn**, dashed, ascending out of the map — because a  
map that hides what is missing lies about its own size.

**The four fields.** 36 of them, 4 per step, and **none came from a model**.  
Each one carries its own label of origin:

| seal | how many | what it means |
|---|---|---|
| `citation` | 10 | faithful translation of a passage, and the passage opens beside it |
| `synthesis` | 9 | summary of the cited passage—the passage opens alongside, so you can check if the summary is honest |
| `craft · ratified` | 17 | judgment of those who teach, which no book writes—**ratified by the author on 2026-08-27**, and each field stamps the date |

The **9 "what is" fields are all quotes from the book**: no concept from this  
ladder was defined by me. There is no label for *"a model wrote"*, and it is  
intentional.

**The instruments.** Five, in `canvas` and arithmetic — without library, without  
network, without server. And they do not illustrate: **they are the warrant of the  
edge**. When the ladder says *"logic gate ← two relays in series"*, the instrument  
connects the two relays and builds the truth table in front of you, without the book  
in hand.

| instrument | the edge it proves |  
|---|---|  
| two relays turn into a gate | relay → logic gate |  
| two gates turn into a sum | logic gate → adder |  
| the circuit that remembers | logic gate → level-triggered flip-flop |  
| level × edge, on the same clock | level-triggered flip-flop → edge-triggered flip-flop |  
| the count appears alone | edge-triggered flip-flop → counter |

The quote continues there, as a second witness. But it is no longer the only thing  
that supports the arrow — and that is the difference between asking you to believe  
a book that you might not have on hand, and showing.

## Quick Start

```bash
git clone https://github.com/mateusalkimim/abstraction-ladder.git
cd abstraction-ladder
xdg-open index.html          # no Windows, duplo clique
```

Or <https://mateusalkimim.github.io/abstraction-ladder/>. To regenerate the page  
(only Python 3, standard library):

```bash
python3 gerar_escada.py      # pt/index.html, the matrix  
python3 gerar_en.py          # en/index.html, derived from the translation table
```

Step by step in [`docs/INSTALLATION.md`](docs/INSTALACAO.en.md).

## What's Here

```
index.html            the door — redirects by language  
pt/index.html         the page, in Portuguese — GENERATED, do not edit by hand  
en/index.html         the same page in English — DERIVED from pt/ + translation/  

degraus.py            the steps, the edges, and the <b>CITATIONS</b> that support them  
conceitos.py          the four fields of each step, with provenance by field  
mapa.py               the SVG map, citing the norm of diagrams that governs it  
instrumentos.js       the five instruments  
gerar_escada.py       the generator, which aborts if warrant is missing  

conferir_citacoes.py     verifies each citation against the book, section by section  
conferir_mapa.py         geometry of the map: intersection, edge crossing node  
conferir_pagina.py       measures the SCREEN in three resolutions  
conferir_instrumentos.py <b>CLICKS</b> each button and verifies that the drawing changed  
conferir_idioma.py       each page is in the language of the folder it resides in  

i18n.py, gerar_en.py, gerar_porta.py   the bilingual machine, for those who clone  
traducao/             the table pt→en, keyed by hash of the original  
pharo/                why a small and readable map beats a large and generated one  
docs/INSTALACAO.md    step by step  
LICENSE               MIT, for the code  
LICENSE-CONTENT       CC BY-SA 4.0, for the content
```

## The Gates

None of them is a promise: all have **negative control** — they plant the  
defect they should find and fail if they don't find it. A gate that never  
failed did not prove anything.

- **`conferir_citacoes.py`** — each citation checked against the book, character by character. Today: **53 check out, 0 fail, 2 without the source in the collection** (the two from SICP, whose book has not yet been dissected). It **never returns "ok" for absence of proof**: without the book at hand, it exits with an error;
- **`conferir_mapa.py`** — measures what the diagram norm mandates instead of promising. Caught an arc that scraped the box of a node, and a color key that fell five pixels outside the frame;
- **`conferir_instrumentos.py`** — the only one that finds an entire class of defect: it **clicks**. In the first translation of this page, `"[data-acao]"` became `"[data-action]"` — an impeccable translation of a CSS selector. The five instruments lost their listener and all buttons became mute, with the HTML intact, the console clean and **all other gates in green**. No text probe finds this.

## The Place in the Larger Cycle

This is the first piece of a larger map of computing, organized by two axes:  
**substance** (pixel · tensor · state, each becoming a silicon organ —  
GPU · GPU/NPU · CPU) and **depth** (this ladder). Only the second axis has  
warrant today, and that's why only it is published.

The machine came from  
[math-prerequisite-map](https://github.com/mateusalkimim/math-prerequisite-map):  
we, edges with declared warrant, and the generated page from the source. The spirit  
of the instruments came from  
[seeing-calculus](https://github.com/mateusalkimim/seeing-calculus), and it is the  
same contract: they do not illustrate what a text has already said, they allow the  
assertion to be verified.

## Provenance and Guarantees

- **Edges come from two books**, read: Petzold, *Code* (2nd ed.) and Abelson & Sussman, *SICP* (2nd ed.). The citations appear under fair use, with source and chapter, and belong to their authors.
- **9 edges between steps, supported by 11 citations**, and **24 constructions verified** — pieces made of pieces from the same layer.
- **An edge has two independent witnesses** — `register → register machine`. Petzold builds the machine from gates; SICP defines it as data paths plus controller and declares that its diagram corresponds to *"a machine that could be built from electrical components"*. The two arrive from opposite sides at the same object.
- **How the edges entered, since 27/08/2026.** A local model sweeps the chapter and **proposes** candidates — it is a prospector, never an author. Each candidate carries the sentence that would support it, and a gate checks that sentence **character by character** against the original in English; what doesn't match dies there, without costing human reading. What survives has the citation proven and **is not yet an edge**: it goes to human judgment, item by item, and only then rises. In the first round, 48 were proposed → 46 passed the gate → **34 accepted by me** (27 directly and 7 after correcting a circular, anaphoric, or duplicated label — the citation remains intact), and **12 discarded**, each decision recorded with the reason.
- **The rule that this preserves**: every citation verified against the source, every interpretation accepted by a human. The model can find; it cannot assert.
- **What the gate doesn't catch**, and therefore human judgment continues: a real citation that does not support the edge. Of the 46 verified, 11 fell exactly there — `CPU ← Intel 8080` is an instance, not a composition; `ULA ← arithmetic operations` is a function, not pieces; and one carried as a warrant the sentence *"Much of this module should look familiar:"*, which states nothing.
- **The translation also has an owner.** The English is derived from the Portuguese by a local model, block by block, with the table keyed by the hash of the original. Where the machine did not decide, a person decided, and **the decision is written in the table** — including why. Example: the four field labels came out in six variants, and `onde se trava` became *"where it locks"* in seven of the nine steps. There "travar" is the student getting stuck, not a lock.
- No network, no telemetry, no dependency. The page opens offline.
- The books **are not** in this repository: they are third-party work and stay out.

## Why This Way

A computation map generated by a model costs an afternoon and seems complete. The problem appears later: in the sibling map of this house, the entries were written by a local model and one of them claims, published until today, that two sets with the same elements can be different. It is false, and it passed because no one read it.

This page has **the same four fields as that map**, and that's why the difference matters. Here, none of them came from a model: those that describe the piece came from Petzold himself—who is a professor and has already answered *what it is* and *why it exists* in prose, with a chapter—and the passage goes along with each field. Those that say **where the student gets stuck** no book writes: they are the craft of those who teach, and they enter through the ritual of the house—proposal first, ratification later. The 17 were ratified on **2026-08-27**, and each one stamps the date. It's not decoration: it says **from when someone is responsible for the text**, and a field that changes after that reverts to being a proposal until it is reread.

Here the order has been reversed — the door to human reading comes **before** the content —  
and the price is this small map. The bet is that nine verifiable edges are worth more  
than sixty that are not.

The funnel does not loosen this order: it only cheapens the **finding**. The judgment remains  
human, and the proof remains the phrase in the book — now with an instrument  
beside it, when the piece can be constructed.

## State, and what is missing

- **10 known but unread edges**, listed on the page with the reference of where they are. They enter when they are read, with the citation;
- **9 verified constructions that have not yet landed on any step** (RAM, ALU, PSW, oscillator, transistor, seven-segment decoder). The citation is proven; the step below them is what hasn't been read. They are visible in their own section, instead of entering the ladder for convenience;
- **four steps still do not have an instrument** — electromagnet, relay, register, and register machine. The two lower ones are physics, and the top one is too large for a `canvas`;
- **there is no glossary of the terms of the house**, and this produced the six label variants in the translation;
- **the ladder has a measured end.** From chapter 5 to 20 in Petzold, a single proposal did not sustain; from chapters 21 to 24, eight out of eleven. This is where the book stops building and starts describing a chip that already exists — and this is why the proven steps stop before the 8080;
- **the axis of substance** (pixel/tensor/state → GPU/NPU/CPU) has no edge yet, although the bibliography exists in the archive;
- **programming languages** are not here and will not be until there is a source: the archive does not have a book on design or comparison of languages. What SICP supports is classification by **mechanism** — interpreted × compiled, paradigm as a variation of the evaluator — and not by history or adoption;
- **the thesis that AI is the first layer that breaks determinism** is mine, without a book behind it. When it enters, it enters as a warrant of class `orientacao`, dated — never disguised as a fact of a book.

## License

Code under **MIT**. Content under **CC BY-SA 4.0**. The citations from the books  
belong to their authors.