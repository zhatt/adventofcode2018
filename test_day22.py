import unittest

import aoc
import day22


class TestDay22(unittest.TestCase):

    example_input = [
        'depth: 510',
        'target: 10,10'
    ]

    def test_parse_input(self):
        depth, target_coord = day22.parse_input(self.example_input)
        self.assertEqual(510, depth)
        self.assertEqual(aoc.Coord(10, 10), target_coord)

    def test_part1_example1(self):
        risk_level = day22.part1(self.example_input)
        self.assertEqual(114, risk_level)

    def test_part1_input(self):
        risk_level = day22.part1(aoc.read_input('day22.input'))
        self.assertEqual(6323, risk_level)

    def test_part2_example1(self):
        rescue_time = day22.part2(self.example_input)
        self.assertEqual(45, rescue_time)

    def test_part2_input(self):
        rescue_time = day22.part2(aoc.read_input('day22.input'))
        self.assertEqual(982, rescue_time)


if __name__ == '__main__':
    unittest.main()
