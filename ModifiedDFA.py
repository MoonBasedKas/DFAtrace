"""
Name: Christopher Montoya, Kassidy Maberry
Date: 2024/02/15
Assignment 2 
"""

import itertools

class DFA:
    def __init__(self, num_states, edge_directions):
        self.num_states = num_states
        self.states = []
        for i in range(0, len(edge_directions)):
            self.states.append(DFAEdge(i, edge_directions[i]))

    def detect_loop(self, trace: list):
        for i in range (0, len(trace)):
            for j in range (i, len(trace)):
                if (trace[i] == trace[j] and i != j):
                    x = trace[:i]
                    y = trace[i:j+1]
                    z = trace[j+1:]
                    print(f"x: {x}\ny: {y}\nz: {z}")
                    return True
        return False

    # Method that will print out the DFA trace for an input string
    def __call__(self, string):
        chars = list(string)
        curr_state = 0
        trace = [0]
        # print(curr_state)
        for i in range(0, len(chars)):
            # Getting the edges for the current state
            state_edges = self.states[curr_state]
            # Feeding the current letter to the current state edges to find the next state
            next_state = state_edges(chars[i])
            # Updating the current state
            curr_state = next_state
            # Appending the current state to the loop list for detecting loops
            trace.append(curr_state)
            # Printing out the trace, for debugging
            # print(curr_state)
        self.detect_loop(trace)
                
            

class DFAEdge:
    def __init__(self, state_num, direction) -> None:
        self.state_num = state_num
        x = direction.split(' ')
        # on a go to...
        self.a_direction = int (x[0])
        # on b go to...
        self.b_direction = int (x[1])
    
    def __call__(self, char):
        if (char == 'a'):
            return self.a_direction
        else:
            return self.b_direction


def generate_strings(length):
    chars = "ab"
    strings = []
    for item in itertools.product(chars, repeat=length):
        print("".join(item))
        strings.append("".join(item))
    return strings

def read_file(file_name):
    with open(file_name, "r") as file:
        num_states = file.readline()
        lines = file.readlines()
        for i in range(0,len(lines)):
            lines[i] = lines[i].strip('\n')
    return num_states, lines

def main():
    num_states, directions = read_file("hw2test.txt")
    automata = DFA(num_states, directions)
    automata("aabb")
    pass


if __name__ == "__main__":
    main()