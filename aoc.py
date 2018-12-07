import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument( '--part', type = int, choices = ( 1, 2 ), default = 1 )
    parser.add_argument( 'inputfile' )
    return parser.parse_args()

def main( part1, part2 ):
    args = parse_args()

    input = readInput( args.inputfile )

    if args.part == 1:
        output = part1( input )
        print( output )
    else:
        output = part2( input )
        print( output )

def readInput( file ):
    input = list()

    with open( file ) as f:
        for line in f:
            input.append( line.rstrip( '\n' ) )

    return input
