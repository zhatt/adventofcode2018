#!/usr/bin/env python3

import string

import aoc

def react_polymer( polymer ):

    # Scan polymer and copy everything but reactive pairs to next_polymer for
    # next interation.  Keep iterating until no reactive pairs are found.
    done = False
    while not done:
        done = True
        next_polymer = ''

        i = 0
        while i <= len( polymer ) - 2:
            if polymer[i] != polymer[i+1] and polymer[i].lower() == polymer[i+1].lower():
                # Drop reactive pair.
                i += 2
                done = False
            else:
                # Copy character that is not part of reactive pair.
                next_polymer += polymer[i]
                i += 1

        # The last character was not destroyed so copy it.
        if i < len( polymer ):
            next_polymer += polymer[i]

        polymer = next_polymer

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
    Find smalled reacted polymer obtained when removing each character.
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
