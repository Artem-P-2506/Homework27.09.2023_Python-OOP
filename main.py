from Atom import *
from Molecule import *

if __name__ == "__main__":
#Молекула воды (H2O):
    atomH1 = Atom('H', 'Водород', 1, 0, 1, 1.00797, 1)
    atomH2 = Atom('H', 'Водород', 1, 0, 1, 1.00797, 1)
    atomO1 = Atom('O', 'Кислород', 8, 8, 8, 15.9994, 2)
    moleculeH2O = Molecule('Вода', [atomH1, atomH2, atomO1])
    moleculeH2O.showAtoms()

#Молекула углевода (C6H12O6):
    atomC1 = Atom('C', 'Углерод', 6, 6, 6, 12.011, 4)
    atomC2 = Atom('C', 'Углерод', 6, 6, 6, 12.011, 4)
    atomC3 = Atom('C', 'Углерод', 6, 6, 6, 12.011, 4)
    atomC4 = Atom('C', 'Углерод', 6, 6, 6, 12.011, 4)
    atomC5 = Atom('C', 'Углерод', 6, 6, 6, 12.011, 4)
    atomC6 = Atom('C', 'Углерод', 6, 6, 6, 12.011, 4)
    atomH1 = Atom('H', 'Водород', 1, 0, 1, 1.00797, 1)
    atomH2 = Atom('H', 'Водород', 1, 0, 1, 1.00797, 1)
    atomH3 = Atom('H', 'Водород', 1, 0, 1, 1.00797, 1)
    atomH4 = Atom('H', 'Водород', 1, 0, 1, 1.00797, 1)
    atomH5 = Atom('H', 'Водород', 1, 0, 1, 1.00797, 1)
    atomH6 = Atom('H', 'Водород', 1, 0, 1, 1.00797, 1)
    atomH7 = Atom('H', 'Водород', 1, 0, 1, 1.00797, 1)
    atomH8 = Atom('H', 'Водород', 1, 0, 1, 1.00797, 1)
    atomH9 = Atom('H', 'Водород', 1, 0, 1, 1.00797, 1)
    atomH10 = Atom('H', 'Водород', 1, 0, 1, 1.00797, 1)
    atomH11 = Atom('H', 'Водород', 1, 0, 1, 1.00797, 1)
    atomH12 = Atom('H', 'Водород', 1, 0, 1, 1.00797, 1)
    atomO1 = Atom('O', 'Кислород', 8, 8, 8, 15.9994, 2)
    atomO2 = Atom('O', 'Кислород', 8, 8, 8, 15.9994, 2)
    atomO3 = Atom('O', 'Кислород', 8, 8, 8, 15.9994, 2)
    atomO4 = Atom('O', 'Кислород', 8, 8, 8, 15.9994, 2)
    atomO5 = Atom('O', 'Кислород', 8, 8, 8, 15.9994, 2)
    atomO6 = Atom('O', 'Кислород', 8, 8, 8, 15.9994, 2)
    moleculeC6H12O6 = Molecule('Углевод', [atomC1, atomC2, atomC3, atomC4, atomC5, atomC6, atomH1, atomH2, atomH3, atomH4, atomH5, atomH6, atomH7, atomH8, atomH9, atomH10, atomH11, atomH12, atomO1, atomO2, atomO3, atomO4, atomO5, atomO6])
    moleculeC6H12O6.showAtoms()