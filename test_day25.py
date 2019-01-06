import unittest

import aoc
import day25


class TestDay25(unittest.TestCase):

    example_input1 = [
        '0,0,0,0',
        '3,0,0,0',
        '0,3,0,0',
        '0,0,3,0',
        '0,0,0,3',
        '0,0,0,6',
        '9,0,0,0',
        '12,0,0,0'
    ]

    example_input2 = [
        '-1,2,2,0',
        '0,0,2,-2',
        '0,0,0,-2',
        '-1,2,0,0',
        '-2,-2,-2,2',
        '3,0,2,-1',
        '-1,3,2,2',
        '-1,0,-1,0',
        '0,2,1,-2',
        '3,0,0,0',
        ]

    example_input3 = [
        '1,-1,0,1',
        '2,0,-1,0',
        '3,2,-1,0',
        '0,0,3,1',
        '0,0,-1,-1',
        '2,3,-2,0',
        '-2,2,0,0',
        '2,-2,0,-1',
        '1,-1,0,-1',
        '3,2,0,2'
        ]

    example_input4 = [
        '1,-1,-1,-2',
        '-2,-2,0,1',
        '0,2,1,3',
        '-2,3,-2,1',
        '0,2,3,-2',
        '-1,-1,1,-2',
        '0,-2,-1,0',
        '-2,2,3,-1',
        '1,2,2,0',
        '-1,-2,0,-2',
    ]


    def test_part1_example1(self):
        num_constellations = day25.part1(self.example_input1)
        self.assertEqual(2, num_constellations)

    def test_part1_example2(self):
        num_constellations = day25.part1(self.example_input2)
        self.assertEqual(4, num_constellations)

    def test_part1_example3(self):
        num_constellations = day25.part1(self.example_input3)
        self.assertEqual(3, num_constellations)

    def test_part1_example4(self):
        num_constellations = day25.part1(self.example_input4)
        self.assertEqual(8, num_constellations)

    def test_part1_input(self):
        num_constellations = day25.part1(aoc.read_input('day25.input'))
        self.assertEqual(375, num_constellations)

    def test_part2_input(self):
        result = day25.part2(aoc.read_input('day25.input'))
        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()
