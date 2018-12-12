

import unittest

import aoc
import day07

class TestDay07( unittest.TestCase ):

    example = [
        'Step C must be finished before step A can begin.',
        'Step C must be finished before step F can begin.',
        'Step A must be finished before step B can begin.',
        'Step A must be finished before step D can begin.',
        'Step B must be finished before step E can begin.',
        'Step D must be finished before step E can begin.',
        'Step F must be finished before step E can begin.'
        ]

    def test_calculate_step_time( self ):
        self.assertEqual( day07.calculate_step_time( 'A', 0 ), 1 )
        self.assertEqual( day07.calculate_step_time( 'G', 0 ), 7 )
        self.assertEqual( day07.calculate_step_time( 'G', 1 ), 8 )
        self.assertEqual( day07.calculate_step_time( 'G', 60 ), 67 )
        self.assertEqual( day07.calculate_step_time( 'Z', 0 ), 26 )

        self.assertRaises( AssertionError, day07.calculate_step_time, 'a', 0 )
        self.assertRaises( AssertionError, day07.calculate_step_time, '@', 10 )
        self.assertRaises( AssertionError, day07.calculate_step_time, '[', 0 )

        self.assertRaises( TypeError, day07.calculate_step_time, 'AA', 0 )

    def test_part1_example1( self ):
        result = day07.part1( self.example )
        self.assertEqual( result, 'CABDFE' )

    def test_part1_input( self ):
        result = day07.part1( aoc.read_input( 'day07.input' ) )
        self.assertEqual( result, 'GDHOSUXACIMRTPWNYJLEQFVZBK' )

    def test_part2_example1( self ):
        _,duration = day07.simulate( self.example, 2, 0 )
        self.assertEqual( duration, 15 )

    def test_part2_input( self ):
        result = day07.part2( aoc.read_input( 'day07.input' ) )
        self.assertEqual( result, 1024 )

if __name__ == '__main__':
    unittest.main()
