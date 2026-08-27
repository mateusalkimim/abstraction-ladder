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
    ("eletroima",   "eletroímã",                  -1,
     "Um pedaço de ferro que vira ímã enquanto passa corrente. É o único "
     "degrau que não é feito de outro degrau: abaixo dele começa a física."),
    ("rele",        "relé",                        0,
     "Um interruptor que outro circuito aciona. É o primeiro componente que "
     "deixa um circuito controlar outro — e é daí que tudo sobe."),
    ("porta",       "porta lógica",                1,
     "AND, OR, NOR, inversor. A partir daqui o assunto deixa de ser eletricidade "
     "e passa a ser lógica."),
    ("somador",     "somador",                     2,
     "Soma dois bits e passa o vai-um adiante. É a primeira peça que faz "
     "<b>conta</b>, e é feita só de portas."),
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
    ("eletroima", "rele", "construção", "petzold", 'cap. 7 — Telegraphs and Relays',
     'A relay is like a sounder in that an incoming current is used to power an electromagnet that pulls down a metal lever.'),
    ("rele", "porta", "construção", "petzold", 'cap. 8 — Relays and Gates',
     'These two relays wired in series are known as an AND gate because it is performing a Boolean AND operation.'),
    ("rele", "porta", "construção", "petzold", 'cap. 8 — Relays and Gates',
     'The next logic gate requires two relays that are wired in parallel, like this:'),
    ("rele", "porta", "construção", "petzold", 'cap. 8 — Relays and Gates',
     'A single relay wired in this way is called an inverter.'),
    ("porta", "somador", "construção", "petzold", 'cap. 14 — Adding with Logic Gates',
     'A half adder is an XOR gate and an AND gate'),
    ("porta", "flipflop", "construção", "petzold", 'cap. 19 — An Assemblage of Memory',
     'the level-triggered D-type flip-flop, which is made from an inverter, two AND gates, and two NOR gates'),
    ("flipflop", "flipflop_b", "construção", "petzold", 'cap. 17 — Feedback and Flip-Flops',
     'An edge-triggered D-type flip-flop is constructed from two stages of level-triggered D-type flip-flops, wired together this way:'),
    ("porta", "flipflop_b", "construção", "petzold", 'cap. 17 — Feedback and Flip-Flops',
     'Here’s the edge-triggered D-type flip-flop with preset and clear built entirely from six 3-input NOR gates and an inverter.'),
    ("flipflop_b", "contador", "construção", "petzold", 'cap. 20 — Automating Arithmetic',
     'This is a job for a counter built from a row of cascading flip-flops, such as the one you saw on page 237 of Chapter 17:'),
    ("flipflop_b", "registrador", "construção", "petzold", 'cap. 20 — Automating Arithmetic',
     'The counter providing the memory address is built from edge-triggered flip-flops, so it probably has a Clear input. The latch is built from edge-triggered flip-flops as well, and edge-triggered flip-flops have been used for generating the control signals.'),

    ("registrador", "maquina", "definição", "sicp", "§5.1 — Designing Register Machines",
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

# Construção POR DENTRO: a peça é feita de peças da MESMA camada, então não é
# degrau — é a textura do degrau. Mesma regra: só entra com a frase da fonte.
# degrau=None ⇒ verificado, mas ainda não pousou em degrau nenhum.
# (degrau, peça, feita de, fonte, referência, citação verificada)
CONSTRUCAO = [
    ('eletroima', 'magnet', 'iron bar, wrap it with a couple of hundred turns of thin insulated wire',
     "petzold", 'cap. 7 — Telegraphs and Relays',
     'If you take an iron bar, wrap it with a couple of hundred turns of thin insulated wire, and then run a current through the wire, the iron bar becomes a magnet.'),
    ('porta', 'NOR', 'an OR gate followed by an inverter',
     "petzold", 'cap. 8 — Relays and Gates',
     'The NOR is the same as an OR gate followed by an inverter.'),
    ('porta', 'NAND', 'the inverse of the AND gate',
     "petzold", 'cap. 8 — Relays and Gates',
     'The NAND gate is drawn just like the AND gate but with a circle at the output, meaning the output is the inverse of the AND gate:'),
    ('porta', 'inverter', 'a NAND gate',
     "petzold", 'cap. 8 — Relays and Gates',
     'For example, here’s how to combine the inputs of a NAND gate to create an inverter:'),
    ('porta', 'AND gate', 'an inverter and a NAND gate',
     "petzold", 'cap. 8 — Relays and Gates',
     'You can use that inverter on the output of another NAND gate to make an AND gate.'),
    ('porta', 'XOR gate', 'an OR gate, a NAND gate, and an AND gate',
     "petzold", 'cap. 14 — Adding with Logic Gates',
     'The XOR gate is actually a combination of an OR gate, a NAND gate, and an AND gate'),
    ('somador', 'full adder', 'two half adders and an OR gate',
     "petzold", 'cap. 14 — Adding with Logic Gates',
     'Each full adder is two half adders and an OR gate'),
    ('registrador', '8-bit latch', 'flip-flops',
     "petzold", 'cap. 20 — Automating Arithmetic',
     'As you’ll recall, an 8-bit latch uses flip-flops to store an 8-bit value.'),
    ('registrador', 'register array', 'seven latches and seven tri-state buffers',
     "petzold", 'cap. 22 — Registers and Busses',
     'The following circuit contains seven latches and seven tri-state buffers. One 3-to-8 decoder is used to latch the incoming value into one of the registers, and another 3-to-8 decoder is used to enable one of the tri-state buffers to select a value from one of the registers:'),
    ('registrador', 'register array', 'latches for seven registers identified by the letters A, B, C, D, E, H, and L',
     "petzold", 'cap. 23 — CPU Control Signals',
     'The register array contains latches for seven registers identified by the letters A, B, C, D, E, H, and L.'),
    ('maquina', 'Triple-Byte Accumulator', 'a counter to access memory, an adder, and latches',
     "petzold", 'cap. 21 — The Arithmetic Logic Unit',
     'Chapter 20 described a Triple-Byte Accumulator that consisted of a counter to access memory, an adder, and latches.'),
    (None, 'seven-segment decoder', 'BCD decoder',
     "petzold", 'cap. 18 — Let’s Build a Clock!',
     'If your seven-segment display will always be displaying a digit, then a seven-segment decoder can be built from a BCD decoder as shown here:'),
    (None, 'byte of memory', '8 bits of memory',
     "petzold", 'cap. 19 — An Assemblage of Memory',
     'it’s fairly easy to assemble an entire byte of memory by wiring together 8 bits of memory.'),
    (None, '8×8 RAM array', 'eight 8×1 RAM arrays',
     "petzold", 'cap. 19 — An Assemblage of Memory',
     'if you have eight 8×1 RAM arrays and you connect all the Address signals together and all the Write signals together, you can make an 8×8 RAM array'),
    (None, '16×8 RAM array', '16 of these 16×8 memory arrays',
     "petzold", 'cap. 19 — An Assemblage of Memory',
     'you’ll need 16 of these 16×8 memory arrays, wired up like this'),
    (None, 'the entire arithmetic logic unit', 'the Add/Subtract module and the Logic module',
     "petzold", 'cap. 21 — The Arithmetic Logic Unit',
     'The entire arithmetic logic unit combines the Add/Subtract module and the Logic module with some rather messy support circuity:'),
    (None, 'PSW', 'accumulator and ALU flags',
     "petzold", 'cap. 24 — Loops, Jumps, and Calls',
     'It’s just the accumulator in one byte and the ALU flags in another byte.'),

    # Rótulo corrigido no julgamento (circular, anafórico ou duplicado);
    # a citação é a mesma que passou no portão, intacta.
    (None, 'speaker wire', 'a pair of two insulated wires',
     "petzold", 'cap. 5 — Communicating Around Corners',
     'Speaker wire consists of a pair of two insulated wires conveniently stuck together, so it’s a good choice for our telegraph system.'),
    ('porta', 'prewired gate bank', 'relays',
     "petzold", 'cap. 14 — Adding with Logic Gates',
     'relays that have been prewired into various logic gates'),
    ('porta', 'logic gate', 'two relays',
     "petzold", 'cap. 14 — Adding with Logic Gates',
     'each of those gates consists of two relays'),
    (None, 'oscillator', 'quartz crystals',
     "petzold", 'cap. 17 — Feedback and Flip-Flops',
     'The oscillators in real computers are somewhat more sophisticated, however, consisting of quartz crystals wired in such a way that they vibrate very consistently and very quickly.'),
    (None, 'transistor', 'base, collector, and emitter',
     "petzold", 'cap. 18 — Let’s Build a Clock!',
     'The three letters stand for base, collector, and emitter.'),
    ('registrador', 'register', '8-bit latch',
     "petzold", 'cap. 22 — Registers and Busses',
     'These latches are called registers, and a primary purpose of these registers is to store bytes as they are processed by the ALU.'),
    ('registrador', '16-bit address', 'H and L registers',
     "petzold", 'cap. 22 — Registers and Busses',
     'The H and L registers form a 16-bit address—for example, in the MOV A,M instruction. When used in this way, HL is called a register pair.'),
]

# O que se sabe que existe e ainda NÃO foi lido. Aparece na página como buraco
# declarado — mapa que esconde o que falta mente sobre o próprio tamanho.
NAO_LIDO = [
    ("eletroímã ← corrente e ferro", "Petzold cap. 6"),
    ("relógio ← oscilador", "Petzold cap. 18"),
    ("memória (RAM) ← registrador", "Petzold cap. 19"),
    ("ULA ← somador e portas", "Petzold cap. 21"),
    ("instrução ← sinais de controle", "Petzold caps. 23–24"),
    ("sistema operacional ← máquina", "Petzold cap. 26"),
    ("assembler ← máquina de registradores", "SICP §5.2"),
    ("compilador ← assembler e avaliador", "SICP §5.5"),
    ("interpretação × compilação", "SICP §5.5.7"),
    ("paradigma como variação do avaliador", "SICP §§4.2–4.4"),
]
