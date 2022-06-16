from automata.fa.nfa import NFA
nfa = NFA(
    states = {'q0','q1','q2','d'},
    input_symbols = {'a','b'},
    transitions = {
        'q0':{'a':{'q0','q1'},'b':{'q0'}},
        'q1':{'a':{'q2'}},
        'q2':{'b':{'d'}},
        'd':{} 
    },
    initial_state = 'q0',
    final_states ={'d'}
)
set = {'aaaabaaba','abababaaab','abababa'}
for s in set:
    if(nfa.accepts_input(s)):
        print(s)