# ForestMHC 
# Copyright 2018, Kevin Michael Boehm
# Use is subject to license as agreed to upon download
# Englander Institute for Precision Medicine, Weill Cornell Medical College

hydropathy_score = {
'G':-0.4, 'A':1.8, 'P':-1.6, 'V':4.2, 'L':3.8, 'I':4.5, 'M':1.9,
'F':2.8, 'Y':-1.3, 'W':-0.9, 'S':-0.8, 'T':-0.7, 'C':2.5, 'N':-3.5,
'Q':-3.5, 'K':-3.9, 'H':-3.2, 'R':-4.5, 'D':-3.5, 'E':-3.5
                    }

molar_mass = {
'G':75, 'A':89, 'P':115, 'V':117, 'L':131, 'I':131, 'M':149,
'F':165, 'Y':181, 'W':204, 'S':105, 'T':119, 'C':121, 'N':132,
'Q':146, 'K':146, 'H':155, 'R':174, 'D':133, 'E':147
              }

aromatics = ['F', 'Y', 'W']

def spar(s,aa):
    o = []
    for e in s:
        for a in aa:
            o.append(1 if e==a else 0)
    return o

def hydropathy(s, aa):
    '''
    hydropathy score (Gibbs free energy transfer upon solvation in water,
    with negative being favorable) Kyte Doolittle, J. Mol. Bio. 1982.
    size len(pep)
    '''
    return [hydropathy_score[e] for e in s]

def mass(s, aa):
    'g/mol, including water. size: len(pep)'
    return [float(molar_mass[e])/204 for e in s]
                                    
def is_aromatic(s, aa):
    'binary membership in aromatic group or not. size: len(pep)'
    o = []
    for e in s:
        o.append(1 if e in aromatics else 0)
    return o

class Extractor():

    def __init__(self,featlist,aa):
        self.recipes = []
        self.aa = aa
        self.menu = {
            'sparse': spar,
            'hydropathy': hydropathy,
            'mass': mass,
            'is_aromatic': is_aromatic
        }
        for feat in featlist:
            func = self.menu.get(feat, lambda: "Invalid feature")
            self.recipes.append(func)
        
    def extract_from_list(self,l):
        o = []
        for pep in l:
            featrow = []
            for recipe in self.recipes:
                featrow.extend(recipe(pep,self.aa))
            o.append(featrow)
        return o
