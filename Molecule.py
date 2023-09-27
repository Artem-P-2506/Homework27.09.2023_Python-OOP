class Molecule:
    def __init__(self, sign ,name, atoms):
        self._sign = sign
        self._name = name
        self._atoms = atoms

#GETTERS
    def getSign(self):
        return self._sign

    def getName(self):
        return self._name

    def getAtoms(self):
        return self._atoms

#SETTERS
    def setSign(self, newSign):
        self._sign = newSign

    def setName(self, newName):
        self._name = newName

#METHODS
    def showAtoms(self):
        print(f"-=-=-=-=-=-=-=-=- Молекула: {self.getSign()} - {self.getName()} -=-=-=-=-=-=-=-=-")
        i = 1
        for atom in self._atoms:
            print(f"\n\tАтом №{i}: {atom.getSign()} - {atom.getName()}")
            atom.print()
            i += 1