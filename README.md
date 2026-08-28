<!-- idioma: linha gerada por i18n.py -->
> [!NOTE]
> ### 🇧🇷 **[Leia esta página em português →](README.pt-BR.md)**

# The ladder of abstractions — `abstraction-ladder`

**A map of computation that only admits what someone has read — and constructs in front what it claims.** From the electromagnet to the programming paradigm, one step at a time. Each step answers **what it is**, **why it exists**, **where it appears**, and **where you get stuck**; each arrow opens the sentence from the book that supports it; and five of the passages you do not need to accept at face value, because they **build the piece right here on the screen**.

The guarantee is structural, not a convention that can be forgotten: **the generator aborts** if an edge comes without citation, or if a field claims a source and does not bring the passage.

Live at <https://mateusalkimim.github.io/abstraction-ladder/> — in
[English](https://mateusalkimim.github.io/abstraction-ladder/en/) and in
[Portuguese](https://mateusalkimim.github.io/abstraction-ladder/pt/).

## The Three Layers

**The map.** An SVG generated that rises: the electromagnet is the ground, the paradigm is the top, and two rulers mark where the subject changes material — the golden one, where it **stops being electricity and becomes logic**; the purple one, where it **stops being circuit and becomes language**. The node's color indicates the regime (physics, combinational, sequential, architecture) and the key stays on the same screen. The edges that no one read are **drawn**, dashed, rising out of the map — because a map that hides what's missing lies about its own size.

**The four fields.** 60 of them, 4 per step, and **none came from a model**.
Each one carries its own seal of origin:

| seal | how many | what it means |
|---|---|---|
| `citation` | 19 | faithful translation of a passage, and the passage opens beside |
| `synthesis` | 12 | summary of the cited passage — the passage opens alongside, for you to check if the summary is honest |
| `craft · confirmed` | 17 | judgment of who teaches, that no book writes — **confirmed by the author on 2026-08-27**, and each field stamps the date |
| `craft · unconfirmed` | 12 | the same, in the six steps that entered **after** the confirmation. Confirmation does not extend by analogy to text that no one read |

The **15 fields "what it is" are all citations from the book**: no concept from this
ladder was defined by me. There is no seal for *"a model wrote"*, and it is on purpose.

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
index.html            the door — routes by language
pt/index.html         the page, in Portuguese — GENERATED, do not edit by hand
en/index.html         the same page in English — DERIVED from pt/ + traducao/

degraus.py            the steps, the edges and the CITATIONS that support them
conceitos.py          the four fields of each step, with provenance per field
mapa.py               the SVG of the map, citing the diagram standard it follows
instrumentos.js       the five instruments
gerar_escada.py       the generator, which aborts if a warrant is missing

conferir_citacoes.py     checks each citation against the book, passage by passage
conferir_mapa.py         map geometry: crossings, edge running through a node
```

## The checks

None of them is a promise: all have **negative control** — they plant the  
defect they should find and fail if they don't find it. A gate that never  
failed did not prove anything.

- **`verify_citations.py`** — each citation verified against the book, character by character. Today: **73 verify, 0 fail, 0 without the source in the collection** — the SICP was dissected on 27/08/2026 and the two citations that were previously unverifiable now verify. It **never returns "ok" for lack of proof**: without the book at hand, it exits with an error;
- **`verify_map.py`** — measures what the diagram norm mandates instead of promising. It caught an arc that scraped the box of a node, and a color key that fell five pixels outside the frame;
- **`verify_tools.py`** — the only one that finds an entire class of defect: it **clicks**. In the first translation of this page, `"[data-acao]"` became `"[data-action]"` — an impeccable translation of a CSS selector. The five tools were left without listeners and all the buttons were silent, with the HTML intact, the console clean and **all other checks in green**. No text probe finds this.

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
- **An edge has two independent witnesses** — `register → register machine`. Petzold builds the machine from checks; SICP defines it as data paths plus controller and declares that its diagram corresponds to *"a machine that could be built from electrical components"*. The two arrive from opposite sides at the same object.
- **How the edges enter, since 27/08/2026.** A local model sweeps the chapter and **proposes** candidates — it is a prospector, never an author. Each candidate carries the sentence that would support it, and the check compares that sentence **character by character** against the English original; whatever does not match dies there, without costing a human reading. What survives has its citation proven and is **still not an edge**: it goes to human judgment, item by item, and only then does it rise — and most of what passes the literal check still does not become an edge. Every decision is recorded with its reason.
.

## Why This Way

A computation map written by a language model costs an afternoon and looks
complete. The price shows up later: a plausible, wrong claim stays published
because nobody read it, and nobody can tell which of the other sixty are in the
same state.

**No field here came from a model.** The ones that describe the piece came from
Petzold himself — a teacher, who already answers *what it is* and *why it
exists* in prose, with a chapter — and the passage travels with each field. The
ones that say **where the student gets stuck** no book writes: they are the
craft of someone who teaches, they enter unconfirmed, and they earn the date on
which the author starts answering for them. The date is not decoration: it says
**from when someone answers for the text**, and a field that changes after it
stops being confirmed until it is read again.

Here the order was inverted — the check of human reading comes **before** the content —
and the price is this small map. The bet is that fifteen verifiable edges are worth more
than sixty that are not.

The funnel does not loosen this order: it only cheapens the **finding**. The judgment remains  
human, and the proof remains the phrase in the book — now with an instrument  
beside it, when the piece can be constructed.

## State, and what is missing

- **The ten that were missing were read on 27/08/2026**, and the result is on the
  page with the reason for each one. All ten passed through the citation gate;
  **five became edges** (ALU, assembler, evaluator→paradigm, and the two
  **rewritten** — RAM and compiler — after correcting the source node they
  named incorrectly), one **was already in the repository** and the line was
  leftover, one was **downgraded** to a note (contrast is not an edge) and three
  remain unsupported. Passing through the check is not sustaining the edge, and
  that's where the difference appears;
- **12 craft fields in proposal**, in the six new steps, awaiting reading and
  confirmation;
- **5 constructions verified that have not yet landed on any step** (PSW,
  oscillator, transistor, seven-segment decoder, speaker wire). The ones from the
  ALU and the three from the RAM landed on 27/08/2026, when these two became a
  step — what was "verified and without a place" became the texture of a step.
  The citation is proven; the step below them is the one that was not read. They
  remain visible, in their own section, instead of entering the ladder for
  convenience;
- **Four steps still do not have an instrument** — electromagnet, relay, register
  and register machine. The two at the bottom are physics, and the top one is too
  large for a `canvas`;
- **The ladder has a measured end.** From chapter 5 to 20 of Petzold, only one
  proposal was not sustained; from chapters 21 to 24, eight of eleven. That's
  where the book stops building and starts describing a chip that already exists
  — and that's why the proven steps end before the 8080;
- **The substance axis** (pixel/tensor/state → GPU/NPU/CPU) has no edges yet,
  although the bibliography exists in the archive;
- **Programming languages** are not here and will not be until there is a source:
  the archive does not have a project book or a comparison of languages. What the
  SICP sustains is classification by **mechanism** — interpreted × compiled,
  paradigm as a variation of the evaluator — and not by history or adoption;
- **The thesis that AI is the first layer that breaks determinism** is mine, with
  no book behind it. When it enters, it enters as a warrant of class `orientacao`,
  dated — never disguised as a fact of a book.

## License

Code under **MIT**. Content under **CC BY-SA 4.0**. The citations from the books  
belong to their authors.