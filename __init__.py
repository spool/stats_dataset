"""
This file provides a class, StataDataset, which implements a dictionary-like
interface to a Stata dataset (requires scikits.statsmodels, Stata file version
9 or above, and all text fields to be strings rather than factors).

"""
import csv
import os

class StataDataset(Dataset):

    def __init__(self, filename="test_stata.dta", key='GISJOIN', path=None):
        self.key = key
        if path: self.filepath = os.path.join(os.path.expanduser(path), filename)
        else: self.filepath = filename
        self.file = open(self.filepath, 'rb')
        self.__parse()
        
    def __getitem__(self, key):
        return dict(zip(self.variables, self.data[key]))

    def __parse(self):
        from scikits.statsmodels.iolib import StataReader
        dta = StataReader(self.file)
        variables = [v.name for v in dta.variables()]
        key_index = variables.index(self.key)
        variables.remove(self.key)
        self.variables = variables
        d = {}
        for row in dta.dataset():
            d[row.pop(key_index)] = row
        self.data = d

    def __len__(self):
        return len(self.data)
