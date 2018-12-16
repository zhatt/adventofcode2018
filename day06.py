#!/usr/bin/env python3

from collections import defaultdict
from operator import itemgetter

import aoc


def parse_input( input_list ):
    output = list()

    for line in input_list:
        ( x_coord, y_coord ) = line.split( ',' )
        x_coord = int( x_coord )
        y_coord = int( y_coord )
        output.append( ( int( x_coord ), int( y_coord ) ) )

    return output

def distance( a_coord, b_coord ):
    """
    Calculate Manhattan distance between to (x,y) tuples.
    """
    return abs( b_coord[0] - a_coord[0] ) + abs( b_coord[1] - a_coord[1] )

def get_bound( coordinate_list, fudge ):
    min_x = coordinate_list[0][0]
    min_y = coordinate_list[0][1]
    max_x = coordinate_list[0][0]
    max_y = coordinate_list[0][1]

    # Find edges
    for coord in coordinate_list:
        min_x = min( min_x, coord[0] )
        min_y = min( min_y, coord[1] )
        max_x = max( max_x, coord[0] )
        max_y = max( max_y, coord[1] )

    min_x -= fudge
    min_y -= fudge
    max_x += fudge
    max_y += fudge

    return ( ( min_x, min_y ), ( max_x, max_y ) )


def part1( input_list ):
    coordinate_list = parse_input( input_list )
    assert coordinate_list

    # We only care about squares inside the region where there are coordinates.
    # Anything that square being claimed more than distance 1 outside of the
    # coordinate area will be part of an infinite region.
    ( min_bound, max_bound ) = get_bound( coordinate_list, 1 )

    # Calculate closest to each square.
    num_squares_owned_by_coordinate = defaultdict( int )
    is_infinite_coordinates = set()
    for x_coord in range( min_bound[0], max_bound[0] + 1 ):
        for y_coord in range( min_bound[1], max_bound[1] + 1 ):
            distance_counts = defaultdict( int )
            distance_coords = dict()
            for coordinate in coordinate_list:
                dist = distance( ( x_coord, y_coord ), coordinate )
                distance_counts[ dist ] += 1
                distance_coords[ dist ] = coordinate

            closest_pair = min( distance_counts.items(), key=itemgetter(0))
            if closest_pair[1] == 1:
                closest_coord = distance_coords[ closest_pair[0] ]

                # If a square on bounding box is owned then the owner will have
                # an infinite region.
                if ( x_coord == min_bound[0] or x_coord == max_bound[0] or
                     y_coord == min_bound[1] or y_coord == max_bound[1] ):
                    is_infinite_coordinates.add( closest_coord )

                num_squares_owned_by_coordinate[ closest_coord ] += 1

    # Remove coordinates that are part of an infinite region.
    for coord in is_infinite_coordinates:
        num_squares_owned_by_coordinate.pop( coord, None )

    # Return the value of the largest remaining.
    return max( num_squares_owned_by_coordinate.items(), key=itemgetter(1))[1]


def part2( input_list, threshold = 10000 ):

    coordinate_list = parse_input( input_list )
    assert coordinate_list

    # Expand the bounding box by threshold / number of coordinates.  We know
    # that no coordinate that is more then this can be in the region because
    # the distance to the coordinate will use up all of threshold.
    ( min_bound, max_bound ) = get_bound( coordinate_list,
                                          threshold // len( coordinate_list ) )

    square_count = 0

    # Check every square in the bounding box to see if the total distance is
    # less than threshold.
    for x_coord in range( min_bound[0], max_bound[0] + 1 ):
        for y_coord in range( min_bound[1], max_bound[1] + 1 ):
            location = ( x_coord, y_coord )
            total_distance = 0

            for coordinate in coordinate_list:
                dist = distance( location, coordinate )
                total_distance += dist

            if total_distance < threshold:
                square_count += 1

    return square_count


if __name__ == "__main__":
    aoc.main( part1, part2 )
