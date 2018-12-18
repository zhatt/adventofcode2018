#!/usr/bin/env python3

import aoc
from aoc import Coord

class Cart:
    def __init__( self, location, direction, track ):
        self.location = location
        self.direction = direction
        self.track = track
        self.turn = 'left'
        self.crashed = False

    # We sort carts from top to bottom of track map by sorting by y then x.
    def sort_key( self ):
        return self.location.y_val, self.location.x_val

    turns = {
        '>\\': 'v',
        '>/' : '^',
        '<\\': '^',
        '</' : 'v',

        '^\\': '<',
        '^/' : '>',
        'v\\': '>',
        'v/' : '<'
    }

    intersection_turns = {
        ( '>', 'left' )  : ( '^', 'none' ),
        ( '>', 'none' )  : ( '>', 'right' ),
        ( '>', 'right' ) : ( 'v', 'left' ),

        ( '<', 'left' )  : ( 'v', 'none' ),
        ( '<', 'none' )  : ( '<', 'right' ),
        ( '<', 'right' ) : ( '^', 'left' ),

        ( '^', 'left' )  : ( '<', 'none' ),
        ( '^', 'none' )  : ( '^', 'right' ),
        ( '^', 'right' ) : ( '>', 'left' ),

        ( 'v', 'left' )  : ( '>', 'none' ),
        ( 'v', 'none' )  : ( 'v', 'right' ),
        ( 'v', 'right' ) : ( '<', 'left' )
    }

    def turn_me( self, next_track ):
        if next_track == '+':
            self.direction, self.turn = \
                type(self).intersection_turns[ ( self.direction, self.turn ) ]

        elif self.direction + next_track in type(self).turns:
            self.direction = type(self).turns[ self.direction + next_track ]

    def move( self ):
        if self.direction == '>':
            next_location = Coord( self.location.x_val + 1, self.location.y_val )
        elif self.direction == '<':
            next_location = Coord( self.location.x_val - 1, self.location.y_val )
        elif self.direction == '^':
            next_location = Coord( self.location.x_val, self.location.y_val - 1 )
        else: #  self.direction == 'v':
            next_location = Coord( self.location.x_val, self.location.y_val + 1 )

        self.location = next_location
        self.turn_me( self.track[ next_location ] )
        return self.location


def parse_input( input_list ):

    carts = dict()
    track = dict()

    line_num = 0
    for line in input_list:
        for index, symbol in enumerate( line ):
            if symbol in r'\/-|+':
                track[ Coord( index, line_num ) ]  = symbol
            elif symbol in 'v^':
                carts[ Coord( index, line_num ) ] = Cart( Coord( index, line_num ), symbol, track )
                track[ Coord( index, line_num ) ]  = '|'
            elif symbol in '<>':
                carts[ Coord( index, line_num ) ] = Cart( Coord( index, line_num ), symbol, track )
                track[ Coord( index, line_num ) ]  = '-'

        line_num += 1

    return carts


def simulate( carts ):

    first_crash_location = None

    while len( carts ) > 1:
        # We need to simulate the carts in a special order.  Create a list of the carts
        # and sort it in the proper order.  left to right, top to bottom
        cart_list = list( carts.values() )
        cart_list.sort( key=lambda cart: cart.sort_key() )

        for cart in cart_list:
            if cart.crashed:
                # Another carts earlier in the list already crashed into this one.
                continue

            old_location = cart.location
            cart.move()
            del carts[ old_location ]

            if cart.location in carts:
                if not first_crash_location:
                    first_crash_location = cart.location

                carts[ cart.location ].crashed = True
                del carts[ cart.location ]

            else:
                carts[ cart.location ] = cart


    if carts:
        # There is only one cart in the list because all of the others
        # have crashed during the simulation.  Get it's location.  Is
        # there a better way to do this?
        for _,cart in carts.items():
            last_location = cart.location
    else:
        last_location = None

    return first_crash_location, last_location


def part1( input_list ):
    carts = parse_input( input_list )
    first_crash_location, _ = simulate( carts )
    return str( first_crash_location.x_val ) + ',' + str( first_crash_location.y_val )

def part2( input_list ):
    carts = parse_input( input_list )
    _ , last_location = simulate( carts )
    return str( last_location.x_val ) + ',' + str( last_location.y_val )

if __name__ == "__main__":
    aoc.main( part1, part2 )
