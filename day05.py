#!/usr/bin/env python3

import string

import aoc

def react_polymer( polymer ):

    # Convert string into list for faster deletions.
    polymer = list( polymer )

    # Scan polymer and copy everything but reactive pairs to next_polymer for
    # next interation.  Keep iterating until no reactive pairs are found.

    i = 0
    while i <= len( polymer ) - 2:
        if polymer[i] != polymer[i+1] and polymer[i].lower() == polymer[i+1].lower():
            # Drop reactive pair.
            polymer.pop( i )
            polymer.pop( i )
            # Next iteration will be at previous index because i and i-1
            # might be reactive now.
            if i:
                i -= 1

        else:
            i += 1

    return polymer


def part1( input_list ):
    """
    Find size of reacted polymer.
    """
    polymer = input_list[ 0 ]

    reacted_polymer = react_polymer( polymer )

    return len( reacted_polymer )


def part2( input_list ):
    """
    Find smallest reacted polymer obtained when removing each character.
    """
    polymer = input_list[ 0 ]

    shortest = len( polymer )

    # Remove each character and perform reaction to find which removed character
    # yields the shorts polymer.
    for character in string.ascii_uppercase:
        polymer_to_test = polymer.replace( character, '' ).replace( character.lower(), '' )
        reacted_polymer = react_polymer( polymer_to_test )
        shortest = min( shortest, len( reacted_polymer ) )

    return shortest

if __name__ == "__main__":
    aoc.main( part1, part2 )
