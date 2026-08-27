# -*- coding: utf-8 -*-
"""Os degraus da escada, e as arestas que alguém LEU.

Regra dura deste repositório: **uma aresta só entra com a frase que a
sustenta**, copiada da fonte, com capítulo. Não há aresta por plausibilidade,
por consenso ou por memória — nem a minha, nem a de um modelo.

O mapa começa quase vazio de propósito. Seis arestas lidas valem mais que
sessenta supostas, e a diferença aparece na página: cada seta abre a citação.
"""

FONTES = {
    "petzold": ("Charles Petzold, <i>Code: The Hidden Language of Computer "
                "Hardware and Software</i>, 2ª ed."),
    "sicp": ("Harold Abelson &amp; Gerald Jay Sussman, <i>Structure and "
             "Interpretation of Computer Programs</i>, 2ª ed."),
}

# nível: a altura do degrau na escada. Mesmo nível = mesma camada de abstração.
DEGRAUS = [
    ("rele",        "relé",                        0,
     "Um interruptor que outro circuito aciona. É o primeiro componente que "
     "deixa um circuito controlar outro — e é daí que tudo sobe."),
    ("porta",       "porta lógica",                1,
     "AND, OR, NOR, inversor. A partir daqui o assunto deixa de ser eletricidade "
     "e passa a ser lógica."),
    ("flipflop",    "flip-flop de nível",          2,
     "O primeiro circuito que <b>lembra</b>: a saída depende do que entrou "
     "antes, não só do que entra agora."),
    ("flipflop_b",  "flip-flop de borda",          3,
     "Lembra no <i>instante</i> da transição do relógio, e não enquanto ele "
     "está alto. É o que torna o tempo discreto."),
    ("contador",    "contador",                    4,
     "Conta pulsos de relógio. Vira o endereço que a máquina lê em seguida — "
     "o embrião do contador de programa."),
    ("registrador", "registrador (latch)",         4,
     "Guarda um byte e o devolve quando mandarem. É a memória de trabalho da "
     "máquina, não a de armazenamento."),
    ("maquina",     "máquina de registradores",    5,
     "Registradores e operações, mais um controlador que sequencia as "
     "operações. É onde a construção física encontra a descrição de linguagem."),
]

# (de, para, classe, fonte, referência, citação verificada)
ARESTAS = [
    ("rele", "porta", "definicao", "petzold", "cap. 8 — Relays and Gates",
     "…are made from relays, of course, but we don’t actually have to look at "
     "the relays anymore."),

    ("porta", "flipflop", "definicao", "petzold", "cap. 19 — An Assemblage of Memory",
     "…is made from an inverter, two AND gates, and two NOR gates: When the "
     "Clock input is 1, the Q output is the same as the Data input."),

    ("flipflop", "flipflop_b", "definicao", "petzold", "cap. 17 — Feedback and Flip-Flops",
     "…an edge-triggered D-type flip-flop [is made from] two stages of "
     "level-triggered D-type flip-flops, wired together…"),

    ("flipflop_b", "contador", "definicao", "petzold", "cap. 20 — Automating Arithmetic",
     "The counter providing the memory address is built from edge-triggered "
     "flip-flops, so it probably has a Clear input."),

    ("flipflop_b", "registrador", "definicao", "petzold", "cap. 20 — Automating Arithmetic",
     "The latch is built from edge-triggered flip-flops as well, and "
     "edge-triggered flip-flops have been used for generating the control signals."),

    ("registrador", "maquina", "definicao", "sicp", "§5.1 — Designing Register Machines",
     "To design a register machine, we must design its data paths (registers "
     "and operations) and the controller that sequences these operations. … If "
     "we view the arrows as wires and the X buttons as switches, the data-path "
     "diagram is very like the wiring diagram for a machine that could be "
     "constructed from electrical components."),
]

# A ÚNICA aresta com duas testemunhas independentes, de lados opostos da escada.
SEGUNDA_TESTEMUNHA = {
    ("registrador", "maquina"): ("petzold", "caps. 22–23 — Registers and Busses · CPU Control Signals",
     "…control signals, so called because they control these components to work "
     "together in executing instructions stored in memory. … The CPU control "
     "signals are the strings."),
}

# O que se sabe que existe e ainda NÃO foi lido. Aparece na página como buraco
# declarado — mapa que esconde o que falta mente sobre o próprio tamanho.
NAO_LIDO = [
    ("relé ← interruptor", "Petzold caps. 4–7"),
    ("somador ← portas lógicas", "Petzold cap. 14"),
    ("relógio ← oscilador", "Petzold cap. 18"),
    ("ULA ← somador e portas", "Petzold cap. 21"),
    ("instrução ← sinais de controle", "Petzold caps. 23–24"),
    ("sistema operacional ← máquina", "Petzold cap. 26"),
    ("assembler ← máquina de registradores", "SICP §5.2"),
    ("compilador ← assembler e avaliador", "SICP §5.5"),
    ("interpretação × compilação", "SICP §5.5.7"),
    ("paradigma como variação do avaliador", "SICP §§4.2–4.4"),
]
