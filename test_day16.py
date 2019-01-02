import unittest

import aoc
import day16


class TestDay16(unittest.TestCase):

    def test_how_many_opcodes_match(self):
        sample = day16.Sample(registers_before=(3, 2, 1, 1), instruction=(9, 2, 1, 2),
                              registers_after=(3, 2, 2, 1))
        opcodes = day16.how_many_opcodes_match(sample)
        self.assertEqual(3, len(opcodes))

    def test_part1_input(self):
        count = day16.part1(aoc.read_input('day16.input'))
        self.assertEqual(640, count)

    def test_part2_input(self):
        final_reg0 = day16.part2(aoc.read_input('day16.input'))
        self.assertEqual(final_reg0, 472)


if __name__ == '__main__':
    unittest.main()
