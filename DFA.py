"""
Name: Christopher Montoya, Kassidy Maberry
Date: 2024/02/15
Assignment 2 
"""

"""
Handles the entire DFA machine.
"""
class DFA:

    """
    Inits the DFA
    """
    def __init__(self, file):
        States = {}
        z = []
        fp = open(file)
        z = fp.readlines()[1:] # We don't need the first line.
        l = len(z)
        for line in range(l):
            States[line] = DFAstate(line, z[line].split(" ")[0], z[line].split(" ")[1])

        for x in range(len(z)):
            States[x].anext = States[States[x].a]
            States[x].bnext = States[States[x].b]

        self.start = States[0]



"""
Handles a single DFA state. 
"""
class DFAstate:
    """
    Inits a DFA state.
    """
    def __init__(self, name, a, b):
        self.name = int(name)
        self.a = int (a)
        self.b = int (b)
        self.anext = None
        self.bnext = None

"""
Prints out the DFA trace.
Takes in a DFA starting state, a empty string, and a empty list to keep track of what's been visited.


"""
def DFATrace(M, S = "", trace = []):
    if trace.count(M.name) > 0:
        repeat = trace.index(M.name)
        print("\t" * len(S), end="")
        print("x =", S[:repeat])

        print("\t" * len(S), end="")
        print("y =", S[repeat:])
        

        print("\t" * len(S), end="")
        print("z = rest")
        return ""
    
    Sa = S + "a"
    Sb = S + "b"
    trace.append(M.name)

    print("\t" * len(S), end="")
    print("if a:")
    DFATrace(M.anext, Sa, trace)


    print("\t" * len(S), end="") 
    print("if b:")
    DFATrace(M.bnext, Sb, trace) # There is an issue with this part. Doesn't do a trace here. It's probably because trace isn't being reset.
    return ""


def main():
    Machine = DFA("hw2test.txt")
    DFATrace(Machine.start)


if __name__ == "__main__":
    main()