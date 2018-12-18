#!/usr/bin/env python3

import aoc


def parse_input( input_list ):

    assert len( input_list ) == 1
    sequence = input_list[0]
    num_recipes_int = int( input_list[0] )
    assert num_recipes_int > 2
    return num_recipes_int, sequence


def part1( input_list ):
    num_recipes_before, _ = parse_input( input_list )

    recipes = [ 3, 7 ]
    num_recipes = num_recipes_before - 2 + 10

    elf1 = 0
    elf2 = 1

    while num_recipes > 0:
        new_sum = recipes[ elf1 ] + recipes[ elf2 ]
        if new_sum >= 10:
            score1 = new_sum // 10
            score2 = new_sum % 10
            recipes.append( score1 )
            recipes.append( score2 )
            num_recipes -= 2
        else:
            recipes.append( new_sum )
            num_recipes -= 1

        elf1 = ( elf1 + 1 + recipes[ elf1 ] ) % len( recipes )
        elf2 = ( elf2 + 1 + recipes[ elf2 ] ) % len( recipes )

    result = ''.join( str(e) for e in recipes[ num_recipes_before : num_recipes_before + 10 ] )

    return result


def part2( input_list ):
    _, sequence = parse_input( input_list )

    recipes = [ 3, 7 ]

    elf1 = 0
    elf2 = 1

    while True:
        new_sum = recipes[ elf1 ] + recipes[ elf2 ]
        if new_sum >= 10:
            score1 = new_sum // 10
            score2 = new_sum % 10
            recipes.append( score1 )
            recipes.append( score2 )
        else:
            recipes.append( new_sum )

        elf1 = ( elf1 + 1 + recipes[ elf1 ] ) % len( recipes )
        elf2 = ( elf2 + 1 + recipes[ elf2 ] ) % len( recipes )

        result = ''.join( str(e) for e in recipes[ -len( sequence ) : ] )
        if result == sequence:
            break

        # We also need to check the sequence ending in score1.
        result = ''.join( str(e) for e in recipes[ -len( sequence ) - 1 : -1 ] )
        if result == sequence:
            del recipes[-1]
            break

    return len( recipes ) - len( sequence )


if __name__ == "__main__":
    aoc.main( part1, part2 )
