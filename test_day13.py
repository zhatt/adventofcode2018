
import unittest

import aoc
import day13

class TestDay13( unittest.TestCase ):

    example_input_part1 = [
        r'/->-\        ',
        r'|   |  /----\\',  # Ugh.  Need to add escape to slash so that we don't have \'.
        r'| /-+--+-\  |',
        r'| | |  | v  |',
        r'\-+-/  \-+--/',
        r'  \------/   '
    ]

    example_input_part2 = [
        r'/>-<\  ',
        r'|   |  ',
        r'| /<+-\\',
        r'| | | v',
        r'\>+</ |',
        r'  |   ^',
        r'  \<->/'
    ]

    #@unittest.skip( 'dev' )
    def test_part1_example1( self ):
        self.assertEqual( day13.part1( self.example_input_part1 ), '7,3' )

    #@unittest.skip( 'dev' )
    def test_part1_input( self ):
        result = day13.part1( aoc.read_input( 'day13.input' ) )
        self.assertEqual( result, '38,57' )

    #@unittest.skip( 'dev' )
    def test_part2_example1( self ):
        self.assertEqual( day13.part2( self.example_input_part2 ), '6,4' )

    #@unittest.skip( 'dev' )
    def test_part2_input( self ):
        result = day13.part2( aoc.read_input( 'day13.input' ) )
        self.assertEqual( result, '4,92' )

if __name__ == '__main__':
    unittest.main()
