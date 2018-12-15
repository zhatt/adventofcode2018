
import unittest

import aoc
import day11

class TestDay11( unittest.TestCase ):

    def test_power_calc( self ):
        self.assertEqual( day11.calc_power( 8, aoc.Coord( 3, 5 ) ), 4 )
        self.assertEqual( day11.calc_power( 57, aoc.Coord( 122, 79 ) ), -5 )
        self.assertEqual( day11.calc_power( 39, aoc.Coord( 217, 196 ) ), 0 )
        self.assertEqual( day11.calc_power( 71, aoc.Coord( 101, 153 ) ), 4 )

    # Note that for a manually input grid x and y are swapped because the rows are the first index.
    grid = [
        [ 1, 2, 3, 4 ],
        [ 3, 4, 6, 7 ],
        [ 5, 6, 7, 8 ],
        [ 7, 8, 9, 0 ]
        ]

    def test_calc_power_box( self ):
        self.assertEqual( day11.calc_power_box( self.grid, aoc.Coord( 0, 0 ), 2 ), 10 )
        self.assertEqual( day11.calc_power_box( self.grid, aoc.Coord( 0, 0 ), 3 ), 37 )
        self.assertEqual( day11.calc_power_box( self.grid, aoc.Coord( 0, 1 ), 3 ), 47 )

    def test_calc_power_delta_x( self ):
        power1 = day11.calc_power_box( self.grid, aoc.Coord( 0, 0 ), 2 )
        expect = day11.calc_power_box( self.grid, aoc.Coord( 1, 0 ), 2 )
        power = day11.calc_power_delta_x( power1, self.grid, aoc.Coord( 1, 0 ), 2 )
        self.assertEqual( power, expect )

        power1 = day11.calc_power_box( self.grid, aoc.Coord( 1, 0 ), 2 )
        expect = day11.calc_power_box( self.grid, aoc.Coord( 2, 0 ), 2 )
        power = day11.calc_power_delta_x( power1, self.grid, aoc.Coord( 2, 0 ), 2 )
        self.assertEqual( power, expect )

        power1 = day11.calc_power_box( self.grid, aoc.Coord( 0, 1 ), 3 )
        expect = day11.calc_power_box( self.grid, aoc.Coord( 1, 1 ), 3 )
        power = day11.calc_power_delta_x( power1, self.grid, aoc.Coord( 1, 1 ), 3 )
        self.assertEqual( power, expect )

    def test_calc_power_delta_y( self ):
        power1 = day11.calc_power_box( self.grid, aoc.Coord( 0, 0 ), 2 )
        expect = day11.calc_power_box( self.grid, aoc.Coord( 0, 1 ), 2 )
        power = day11.calc_power_delta_y( power1, self.grid, aoc.Coord( 0, 1 ), 2 )
        self.assertEqual( power, expect )

        power1 = day11.calc_power_box( self.grid, aoc.Coord( 0, 1 ), 2 )
        expect = day11.calc_power_box( self.grid, aoc.Coord( 0, 2 ), 2 )
        power = day11.calc_power_delta_y( power1, self.grid, aoc.Coord( 0, 2 ), 2 )
        self.assertEqual( power, expect )

        power1 = day11.calc_power_box( self.grid, aoc.Coord( 1, 0 ), 3 )
        expect = day11.calc_power_box( self.grid, aoc.Coord( 1, 1 ), 3 )
        power = day11.calc_power_delta_y( power1, self.grid, aoc.Coord( 1, 1 ), 3 )
        self.assertEqual( power, expect )


    def test_part1_example1( self ):
        self.assertEqual( day11.part1( [ 18 ] ), '33,45' )
        self.assertEqual( day11.part1( [ 42 ] ), '21,61' )

    def test_part1_input( self ):
        result = day11.part1( aoc.read_input( 'day11.input' ) )
        self.assertEqual( result, '245,14' )

    #@unittest.skip( 'dev' )
    def test_part2_example1( self ):
        self.assertEqual( day11.part2( [ 18 ] ), '90,269,16' )
        self.assertEqual( day11.part2( [ 42 ] ), '232,251,12' )


    #@unittest.skip( 'dev' )
    def test_part2_input( self ):
        result = day11.part2( aoc.read_input( 'day11.input' ) )
        self.assertEqual( result, '235,206,13' )

if __name__ == '__main__':
    unittest.main()
