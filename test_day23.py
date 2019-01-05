import unittest

import aoc
import day23


class TestDay23(unittest.TestCase):

    example_input1 = [
        'pos=<0,0,0>, r=4',
        'pos=<1,0,0>, r=1',
        'pos=<4,0,0>, r=3',
        'pos=<0,2,0>, r=1',
        'pos=<0,5,0>, r=3',
        'pos=<0,0,3>, r=1',
        'pos=<1,1,1>, r=1',
        'pos=<1,1,2>, r=1',
        'pos=<1,3,1>, r=1'
    ]

    example_input2 = [
        'pos=<10,12,12>, r=2',
        'pos=<12,14,12>, r=2',
        'pos=<16,12,12>, r=4',
        'pos=<14,14,14>, r=6',
        'pos=<50,50,50>, r=200',
        'pos=<10,10,10>, r=5'
    ]

    def test_part1_example1(self):
        num_bots = day23.part1(self.example_input1)
        self.assertEqual(7, num_bots)

    def test_part1_input(self):
        risk_level = day23.part1(aoc.read_input('day23.input'))
        self.assertEqual(588, risk_level)

    def test_part2_example1(self):
        distance = day23.part2(self.example_input2)
        self.assertEqual(36, distance)

    def test_part2_input(self):
        distance = day23.part2(aoc.read_input('day23.input'))
        self.assertEqual(111227643, distance)


if __name__ == '__main__':
    unittest.main()
