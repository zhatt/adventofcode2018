#!/usr/bin/env python3

import re
from blist import blist

import aoc

def parse_input( input_list ):
    assert len( input_list ) == 1

    # Example
    # 447 players; last marble is worth 71510 points
    match_obj = re.search( r'(\d+) players; last marble is worth (\d+) points',
                           input_list[0] )
    assert match_obj

    num_players = int( match_obj.group( 1 ) )
    last_marble = int( match_obj.group( 2 ) )

    return num_players, last_marble


def simulate( num_players, last_marble ):
    score_list = [ 0 ] * num_players

    # Use blist because we do insertion on large list.
    marbles = blist( [ 0 ] )
    current_marble = 0
    current_player = 0

    # Add each marble.  Rotating through current_player.
    for marble in range( 1, last_marble + 1 ):
        # Marble 23 has a special rule for scoring.
        if marble % 23 == 0:
            remove_location = ( ( current_marble + len( marbles ) - 7 ) %
                                len( marbles ) )
            removed_marble = marbles.pop( remove_location )
            current_marble = remove_location
            score_list[ current_player ] += removed_marble + marble
        else:
            insert_location = ( ( current_marble + 1 ) % len( marbles ) ) + 1
            marbles.insert( insert_location, marble )
            current_marble = insert_location

        current_player = ( current_player + 1 ) % num_players

    return max( score_list )


def part1( input_list ):
    num_players, last_marble = parse_input( input_list )

    return simulate( num_players, last_marble )


def part2( input_list ):
    num_players, last_marble = parse_input( input_list )
    last_marble *= 100

    return simulate( num_players, last_marble )


if __name__ == "__main__":
    aoc.main( part1, part2 )
