
import unittest

import aoc
import day09

class TestDay09( unittest.TestCase ):

    # Input, answer
    example = ( '9 players; last marble is worth 25 points', 32 )

    more_examples = (
        ( '10 players; last marble is worth 1618 points', 8317 ),
        ( '13 players; last marble is worth 7999 points', 146373 ),
        ( '17 players; last marble is worth 1104 points', 2764 ),
        ( '21 players; last marble is worth 6111 points', 54718 ),
        ( '30 players; last marble is worth 5807 points', 37305 )
    )

    def test_part1_example1( self ):
        result = day09.part1( ( self.example[0], ) )
        self.assertEqual( result, self.example[1] )

    def test_part1_example2( self ):
        for case in self.more_examples:
            result = day09.part1( ( case[0], ) )
            self.assertEqual( result, case[1] )

    def test_part1_input( self ):
        result = day09.part1( aoc.read_input( 'day09.input' ) )
        self.assertEqual( result, 398242 )

    def test_part2_input( self ):
        result = day09.part2( aoc.read_input( 'day09.input' ) )
        self.assertEqual( result, 3273842452 )

if __name__ == '__main__':
    unittest.main()
