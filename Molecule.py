class Molecule:
    def __init__(self, name, atoms):
        self._name = name
        self._atoms = atoms

    def getName(self):
        return self._name

    def setName(self, newName):
        self._name = newName

    def getAtoms(self):
        return self._atoms

    def showAtoms(self):
        print(f"\n-=-=-=-=-=- Молекула: {self.getName()} -=-=-=-=-=-")
        i = 1
        for atom in self._atoms:
            print(f"\n\tАтом №{i}: {atom.getSign()}-{atom.getName()}")
            atom.print()
            i += 1