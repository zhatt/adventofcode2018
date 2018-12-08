#!/usr/bin/env python3

import operator
import re
from collections import defaultdict

import aoc

def readData( input ):
    """
    Return dictionary indexed by guard number of histogram lists.

    The histogram lists are elements long and contain the amount of time the
    guard sleep during each minute.
    """

    # ASCII sort will put the entries in time order.
    input.sort()

    # Data looks like this.
    # [1518-10-31 23:54] Guard #409 begins shift
    # [1518-08-02 00:53] wakes up
    # [1518-05-23 00:08] falls asleep

    # This are used to sanity check the input.  The guard must be awake at
    # when changing and asleep and awakes must be paired correctly.
    isAwake = True

    data = defaultdict( lambda: [0]*60 ) # Array of 0-59 minutes

    for line in input:
        matchObjG = re.search( r'Guard #(\d+) begins shift', line )
        matchObjA = re.search( r':(\d\d)] falls asleep', line )
        matchObjW = re.search( r':(\d\d)] wakes up', line )

        if matchObjG:
            assert( isAwake )
            guard = int( matchObjG.group( 1 ) )

        elif matchObjA:
            assert( isAwake )
            isAwake = False

            asleepTime = int( matchObjA.group( 1 ) )

        elif matchObjW:
            assert( not isAwake )
            isAwake = True

            wakeupTime = int( matchObjW.group( 1 ) )

            record = data[ guard ]
            for i in range( asleepTime, wakeupTime ):
                record[ i ] += 1

        else:
            # Can't parse.
            assert( 0 )

    return data


def part1( input ):
    """
    Find the guard with the most total minutes slept and report what minute
    he slept the most.
    """

    guardData = readData( input )

    sleepiestGuardNumber = 0
    sleepiestGuardMinutes = 0

    # Find the that has the most minutes asleep.
    for guard,histogram in guardData.items():
        minutesSlept = sum( histogram )
        if minutesSlept > sleepiestGuardMinutes:
            sleepiestGuardMinutes = minutesSlept
            sleepiestGuardNumber = guard

    # What minute did he sleep the most?
    minute, value = max( enumerate( guardData[sleepiestGuardNumber] ),
                         key=operator.itemgetter( 1 ) )

    return sleepiestGuardNumber * minute


def part2( input ):
    """
    Find the guard with the single most likely minute to be asleep.
    """

    guardData = readData( input )

    sleepiestGuardNumber = 0
    sleepiestGuardMinutes = 0
    sleepiestGuardMinute = 0

    # Find the guard that has the highest sleep minute value.
    for guard,histogram in guardData.items():
        minute, value = max( enumerate( guardData[guard] ),
                             key=operator.itemgetter( 1 ) )
        if value > sleepiestGuardMinutes:
            sleepiestGuardMinutes = value
            sleepiestGuardMinute = minute
            sleepiestGuardNumber = guard

    return sleepiestGuardNumber * sleepiestGuardMinute


if __name__ == "__main__":
    aoc.main( part1, part2 )

