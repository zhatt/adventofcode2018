
import unittest

import aoc
import day10

class TestDay10( unittest.TestCase ):

    # Input, answer
    example = (
        'position=< 9,  1> velocity=< 0,  2>',
        'position=< 7,  0> velocity=<-1,  0>',
        'position=< 3, -2> velocity=<-1,  1>',
        'position=< 6, 10> velocity=<-2, -1>',
        'position=< 2, -4> velocity=< 2,  2>',
        'position=<-6, 10> velocity=< 2, -2>',
        'position=< 1,  8> velocity=< 1, -1>',
        'position=< 1,  7> velocity=< 1,  0>',
        'position=<-3, 11> velocity=< 1, -2>',
        'position=< 7,  6> velocity=<-1, -1>',
        'position=<-2,  3> velocity=< 1,  0>',
        'position=<-4,  3> velocity=< 2,  0>',
        'position=<10, -3> velocity=<-1,  1>',
        'position=< 5, 11> velocity=< 1, -2>',
        'position=< 4,  7> velocity=< 0, -1>',
        'position=< 8, -2> velocity=< 0,  1>',
        'position=<15,  0> velocity=<-2,  0>',
        'position=< 1,  6> velocity=< 1,  0>',
        'position=< 8,  9> velocity=< 0, -1>',
        'position=< 3,  3> velocity=<-1,  1>',
        'position=< 0,  5> velocity=< 0, -1>',
        'position=<-2,  2> velocity=< 2,  0>',
        'position=< 5, -2> velocity=< 1,  2>',
        'position=< 1,  4> velocity=< 2,  1>',
        'position=<-2,  7> velocity=< 2, -2>',
        'position=< 3,  6> velocity=<-1, -1>',
        'position=< 5,  0> velocity=< 1,  0>',
        'position=<-6,  0> velocity=< 2,  0>',
        'position=< 5,  9> velocity=< 1, -2>',
        'position=<14,  7> velocity=<-2,  0>',
        'position=<-3,  6> velocity=< 2, -1>'
    )

    example_solution = (
        '#...#..###',
        '#...#...#.',
        '#...#...#.',
        '#####...#.',
        '#...#...#.',
        '#...#...#.',
        '#...#...#.',
        '#...#..###'
    )

    input_solution = (
        '######..######...####...#####....####....####....####......###',
        '.....#.......#..#....#..#....#..#....#..#....#..#....#......#.',
        '.....#.......#..#.......#....#..#.......#.......#...........#.',
        '....#.......#...#.......#....#..#.......#.......#...........#.',
        '...#.......#....#.......#####...#.......#.......#...........#.',
        '..#.......#.....#.......#....#..#..###..#..###..#...........#.',
        '.#.......#......#.......#....#..#....#..#....#..#...........#.',
        '#.......#.......#.......#....#..#....#..#....#..#.......#...#.',
        '#.......#.......#....#..#....#..#...##..#...##..#....#..#...#.',
        '######..######...####...#####....###.#...###.#...####....###..'
    )

    def test_part1_example1( self ):
        result = day10.part1( self.example )
        self.assertEqual( result, '\n'.join( self.example_solution ) )

    @unittest.skip('dev')
    def test_part1_input( self ):
        result = day10.part1( aoc.read_input( 'day10.input' ) )
        self.assertEqual( result, '\n'.join( self.input_solution ) )

    def test_part2_example1( self ):
        result = day10.part2( self.example )
        self.assertEqual( result, 3 )

    @unittest.skip('dev')
    def test_part2_input( self ):
        result = day10.part2( aoc.read_input( 'day10.input' ) )
        self.assertEqual( result, 10886 )

if __name__ == '__main__':
    unittest.main()
