import unittest

import aoc
import day19


class TestDay19(unittest.TestCase):

    example_input = [
        '#ip 0',
        'seti 5 0 1',
        'seti 6 0 2',
        'addi 0 1 0',
        'addr 1 2 3',
        'setr 1 0 0',
        'seti 8 0 4',
        'seti 9 0 5'
    ]

    def test_part1_input(self):
        reg0 = day19.part1(aoc.read_input('day19.input'))
        self.assertEqual(1152, reg0)

    def test_part2_input(self):
        reg0 = day19.part2(aoc.read_input('day19.input'))
        self.assertEqual(12690000, reg0)


if __name__ == '__main__':
    unittest.main()
