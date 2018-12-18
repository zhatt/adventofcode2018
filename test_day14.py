
import unittest

import aoc
import day14

class TestDay14( unittest.TestCase ):

    #@unittest.skip( 'dev' )
    def test_part1_example1( self ):
        self.assertEqual( day14.part1( [ '9' ] ), '5158916779' )
        self.assertEqual( day14.part1( [ '5' ] ), '0124515891' )
        self.assertEqual( day14.part1( [ '18' ] ), '9251071085' )
        self.assertEqual( day14.part1( [ '2018' ] ), '5941429882' )

    #@unittest.skip( 'dev' )
    def test_part1_input( self ):
        result = day14.part1( aoc.read_input( 'day14.input' ) )
        self.assertEqual( result, '5715102879' )

    #@unittest.skip( 'dev' )
    def test_part2_example1( self ):
        self.assertEqual( day14.part2( [ '51589'] ), 9 )
        self.assertEqual( day14.part2( [ '01245'] ), 5 )
        self.assertEqual( day14.part2( [ '92510'] ), 18 )
        self.assertEqual( day14.part2( [ '59414'] ), 2018 )

    #@unittest.skip( 'dev' )
    def test_part2_input( self ):
        result = day14.part2( aoc.read_input( 'day14.input' ) )
        self.assertEqual( result,  20225706 )

if __name__ == '__main__':
    unittest.main()
