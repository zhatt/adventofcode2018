#!/usr/bin/env python3

from collections import defaultdict
import re

import aoc

def parse_input( input_list ):

    # dict of lists  i.e. key depends on everything in list.
    dependencies = defaultdict( list )

    for line in input_list:
        # Lines look like:
        # 'Step C must be finished before step A can begin.',
        match_obj = re.search( r'Step (.+) must be finished before step (.+) can begin\.',
                               line )
        assert match_obj

        first = match_obj.group( 1 )
        second = match_obj.group( 2 )

        dependencies[ first ] += []
        dependencies[ second ] += [ first ]

    return dependencies

def dependencies_met( deplist, depdata, working_on ):

    # Check that all steps in the dependency list are complete.
    # If a dependency step is still in depdata or working_on list, the
    # dependencies are not complete.

    for dep in deplist:
        if dep in depdata or dep in working_on:
            return False

    return True


def calculate_step_time( step_name, constant_time_per_step ):

    step_number = ord( step_name ) - ord( 'A' ) + 1

    assert 1 <= step_number <= ( ord( 'Z' ) - ord( 'A' ) + 1 )

    return step_number + constant_time_per_step


def simulate( input_list, num_workers, constant_time_per_step ):
    dependencies = parse_input( input_list )

    # Steps we are working on and how much time is left;
    # key: step, value: time left
    working_on = dict()

    sequence = ''
    duration = 0
    workers = num_workers

    while dependencies or working_on:
        duration += 1

        # Schedule work.
        if workers:
            for step, depends in sorted( dependencies.items() ):
                met = dependencies_met( depends, dependencies, working_on )
                if met:
                    working_on[ step ] = calculate_step_time( step,
                                                              constant_time_per_step )
                    del dependencies[ step ]
                    # Allocate a worker.
                    workers -= 1

                    if not workers:
                        break

        # Do scheduled work.
        for step in list( working_on ):
            time_left = working_on[ step ] - 1

            if time_left == 0:
                # The work for this step is done.  Add it to the output
                # sequence.
                del working_on[ step ]
                sequence += step

                # Worker is now available again.
                workers += 1

            else:
                working_on[ step ] = time_left

    return sequence, duration


def part1( input_list ):
    sequence, _ = simulate( input_list, 1, 0 )
    return sequence


def part2( input_list ):
    _, duration = simulate( input_list, 5, 60 )
    return duration

if __name__ == "__main__":
    aoc.main( part1, part2 )
