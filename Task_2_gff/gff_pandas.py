import pandas as pd
import argparse
import re

df = pd.read_csv('GCF_017821535.1_ASM1782153v1_genomic.gff_Mod.csv', delimiter = '\t')

# Filter the data with the keyword
def filter(f):
    global filtered_data
    filter_type = df.loc[df['Type'].str.contains(f, flags = re.I, regex = True)] # Filter by 'Type'
    filtered_data = filter_type[['Start', 'End', 'Strand', 'Phase']] # Keep the specified columns
    filtered_data.reset_index(drop = True, inplace = True) # Reset the index, and drop the old one

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Read the modified gff files and filter what we need')
    parser.add_argument('filter_by', type = str, help = 'filter Type')
    parsed_args = parser.parse_args()

    filter_by = parsed_args.filter_by # the filter keyword
    filter(filter_by)
    #print(filtered_data)

    # Retrieve data from filtered data for fasta file
    for i in filtered_data.index:
        Start = filtered_data.at[i, 'Start']
        End = filtered_data.at[i, 'End']
        Strand = filtered_data.at[i, 'Strand']
        Phase = filtered_data.at[i, 'Phase']
        print(Start, End, Strand, Phase)