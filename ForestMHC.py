# ForestMHC 
# Copyright 2018, Kevin Michael Boehm
# Use is subject to license as agreed to upon download
# Englander Institute for Precision Medicine, Weill Cornell Medical College

from lib.forest_mhc_func import forest_mhc
from lib.auxiliary import getopts, get_in_list, write_results
from sys import argv

myargs = getopts(argv)
alleles = myargs['-a'].split(',')
infile_path = myargs['-i']
outfile_path = myargs['-o']
    
in_list = get_in_list(infile_path)
alleles, sorted_data, failed_peptides = forest_mhc(alleles, in_list)
    
write_results(alleles,
        infile_path,
        outfile_path,
        sorted_data,
        failed_peptides
        )
