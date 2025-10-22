# SDMO-2025-group-3-project

This is the repository for project 1, identifying unique developers in OSS
repositories.

Some files from this repository were used as a base: https://github.com/M3SOulu/SDMO2025Project

## How to use

### Files

* developers.py
  The new implementation.

* inspect-csv.py

  A tool for sorting out FPs and TPs. To use it run it in the terminal and paste the path to the csv file you want to inspect. It will print out the file line by line and all you have to do is press t for a true positive of f for a false positive and press enter. The resulting FP and TP pairs will be stored in files in the inspect-output directory. Lastly the program will print the number of TPs and FPs.

* inspect-output/

  Target directory for files written by inspect-csv.py.

* compare.py

  A program that will compare two FP and two TP files. Run the program in the terminal and paste the path to the files according to the instructions in the terminal. After that the program will create four .csv files in the compare-results/ directory: addedFPs and removedFPs, and addedTPs and removedTPs. The program will also print the number of elements in each file.

  Hint: You'll probably want to choose the old false and true similarity files in devs/ to measure the performance of new implementations compared to the old one.

* old-devs.py

  The original implementation.

* requirements.txt

  List of dependencies.

* devs/

  A directory of the mined developer data from the selected repositories. It includes:

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
