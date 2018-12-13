#!/usr/bin/env python3

import operator
import re
from collections import defaultdict

import aoc

def read_data( input_list ):
    """
    Return dictionary indexed by guard number of histogram lists.

    The histogram lists are elements long and contain the amount of time the
    guard sleep during each minute.
    """

    # ASCII sort will put the entries in time order.
    input_list.sort()

    # Data looks like this.
    # [1518-10-31 23:54] Guard #409 begins shift
    # [1518-08-02 00:53] wakes up
    # [1518-05-23 00:08] falls asleep

    # This are used to sanity check the input.  The guard must be awake at
    # when changing and asleep and awakes must be paired correctly.
    is_awake = True

    data = defaultdict( lambda: [0]*60 ) # Array of 0-59 minutes

    for line in input_list:
        match_obj_g = re.search( r'Guard #(\d+) begins shift', line )
        match_obj_a = re.search( r':(\d\d)] falls asleep', line )
        match_obj_w = re.search( r':(\d\d)] wakes up', line )

        if match_obj_g:
            assert is_awake
            guard = int( match_obj_g.group( 1 ) )

        elif match_obj_a:
            assert is_awake
            is_awake = False

            asleep_time = int( match_obj_a.group( 1 ) )

        elif match_obj_w:
            assert not is_awake
            is_awake = True

            wakeup_time = int( match_obj_w.group( 1 ) )

            record = data[ guard ]
            for i in range( asleep_time, wakeup_time ):
                record[ i ] += 1

        else:
            # Can't parse.
            assert False

    return data


def part1( input_list ):
    """
    Find the guard with the most total minutes slept and report what minute
    he slept the most.
    """

    guard_data = read_data( input_list )

    sleepiest_guard_number = 0
    sleepiest_guard_minutes = 0

    # Find the that has the most minutes asleep.
    for guard,histogram in guard_data.items():
        minutes_slept = sum( histogram )
        if minutes_slept > sleepiest_guard_minutes:
            sleepiest_guard_minutes = minutes_slept
            sleepiest_guard_number = guard

    # What minute did he sleep the most?
    minute, _ = max( enumerate( guard_data[sleepiest_guard_number] ),
                     key=operator.itemgetter( 1 ) )

    return sleepiest_guard_number * minute


def part2( input_list ):
    """
    Find the guard with the single most likely minute to be asleep.
    """

    guard_data = read_data( input_list )

    sleepiest_guard_number = 0
    sleepiest_guard_minutes = 0
    sleepiest_guard_minute = 0

    # Find the guard that has the highest sleep minute value.
    for guard, _ in guard_data.items():
        minute, value = max( enumerate( guard_data[guard] ),
                             key=operator.itemgetter( 1 ) )
        if value > sleepiest_guard_minutes:
            sleepiest_guard_minutes = value
            sleepiest_guard_minute = minute
            sleepiest_guard_number = guard

    return sleepiest_guard_number * sleepiest_guard_minute


if __name__ == "__main__":
    aoc.main( part1, part2 )
