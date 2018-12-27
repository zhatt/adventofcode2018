import unittest

import aoc
import day18


class TestDay18(unittest.TestCase):

    example_input = [
        '.#.#...|#.',
        '.....#|##|',
        '.|..|...#.',
        '..|#.....#',
        '#.#|||#|#|',
        '...#.||...',
        '.|....|...',
        '||...#|.#|',
        '|.||||..|.',
        '...#.|..|.'
    ]

    def test_part1_example(self):
        result = day18.part1(self.example_input)
        self.assertEqual(1147, result)

    def test_part1_input(self):
        result = day18.part1(aoc.read_input('day18.input'))
        self.assertEqual(536370, result)

    def test_part2_example(self):
        result = day18.part2(self.example_input)
        self.assertEqual(0, result)

    def test_part2_input(self):
        result = day18.part2(aoc.read_input('day18.input'))
        self.assertEqual(190512, result)


if __name__ == '__main__':
    unittest.main()
