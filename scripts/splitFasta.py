#!/usr/bin/env python
import argparse
from os.path import isfile
import sys

parser = argparse.ArgumentParser(description='Split one fasta file into multiple fasta files.', epilog="Created by Travis Wrightsman")
parser.add_argument('inputFile', help='FASTA input file', metavar='file')
parser.add_argument('outcount', help='Number of output files', metavar='outcount', type=int)
parser.add_argument('-b', '--basename', help='Base name of output files, default is appending _1, _2, ... to input filename')
parser.add_argument('-r', '--random', help='Place each record into a random output file', action='store_true')
parser.add_argument('-s', '--sizes', help='List of integers corresponding to the number of fasta records for each file', nargs="*", type=list, metavar=('N1','N2'))
opts = parser.parse_args()

def outFileNames(n, basename):
    num = 0
    while num < n:
        yield '%s_%s.fa' % (basename, num)
        num += 1

records = []
if isfile(opts.inputFile):
    with open(opts.inputFile) as inputHandle:
        record = ''
        for line in inputHandle:
            if line.startswith('>'):
                records.append(record)
                record = line
            else:
                record += line
        records.append(record)

if len(records) < opts.outcount:
    sys.exit('Asked for more files than records!')
if opts.basename:
    basename = opts.basename
else:
    basename = opts.inputFile

outRecords = []
if opts.sizes:
    if len(opts.sizes) != opts.outcount:
        sys.exit('List of sizes not equal to desired number of output files!')
    if opts.random:
        print 'Random defined size mode initiate'
    else:
        print 'Defined size mode initiate'
else:
    if opts.random:
        print 'Random even size mode initiate'
    else:
        recordsPerFile = len(records) // opts.outcount
        remainingRecords = len(records) % opts.outcount
        for index in xrange(0, opts.outcount):
            if remainingRecords != 0:
                outRecords.append(records[:recordsPerFile + 1])
                records = records[recordsPerFile + 1:]
                remainingRecords -= 1
            else:
                outRecords.append(records[:recordsPerFile])
                records = records[recordsPerFile:]

for (index, outFile) in enumerate(outFileNames(opts.outcount, basename)):
    with open(outFile, 'w') as outFileHandle:
        outFileHandle.write(''.join(outRecords[index]))
