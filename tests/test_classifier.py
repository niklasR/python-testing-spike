import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from mock import MagicMock
from lib.classifier import Classifier, DependentClass

dependentClassThing = DependentClass()
dependentClassThing.dependentFunction = MagicMock(return_value=True)
classifierThing = Classifier(dependentClassThing)

class MyTest(unittest.TestCase):
    def test_classify_works_no(self):
        self.assertEqual(classifierThing.classify("no"), "oh no")

    def test_classify_works_yes(self):
        self.assertEqual(classifierThing.classify("yes"), "say what")

    def test_classify_failingtest(self):
        self.assertEqual(classifierThing.classify("yes"), "oh no")

if __name__ == '__main__':
    unittest.main()
