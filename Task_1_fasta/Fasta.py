# Read fasta file
import csv
import argparse

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
    print('The Sequence:                  ' + Seq_select)
    Seq_select_Comp = Complement_D(Seq_select)
    print('The Complement strand:         ' + Seq_select_Comp)
    Seq_select_Rev_Comp = Seq_select_Comp[::-1]
    print('The Reverse Complement strand: ' + Seq_select_Rev_Comp)

def Seq_codon(s): # Print the selected strand's codon
    Seq_count = len(s)
    Codon_count = (Seq_count - Phase) // 3 
    Codon = []
    loc1 = 0 + Phase
    loc2 = 3 + Phase
    for i in range(Codon_count):
        Codon += [s[loc1:loc2]]
        loc1 += 3
        loc2 += 3
    return Codon

def print_codon(b): # print out the codon
    if b.codon:
        global Phase
        Phase = 0
        Codon_Comp = Seq_codon(Seq_select_Comp)
        print('The codon is:            ', Codon_Comp)
        Codon_Rev_Comp = Seq_codon(Seq_select_Rev_Comp)
        print('The reversed codon is:   ', Codon_Rev_Comp)
        Phase = 1
        Codon_Comp_1 = Seq_codon(Seq_select_Comp)
        print('The +1 codon is:         ', Codon_Comp_1)
        Codon_Rev_Comp_1 = Seq_codon(Seq_select_Rev_Comp)
        print('The +1 reversed codon is:', Codon_Rev_Comp_1)
        Phase = 2
        Codon_Comp_2 = Seq_codon(Seq_select_Comp)
        print('The +2 codon is:         ', Codon_Comp_2)
        Codon_Rev_Comp_2 = Seq_codon(Seq_select_Rev_Comp)
        print('The +2 reversed codon is:', Codon_Rev_Comp_2)

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

def print_aa(b): # print out the amino acids
    if b.aa:
        global Phase
        Phase = 0
        aa_Comp = Seq_aa(Seq_select_Comp)
        print('The aa is:            ', aa_Comp)
        aa_Rev_Comp = Seq_aa(Seq_select_Rev_Comp)
        print('The reversed aa is:   ', aa_Rev_Comp)
        Phase = 1
        aa_Comp_1 = Seq_aa(Seq_select_Comp)
        print('The +1 aa is:         ', aa_Comp_1)
        aa_Rev_Comp_1 = Seq_aa(Seq_select_Rev_Comp)
        print('The +1 reversed aa is:', aa_Rev_Comp_1)
        Phase = 2
        aa_Comp_2 = Seq_aa(Seq_select_Comp)
        print('The +2 aa is:         ', aa_Comp_2)
        aa_Rev_Comp_2 = Seq_aa(Seq_select_Rev_Comp)
        print('The +2 reversed aa is:', aa_Rev_Comp_2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Read Fasta files and print out the data needed')
    parser.add_argument('file_name', type = str, help = 'the fasta file name')
    parser.add_argument('Seq_start', type = int, help = 'the sequence starting point')
    parser.add_argument('Seq_end', type = int, help = 'the sequence ending point')
    parser.add_argument('-c', '--codon', action = 'store_false', help = 'do not print out the codon')
    parser.add_argument('-a', '--aa', action = 'store_false', help = 'do not print out the amino acid')
    parsed_args = parser.parse_args()
    
    file_name = parsed_args.file_name # the fasta file name
    with open(file_name, 'r', newline = '') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader) # Set first row as header and move to the next row
        print('The Fasta:' + str(header))
    
        GeneSeq = '' # Put the entire sequence in GeneSeq
        for row in csv_reader:
            if len(row) == 0: # Skip the empty rows
                continue
            GeneSeqTemp = str(row[0])
            GeneSeq += GeneSeqTemp

    Seq_start = parsed_args.Seq_start # the sequence start point
    Seq_end = parsed_args.Seq_end # the sequence end point
    Seq_selector() # select the sequence
    print_codon(parsed_args) # print out the codon
    print_aa(parsed_args) # print out the amino acids