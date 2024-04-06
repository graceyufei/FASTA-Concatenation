from Bio import SeqIO
import glob
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')  # today's date

# file path
data_path = './Data'
output_path = './Output/'

file_list = glob.glob(data_path + '/*.fasta')
output_file = output_path + f'{today}_output.fasta'
input_file = './Input/input.csv'


# customize/edit fasta header
def to_dict_remove_dupe(record_dict, sequences):
    for record in sequences:
        # strip 0s before sample name
        # record_dict[record.description.lstrip('0')] = record
        # strip any metadata after |
        # record_dict[record.description.split('|')[0]] = record
        record_dict[record.description] = record
    return record_dict


# read in input csv file
input_list = []
with open(input_file, 'r') as f:
    input_list = [row.strip() for row in f]

with open(output_file, 'w') as write_file:
    records_dict = {}
    for file in file_list:
        records = SeqIO.parse(file, 'fasta')
        records_dict = to_dict_remove_dupe(records_dict, records)

    # select samples based on input list
    records_dict = {k: v for k, v in records_dict.items() if k in input_list}
    SeqIO.write(records_dict.values(), write_file, 'fasta')

    # print out sample names that could not be found in the Data folder
    difference = [item for item in input_list if item not in records_dict.keys()]
    if len(difference) > 0:
        print('Samples ' + ','.join(difference) + ' are missing from the Data folder.')
