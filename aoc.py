import argparse
from collections import namedtuple

Coord = namedtuple( 'Coord', [ 'x_val', 'y_val' ] )

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument( '--part', type = int, choices = ( 1, 2 ), default = 1 )
    parser.add_argument( 'input_file' )
    return parser.parse_args()

def main( part1, part2 ):
    args = parse_args()

    input_list = read_input( args.input_file )

    if args.part == 1:
        output = part1( input_list )
        print( output )
    else:
        output = part2( input_list )
        print( output )

def read_input( file_name ):
    input_list = list()

    with open( file_name ) as file_iter:
        for line in file_iter:
            input_list.append( line.rstrip( '\n' ) )

    return input_list
