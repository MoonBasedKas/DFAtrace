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
        for line in range(len(z)):
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



def main():
    Machine = DFA("DFA.txt")

    print(Machine.start.bnext.bnext.name)
    pass


if __name__ == "__main__":
    main()