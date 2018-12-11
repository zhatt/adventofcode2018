import unittest

import aoc
import day02

class TestDay02( unittest.TestCase ):

    def test_part1_example1( self ):
        input = [
                'abcdef',
                'bababc',
                'abbcde',
                'abcccd',
                'aabcdd',
                'abcdee',
                'ababab'
                ]

        result = day02.part1( input )
        self.assertEqual( result, 12 )

    def test_part1_input( self ):
        result = day02.part1( aoc.read_input( 'day02.input' ) )
        self.assertEqual( result, 5478 )


    def test_part2_example1( self ):
        input = [
                'abcde',
                'fghij',
                'klmno',
                'pqrst',
                'fguij',
                'axcye',
                'wvxyz'
                ]

        result = day02.part2( input )
        self.assertEqual( result, 'fgij' )

    def test_part2_input( self ):
        result = day02.part2( aoc.read_input( 'day02.input' ) )
        self.assertEqual( result, 'qyzphxoiseldjrntfygvdmanu' )

if __name__ == '__main__':
    unittest.main()
