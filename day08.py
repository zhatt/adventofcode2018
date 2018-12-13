#!/usr/bin/env python3

import aoc

def parse_input( input_list ):
    assert len( input_list ) == 1
    license_nums = input_list[0].split()

    license_nums = list( map( int, license_nums ) )

    return license_nums


def recurse( license_nums ):
    metadata_sum = 0

    num_children = license_nums.pop( 0 )
    num_metadata = license_nums.pop( 0 )

    # Each of this nodes child values.
    child_values = []

    # Calculate values for each child node.
    for _ in range( num_children ):
        child_metadata_sum, child_node_value = recurse( license_nums )

        metadata_sum += child_metadata_sum
        child_values.append( child_node_value )

    # Caluate the values for this node.
    node_value = 0
    for _ in range( num_metadata ):
        value = license_nums.pop( 0 )
        metadata_sum += value

        if num_children:
            # Convert to 0-based to index list.
            meta = value - 1

            if meta < num_children:
                node_value += child_values[ meta ]

        else:
            node_value += value

    return metadata_sum, node_value


def part1( input_list ):
    license_nums = parse_input( input_list )
    return recurse( license_nums )[0]


def part2( input_list ):
    license_nums = parse_input( input_list )
    return recurse( license_nums )[1]


if __name__ == "__main__":
    aoc.main( part1, part2 )
