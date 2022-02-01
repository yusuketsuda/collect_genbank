#!/usr/bin/python

import os
import sys
import argparse
import pandas as pd
from Bio import SeqIO
from Bio import Entrez

parser = argparse.ArgumentParser(description='Download genbank files')

parser.add_argument('-e',
                                    '--email',
                                    required = True,
                                    help = 'write your email address to download genbank file from NCBI')
                                    
parser.add_argument('-f',
                                    '--infile',
                                    required = True,
                                    help = 'list of accession number (csv file or txt file)')
                                    
parser.add_argument('-o',
                                    '--outdir',
                                    required = False,
                                    help = 'location for directory to store genbank files')

args = parser.parse_args()

accession_list = []
file_name = args.infile

if file_name.endswith('csv'):
    accession_list = list(pd.read_csv(args.infile, header=None)[0])
elif file_name.endswith('text') or args.inflie.endswith('txt'):
    text = open(args.infile, 'r')
    content = text.read()
    accession_list = content.split('\n')
    text.close()
else:
    print('Infile is neither csv file nor text file.')

if args.outdir:
    if os.path.isdir(args.outdir):
        print('outdir "' + args.outdir + '" already exists. Overwrite?')
        string = input('yes or no : ')
        if string == 'no':
            sys.exit()
        else:
            outdir = args.outdir
    else:
        if os.path.isdir(args.outdir):
            outdir = args.outdir
        else:
            print(args.outdir + ' : No such directory')
            sys.exit()
else:
    outdir = 'genbank'
    os.mkdir(outdir)

Entrez.email = args.email

miss_genbank = []
for i in range(len(accession_list)):
    print(i, accession_list[i])
    try:
        handle = Entrez.efetch(db = 'nucleotide', id = accession_list[i],rettype = 'gb', retmode = 'text')
        text_write = open(outdir + '/' + accession_list[i] + '.gb','w')
        text_write.write(handle.read())
        handle.close()
        text_write.close()
    except:
        print('not downloaded : ' + accession_list[i])
        miss_genbank.append(accession_list[i])   

print('Downloaded : ' + str(len(accession_list)-len(miss_genbank)) + ', Missing : ' + str(len(miss_genbank)))
if len(miss_genbank) > 0:
    for i in miss_genbank:
        print(i)
    print('done')
else:
    print('done')
