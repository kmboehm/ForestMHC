ForestMHC 1.0

About
ForestMHC prioritizes peptides of length 9 by likelihood of binding to
given alleles of MHC-I. Given a list of peptides and a list of alleles,
ForestMHC returns an ordered list of peptides, from most confident to be
bound to least confident. For more information, please see the following:


Installation instructions:
1. Clone the repository to your preferred directory.

2. Open ForestMHC/lib/forest_mhc_func.py, and modify the PATH string on
   line 17. Please set it as the path for the main ForestMHC directory
   on your system.

3. Within ForestMHC/forests/mono_HASM, untar the classifiers for B39 and
   A0201, e.g.:
      tar -xzvf A0201.pkl.tar.gz
      tar -xzvf B39.pkl.tar.gz
   Delete the .tar.gz files, as they are not needed any longer.

4. Be sure that scikit-learn for Python 2 is installed on your system.
   If it is not, install using your favorite package manager, e.g.
      pip install scikit-learn

5. Next, test your installation. From ForestMHC/test, enter the following
   command into your command line:
      python ../ForestMHC.py -i input -a A0101,C0501 -o my_output
   The contents of ForestMHC/test/correct_output and
   ForestMHC/test/my_output should be identical.

Please note that ForestMHC was written for Python 2.7.11 and scikit-learn
version 0.19.1. The software has been tested in Linux and Mac OS X operating
environments.


Instructions for use:
1. From the command line, call the Python script with the following flags:
    -i [path to input file, formatted as one peptide per line]
    -o [path to use for output of ForestMHC]
    -a [alleles, separated by commas and formatted like 'A0101']
E.g. python ForestMHC.py -i peptide_list.txt -a A0101,A2601,B2705 -o output.txt

2. The software will list alleles as it is processing them. If no classifier is
   available for a specified allele, a message will be printed to standard
   output.

3. After the run finishes, the output file will be formatted as follows:
    # ForestMHC Output
    # Input: [input file path]
    Sequence  [Allele 1]  [Allele 2]  [Allele 3] [...] Predicted  Rank
    AAAAAAAAA 0.9980      0.1042      0. 5032          Allele1    1
    ...
    # No predictions available for RRRRRRRRRR,LLLLLLLLLLLLL,...
  Note that only alleles with available predictions are included as columns
  in the output file. The "Pred." (Predicted) column indicates the allele
  for which the random forest score was highest. Rank is from 1 to N, where
  N is the number of peptides successfully processed by ForestMHC from the
  input file.
