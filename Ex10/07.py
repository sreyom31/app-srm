from automata.fa.nfa import NFA
nfa = NFA(
    states = {'q0','q1','q2','q3','q4','q5'},
    input_symbols = {'0','1'},
    transitions = {
        'q0':{'':{'q1','q3'}},
        'q1':{'0':{'q2'},'1':{'q1'}},
        'q2':{'0':{'q1'},'1':{'q2'}},
        'q3':{'0':{'q3'},'1':{'q5'}},
        'q4':{'0':{'q4'},'1':{'q3'}},
        'q5':{'0':{'q5'},'1':{'q4'}}
    },
    initial_state = 'q0',
    final_states ={'q2','q3'}
)
set = {'000101010101','101010101','111111'}
for s in set:
    if(nfa.accepts_input(s)):
        print(s)
