
import unittest

import aoc
import day05

class TestDay05( unittest.TestCase ):

    example = [ 'dabAcCaCBAcCcaDA' ]

    def test_part1_example1( self ):
        result = day05.part1( self.example )
        self.assertEqual( result, 10 )

    def test_part1_1( self ):
        result = day05.part1( [ 'Aa' ] )
        self.assertEqual( result, 0 )

    def test_part1_2( self ):
        result = day05.part1( [ 'AaXXAa' ] )
        self.assertEqual( result, 2 )

    def test_part1_3( self ):
        result = day05.part1( [ 'AaAaXXAa' ] )
        self.assertEqual( result, 2 )

    def test_part1_4( self ):
        result = day05.part1( [ 'XXXAaAaXXAa' ] )
        self.assertEqual( result, 5 )

    def test_part1_5( self ):
        result = day05.part1( [ 'XXXAaAaXX' ] )
        self.assertEqual( result, 5 )

    def test_part1_input( self ):
        result = day05.part1( aoc.read_input( 'day05.input' ) )
        self.assertEqual( result, 11152 )

    def test_part2_example1( self ):
        result = day05.part2( self.example )
        self.assertEqual( result, 4 )

    def test_part2_input( self ):
        result = day05.part2( aoc.read_input( 'day05.input' ) )
        self.assertEqual( result, 6136 )

if __name__ == '__main__':
    unittest.main()
