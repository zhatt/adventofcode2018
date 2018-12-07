#!/usr/bin/env python3

import re
from collections import defaultdict

import aoc

def parseLine( line ):
    """
    Parse line of this form:
    #1 @ 1,3: 4x4
    """

    matchObj = re.match( r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line )
    assert( matchObj )

    claimNumber = int( matchObj.group( 1 ) )
    x = int( matchObj.group( 2 ) )
    y = int( matchObj.group( 3 ) )
    width = int( matchObj.group( 4 ) )
    height = int( matchObj.group( 5 ) )

    return ( claimNumber, x, y, width, height )

def countSquareClaims( input ):
    """
    Create a dictionary indexed by (x,y) that contains the number of claims
    on (x,y).  We use a dictionary because we don't know the size of the cloth.
    """
    fabricClaims = defaultdict( int )

    for line in input:
        ( claimNumber, x, y, width, height ) = parseLine( line )

        for xindex in range( x, x + width ):
            for yindex in range( y, y + height ):
                fabricClaims[(xindex,yindex)] += 1

    return fabricClaims

def part1( input ):
    """
    Find fabric with multple claims to the same square.
    """

    fabricClaims = countSquareClaims( input )

    count = 0
    for i in fabricClaims.values():
        if i > 1:
            count += 1

    return count

def part2( input ):

    fabricClaims = countSquareClaims( input )

    for line in input:
        ( claimNumber, x, y, width, height ) = parseLine( line )

        # Check all squares in each claim.  We are looking for a claim where
        # all squares are 1 which means only this claim needs that square.
        found = True
        for xindex in range( x, x + width ):
            for yindex in range( y, y + height ):
                if ( fabricClaims[(xindex,yindex)] != 1 ):
                    found = False

        if found:
            return claimNumber


if __name__ == "__main__":
    aoc.main( part1, part2 )
