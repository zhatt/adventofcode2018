import unittest

import aoc
import day03

class TestDay03( unittest.TestCase ):

    example = [
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2'
        ]

    def test_part1_example1( self ):
        result = day03.part1( self.example )
        self.assertEqual( result, 4 )

    def test_part1_input( self ):
        result = day03.part1( aoc.read_input( 'day03.input' ) )
        self.assertEqual( result, 113716 )

    def test_part2_example1( self ):
        result = day03.part2( self.example )
        self.assertEqual( result, 3 )

    def test_part2_input( self ):
        result = day03.part2( aoc.read_input( 'day03.input' ) )
        self.assertEqual( result, 742 )

if __name__ == '__main__':
    unittest.main()
