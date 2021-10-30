import pandas as pd
import re

df = pd.read_csv('GCF_017821535.1_ASM1782153v1_genomic.gff_Mod.csv', delimiter = '\t')

# Filter the data
print(df.loc[df['Type'].str.contains('gene', flags = re.I, regex = True)])