#!/usr/bin/env python3

import aoc

def part1( input_list ):
    """
    Calculate the final frequency based on a list of changes.
    """

    frequency = 0

    for change in input_list:
        frequency += int( change )

    return frequency


def part2( input_list ):
    """
    Find the first frequency seen first when processing changes.  You may need
    to process the input list multiple times.
    """

    frequency = 0
    seen = { 0 }

    while True:
        for change in input_list:
            frequency += int( change )

            if frequency in seen:
                return frequency

            seen.add( frequency )


if __name__ == "__main__":
    aoc.main( part1, part2 )
