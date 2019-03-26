import sys
import getopt
import math


#TODO: Call this function cause it needs to be printed :-)
def printResults():
    print('-----Results-----')
    print('Cache Hit Rate: ', '***', '%', sep='')


#TODO: You know, actually calculate these values
def printCalculatedValues():
    offset = int(math.log(blockSize, 2))

    #Total blocks is always cacheSize / blockSize
    totalBlocks = int(cacheSize/blockSize)

    #Total index will be cacheSize / (associativity * blockSize)
    totalIndices =  int(cacheSize / (associativity * blockSize))
    indexSize = int(math.log(totalIndices, 2)) + 10 #10 for the KB (2^10)

    tagSize = 32 - indexSize - offset;

    print('-----Calculated Values-----')
    print('Total # of Blocks:', totalBlocks, 'KB')
    print('Tag Size:', tagSize, 'bits')
    print('Index Size:', indexSize, 'bits,', 'Total Indices:', totalIndices, 'KB')
    print('Implementation Memory Size:')


def printHeader():
    sizeString = 'KB'
    tmpSize = int(cacheSize)

    if tmpSize >= 1024:
        tmpSize = int(tmpSize/1024);
        sizeString = 'MB'

    print('Cache Simulator CS 3853 Spring 2019 - Group #19\n')
    print('Cmd Line:', ' '.join(sys.argv[1:]))
    print('Trace File:', filename)
    print('Cache Size:', tmpSize, sizeString)
    print('Block Size:', blockSize, 'bytes')
    print('Associativity:', associativity)
    print('Replacement Policy:', replacementPolicy, '\n')


def readArguments():
    global filename
    global cacheSize
    global blockSize
    global associativity
    global replacementPolicy

    try:
        options, arguments = getopt.getopt(sys.argv[1:], 'f:s:b:a:r:')
    except getopt.GetoptError as e:
        print('ERROR:', e)
        sys.exit(2)

    for opt, arg in options:
        if opt == '-f':
            filename = arg
        elif opt == '-s':
            cacheSize = int(arg)
        elif opt == '-b':
            blockSize = int(arg)
        elif opt == '-a':
            associativity = int(arg)
        elif opt == '-r':
            replacementPolicy = arg


# Globals
filename = None
cacheSize = None
blockSize = None
associativity = None
replacementPolicy = None

if __name__ == '__main__':
    readArguments()
    printHeader()
    printCalculatedValues()
    printResults()
