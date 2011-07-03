import unittest
import os
from scikits.statsmodels.iolib import StataReader
from __init__ import StataDataset
from formats import DataFormat

#class Defaults(unittest.TestCase):
#
#    def setUp(self):
#        self.default_dataset = Dataset()
#
#    def testFileDefault(self):
#        filepath = os.path.join(os.path.expanduser('~/data'), 'test_stata.dta')
#        self.assertEqual(self.default_dataset.filepath, filepath)
#        self.assertEqual(self.default_dataset.file.read(), open(filepath).read())
#
#    def testKeyNameDefault(self):
#        self.assertEqual(self.default_dataset.key, 'GISJOIN')
#
#    def testTypeDefault(self):
#        self.assertEqual(self.default_dataset.format, DataFormat('Stata'))
#
class Api(unittest.TestCase):

    def setUp(self):
        self.dataset = StataDataset('test.dta', 'join')
        #self.test_file = StataReader(open('test_stata.dta', 'rb'))

    def testRow(self):
        self.assertEqual(self.dataset['a'], {
            'State': '06',
            'PUMA': '03311',
            'County': '06073',
            'Tract': '0187.00',
            'Population': 35682,
            'Weight': 0.228,
            })

    #def testVariables(self):
    #    self.assertEqual(self.dataset.variables, [i.name for i in self.test_file.variables() if i.name != 'GISJOIN'])

#class DataFormat(unittest.TestCase):
#
#    def setUp(self):
#        self.format = DataFormat('Stata')
#        self.test_file
#
#    def testName(self):
#        self.assertEqual(self.format.name, 'Stata')
#
#    def testVariables(self):
#        self.assertEqual(self.format.parse_variables


if __name__ == "__main__":
    unittest.main()
