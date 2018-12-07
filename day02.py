#!/usr/bin/env python3

import aoc

from collections import defaultdict

def part1( input ):
    """
    Calculate checksum of all labels.
    """

    sum2 = 0
    sum3 = 0

    for label in input:
        # Create histogram of letters in the label.
        histogram = defaultdict( int )

        for character in label:
            histogram[ character ] += 1

        if 2 in histogram.values():
            sum2 += 1

        if 3 in histogram.values():
            sum3 += 1

    checksum = sum2 * sum3
    return checksum


def part2( input ):
    """
    Find labels that differ by only one character.
    """

    for label1 in input:
        for label2 in input:
            # All labels are supposed to be the same length.
            assert( len( label2 ) == len( label1 ) )

            if label1 == label2:  continue

            numdiff = 0
            for i in range( len( label1 ) ):
                if label1[i] != label2[i]:
                    numdiff += 1

            # If only one character is different between the two labels, we have
            # found the one we want.  Generate a new string that contains the
            # common characters.
            if ( numdiff == 1 ):
                out = ""
                for i in range( len( label1 ) ):
                    if label1[i] == label2[i]:
                        out += label1[i]

                return out


if __name__ == "__main__":
    aoc.main( part1, part2 )

