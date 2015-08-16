import unittest
from math import ceil

CHUNK_LIMIT = 1000

class FormatError(Exception):
    pass


class TestFastaParse(unittest.TestCase):
    def setUp(self):
        import StringIO
        self.singleInputFile = StringIO.StringIO(
           ">myFasta1 description1\nACTG\nGTCA\n")

        self.multipleInputFile = StringIO.StringIO(
            ">myFasta1 description1\nACTG\nGTCA\n>myFasta2 description2\n"
            "GATACA\nACATAG\n")

    def test_SingleRecord(self):
        self.assertEqual(
                         [">myFasta1 description1\nACTG\nGTCA\n"],
                         parseFASTA(self.singleInputFile))

    def test_MultipleRecords(self):
        self.assertEqual(
                         [">myFasta1 description1\nACTG\nGTCA\n",
                          ">myFasta2 description2\nGATACA\nACATAG\n"],
                         parseFASTA(self.multipleInputFile))

    def tearDown(self):
        self.singleInputFile.close()
        self.multipleInputFile.close()


class TestPartition(unittest.TestCase):
    def test_SmallEvenDivision(self):
        self.assertEqual(partition([1,2,3,4,5,6], 2), [[1,2,3],[4,5,6]])

    def test_SmallOddDivision(self):
        self.assertEqual(partition([1,2,3,4,5,6,7], 3), [[1,2],[3,4,5],[6,7]])

    def test_LargeEvenDivision(self):
        self.assertEqual(partition(range(1,21), 4), 
                         [range(1,6), range(6,11), range(11,16), range(16,21)])

    def test_LargeOddDivision(self):
        self.assertEqual(partition(range(1,23), 5),
                         [range(1,5), range(5,10), range(10,14), range(14,19),
                          range(19,23)])

    def test_ZeroDivision(self):
        with self.assertRaises(ZeroDivisionError):
            partition([1,2,3,4,5], 0)

    def test_NegativeDivision(self):
        with self.assertRaises(ValueError):
            partition([1,2,3,4,5], -1)

    def test_TooBigDivisor(self):
        with self.assertRaises(ValueError):
            partition([1,2,3,4,5], 10)

    def test_NonIntegerDivisor(self):
        with self.assertRaises(TypeError):
            partition([1,2,3,4,5], 0.7)

class TestSplitRecords(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


class TestFilenameGenerator(unittest.TestCase):
    def setUp(self):
        self.normalGen = filenameGenerator('myFile', 'fa', 5)
        self.negativeGen = filenameGenerator('myFile', 'fa', -4)
        self.zeroGen = filenameGenerator('myFile', 'fa', 0)
        self.nonStringFilenameGen = filenameGenerator(1, 'fa', 5)
        self.nonStringExtensionGen = filenameGenerator('myFile', 1, 5)

    def test_NormalIterables(self):
        self.assertEqual(list(self.normalGen), ['myFile_0.fa',
                                                'myFile_1.fa',
                                                'myFile_2.fa',
                                                'myFile_3.fa',
                                                'myFile_4.fa'])

    def test_NegativeIterables(self):
        self.assertEqual(list(self.negativeGen), [])

    def test_ZeroIterables(self):
        self.assertEqual(list(self.zeroGen), [])

    def test_NonStringBasename(self):
        with self.assertRaises(TypeError):
            list(self.nonStringFilenameGen)

    def test_NonStringExtension(self):
        with self.assertRaises(TypeError):
            list(self.nonStringExtensionGen)

    def tearDown(self):
        pass


class TestWriteFiles(unittest.TestCase):
    pass


def parseFASTA(fileHandle):
    """Takes the filename of a FASTA file and extracts each FASTA record
    before appending each one to a list.

    Parameters
    ----------
    inputFilename : string
        the path to the FASTA file to be split

    Returns
    -------
    records : ['>fasta1\nACTG\n', '>fasta2\nACTG\nACTG\n', ...] list
        a list of FASTA records (including newlines)

    """
    records = []

    for line in fileHandle:
        if line.startswith('>'):
            records.append(line)
        else:
            try:
                records[-1] += line
            except IndexError:
                raise FormatError("Check your FASTA file for format errors")

    return records

def partition(lst, n):
    """Splits a list into n chunks of equal or nearly equal length.
    Parameters
    ----------
    lst : [1, 2, 3, 4, 5, ...] list
        the list to be split
    n : integer
        number of chunks to split the list into

    Returns
    -------
    list : [[1,2,3], [4,5]]
        a partitioned list with the smaller index chunks keeping extras
        remaining after uneven division

    Examples
    --------
    >>> myList = [1, 2, 3, 4, 5]
    >>> partition(myList, 5)
    [[1], [2], [3], [4], [5]]
    >>> partition(myList, 2)
    [[1, 2, 3], [4, 5]]
    >>> partition(myList, 3)
    [[1, 2], [3, 4], [5]]

    Credit
    ------
    [Joao Silva](http://stackoverflow.com/questions/2659900/)
    """
    if n < 0:
        raise ValueError("Can't divide list into negative chunks")
    if n > len(lst):
        raise ValueError("Can't divide list into more chunks than items in list")
    if not type(n) == int:
        raise TypeError("Can't divide list by non-integer value")

    division = len(lst) / float(n)
    return [ lst[int(round(division * i)) : int(round(division * (i + 1)))] 
             for i in xrange(n)
            ]

def splitRecords(records, chunks, customSizes=False, random=False):
    """Splits up the FASTA records into chunks to be written to
    different files.

    Parameters
    ----------
    records : ['>fasta1\nACTG\n', '>fasta2\nACTG\nACTG\n', ...] list
        a list of FASTA records (including newlines)
    chunks : int
        number of chunks/files to split the FASTA records into
    customSizes : [4, 6, 8, 10] list of ints
        a list of integers that will be used in order to build
        chunks of the given sizes instead of evenly sized
    random : boolean
        whether the records will be scrambled before chunking

    Returns
    -------
    list : [['>fasta1\nACTG\n', '>fasta2\nACTG\nACTG\n'], 
            ['>fasta3\nACTG\n']]
        a chunked list based on critera passed to function

    """

    if customSizes or random:
        raise NotImplementedError()
    if chunks > CHUNK_LIMIT:
        raise ValueError("Cannot split into more than %s files" % CHUNK_LIMIT)

    return partition(records, chunks)

def filenameGenerator(base, ext, n):
    """Generator that returns n filenames.

    Parameters
    ----------
    base : 'myFile' string
        the base name of the output files to which _0, _1, ... will be
        appended to for each output file
    ext : 'fasta' string
        file extension to be appended to each file, no period needed
    n : integer
        number of filenames to generate

    Returns
    -------
    generator
        iterable that returns generated filenames

    """
    if not type(base) == str:
        raise TypeError("Basename for file must be a string")
    if not type(ext) == str:
        raise TypeError("Extension must be a string")

    generated = 0

    while generated < n:
        yield '%s_%s.%s' % (base, generated, ext)
        generated += 1

def writeFiles(chunks, filenameBase, fileExtension=''):
    """Writes out a file for each chunk in a list.

    Parameters
    ----------
    chunks : [[1, 2, 3], [4, 5]] list of lists
        each list in the top list will be written to a different file
        after being joined by an empty string
    filenameBase : 'myFile' string
        the base name of the output files to which _0, _1, ... will be
        appended to for each output file
    fileExtension : 'fasta' string, optional
        file extension to be appended to each file, no period needed

    Returns
    -------
    Nothing

    """
    if len(chunks) > CHUNK_LIMIT:
        raise ValueError("Cannot split into more than %s files" % CHUNK_LIMIT)
    outFiles = filenameGenerator(filenameBase, fileExtension, len(chunks))
    for (index, outFile) in enumerate(outFiles):
        try:
            with open(outFile, 'w') as output:
                for record in chunks[index]:
                    output.write(record)
        except IOError as e:
            if e.errno == errno.EACCES:
                sys.exit("Do not have permission to write %s" % outFile)
            raise

if __name__ == "__main__":
    import argparse
    import os
    import sys

    parser = argparse.ArgumentParser(
                description='Split one fasta file into multiple fasta files.',
                epilog="Created by Travis Wrightsman")
    parser.add_argument('inputFile',
                        help='FASTA input file',
                        metavar='file')
    parser.add_argument('outputFileCount',
                        help='Number of output files',
                        metavar='outcount',
                        type=int)
    parser.add_argument('-b', '--basename',
                        help=('Base name of output files, default is '
                              'appending _1, _2, ... to input filename'))
    parser.add_argument('-r', '--random',
                        help='Place each record into a random output file',
                        action='store_true')
    parser.add_argument('-s', '--sizes',
                        help=('List of integers corresponding to the number of'
                        ' fasta records for each file'),
                        nargs="*",
                        metavar=('N1','N2'),
                        type=list)
    opts = parser.parse_args()

    if os.path.isfile(opts.inputFile):
        try:
            with open(opts.inputFile) as inputFASTAHandle:
                recordsList = parseFASTA(inputFASTAHandle)
        except IOError as e:
            if e.errno == errno.EACCES:
                sys.exit("Do not have permission to read the input file!")
    else:
        raise IOError('The specified input file was not found!')

    outputRecords = splitRecords(recordsList,
                                 opts.outputFileCount,
                                 customSizes=opts.sizes,
                                 random=opts.random)

    if not opts.basename:
        opts.basename = opts.inputFile

    writeFiles(outputRecords, opts.basename, 'fa')