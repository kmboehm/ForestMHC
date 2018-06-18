# ForestMHC 
# Copyright 2018, Kevin Michael Boehm
# Use is subject to license as agreed to upon download
# Englander Institute for Precision Medicine, Weill Cornell Medical College

import sys
import os
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier
from lib.vanilla import Extractor
from lib.filt import Filter
from lib.auxiliary import condition_allele

#######
##
## user must insert path for ForestMHC main directory below
PATH = '/Users/kevinboehm/ForestMHC'
##
##
#######

def forest_mhc(alleles, in_list):
    with open(os.path.join(PATH, 'lib', 'aa.txt')) as aa_f:
        AA = aa_f.read().split(',')
    orig_peptides = in_list

    # remove peptides of len != 9 or with non-standard amino acids
    fil = Filter(removeC=False, aa=AA, len_set=[9])
    peptides = []
    failed_peptides = []
    for peptide in orig_peptides:
        if fil.may_pass(peptide):
            peptides.append(peptide)
        else:
            failed_peptides.append(peptide)
    del orig_peptides, fil
    
    # extract features and score each peptide
    features_to_use = ['hydropathy','is_aromatic','sparse','mass']
    extractor = Extractor(features_to_use, AA)
    features = extractor.extract_from_list(peptides)
    del extractor
    scores = []
    removal_list = []
    for raw_allele in alleles:
        allele = condition_allele(raw_allele)
        clf_fn = os.path.join(PATH, 'forests', 'mono_HASM', '.'.join([allele, 'pkl']))
        try:
            clf = joblib.load(clf_fn)
            print(allele)
        except IOError:
            print('No predictions available for {}'.format(raw_allele))
            removal_list.append(raw_allele)
            continue
        score = clf.predict_proba(features)
        scores.append(zip(*score)[1])

    # end script if no predictions available for any alleles
    for allele in removal_list:
        alleles.remove(allele)
    if alleles == []:
        return None, None, None
    
    # sort peptides by maximum predicted RF score
    predicted = []
    for scores_for_peptide in zip(*scores):
        ind = scores_for_peptide.index(max(scores_for_peptide))
        predicted.append(alleles[ind])
    # sort by maximal probability
    all_data = zip(peptides, predicted, *scores)
    maxes = [max(el[2:]) for el in all_data]
    temp = zip(maxes, all_data)
    temp.sort(reverse=True)
    sorted_data = [el[1] for el in temp]
    return alleles, sorted_data, failed_peptides
