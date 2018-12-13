
import unittest

import aoc
import day08

class TestDay08( unittest.TestCase ):

    example = [
        '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
        ]

    def test_part1_example1( self ):
        result = day08.part1( self.example )
        self.assertEqual( result, 138 )

    def test_part1_input( self ):
        result = day08.part1( aoc.read_input( 'day08.input' ) )
        self.assertEqual( result, 41926 )

    def test_part2_example1( self ):
        result = day08.part2( self.example )
        self.assertEqual( result, 66 )

    def test_part2_input( self ):
        result = day08.part2( aoc.read_input( 'day08.input' ) )
        self.assertEqual( result, 24262 )

if __name__ == '__main__':
    unittest.main()
