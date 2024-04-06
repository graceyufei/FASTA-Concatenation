# FASTA-Concatenation

This is a local Python program that helps to concatenate sequences into one FASTA file.

1. Place all sequence files in the Data folder.
2. In the Input/input.csv file, list all sample names that you would like to pull, separated by line break. 
   Note: the sample name should match its FASTA header.<br>
   ex: <br>00001<br>00002<br>00003
3. In your terminal, go into this folder and run the below command. The output file will be built in the Output folder with today's date.
````
python concatenate_fasta.py
````

If you would like to customize or extract parts of fasta header to match with your sample name, you can edit the method *to_dict_remove_dupe*. I have provided two examples of how you can customize the fasta headers.

Packages and versions:
- Python version 3.8 or above 
- Biopython

