#!/usr/bin/env python3

import re
from collections import defaultdict

import aoc

def parse_line( line ):
    """
    Parse line of this form:
    #1 @ 1,3: 4x4
    """

    match_obj = re.match( r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line )
    assert match_obj

    claim_number = int( match_obj.group( 1 ) )
    x_coord = int( match_obj.group( 2 ) )
    y_coord = int( match_obj.group( 3 ) )
    width = int( match_obj.group( 4 ) )
    height = int( match_obj.group( 5 ) )

    return ( claim_number, x_coord, y_coord, width, height )

def count_square_claims( input_list ):
    """
    Create a dictionary indexed by (x,y) that contains the number of claims
    on (x,y).  We use a dictionary because we don't know the size of the cloth.
    """
    fabric_claims = defaultdict( int )

    for line in input_list:
        ( _, x_coord, y_coord, width, height ) = parse_line( line )

        for xindex in range( x_coord, x_coord + width ):
            for yindex in range( y_coord, y_coord + height ):
                fabric_claims[(xindex,yindex)] += 1

    return fabric_claims

def part1( input_list ):
    """
    Find fabric with multple claims to the same square.
    """

    fabric_claims = count_square_claims( input_list )

    count = 0
    for i in fabric_claims.values():
        if i > 1:
            count += 1

    return count

def part2( input_list ):

    fabric_claims = count_square_claims( input_list )

    for line in input_list:
        ( claim_number, x_coord, y_coord, width, height ) = parse_line( line )

        # Check all squares in each claim.  We are looking for a claim where
        # all squares are 1 which means only this claim needs that square.
        found = True
        for xindex in range( x_coord, x_coord + width ):
            for yindex in range( y_coord, y_coord + height ):
                if fabric_claims[(xindex,yindex)] != 1:
                    found = False

        if found:
            return claim_number

    assert False
    return None


if __name__ == "__main__":
    aoc.main( part1, part2 )
