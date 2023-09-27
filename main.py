from Atom import *
from Molecule import *

if __name__ == "__main__":
#Атомы:
    atomH = Atom('H', 'Водород', 1, 0, 1, 1.00797, 1)
    atomO = Atom('O', 'Кислород', 8, 8, 8, 15.9994, 2)
    atomC = Atom('C', 'Углерод', 6, 6, 6, 12.011, 4)
    atomK = Atom('K', 'Калий', 19, 20, 19, 39.102, 1)

    choise = input("Информацию про какую молекулу вывести?\nH20 - '1'  |  C6H12O6 - '2'  |  K - '3'\nВыбор: ")
    if choise == '1': #Молекула воды (H2O):
        moleculeH2O = Molecule('H2O', 'Вода', [atomH, atomH, atomO])
        moleculeH2O.showAtoms()
    elif choise == '2': #Молекула углевода (C6H12O6):
        moleculeC6H12O6 = Molecule('C6H12O6', 'Углевод', [atomC, atomC, atomC, atomC, atomC, atomC, atomH, atomH, atomH, atomH, atomH, atomH,
                                                            atomH, atomH, atomH, atomH, atomH, atomH, atomO, atomO, atomO, atomO, atomO, atomO])
        moleculeC6H12O6.showAtoms()
    elif choise == '3': #Молекула калия (K):
        moleculeK = Molecule('K', 'Калий', [atomK])
        moleculeK.showAtoms()
    else:
        print("Wrong input!")