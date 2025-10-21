# SDMO-2025-group-3-project

This is the repository for project 1, identifying unique developers in OSS
repositories.

Some files from this repository were used as a base: https://github.com/M3SOulu/SDMO2025Project

## How to use

### Files

* developers.py
  The new implementation.

* inspect-csv.py
  A tool for sorting out FPs and TPs.

* original-project1developers.py
  The original implementation.

* output-inspection
  Target directory for files written by inspect-csv.py.

* requirements.txt
  List of dependencies.

* devs 
  Has the mined developer data from the selected repositories. It includes:
    * devs.csv
      A list of developer names and emails

    * original_devs_similarity_t=0.7.csv
      Duplicate pairs identified using the original implementation.

    * 1k_devs_similarity_t=7.csv
      A random assortment of 1000 duplicates from the original_devs_similarity_t=0.7.csv file for easier FP and TP identification.


### Main program

### Inspecting CSV files

1. Run inspect-csv.py

2. Add the file path for the csv file you want to inspect

3. Type the number of lines you want to read, or press enter to read the whole file.

4. The FPs and TPs are now separated into two .csv files in output-inspection.

Note: Be careful when naming the .csv file that will be read because the output file will remove the contents of files with the same name.
