class Classifier:
    def __init__(self, dependentClass):
        self.dependentClass = dependentClass

    def classify(self, word):
        if not self.dependentClass.dependentFunction():
            return "WRONG"

        if word == "yes":
            return "say what"
        else:
            return "oh no"

class DependentClass:
    def dependentFunction(self):
        return False
