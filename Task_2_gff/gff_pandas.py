import pandas as pd
import argparse
import re
import csv

df = pd.read_csv('GCF_017821535.1_ASM1782153v1_genomic.gff_Mod.csv', delimiter = '\t')

# Filter the data with the keyword
def filter(f):
    global filtered_data
    filtered_data = df.loc[df['Type'].str.contains(f, flags = re.I, regex = True)] # Filter by 'Type'
    #filtered_data['Phase'].replace('.', 0, inplace = True) # Replace the Phase '.' to 0
    filtered_data.reset_index(drop = True, inplace = True) # Reset the index, and drop the old one

# DNA Complement strand converter
def Complement_D(s):
        s = s.replace('A', 't')
        s = s.replace('T', 'A')
        s = s.replace('G', 'c')
        s = s.replace('C', 'G')
        s = s.replace('t', 'T')
        s = s.replace('c', 'C')
        return s

def Seq_selector(): # sequence selector
    global Seq_select, Seq_select_Comp, Seq_select_Rev_Comp
    Seq_select = GeneSeq[Seq_start:Seq_end]
    Seq_select_Comp = Complement_D(Seq_select)
    if Strand == '+':
        print( Seq_select_Comp)
    elif Strand == '-':
        Seq_select_Rev_Comp = Seq_select_Comp[::-1]
        print(Seq_select_Rev_Comp)
    else:
        print('Strand not specified')

# Convert codon to amino acid from string
def Codon_aa(c):
    if   c == 'GTT' or c == 'GTC' or c == 'GTA' or c == 'GTG' or c == 'GUU' or (
                   c == 'GUC' or c == 'GUA' or c == 'GUG'):
        c = 'V' # Val
    elif c == 'GCT' or c == 'GCC' or c == 'GCA' or c == 'GCG' or c == 'GCU':
        c = 'A' # Ala
    elif c == 'GAT' or c == 'GAC' or c == 'GAU':
        c = 'D' # Asp
    elif c == 'GAA' or c == 'GAG':
        c = 'E' # Glu
    elif c == 'GGT' or c == 'GGC' or c == 'GGA' or c == 'GGG' or c == 'GGU':
        c = 'G' # Gly
    elif c == 'TTT' or c == 'TTC' or c == 'UUU' or c == 'UUC':
        c = 'F' # Phe
    elif c == 'TTA' or c == 'TTG' or c == 'UUA' or c == 'UUG' or c == 'CTT' or (
                    c == 'CTC' or c == 'CTA' or c == 'CTG' or c == 'CUU' or 
                    c == 'CUC' or c == 'CUA' or c == 'CUG'):
        c = 'L' # Leu
    elif c == 'TCT' or c == 'TCC' or c == 'TCA' or c == 'TCG' or c == 'UCU' or (
                    c == 'UCC' or c == 'UCA' or c == 'UCG' or c == 'AGT' or 
                    c == 'AGC' or c == 'AGU'):
        c = 'S' # Ser
    elif c == 'TAT' or c == 'TAC' or c == 'UAU' or c == 'UAC':
        c = 'Y' # Tyr
    elif c == 'TGT' or c == 'TGC' or c == 'UGU' or c == 'UGC':
        c = 'C' # Cys
    elif c == 'TGG' or c == 'UGG':
        c = 'W' # Trp
    elif c == 'CCT' or c == 'CCC' or c == 'CCA' or c == 'CCG' or c == 'CCU':
        c = 'P' # Pro
    elif c == 'CAT' or c == 'CAC' or c == 'CAU':
        c = 'H' # His
    elif c == 'CAA' or c == 'CAG':
        c = 'Q' # Gln
    elif c == 'CGT' or c == 'CGC' or c == 'CGA' or c == 'CGG' or (
                    c == 'CGU' or c == 'AGA' or c == 'AGG'):
        c = 'R' # Arg
    elif c == 'ATT' or c == 'ATC' or c == 'ATA' or (
                    c == 'AUU' or c == 'AUC' or c == 'AUA'):
        c = 'I' # Ile
    elif c == 'ATG' or c == 'AUG':
        c = 'M' # Met (Starting codon)
    elif c == 'ACT' or c == 'ACC' or c == 'ACA' or c == 'ACG' or c == 'ACU':
        c = 'T' # Thr
    elif c == 'AAT' or c == 'AAC' or c == 'AAU':
        c = 'N' # Asn
    elif c == 'AAA' or c == 'AAG':
        c = 'K' # Lys
    elif c == 'TAA' or c == 'TAG' or c == 'UAA' or (
                    c == 'UAG' or c == 'TGA' or c == 'UGA'):
        c = '*' # STOP   
    return c

# Print the strand's converted aa with sequence shift
def Seq_aa(s):
    Seq_count = len(s)
    Codon_count = (Seq_count - Phase) // 3 
    aa = ''
    loc1 = 0 + Phase
    loc2 = 3 + Phase
    for i in range(Codon_count):
        codon = s[loc1:loc2]
        aa += Codon_aa(codon)
        loc1 += 3
        loc2 += 3
    return aa

def print_aa(): # print out the amino acids
    if Strand == '+':
        if Phase == '.':
            print('.')
        elif Phase == '0':
            aa_Comp = Seq_aa(Seq_select_Comp)
            print(aa_Comp)
        elif Phase == '1':
            aa_Comp_1 = Seq_aa(Seq_select_Comp)
            print(aa_Comp_1)
        elif Phase == '2':
            aa_Comp_2 = Seq_aa(Seq_select_Comp)
            print(aa_Comp_2)
        else:
            print('Phase error')
    if Strand == '-':
        if Phase == '.':
            print('.')
        elif Phase == '0':
            aa_Rev_Comp = Seq_aa(Seq_select_Rev_Comp)
            print(aa_Rev_Comp)
        elif Phase == '1':
            aa_Rev_Comp_1 = Seq_aa(Seq_select_Rev_Comp)
            print(aa_Rev_Comp_1)
        elif Phase == '2':
            aa_Rev_Comp_2 = Seq_aa(Seq_select_Rev_Comp)
            print(aa_Rev_Comp_2)
        else:
            print('Phase error')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Read the modified gff files and filter what we need')
    parser.add_argument('filter_by', type = str, help = 'filter Type')
    parsed_args = parser.parse_args()

    filter_by = parsed_args.filter_by # the filter keyword
    filter(filter_by)
    print(filtered_data)

    # Open fasta file and prepare the sequence
    file_name = 'GCF_017821535.1_ASM1782153v1_genomic.fna' # the fasta file name
    with open(file_name, 'r', newline = '') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader) # Set first row as header and move to the next row
        print(header[0], end = ',')
        print(header[1])
    
        GeneSeq = '' # Put the entire sequence in GeneSeq
        for row in csv_reader:
            if len(row) == 0: # Skip the empty rows
                continue
            GeneSeqTemp = str(row[0])
            GeneSeq += GeneSeqTemp

    # Retrieve data from filtered data for fasta file
    for i in filtered_data.index:
        global Seq_start, Seq_end, Strand, Phase
        Seq_start = filtered_data.at[i, 'Start'] # the sequence start point
        Seq_end = filtered_data.at[i, 'End'] # the sequence end point
        Strand = filtered_data.at[i, 'Strand']
        Phase = filtered_data.at[i, 'Phase']
        print('>', end = '') # Print '>' and don't move to next line
        #Attributes = {}
        #Attributes = filtered_data.at[i, 'Attributes']
        #print(type(Attributes))

        print(Seq_start, Seq_end, Strand, Phase)
        Seq_selector() # select the sequence
        print_aa() # print out the amino acids