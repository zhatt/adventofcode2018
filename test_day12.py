
import unittest

import aoc
import day12

class TestDay12( unittest.TestCase ):

    example_input = [
        'initial state: #..#.#..##......###...###',
        '',
        '...## => #',
        '..#.. => #',
        '.#... => #',
        '.#.#. => #',
        '.#.## => #',
        '.##.. => #',
        '.#### => #',
        '#.#.# => #',
        '#.### => #',
        '##.#. => #',
        '##.## => #',
        '###.. => #',
        '###.# => #',
        '####. => #'
    ]

    def test_part1_example1( self ):
        self.assertEqual( day12.part1( self.example_input ), 325 )

    def test_part1_input( self ):
        result = day12.part1( aoc.read_input( 'day12.input' ) )
        self.assertEqual( result, 3472 )

    def test_part2_example1( self ):
        self.assertEqual( day12.part2( self.example_input ), 999999999374 )

    def test_part2_input( self ):
        result = day12.part2( aoc.read_input( 'day12.input' ) )
        self.assertEqual( result, 2600000000919 )

if __name__ == '__main__':
    unittest.main()
