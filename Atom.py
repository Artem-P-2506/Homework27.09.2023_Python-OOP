class Atom:
    def __init__(self, sign, name, numberOfProtons, numberOfNeutrons, numberOfElectrons, weight, valency):
        self._sign = sign
        self._name = name
        self._numberOfProtons = numberOfProtons
        self._numberOfNeutrons = numberOfNeutrons
        self._numberOfElectrons = numberOfElectrons
        self._weight = weight
        self._valency = valency

#GETTERS:
    def getSign(self):
        return self._sign

    def getName(self):
        return self._name

    def getNumberOfProtons(self):
        return self._numberOfProtons

    def getNumberOfNeutrons(self):
        return self._numberOfNeutrons

    def getNumberOfElectrons(self):
        return self._numberOfElectrons

    def getWeight(self):
        return self._weight

    def getValency(self):
        return self._valency

#SETTERS:
    def setNumberOfProtons(self, newNumberOfProtons):
        self._numberOfProtons = newNumberOfProtons

    def setNumberOfNeutrons(self, newNumberOfNeutrons):
        self._numberOfNeutrons = newNumberOfNeutrons

    def setNumberOfElectrons(self, newNumberOfElectrons):
        self._numberOfElectrons = newNumberOfElectrons

    def setWeight(self, newWeight):
        self._weight = newWeight

    def setValency(self, newValency):
        self._valency = newValency

#METHODS:
    def print(self):
        print("Число протонов: " + str(self.getNumberOfProtons()) + "\nЧисло нейтронов: " + str(self.getNumberOfNeutrons()) +
              "\nЧисло електронов: " + str(self.getNumberOfElectrons()) + "\nВес: " + str(self.getWeight()) + "g" +
              "\nВалентность: " + str(self.getValency()))