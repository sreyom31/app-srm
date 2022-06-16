from automata.fa.dfa import DFA
dfa = DFA(
    states = {'q0','q1','q2','d'},
    input_symbols = {'0','1'},
    transitions = {
        'q0':{'0':'q2','1':'q1'},
        'q1':{'0':'q2','1':'q1'},
        'q2':{'0':'d','1':'q1'},
        'd':{'0':'d','1':'d'}
    },
    initial_state = 'q0',
    final_states ={'q2','q1'}
)
if(dfa.accepts_input('011001')):
    print("accepted")
else :print("rejected")