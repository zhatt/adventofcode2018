#!/usr/bin/env python3

import aoc

def part1( input ):
    """
    Calculate the final frequency based on a list of changes.
    """

    frequency = 0

    for change in input:
        frequency += int( change )

    return frequency


def part2( input ):
    """
    Find the first frequency seen first when processing changes.  You may need
    to process the input list multiple times.
    """

    # Read the input into a list.
    changes = list()
    for change in input:
        changes.append( int( change ) )

    frequency = 0

    seen = set()
    seen.add( 0 )

    while True:
        for change in changes:
            frequency += change

            if frequency in seen:
                return frequency

            seen.add( frequency )


if __name__ == "__main__":
    aoc.main( part1, part2 )

