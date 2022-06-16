from automata.fa.nfa import NFA
nfa = NFA(
    states = {'q0','q1','q2'},
    input_symbols = {'a','b'},
    transitions = {
        'q0':{'a':{'q0','q1'},'b':{'q0'}},
        'q1':{'b':{'q2'}},
        'q2':{}
        
        
    },
    initial_state = 'q0',
    final_states ={'q2'}
)
set = {'ababababab','aaaa','ababaaab'}
for s in set:
    if(nfa.accepts_input(s)):
        print(s)