import unittest

import aoc
import day21


class TestDay21(unittest.TestCase):

    def test_part1_input(self):
        reg0 = day21.part1(aoc.read_input('day21.input'))
        self.assertEqual(6778585, reg0)

    def test_part2_input(self):
        reg0 = day21.part2(aoc.read_input('day21.input'))
        self.assertEqual(6534225, reg0)


if __name__ == '__main__':
    unittest.main()
