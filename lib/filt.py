# ForestMHC 
# Copyright 2018, Kevin Michael Boehm
# Use is subject to license as agreed to upon download
# Englander Institute for Precision Medicine, Weill Cornell Medical College

class Filter():
    def __init__(self,removeC,aa,threshold=None,len_set=[9]):
        self.removeC = removeC
        self.aa = aa
        self.len_set = len_set
        self.threshold = threshold
        self.forbiddenct = 0
        self.lenct = 0
        self.thresholdct = 0
        self.cysct = 0
        self.times_called = 0

    def may_pass(self,pep):
        self.times_called += 1
        for a in str(pep):
            if a not in self.aa:
                self.forbiddenct += 1
                return False
        if len(pep) not in self.len_set:
            self.lenct += 1
            return False
        if self.removeC and 'C' in pep:
            self.cysct += 1
            return False
        else:
            return True

    def report(self):
        print(str(self.times_called) + ' peptides inspected.')
        print(str(self.forbiddenct) + ' removed because of char not in AA set.')
        print(str(self.lenct) + ' removed because not in length set.')
        print(str(self.cysct) + ' removed because contained cysteine.')
