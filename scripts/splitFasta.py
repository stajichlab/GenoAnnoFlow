if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Split one fasta file into multiple fasta files.', epilog="Created by Travis Wrightsman")
    parser.add_argument('inputFile', help='FASTA input file', metavar='file')
    parser.add_argument('outputFileCount', help='Number of output files', metavar='outcount', type=int)
    parser.add_argument('-b', '--basename', help='Base name of output files, default is appending _1, _2, ... to input filename')
    parser.add_argument('-r', '--random', help='Place each record into a random output file', action='store_true')
    parser.add_argument('-s', '--sizes', help='List of integers corresponding to the number of fasta records for each file', nargs="*", type=list, metavar=('N1','N2'))
    opts = parser.parse_args()

    records = parseFASTA(opts.inputFile)

    outputRecords = splitRecords(records, customSizes=opts.sizes, random=opts.random)

    writeFiles(outputRecords)