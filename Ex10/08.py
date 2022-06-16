from automata.fa.nfa import NFA
nfa = NFA(
    states = {'q0','q1','q2','q3','q4'},
    input_symbols = {'a','b'},
    transitions = {
        'q0':{'a':{'q1','q3'}},
        'q1':{'b':{'q2'}},
        'q2':{'b':{'q4'},'a':{'q1'}},
        'q3':{'a':{'q3'}},
        'q4':{'a':{'q2'}}
    },
    initial_state = 'q0',
    final_states ={'q2','q3'}
)
set = {'aaaabaaba','abababab','aaaaaa'}
for s in set:
    if(nfa.accepts_input(s)):
        print(s)