from automata.fa.nfa import NFA
nfa = NFA(
    states = {'q0','q1','q2','q3','q4'},
    input_symbols = {'0','1'},
    transitions = {
        'q0':{'0':{'q1','q3'}},
        'q1':{'1':{'q2'}},
        'q2':{'0':{'q1','q3'}},
        'q3':{'1':{'q4'}},
        'q4':{'0':{'q2'}}
    },
    initial_state = 'q0',
    final_states ={'q2'}
)
set = {'1010111','010','1010'}
for s in set:
    if(nfa.accepts_input(s)):
        print(s)
