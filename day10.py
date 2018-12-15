#!/usr/bin/env python3

import re

import aoc
from aoc import Coord

class StarData:
    def __init__( self, coord, velocity ):
        self.coord = coord
        self.vel = velocity

    def __str__( self ):
        return "(%s,%s)" % ( self.coord, self.vel )

    def __repr__( self ):
        return "(%s,%s)" % ( self.coord, self.vel )


def parse_input( input_list ):

    # Map of velocitys keyed by coordinate.
    data = list()

    # Example input data
    # position=< 9,  1> velocity=< 0,  2>
    regex = r'position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>'

    for line in input_list:
        match_obj = re.search( regex, line )
        assert match_obj

        coord = Coord( int( match_obj.group( 1 ) ), int( match_obj.group( 2 ) ) )
        vel   = Coord( int( match_obj.group( 3 ) ), int( match_obj.group( 4 ) ) )

        data.append( StarData( coord, vel ) )

    return data


def draw( data ):
    min_bound, max_bound = calc_bound( data )

    stars = set()

    for star_data in data:
        stars.add( star_data.coord )

    output = ''
    for y_val in range( min_bound.y_val, max_bound.y_val + 1 ):
        for x_val in range( min_bound.x_val, max_bound.x_val + 1 ):
            if ( x_val, y_val ) in stars:
                output += '#'
            else:
                output += '.'

        if y_val != max_bound.y_val:
            output += '\n'

    return output


def move_stars( data ):
    for star in data:
        star.coord = Coord( star.coord.x_val + star.vel.x_val, star.coord.y_val + star.vel.y_val )


def calc_bound( data ):
    coord = data[0].coord

    x_min = x_max = coord.x_val
    y_min = y_max = coord.y_val

    for star_data in data:
        x_min = min( x_min, star_data.coord.x_val )
        x_max = max( x_max, star_data.coord.x_val )
        y_min = min( y_min, star_data.coord.y_val )
        y_max = max( y_max, star_data.coord.y_val )

    return Coord( x_min, y_min ), Coord( x_max, y_max )


def calc_area( min_coord, max_coord ):
    area = ( max_coord.x_val - min_coord.x_val + 1 ) * ( max_coord.y_val - min_coord.y_val + 1 )

    return area


def simulate( input_list, time_to_simulate = -1 ):
    data = parse_input( input_list )
    seconds = 0

    min_bound, max_bound = calc_bound( data )
    area = calc_area( min_bound, max_bound )

    # Simulate until the area stars gets bigger or for the amount of time
    # passed in.  Unfortuately, when we figure out that we are one past the
    # correct time, we don't have the previous frame anymore.  It is actually
    # faster to resimulate then it is to save the previous frame each iteration
    # so the caller needs to call this twice to if the output is needed.
    while time_to_simulate:
        time_to_simulate -= 1

        move_stars( data )
        min_bound, max_bound = calc_bound( data )
        new_area = calc_area( min_bound, max_bound )
        if new_area > area:
            break

        seconds += 1
        area = new_area

    output = draw( data )

    return output, seconds


def part1( input_list ):
    # Find out how long we need to simulate.
    _, seconds = simulate( input_list )

    # Resimulate to get the correct output.
    output, _ = simulate( input_list, seconds )
    #print( output )
    return output


def part2( input_list ):
    _, seconds = simulate( input_list )
    return seconds


if __name__ == "__main__":
    aoc.main( part1, part2 )
