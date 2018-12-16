#!/usr/bin/env python3

import aoc

def parse_input( input_list ):
    initial_state = input_list[ 0 ][ 15: ]
    assert input_list[ 1 ] == ''

    transistions = dict()

    for line in input_list[ 2: ]:
        plant_state = line[ 0:5 ]
        next_state = line[ 9 ]
        transistions[ plant_state ] = next_state

    return initial_state, transistions


def trim_pot_state( pot_state ):
    '''
    Trim the leading and trailing . from the pot_state string.
    Return the new pot state and the number of pots trimmed from the
    beginning of the pot_state string so that it can be adjusted.
    '''

    index = pot_state.index( '#' )
    rindex = pot_state.rindex( '#' )

    pot_state = pot_state[ index: rindex + 1 ]
    return pot_state, index


def calculate_pot_sum( pot_state, first_pot ):
    pot_sum = 0
    for index, state in enumerate( pot_state ):
        if state == '#':
            pot_sum += index + first_pot

    return pot_sum


def simulate( input_list, generations_to_simulate ):
    pot_state, transistions = parse_input( input_list )
    first_pot = 0

    last_pot_state = ''
    last_first_pot = 0

    gen = 0
    while True:
        # Add empty pots at the beginning and ending of the sequence to make
        # matching the pattern work at the ends of the sequence.
        pot_state = '....' + pot_state + '....'
        first_pot -= 4

        next_pot_state = '..'

        for pot_index in range( 0, len( pot_state ) - 5 ):
            key = pot_state[ pot_index : pot_index + 5 ]

            # If key doesn't exist, we assume no plant in the next generation
            # this should only happen with the example transitions because
            # the normal input should have all possible transitions.
            next_pot = transistions.get( key, '.' )

            next_pot_state += next_pot

        pot_state, adjustement = trim_pot_state( next_pot_state )
        first_pot += adjustement

        gen += 1
        if gen == generations_to_simulate:
            break

        # When simulating a large number, we found that eventually, the two
        # generations will have the same sequence but the first pot may have
        # changed.  Update the first pot to the final value and end the
        # simulation.
        elif last_pot_state == pot_state:
            delta_per_gen = first_pot - last_first_pot
            first_pot += ( generations_to_simulate - gen ) * delta_per_gen
            break

        last_pot_state = pot_state
        last_first_pot = first_pot

    return calculate_pot_sum( pot_state, first_pot )


def part1( input_list ):
    return simulate( input_list, 20 )

def part2( input_list ):
    return simulate( input_list, 50000000000 )

if __name__ == "__main__":
    aoc.main( part1, part2 )
