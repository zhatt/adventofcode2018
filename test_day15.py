import unittest

import aoc
from aoc import Coord
import day15


class TestDay15(unittest.TestCase):
    map_data_input_order_tests = [
        '#######',
        '#.G.E.#',
        '#E.G.E#',
        '#.G.E.#',
        '#######'
    ]

    map_data_input_choose_open_tests = [
        '#######',
        '#E..G.#',
        '#...#.#',
        '#.G.#G#',
        '#######'
    ]

    map_data_input_next_step_tests = [
        '#######',
        '#.E...#',
        '#.....#',
        '#...G.#',
        '#######'
    ]

    def test_parse(self):
        map_data = day15.parse_input(self.map_data_input_order_tests)
        map_output = day15.print_map(map_data)
        self.assertEqual('\n'.join(self.map_data_input_order_tests) + '\n', map_output)

    def test_sort_coord(self):
        input_list = [
            Coord(3, 1), Coord(4, 5), Coord(2, 4)
        ]
        expected_output_list = [
            Coord(3, 1), Coord(2, 4), Coord(4, 5)
        ]
        day15.sort_coord_list_by_reading_order(input_list)
        self.assertEqual(expected_output_list, input_list)

    def test_get_turn_order(self):
        map_data = day15.parse_input(self.map_data_input_order_tests)
        order = day15.get_turn_order(map_data)
        self.assertEqual([
            Coord(2, 1), Coord(4, 1),
            Coord(1, 2), Coord(3, 2), Coord(5, 2),
            Coord(2, 3), Coord(4, 3)
        ], list(map(lambda square: square.coord, order)))

    def test_get_nearby_coords(self):
        nearby_set = day15.get_nearby_set(Coord(2, 5))
        nearby_list = list(nearby_set)
        day15.sort_coord_list_by_reading_order(nearby_list)
        self.assertEqual([Coord(2, 4), Coord(1, 5), Coord(3, 5), Coord(2, 6)], nearby_list)

    def test_is_enemy_nearby(self):
        map_data = day15.parse_input(self.map_data_input_choose_open_tests)
        # Not close
        self.assertFalse(day15.is_enemy_nearby(map_data, 'G', Coord(1, 1)))
        # Is Diagonal
        self.assertFalse(day15.is_enemy_nearby(map_data, 'E', Coord(2, 2)))
        self.assertFalse(day15.is_enemy_nearby(map_data, 'G', Coord(3, 2)))
        self.assertFalse(day15.is_enemy_nearby(map_data, 'G', Coord(1, 2)))
        self.assertFalse(day15.is_enemy_nearby(map_data, 'G', Coord(3, 2)))
        # I am above
        self.assertTrue(day15.is_enemy_nearby(map_data, 'G', Coord(2, 2)))
        # I am below
        self.assertTrue(day15.is_enemy_nearby(map_data, 'E', Coord(1, 2)))
        # I am left
        self.assertTrue(day15.is_enemy_nearby(map_data, 'G', Coord(1, 3)))
        # I am right
        self.assertTrue(day15.is_enemy_nearby(map_data, 'G', Coord(3, 3)))

    def test_find_closest_enemy_paths(self):
        map_data = day15.parse_input(self.map_data_input_choose_open_tests)
        closest_paths = day15.find_closest_enemy_paths(map_data, Coord(1, 1))
        # There are 4 possible paths
        self.assertEqual(4, len(closest_paths))
        # All paths are 3 long.
        self.assertEqual(3, len(list(closest_paths)[0]))
        self.assertEqual(3, len(list(closest_paths)[1]))
        self.assertEqual(3, len(list(closest_paths)[2]))
        self.assertEqual(3, len(list(closest_paths)[3]))
        # Check the paths.
        self.assertTrue((Coord(1, 1), Coord(2, 1), Coord(3, 1)) in closest_paths)
        self.assertTrue((Coord(1, 1), Coord(2, 1), Coord(2, 2)) in closest_paths)
        self.assertTrue((Coord(1, 1), Coord(1, 2), Coord(2, 2)) in closest_paths)
        self.assertTrue((Coord(1, 1), Coord(1, 2), Coord(1, 3)) in closest_paths)

    def test_choose_enemy_and_next_square1(self):
        map_data = day15.parse_input(self.map_data_input_choose_open_tests)
        closest_paths = day15.find_closest_enemy_paths(map_data, Coord(1, 1))
        next_square = day15.choose_next_square_coord(closest_paths)
        self.assertEqual(Coord(2, 1), next_square)

    def test_choose_enemy_and_next_square2(self):
        map_data = day15.parse_input(self.map_data_input_next_step_tests)
        closest_paths = day15.find_closest_enemy_paths(map_data, Coord(2, 1))
        next_square = day15.choose_next_square_coord(closest_paths)
        self.assertEqual(Coord(3, 1), next_square)

    def test_movement(self):
        input_list = [
            '#########',
            '#G..G..G#',
            '#.......#',
            '#.......#',
            '#G..E..G#',
            '#.......#',
            '#.......#',
            '#G..G..G#',
            '#########'
        ]

        output_list = [
            '#########',
            '#.......#',
            '#..GGG..#',
            '#..GEG..#',
            '#G..G...#',
            '#......G#',
            '#.......#',
            '#.......#',
            '#########'
        ]

        map_data = day15.parse_input(input_list)
        day15.combat(map_data, max_rounds=3)
        map_output = day15.print_map(map_data)
        self.assertEqual('\n'.join(output_list) + '\n', map_output)

    def test_battle1(self):
        input_list = [
            '#######',
            '#.G...#',
            '#...EG#',
            '#.#.#G#',
            '#..G#E#',
            '#.....#',
            '#######'
        ]

        map_data = day15.parse_input(input_list)
        final_sum, _ = day15.combat(map_data)
        self.assertEqual(27730, final_sum)

    def test_battle2(self):
        input_list = [
            '#######',
            '#G..#E#',
            '#E#E.E#',
            '#G.##.#',
            '#...#E#',
            '#...E.#',
            '#######'
        ]

        map_data = day15.parse_input(input_list)
        final_sum, _ = day15.combat(map_data)
        self.assertEqual(36334, final_sum)

    def test_battle3(self):
        input_list = [
            '#######',
            '#E..EG#',
            '#.#G.E#',
            '#E.##E#',
            '#G..#.#',
            '#..E#.#',
            '#######'
        ]

        map_data = day15.parse_input(input_list)
        final_sum, _ = day15.combat(map_data)
        self.assertEqual(39514, final_sum)

    def test_battle4(self):
        input_list = [
            '#######',
            '#E.G#.#',
            '#.#G..#',
            '#G.#.G#',
            '#G..#.#',
            '#...E.#',
            '#######'
        ]

        map_data = day15.parse_input(input_list)
        final_sum, _ = day15.combat(map_data)
        self.assertEqual(27755, final_sum)

    def test_battle5(self):
        input_list = [
            '#######',
            '#.E...#',
            '#.#..G#',
            '#.###.#',
            '#E#G#G#',
            '#...#G#',
            '#######'
        ]

        map_data = day15.parse_input(input_list)
        final_sum, _ = day15.combat(map_data)
        self.assertEqual(28944, final_sum)


    def test_battle6(self):
        input_list = [
            '#########',
            '#G......#',
            '#.E.#...#',
            '#..##..G#',
            '#...##..#',
            '#...#...#',
            '#.G...G.#',
            '#.....G.#',
            '#########'
        ]

        map_data = day15.parse_input(input_list)
        final_sum, _ = day15.combat(map_data)
        self.assertEqual(18740, final_sum)


    def test_part1_input(self):
        final_sum = day15.part1(aoc.read_input('day15.input'))
        self.assertEqual(346574, final_sum)


    def test_part2_input(self):
        final_sum = day15.part2(aoc.read_input('day15.input'))
        self.assertEqual(final_sum, 60864)


if __name__ == '__main__':
    unittest.main()
