import unittest

import aoc
import day24


class TestDay24(unittest.TestCase):

    example_input1 = [
        'Immune System:',

        '17 units each with 5390 hit points (weak to radiation, bludgeoning) '
        'with an attack that does 4507 fire damage at initiative 2',

        '989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) '
        'with an attack that does 25 slashing damage at initiative 3',
        '',

        'Infection:',

        '801 units each with 4706 hit points (weak to radiation) '
        'with an attack that does 116 bludgeoning damage at initiative 1',

        '4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) '
        'with an attack that does 12 slashing damage at initiative 4'
    ]

    def test_part1_example1(self):
        num_units = day24.part1(self.example_input1)
        self.assertEqual(5216, num_units)

    def test_part1_input(self):
        num_units = day24.part1(aoc.read_input('day24.input'))
        self.assertEqual(14799, num_units)

    def test_part2_example1(self):
        distance = day24.part2(self.example_input1)
        self.assertEqual(51, distance)

    def test_part2_input(self):
        distance = day24.part2(aoc.read_input('day24.input'))
        self.assertEqual(4428, distance)


if __name__ == '__main__':
    unittest.main()
