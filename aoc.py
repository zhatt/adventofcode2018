import argparse
from collections import namedtuple

Coord = namedtuple( 'Coord', [ 'x_val', 'y_val' ] )

def add_coords(*coords):
    assert coords
    x_sum = 0
    y_sum = 0
    for x_val, y_val in coords:
        x_sum += x_val
        y_sum += y_val
    return Coord(x_sum, y_sum)

def min_bound_coord(*coords):
    assert coords
    x_min = coords[0].x_val
    y_min = coords[0].y_val
    for x_val, y_val in coords:
        x_min = min(x_min, x_val)
        y_min = min(y_min, y_val)
    return Coord(x_min, y_min)

def max_bound_coord(*coords):
    assert coords
    x_max = coords[0].x_val
    y_max = coords[0].y_val
    for x_val, y_val in coords:
        x_max = max(x_max, x_val)
        y_max = max(y_max, y_val)
    return Coord(x_max, y_max)

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
