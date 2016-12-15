class Automaton(object):
    
    @staticmethod
    def read_commands(commands):
        cmds = {'q1':[{'0':'q1','1':'q2'}],
                'q2':[{'0':'q3','1':'q2'}],
                'q3':[{'0':'q2','1':'q2'}]}
        curr_state = 'q1'
        for c in commands:
            curr_state = cmds[curr_state][0][c]
        return True if curr_state == 'q2' else False

my_automaton = Automaton()

if __name__ == '__main__':

  a = Automaton()
  # Do anything you need to set up this automaton's states.
  is_accepted = a.read_commands(["1", "0", "0", "1", "0"])
