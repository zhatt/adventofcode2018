
import unittest

import aoc

class TestAoc( unittest.TestCase ):

    coord1 = aoc.Coord(1, 3)
    coord2 = aoc.Coord(21, 2)
    coord3 = aoc.Coord(1, 43)

    def test_add_coord( self ):
        self.assertEqual(aoc.Coord(22, 5), aoc.add_coords(self.coord1, self.coord2))
        self.assertEqual(aoc.Coord(23, 48), aoc.add_coords(self.coord1, self.coord2, self.coord3))

    def test_min_bound_coord( self ):
        self.assertEqual(aoc.Coord(1, 2), aoc.min_bound_coord(self.coord1, self.coord2))
        self.assertEqual(aoc.Coord(1, 2), aoc.min_bound_coord(self.coord1, self.coord2, self.coord3))

    def test_min_bound_coord( self ):
        self.assertEqual(aoc.Coord(1, 43), aoc.max_bound_coord(self.coord1, self.coord3))
        self.assertEqual(aoc.Coord(21, 43), aoc.max_bound_coord(self.coord1, self.coord2, self.coord3))


if __name__ == '__main__':
    unittest.main()
