#!/usr/bin/env python3

import aoc
from aoc import Coord

def parse_input( input_list ):
    assert len( input_list ) == 1
    return int( input_list[0] )

def calc_power( serial_num, coord ):
    rack_id = coord.x_val + 10
    power_level = rack_id * coord.y_val
    power_level += serial_num
    power_level *= rack_id
    power_level = power_level // 100 - ( power_level // 1000 * 10 )
    power_level -= 5

    return power_level


def calc_power_box( grid, coord, box_size ):
    total_power = 0

    for x_index in range(coord.x_val, coord.x_val + box_size):
        total_power += sum( grid[ x_index ][ coord.y_val:coord.y_val + box_size] )

    return total_power

def calc_power_delta_x( power, grid, coord, box_size ):
    power -= sum( grid[ coord.x_val - 1 ][ coord.y_val : coord.y_val + box_size ] )
    power += sum( grid[ coord.x_val + box_size - 1 ][ coord.y_val : coord.y_val + box_size ] )

    return power

def calc_power_delta_y( power, grid, coord, box_size ):
    for x_index in range( coord.x_val, coord.x_val + box_size ):
        power -= grid[ x_index ][ coord.y_val - 1 ]
        power += grid[ x_index ][ coord.y_val + box_size - 1 ]

    return power

def compute_grid( serial_num ):
    grid = [ [0] * 300 for i in range( 300 ) ]

    for x_index in range( 300 ):
        for y_index in range( 300 ):
            grid[ x_index ][ y_index ] = calc_power( serial_num, Coord( x_index, y_index) )

    return grid

def find_largest_power( serial_num, grid_size_min, grid_size_max ):
    grid = compute_grid( serial_num )

    largest_power = calc_power_box( grid, Coord(0, 0), grid_size_min )
    largest_coord = Coord( 0, 0 )
    largest_grid_size = 0

    for grid_size in range( grid_size_min, grid_size_max + 1 ):
        for y_index in range(0, 300 - (grid_size - 1)):
            for x_index in range( 0, 300 - ( grid_size - 1) ):
                coord = Coord( x_index, y_index )
                if x_index == 0 and y_index == 0:
                    power = calc_power_box( grid, coord, grid_size )
                    last_x0_power = power

                elif x_index == 0:
                    power = calc_power_delta_y( last_x0_power, grid, coord, grid_size )
                    last_x0_power = power

                else:
                    power = calc_power_delta_x( power, grid, coord, grid_size )

                if power > largest_power:
                    largest_power = power
                    largest_coord = coord
                    largest_grid_size = grid_size

    return largest_coord, largest_grid_size


def part1( input_list ):
    serial_num = parse_input( input_list )
    coord,_ = find_largest_power( serial_num, 3, 3 )
    return "%d,%d" % ( coord.x_val, coord.y_val )

def part2( input_list ):
    serial_num = parse_input( input_list )

    coord,grid_size = find_largest_power( serial_num, 1, 300 )
    return "%d,%d,%d" % ( coord.x_val, coord.y_val, grid_size )

if __name__ == "__main__":
    aoc.main( part1, part2 )
