# ForestMHC 
# Copyright 2018, Kevin Michael Boehm
# Use is subject to license as agreed to upon download
# Englander Institute for Precision Medicine, Weill Cornell Medical College

import sys

def condition_allele(allele):
    to_remove = ['HLA', '-', '*', ':']
    for bad_str in to_remove:
        allele = allele.replace(bad_str, '')
    return allele

def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':
            opts[argv[0]] = argv[1]
        argv = argv[1:]
    return opts

def get_in_list(infile_path):
    try:
        with open(infile_path,'r') as infile:
            orig_peptides = infile.read().split('\n')
        return orig_peptides
    except IOError:
        sys.exit('No input file at specified path')

def write_results(alleles, infile_path, outfile_path, sorted_data, failed_peps):
    try:
        outfile = open(outfile_path, 'w')
    except IOError:
        sys.exit('Cannot open specified output file')
    
    outfile.write('#ForestMHC Output\n')
    outfile.write('#Input: '+infile_path+'\n')
    if alleles is None:
        outfile.write('No predictions available for specified allele(s).')
    else:
        outfile.write('Sequence\t'+'\t'.join([el.ljust(5) for el in alleles])+'\tPred.'+'\t'+'Rank'+'\n')
        for rank, line_items in enumerate(sorted_data):
            outfile.write(line_items[0]+'\t')
            outfile.write('\t'.join('{:4.4f}'.format(s) for s in line_items[2:]))
            outfile.write('\t'+line_items[1].ljust(5)+'\t'+str(rank+1)+'\n')
        outfile.write('\n#No predictions available for '+','.join(failed_peps))
    outfile.close()
