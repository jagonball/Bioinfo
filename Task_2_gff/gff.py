# Read gff file
import csv
import argparse

def Mod_write(w): # write the data into a modified file
    with open(file_name + '_Mod.csv', mode = 'a', newline = '') as Mod_file:
        Mod_writer = csv.writer(Mod_file, delimiter = '\t')
        Mod_writer.writerow(w)

def Split_Attribute(a): # split the Attributes into a dictionary
    Att = a[8]
    Att_sp = Att.split(';') # split with ';'
    for i in Att_sp:
        Att_spsp = i.split('=') # split again with '='
        Att_key = Att_spsp[0]
        Att_value = Att_spsp[1]
        Att_D[Att_key] = Att_value # assign key and value to the dictionary
    return Att_D

# read the original gff file, remove the unwated rows, then write to a temporary file
def gff_read(f):
    with open(f, 'r', newline = '') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = '\t')
        for row in list(csv_reader)[0:50]:
            if len(row) == 0: # Skip the empty rows
                continue
            if '#' in row[0]: # Skip the rows begin with '#'
                continue
            else: # write the rows into the modified file
                Att_sp = Split_Attribute(row) # after-split Attribute (list)
                row[8] = Att_D # replace Attribute with the split Attribute list
                Mod_write(row)

if __name__ == '__main__':
    #open gff with csv, and exclude '#' started rows and empty rows
    parser = argparse.ArgumentParser(description = 'Read gff files and write the data into a modified file')
    parser.add_argument('file_name', type = str, help = 'the gff file name')
    parsed_args = parser.parse_args()
    
    file_name = parsed_args.file_name # the gff file name
    Att_D = {}  # create a dictionary named Att_D
    Mod_write(['SeqID', 'Source', 'Type', 'Start', 'End',
                   'Score', 'Strand', 'Phase', 'Attributes'])
    gff_read(file_name) # read the original gff file and write the modified file
