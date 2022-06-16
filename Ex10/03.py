from automata.fa.dfa import DFA
dfa = DFA(
    states = {'q0','q1','q2','d'},
    input_symbols = {'0','1'},
    transitions = {
        'q0':{'0':'q1','1':'d'},
        'q1':{'0':'q0','1':'q2'},
        'q2':{'0':'d','1':'q1'},
        'd':{'0':'q2','1':'q0'} 
    },
    initial_state = 'q0',
    final_states ={'q0'}
)
set = {'111100','010101','110101010110','10101101110'}
for s in set:
    if(dfa.accepts_input(s)):
        print(s)