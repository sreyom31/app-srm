from automata.fa.dfa import DFA
dfa = DFA(
    states = {'q0','q1','q2','d','e'},
    input_symbols = {'0','1'},
    transitions = {
        'q0':{'0':'e','1':'q1'},
        'q1':{'0':'q2','1':'e'},
        'q2':{'0':'e','1':'d'},
        'd':{'0':'e','1':'e'},
        'e':{'0':'e','1':'e'} 
    },
    initial_state = 'q0',
    final_states ={'d'}
)
set = {'11100','101','110101010110','10101101110'}
for s in set:
    if(dfa.accepts_input(s)):
        print(s)