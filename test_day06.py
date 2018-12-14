
import unittest

import aoc
import day06

class TestDay06( unittest.TestCase ):

    example = [
        '1, 1',
        '1, 6',
        '8, 3',
        '3, 4',
        '5, 5',
        '8, 9'
        ]

    def test_distance( self ):
        self.assertEqual( day06.distance( ( 1, 3 ), ( 3, 5 ) ), 4 )
        self.assertEqual( day06.distance( ( 3, 5 ), ( 1, 3 ) ), 4 )
        self.assertEqual( day06.distance( ( 3, 1 ), ( 5, 3 ) ), 4 )
        self.assertEqual( day06.distance( ( 5, 4 ), ( 3, 1 ) ), 5 )
        self.assertEqual( day06.distance( ( 1, 1 ), ( 1, 2 ) ), 1 )
        self.assertEqual( day06.distance( ( 1, 1 ), ( 1, 1 ) ), 0 )

    def test_get_bound( self ):
        data = ( (1, 1), (3, 5), (4, 4) )
        self.assertEqual( day06.get_bound( data, 0  ), ( ( 1, 1 ), ( 4, 5 ) ) )
        self.assertEqual( day06.get_bound( data, 2  ), ( ( -1, -1 ), ( 6, 7 ) ) )

    def test_part1_example1( self ):
        result = day06.part1( self.example )
        self.assertEqual( result, 17 )

    def test_part1_input( self ):
        result = day06.part1( aoc.read_input( 'day06.input' ) )
        self.assertEqual( result, 3260 )

    def test_part2_example1( self ):
        result = day06.part2( self.example, 32 )
        self.assertEqual( result, 16 )

    def test_part2_input( self ):
        result = day06.part2( aoc.read_input( 'day06.input' ) )
        self.assertEqual( result, 42535 )

if __name__ == '__main__':
    unittest.main()
