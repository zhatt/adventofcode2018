
import unittest

import aoc
import day04

class TestDay04( unittest.TestCase ):

    example =   [
                '[1518-11-01 00:00] Guard #10 begins shift',
                '[1518-11-01 00:05] falls asleep',
                '[1518-11-01 00:25] wakes up',
                '[1518-11-01 00:30] falls asleep',
                '[1518-11-01 00:55] wakes up',
                '[1518-11-01 23:58] Guard #99 begins shift',
                '[1518-11-02 00:40] falls asleep',
                '[1518-11-02 00:50] wakes up',
                '[1518-11-03 00:05] Guard #10 begins shift',
                '[1518-11-03 00:24] falls asleep',
                '[1518-11-03 00:29] wakes up',
                '[1518-11-04 00:02] Guard #99 begins shift',
                '[1518-11-04 00:36] falls asleep',
                '[1518-11-04 00:46] wakes up',
                '[1518-11-05 00:03] Guard #99 begins shift',
                '[1518-11-05 00:45] falls asleep',
                '[1518-11-05 00:55] wakes up'
                ]

    def test_part1_example1( self ):
        result = day04.part1( self.example )
        self.assertEqual( result, 240 )

    def test_part1_input( self ):
        result = day04.part1( aoc.readInput( 'day04.input' ) )
        self.assertEqual( result, 76357 )

    def test_part2_example1( self ):
        result = day04.part2( self.example )
        self.assertEqual( result, 4455 )

    def test_part2_input( self ):
        result = day04.part2( aoc.readInput( 'day04.input' ) )
        self.assertEqual( result, 41668 )

if __name__ == '__main__':
    unittest.main()