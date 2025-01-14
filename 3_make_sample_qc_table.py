from __future__ import print_function
from pprint import pprint
import sys
import hail as hl
# c
#hc = hail.HailContext()
# sampddd
SAMPLE_QC_FILE = 'qc.tsv'
SAMPLE_QC_TABLE = 'qc.kt' 
df = hl.import_table("qc.tsv")
df = df.annotate(PC1 = hl.float64(df['PC1']),
                 PC2 = hl.float64(df['PC2']),
                 PC3 = hl.float64(df['PC3']),
                 PC4 = hl.float64(df['PC4']),
                 PC5 = hl.float64(df['PC5']),
                 PC6 = hl.float64(df['PC6']),
                 PC7 = hl.float64(df['PC7']),
                 PC8 = hl.float64(df['PC8']),
                 PC9 = hl.float64(df['PC9']),
                 PC10 = hl.float64(df['PC10']),
                 sample = df['eid'],
                 in_white_British_ancestry_subset = df['ethnicity'] == "1",
                 used_in_pca_calculation = df['used.in.pca.calculation'] == "1",
                 excess_relatives = df['excess.relatives']=="1",
                 putative_sex_chromosome_aneuploidy = df['putative.sex.chromosome.aneuploidy']=="1",
                 isFemale = df['Inferred.Gender'] == '0')

#df = df.key_by('sample')
df = df.filter(df.sample!= "-1")
df = df.filter(df.sample!= "-2")
df = df.filter(df.sample!= "-3")
df = df.filter(df.used_in_pca_calculation==True)
df = df.filter(df.excess_relatives==False)
df.select('sample',
           'isFemale',
           'PC1',
           'PC2',
           'PC3',
           'PC4',
           'PC5',
           'PC6',
           'PC7',
           'PC8',
           'PC9',
           'PC10').write('qc.kt',overwrite=True)

SAMPLE_QC_TABLE = "qc.kt"
kt = hl.read_table(SAMPLE_QC_TABLE)
n_samples = kt.count()
n_samples
kt.show()
