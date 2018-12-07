import unittest

import aoc
import day01

class TestDay01( unittest.TestCase ):

    example = ( 1, -2, 3, 1 )

    def test_part1_example1( self ):
        result = day01.part1( self.example )
        self.assertEqual( result, 3 )

    def test_part1_example2( self ):
        result = day01.part1( ( 1, 1, 1 ) )
        self.assertEqual( result, 3 )

    def test_part1_example3( self ):
        result = day01.part1( ( 1, 1, -2 ) )
        self.assertEqual( result, 0 )

    def test_part1_example4( self ):
        result = day01.part1( ( -1, -2, -3 ) )
        self.assertEqual( result, -6 )

    def test_part1_input( self ):
        result = day01.part1( aoc.readInput( 'day01.input' ) )
        self.assertEqual( result, 561 )


    def test_part2_example1( self ):
        result = day01.part2( self.example )
        self.assertEqual( result, 2 )

    def test_part2_example2( self ):
        result = day01.part2( ( 1, -1 ) )
        self.assertEqual( result, 0 )

    def test_part2_example3( self ):
        result = day01.part2( ( 3, 3, 4, -2, -4 ) )
        self.assertEqual( result, 10 )

    def test_part2_example4( self ):
        result = day01.part2( ( -6, 3, 8, 5, -6 ) )
        self.assertEqual( result, 5 )

    def test_part2_example5( self ):
        result = day01.part2( ( 7, 7, -2, -7, -4 ) )
        self.assertEqual( result, 14 )

    def test_part2_input( self ):
        result = day01.part2( aoc.readInput( 'day01.input' ) )
        self.assertEqual( result, 563 )

if __name__ == '__main__':
    unittest.main()
