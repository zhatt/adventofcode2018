#!/usr/bin/env python3

from collections import defaultdict
from operator import itemgetter

import aoc
import string

def parseInput( input ):
    output = list()

    for line in input:
        ( x, y ) = line.split( ',' )
        x = int( x )
        y = int( y )
        output.append( ( int( x ), int( y ) ) )

    return output

def distance( a, b ):
    """
    Calculate Manhattan distance between to (x,y) tuples.
    """
    return ( abs( b[0] - a[0] ) + abs( b[1] - a[1] ) )

def getBound( coordinateList, fudge ):
    minX = coordinateList[0][0]
    minY = coordinateList[0][1]
    maxX = coordinateList[0][0]
    maxY = coordinateList[0][1]

    # Find edges
    for d in coordinateList:
        minX = min( minX, d[0] )
        minY = min( minY, d[1] )
        maxX = max( maxX, d[0] )
        maxY = max( maxY, d[1] )

    minX -= fudge
    minY -= fudge
    maxX += fudge
    maxY += fudge

    return ( minX, minY, maxX, maxY )


def part1( input ):
    """
    """

    coordinateList = parseInput( input )
    assert( len( coordinateList ) > 0 )

    # We only care about squares inside the region where there are coordinates.
    # Anything that square being claimed more than distance 1 outside of the
    # coordinate area will be part of an infinite region.
    ( minX, minY, maxX, maxY ) = getBound( coordinateList, 1 )

    # Calculate closest to each square.
    numSquaresOwnedByCoordinate = defaultdict( int )
    isInfiniteCoordinates = set()
    for x in range( minX, maxX + 1 ):
        for y in range( minY, maxY + 1 ):
            location = ( x, y )
            distanceCounts = defaultdict( int )
            distanceCoords = dict()
            for coordinate in coordinateList:
                d = distance( location, coordinate )
                distanceCounts[ d ] += 1
                distanceCoords[ d ] = coordinate

            closestPair = min( distanceCounts.iteritems(), key=itemgetter(0))
            if ( closestPair[1] == 1 ):
                closestCoord = distanceCoords[ closestPair[0] ]

                # If a square on bounding box is owned then the owner will have
                # an infinite region.
                if ( x == minX or x == maxX or y == minY or y == maxY ):
                    isInfiniteCoordinates.add( closestCoord )

                numSquaresOwnedByCoordinate[ closestCoord ] += 1

    # Remove coordinates that are part of an infinite region.
    for coord in isInfiniteCoordinates:
        numSquaresOwnedByCoordinate.pop( coord, None )

    # Return the largest remaining.
    largest = max( numSquaresOwnedByCoordinate.iteritems(), key=itemgetter(1))
    return largest[1]


def part2( input, threshold = 10000 ):
    """
    """
    coordinateList = parseInput( input )
    assert( len( coordinateList ) > 0 )

    # Expand the bounding box by threshold / number of coordinates.  We know
    # that no coordinate that is more then this can be in the region because
    # the distance to the coordinate will use up all of threshold.
    ( minX, minY, maxX, maxY ) = getBound( coordinateList,
                                           threshold / len( coordinateList ) )

    squareCount = 0

    # Check every square in the bounding box to see if the total distance is
    # less than threshold.
    for x in range( minX, maxX + 1 ):
        for y in range( minY, maxY + 1 ):
            location = ( x, y )
            totalDistance = 0

            for coordinate in coordinateList:
                d = distance( location, coordinate )
                totalDistance += d

            if totalDistance < threshold:
                squareCount += 1

    return squareCount


if __name__ == "__main__":
    aoc.main( part1, part2 )

