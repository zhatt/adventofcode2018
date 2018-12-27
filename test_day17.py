import unittest

import aoc
import day17


class TestDay17(unittest.TestCase):

    example_input = [
        'x=495, y=2..7',
        'y=7, x=495..501',
        'x=501, y=3..7',
        'x=498, y=2..4',
        'x=506, y=1..2',
        'x=498, y=10..13',
        'x=504, y=10..13',
        'y=13, x=498..504'
    ]

    def test_part1_example(self):
        result = day17.part1(self.example_input)
        self.assertEqual(57, result)

    def test_part1_input(self):
        result = day17.part1(aoc.read_input('day17.input'))
        self.assertEqual(50838, result)

    def test_part2_example(self):
        result = day17.part2(self.example_input)
        self.assertEqual(29, result)

    def test_part2_input(self):
        result = day17.part2(aoc.read_input('day17.input'))
        self.assertEqual(43039, result)


if __name__ == '__main__':
    unittest.main()
