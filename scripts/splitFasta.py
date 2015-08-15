import unittest

class TestFastaParse(unittest.TestCase):
    def setUp(self):
        import StringIO
        self.singleInputFile = StringIO.StringIO(
           """>myFasta1 description1
           ACTG
           GTCA
           """)

        self.multipleInputFile = StringIO.StringIO(
            """>myFasta1 description1
            ACTG
            GTCA
            >myFasta2 description2
            GATACA
            ACATAG
            """)

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
        self.fail()

    def test_SmallOddDivision(self):
        self.fail()

    def test_LargeEvenDivision(self):
        self.fail()

    def test_LargeOddDivision(self):
        self.fail()

    def test_NegativeDivision(self):
        self.fail()

    def test_TooBigDivisor(self):
        self.fail()

    def test_NonIntegerDivisor(self):
        self.fail()

class TestSplitRecords(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


class TestFilenameGenerator(unittest.TestCase):
    def setUp(self):
        pass

    def test_NormalIterables(self):
        self.fail()

    def test_NegativeIterables(self):
        self.fail()

    def test_ZeroIterables(self):
        self.fail()

    def test_NonStringBasename(self):
        self.fail()

    def test_NonStringExtension(self):
        self.fail()

    def tearDown(self):
        pass


class TestWriteFiles(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
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
    #for line in fileHandle:

    return []

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
    division = len(lst) / float(n)
    return [ lst[int(round(division * i)) : int(round(division * (i + 1)))] 
             for i in xrange(n)
            ]

def splitRecords(records, customSizes=False, random=False):
    """Splits up the FASTA records into chunks to be written to
    different files.

    Parameters
    ----------
    records : ['>fasta1\nACTG\n', '>fasta2\nACTG\nACTG\n', ...] list
        a list of FASTA records (including newlines)
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

    if customSizes:
        raise NotImplementedError()

    return []

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

if __name__ == "__main__":
    import argparse
    import os

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

    if not os.path.isfile(inputFilename):
        if not os.access(inputFilename, os.R_OK):
            sys.exit('Do not have permissions to read the input file!')
        else:
            raise IOError('The specified input file was not found!')
    else:
        with open(inputFilename) as inputFASTAHandle:
            recordsList = parseFASTA(inputFASTAHandle)

    outputRecords = splitRecords(recordsList,
                                 customSizes=opts.sizes,
                                 random=opts.random)

    writeFiles(outputRecords)