#!/usr/bin/env python3

import aoc
import string

def reactPolymer( polymer ):

    # Scan polymer and copy everything but reactive pairs to nextPolymer for
    # next interation.  Keep iterating until no reactive pairs are found.
    done = False
    while not done:
        done = True
        nextPolymer = ''

        i = 0
        while i <= len( polymer ) - 2:
            if polymer[i] != polymer[i+1] and polymer[i].lower() == polymer[i+1].lower():
                # Drop reactive pair.
                i += 2
                done = False
            else:
                # Copy character that is not part of reactive pair.
                nextPolymer += polymer[i]
                i += 1

        # The last character was not destroyed so copy it.
        if i < len( polymer ):
            nextPolymer += polymer[i]

        polymer = nextPolymer

    return polymer

def part1( input ):
    """
    Find size of reacted polymer.
    """
    polymer = input[ 0 ]

    reactedPolymer = reactPolymer( polymer )

    return len( reactedPolymer )


def part2( input ):
    """
    Find smalled reacted polymer obtained when removing each character.
    """
    polymer = input[ 0 ]

    shortest = len( polymer )

    # Remove each character and perform reaction to find which removed character
    # yields the shorts polymer.
    for c in string.ascii_uppercase:
        polymerToTest = polymer.replace( c, '' ).replace( c.lower(), '' )
        reactedPolymer = reactPolymer( polymerToTest )
        shortest = min( shortest, len( reactedPolymer ) )

    return shortest

if __name__ == "__main__":
    aoc.main( part1, part2 )

