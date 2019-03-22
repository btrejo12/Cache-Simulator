import sys
import getopt


def printResults():
    print('-----Results-----')
    print('Cache Hit Rate: ', '***', '%', sep='')

    
def printCalculatedValues():

    print('-----Calculated Values-----')
    print('Total # of Blocks:')
    print('Tag Size:')
    print('Index Size:')
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
    except getopt.GetoptError:
        print('Oops! Something happened...')
        sys.exit(2)

    for opt, arg in options:
        if opt == '-f':
            filename = arg
        elif opt == '-s':
            cacheSize = arg
        elif opt == '-b':
            blockSize = arg
        elif opt == '-a':
            associativity = arg
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
