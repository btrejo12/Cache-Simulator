import sys
import getopt
import math


def readAddresses():
    lineCounter = 0
    with open(filename) as f:
        for line in f:
            tokens = line.split(' ')
            if tokens[0] == "EIP":
                print('0x{}: {}'.format(tokens[2], tokens[1][:4]))
                lineCounter += 1
            if lineCounter >= 20:
                break
    f.close()


def printResults():
    print('\n-----Results-----')
    print('Cache Hit Rate: {} %'.format('***'))


def printCalculatedValues():
    offset = int(math.log(blockSize, 2))

    # Total blocks is always cacheSize / blockSize
    totalBlocks = int(cacheSize/blockSize)

    # Total index will be cacheSize / (associativity * blockSize)
    totalIndices =  int(cacheSize / (associativity * blockSize))
    indexBits = int(math.log(totalIndices, 2)) + 10  # 10 for the KB (2^10)

    tagSize = 32 - indexBits - offset

    # implementation bytes = (((tag+valid)associativity)*numOfRows) / 8 bits
    overhead = int((((tagSize+1) * associativity) * (2**indexBits)) / 8)
    implementation = overhead + cacheSize

    print('***** Cache Calculated Parameters *****')
    print('Total # of Blocks: {} KB'.format(totalBlocks))
    print('Tag Size: {} bits'.format(tagSize))
    print('Index Size: {} bits, Total Indices: {} KB'.format(indexBits, totalIndices))
    print('Overhead Memory Size: {:,} bytes'.format(overhead))
    print('Implementation Memory Size: {:,} bytes\n'.format(implementation))


def printHeader():
    sizeString = 'KB'
    tmpSize = int(cacheSize)

    if tmpSize >= 1024:
        tmpSize = int(tmpSize/1024);
        sizeString = 'MB'

    print('\nCache Simulator CS 3853 Spring 2019 - Group #19\n')
    print('***** Cache Input Parameters *****')
    print('Cmd Line: {}'.format(' '.join(sys.argv[1:])))
    print('Trace File: {}'.format(filename))
    print('Cache Size: {} {}'.format(tmpSize, sizeString))
    print('Block Size: {} bytes'.format(blockSize))
    print('Associativity: {}'.format(associativity))
    print('Replacement Policy: {}\n'.format(replacementPolicy))


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
    readAddresses()
    printResults()
