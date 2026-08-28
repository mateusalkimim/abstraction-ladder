# -*- coding: utf-8 -*-
"""Os quatro campos de cada degrau — o que ele É, por que EXISTE, onde APARECE
e onde o leitor TRAVA.

Por que este arquivo existe
---------------------------
O `degraus.py` responde *como a escada se sustenta*: cada aresta com a frase do
livro. Ele não responde *o que a peça é* — e a página, por isso, nomeava 33
componentes que nunca definia. Este arquivo paga essa dívida.

A REGRA, e ela é o motivo de o arquivo não ter sido gerado por modelo
---------------------------------------------------------------------
O mapa irmão desta casa, o `math-prerequisite-map`, tem estes mesmos quatro
campos escritos por um phi-4 local, e **um deles afirma, no ar até hoje, que
dois conjuntos com os mesmos elementos podem ser diferentes**. É falso, e passou
porque ninguém leu. Copiar aquele molde traria para cá exatamente o defeito que
este repositório existe para recusar.

A saída, neste domínio, é que **não é preciso modelo nenhum**: o Petzold é
professor, e o livro já responde *o que é* e *por que existe*, em prosa, com
capítulo. Então cada campo carrega a sua classe:

  (a) CITAÇÃO — o campo é tradução fiel de uma passagem, e a passagem vai junto;
  (b) SÍNTESE — o campo é resumo meu de passagem citada, e a passagem vai junto
      para o leitor conferir se o resumo é honesto;
  (d) OFÍCIO  — julgamento didático de quem ensina. Nenhum livro escreve "onde
      o aluno trava"; isso vem da sala de aula. **Entra como PROPOSTA e a
      página o marca como tal até o operador ratificar** — rito da casa:
      norma é proposta + ratificação, e conteúdo não é diferente.

Não há classe para "o modelo escreveu". Se um campo não tem fonte nem dono, ele
não entra — fica em branco, e a página diz que está em branco.

Fonte da prosa citada: o `livro.md` da dissecação `petzold-code-2ed` do
Mouseion (classe A, epub nato-digital), conferido capítulo a capítulo.
"""

# (texto em português, classe, referência, passagem original)
# classe: "a" citação · "b" síntese de passagem citada · "d" ofício (PROPOSTA)
C = lambda t, ref, cit: (t, "a", ref, cit)
S = lambda t, ref, cit: (t, "b", ref, cit)
O = lambda t: (t, "d", None, None)

CONCEITOS = {

"eletroima": {
 "o_que_e": C(
   "Uma barra de ferro que vira ímã enquanto passa corrente pelo fio enrolado "
   "nela.",
   "cap. 7 — Telegraphs and Relays",
   "If you take an iron bar, wrap it with a couple of hundred turns of thin "
   "insulated wire, and then run a current through the wire, the iron bar "
   "becomes a magnet."),
 "por_que_existe": S(
   "Porque é o jeito de a eletricidade <b>puxar</b> alguma coisa. Morse "
   "precisava de um sinal que agisse à distância e não podia usar lâmpada: a "
   "lâmpada prática só apareceria em 1879. Restou o magnetismo.",
   "cap. 7 — Telegraphs and Relays",
   "Morse couldn’t use a lightbulb as his signaling device because a practical "
   "one wouldn’t be invented until 1879. Instead, Morse relied upon the "
   "phenomenon of electromagnetism."),
 "onde_aparece": O(
   "A campainha da sua porta, a tranca elétrica do portão, o alto-falante que "
   "está tocando agora, o disjuntor que desarma o quadro. E o relé — que é o "
   "degrau seguinte."),
 "onde_se_trava": O(
   "Ele não <i>é</i> ímã: é ímã <b>enquanto</b> passa corrente. Quem lê “vira "
   "ímã” e guarda “é ímã” perde a única propriedade que importa, que é ele "
   "<b>desligar</b>. Toda a escada acima depende de desligar."),
},

"rele": {
 "o_que_e": C(
   "Um eletroímã que puxa uma alavanca de metal, e a alavanca é parte de um "
   "interruptor que liga uma bateria a um fio de saída.",
   "cap. 7 — Telegraphs and Relays",
   "A relay is like a sounder in that an incoming current is used to power an "
   "electromagnet that pulls down a metal lever. The lever, however, is used "
   "as part of a switch connecting a battery to an outgoing wire."),
 "por_que_existe": S(
   "Porque fio tem resistência: quanto mais longo, mais ele engole o sinal, e "
   "a linha telegráfica não podia crescer indefinidamente. O relé escuta o "
   "sinal fraco que sobrou e usa uma bateria <b>local</b> para reemitir forte. "
   "Ele não conserta o fio — ele recomeça o sinal.",
   "cap. 7 — Telegraphs and Relays",
   "the longer a length of wire becomes, the more resistance it has to the "
   "flow of electricity. This was a major impediment to long-distance "
   "telegraphy. … In this way, a weak incoming current is “amplified” to make "
   "a stronger outgoing current."),
 "onde_aparece": S(
   "A partida do seu carro, o contator do ar-condicionado, o painel de "
   "automação de um galpão. E, historicamente, o computador inteiro.",
   "cap. 7 — Telegraphs and Relays",
   "It’s a switch, surely, but a switch that’s turned on and off not by human "
   "hands but by an electrical current. You could do amazing things with such "
   "devices. You could actually assemble much of a computer with them."),
 "onde_se_trava": O(
   "O circuito que <b>comanda</b> e o circuito <b>comandado</b> são dois "
   "circuitos separados, que não se encostam — só o campo magnético atravessa. "
   "Quem funde os dois num só não consegue enxergar por que dá para encadear "
   "relé em relé. E encadear é tudo o que vem depois."),
},

"porta": {
 "o_que_e": C(
   "O componente em que a álgebra de Boole encontra a eletricidade: ele faz "
   "operação lógica <b>bloqueando ou deixando passar</b> a corrente.",
   "cap. 8 — Relays and Gates",
   "Reduced to its essentials, a computer is a synthesis of Boolean algebra "
   "and electricity. The crucial components that embody this melding of math "
   "and hardware are known as logic gates. … Logic gates perform simple "
   "operations in Boolean logic by blocking or letting through the flow of "
   "electrical current."),
 "por_que_existe": S(
   "Dois relés em série só acendem a lâmpada se os <b>dois</b> estiverem "
   "acionados — o E de Boole, feito de metal. E a vantagem do relé sobre o "
   "interruptor é que ele é ligado por outro relé, não por um dedo: é isso, e "
   "só isso, que permite combinar porta com porta até virar aritmética.",
   "cap. 8 — Relays and Gates",
   "Relays have an advantage over switches in that relays can be switched on "
   "and off by other relays rather than by fingers. This means that logic "
   "gates can be combined to perform more complex tasks, such as simple "
   "functions in arithmetic and, eventually, the workings of entire computers."),
 "onde_aparece": O(
   "Toda condição de todo programa que você já escreveu. O <code>if (a &amp;&amp; b)</code> "
   "da sua última função é esta porta, com sessenta anos de camadas em cima."),
 "onde_se_trava": O(
   "Aqui <b>nada mudou fisicamente</b> — mudou a descrição. Continua sendo "
   "corrente atravessando metal; o que passou a existir foi <i>chamar</i> "
   "aquilo de verdadeiro e falso. Este é o primeiro salto de abstração da "
   "escada, e é o mais fácil de atravessar sem perceber que se atravessou — "
   "por isso quem pula aqui não entende mais nada lá em cima."),
},

"somador": {
 "o_que_e": C(
   "Soma dois bits e devolve <b>dois</b>: o bit da soma e o bit do vai-um.",
   "cap. 14 — Adding with Logic Gates",
   "adding a pair of binary numbers results in two bits, which are called the "
   "sum bit and the carry bit (as in “1 plus 1 equals 0, carry the 1”)"),
 "por_que_existe": S(
   "Porque somar uma coluna só não basta. Da segunda coluna em diante são "
   "<b>três</b> bits para somar: os dois da coluna mais o vai-um que veio da "
   "anterior. É essa terceira entrada que separa o meio-somador do somador "
   "completo.",
   "cap. 14 — Adding with Logic Gates",
   "We can use the half adder only for the addition of the rightmost column: 1 "
   "plus 1 equals 0, carry the 1. For the second column from the right, we "
   "really need to add three binary numbers because of the carry. And that "
   "goes for all subsequent columns."),
 "onde_aparece": O(
   "Toda soma de todo processador do mundo, inclusive a que somou o índice do "
   "laço que você rodou hoje. Também é onde mora o estouro: o vai-um que sai "
   "da última coluna e não tem para onde ir."),
 "onde_se_trava": S(
   "A armadilha é tratar o somador como caixa-preta — entra isto, sai aquilo, "
   "não pergunte. O próprio Petzold corrige: como se sabe o que há dentro, o "
   "nome certo é <b>caixa transparente</b>. Quem aceita a caixa-preta aqui "
   "aceita em todos os degraus seguintes, e a escada inteira vira mágica.",
   "cap. 14 — Adding with Logic Gates",
   "Sometimes a box like this is called a black box. A particular combination "
   "of inputs results in particular outputs, but the implementation is hidden. "
   "But since we know what goes on inside the half adder, it’s more correctly "
   "termed a clear box."),
},

"flipflop": {
 "o_que_e": C(
   "O primeiro circuito com <b>dois estados estáveis</b> para a mesma entrada. "
   "Ele guarda informação: lembra qual chave foi fechada por último.",
   "cap. 17 — Feedback and Flip-Flops",
   "We can say that this circuit has two stable states when both switches are "
   "open. Such a circuit is called a flip-flop… A flip-flop circuit retains "
   "information. It “remembers.” It only remembers what switch was most "
   "recently closed, but that is significant."),
 "por_que_existe": O(
   "Até este degrau, a saída dependia só das entradas <i>de agora</i>. Sem "
   "memória não existe “antes”: não há conta acumulada, não há contagem, não "
   "há programa. Tudo o que a máquina faz com o tempo começa aqui."),
 "onde_aparece": S(
   "É de 1918, dos físicos de rádio Eccles e Jordan — anterior ao computador. "
   "Hoje: cada bit de cada registrador, e o antitrepidação de todo botão "
   "físico que você aperta.",
   "cap. 17 — Feedback and Flip-Flops",
   "The flip-flop dates from 1918 with the work of English radio physicists "
   "William Henry Eccles (1875–1966) and F.W. Jordan (1881–1941)."),
 "onde_se_trava": S(
   "A realimentação. A saída volta e vira entrada, então <b>não existe um "
   "primeiro instante</b> por onde começar a traçar o sinal. Quem tenta seguir "
   "em ordem cronológica entra em looping e conclui que não entendeu. O jeito "
   "de ler é outro: parar de seguir o caminho e procurar quais combinações "
   "<i>se sustentam</i> — os estados estáveis.",
   "cap. 17 — Feedback and Flip-Flops",
   "The output of the NOR gate on the left is an input to the NOR gate on the "
   "right, and the output of that NOR gate is an input to the first NOR gate. "
   "This is a type of feedback. Indeed, just as in the oscillator, an output "
   "circles back to become an input."),
},

"flipflop_b": {
 "o_que_e": C(
   "Guarda o dado no <b>instante da transição</b> do relógio, e não durante "
   "todo o tempo em que o relógio está alto. Por dentro, são dois flip-flops "
   "de nível em série.",
   "cap. 17 — Feedback and Flip-Flops",
   "An edge-triggered D-type flip-flop is constructed from two stages of "
   "level-triggered D-type flip-flops, wired together this way:"),
 "por_que_existe": C(
   "Porque o de nível <b>vaza</b>. Enquanto o relógio está em 1, o dado pode "
   "mudar — e essas mudanças atravessam para a saída. Num circuito que "
   "realimenta a própria saída, isso vira laço infinito.",
   "cap. 17 — Feedback and Flip-Flops",
   "This is what’s called an “infinite loop.” It occurs because the D-type "
   "flip-flop we designed was level-triggered. The Clock input must change its "
   "level from 0 to 1 in order for the value of the Data input to be stored in "
   "the latch. But during the time that the Clock input is 1, the Data input "
   "can change, and those changes will be reflected in the values of the "
   "outputs."),
 "onde_aparece": O(
   "Todo “clock” de que se fala em processador. Os 3,6 GHz da sua máquina são "
   "3,6 bilhões dessas bordas por segundo — não 3,6 bilhões de instantes em "
   "que o relógio está ligado."),
 "onde_se_trava": O(
   "O modelo errado é “o relógio <b>habilita</b> o circuito”. Não é: o evento "
   "é a <b>transição</b>, não o estado. Enquanto o relógio for lido como uma "
   "chave que fica ligada um tempo, o contador não faz sentido nenhum — e "
   "quase todo mundo carrega esse modelo errado sem nunca ter sido corrigido, "
   "porque em prosa os dois soam iguais."),
},

"contador": {
 "o_que_e": C(
   "Uma fileira de flip-flops de borda em cascata: cada um dispara o seguinte, "
   "e a fileira lida em binário conta os pulsos do relógio.",
   "cap. 20 — Automating Arithmetic",
   "This is a job for a counter built from a row of cascading flip-flops, such "
   "as the one you saw on page 237 of Chapter 17:"),
 "por_que_existe": O(
   "Porque a máquina precisa saber <b>qual é a próxima</b>. O número que o "
   "contador guarda vira o endereço que ela vai ler em seguida — é o embrião "
   "do contador de programa."),
 "onde_aparece": O(
   "O <code>PC</code> que o depurador te mostra parado numa linha. O relógio "
   "digital da parede. E o índice do laço, uma camada acima."),
 "onde_se_trava": O(
   "Ninguém <i>projetou</i> a contagem binária: ela <b>aparece</b> de graça "
   "quando se encadeia flip-flop em flip-flop, porque cada um vira na metade "
   "da frequência do anterior. Quem procura a peça que “faz a conta” não acha, "
   "e conclui que faltou alguma coisa. Não faltou — a conta é a fiação."),
},

"registrador": {
 "o_que_e": C(
   "Um latch de 8 bits que o processador comanda por instrução. Guarda bytes "
   "enquanto a ULA trabalha neles.",
   "cap. 22 — Registers and Busses",
   "These latches are called registers, and a primary purpose of these "
   "registers is to store bytes as they are processed by the ALU."),
 "por_que_existe": O(
   "Porque a ULA precisa de algum lugar para pousar os operandos e o resultado "
   "<b>dentro</b> do processador. Ir buscar na memória a cada passo custaria "
   "uma viagem pelo barramento a cada conta."),
 "onde_aparece": O(
   "Quando a ficha de um processador diz “16 registradores de 64 bits”, são "
   "estes. E é o que o compilador está disputando quando decide o que fica "
   "perto e o que vai para a memória."),
 "onde_se_trava": O(
   "Achar que registrador é só uma memória pequena. A diferença não é de "
   "tamanho, é de <b>endereçamento</b>: memória se acessa por endereço "
   "calculado; registrador se nomeia na própria instrução. Por isso um cabe "
   "numa instrução e o outro não."),
},

"maquina": {
 "o_que_e": C(
   "Caminhos de dados — registradores e operações — mais um <b>controlador</b> "
   "que põe as operações em sequência. Vista assim, ela é literalmente um "
   "diagrama de fiação.",
   "SICP §5.1 — Designing Register Machines",
   "To design a register machine, we must design its data paths (registers and "
   "operations) and the controller that sequences these operations. … If we "
   "view the arrows as wires and the X buttons as switches, the data-path "
   "diagram is very like the wiring diagram for a machine that could be "
   "constructed from electrical components."),
 "por_que_existe": S(
   "Porque peça solta não faz nada em ordem. O que faltava era um sinal que "
   "mandasse as peças trabalharem <b>juntas</b> para executar uma instrução "
   "guardada na memória — e é esse sinal que costura a máquina.",
   "caps. 22–23 — Registers and Busses · CPU Control Signals",
   "…control signals, so called because they control these components to work "
   "together in executing instructions stored in memory. … The CPU control "
   "signals are the strings."),
 "onde_aparece": O(
   "É o degrau em que a construção física encontra a descrição de linguagem: "
   "daqui para cima fala-se em instrução, montador, compilador. Abaixo, em "
   "fio."),
 "onde_se_trava": O(
   "O “controlador” soa como alguém que decide. Não é: ele é <b>mais "
   "circuito</b> — contador, decodificador e portas, feitos das mesmas peças "
   "de baixo. Enquanto restar um homenzinho dentro da máquina, a escada não "
   "fechou; e é justamente aqui que quase todo curso para de descer."),
},

}

# Os quatro campos, na ordem em que a página os mostra, com o rótulo.
CAMPOS = [
    ("o_que_e",       "o que é"),
    ("por_que_existe","por que existe"),
    ("onde_aparece",  "onde aparece"),
    ("onde_se_trava", "onde se trava"),
]

CLASSES = {
    "a": ("citação",  "o campo é tradução fiel da passagem ao lado"),
    "b": ("síntese",  "resumo de passagem citada — a passagem vai junto para conferir"),
    "d": ("ofício",   "julgamento de quem ensina; nenhum livro escreve isto. "
                      "PROPOSTA — aguarda ratificação do operador"),
}
