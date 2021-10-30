import csv
import argparse

parser = argparse.ArgumentParser(description = 'Read Fasta files')
parser.add_argument('file_name', type = str, help = 'the fasta file name')
parsed_args = parser.parse_args()

file_name = parsed_args.file_name
with open(file_name, 'r', newline = '') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader) #Set first line as header and move to the next line
    print('The Fasta:' + str(header))

    GeneSeq = '' # Put the entire sequence in GeneSeq
    for line in csv_reader:
        if len(line) == 0: # Skip the empty line
            continue
        GeneSeqTemp = str(line[0])
        GeneSeq += GeneSeqTemp

