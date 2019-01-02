import unittest
import regex

import aoc
from aoc import Coord
import day20

class TestDay20(unittest.TestCase):

    example_regex1 = r'^WNE$'
    example_map1 = [
        '#####',
        '#.|.#',
        '#-###',
        '#.|X#',
        '#####'
    ]

    example_regex2 = r'^ENWWW(NEEE|SSE(EE|N))$'
    example_map2 = [
        '#########',
        '#.|.|.|.#',
        '#-#######',
        '#.|.|.|.#',
        '#-#####-#',
        '#.#.#X|.#',
        '#-#-#####',
        '#.|.|.|.#',
        '#########'
    ]

    example_regex3 = r'^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$'
    example_map3 = [
        '###########',
        '#.|.#.|.#.#',
        '#-###-#-#-#',
        '#.|.|.#.#.#',
        '#-#####-#-#',
        '#.#.#X|.#.#',
        '#-#-#####-#',
        '#.#.|.|.|.#',
        '#-###-###-#',
        '#.|.|.#.|.#',
        '###########'
    ]

    example_regex4 = r'^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$'
    example_map4 = [
        '#############',
        '#.|.|.|.|.|.#',
        '#-#####-###-#',
        '#.#.|.#.#.#.#',
        '#-#-###-#-#-#',
        '#.#.#.|.#.|.#',
        '#-#-#-#####-#',
        '#.#.#.#X|.#.#',
        '#-#-#-###-#-#',
        '#.|.#.|.#.#.#',
        '###-#-###-#-#',
        '#.|.#.|.|.#.#',
        '#############'
    ]

    example_regex5 = r'^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$'
    example_map5 = [
        '###############',
        '#.|.|.|.#.|.|.#',
        '#-###-###-#-#-#',
        '#.|.#.|.|.#.#.#',
        '#-#########-#-#',
        '#.#.|.|.|.|.#.#',
        '#-#-#########-#',
        '#.#.#.|X#.|.#.#',
        '###-#-###-#-#-#',
        '#.|.#.#.|.#.|.#',
        '#-###-#####-###',
        '#.|.#.|.|.#.#.#',
        '#-#-#####-#-#-#',
        '#.#.|.|.|.#.|.#',
        '###############'
    ]

    def test_regex_partial_matching(self):
        """
        Test out regex library's partial matching capability.  This is needed
        for validating shorter paths as the map is built.
        """
        example_route = r'^ENWWW(NEEE|SSE(EE|N))$'
        map_re = regex.compile(example_route)
        self.assertFalse(map_re.fullmatch("EE", partial=True))
        self.assertTrue(map_re.fullmatch("ENW", partial=True))
        self.assertTrue(map_re.fullmatch("ENWWWSS", partial=True))

    def test_strip_detours(self):
        example_route = r'^ENNWSWW(NEWS|)SSSEEN(WNSENS|)EE(SWEN|)NNN$'
        np_map = day20.NorthPoleMap(example_route)
        route_without_detours, longest_detour = np_map._remove_detours_from_regex(example_route)
        self.assertEqual('^ENNWSWWSSSEENEENNN$', route_without_detours)
        self.assertEqual(6, longest_detour)

    def test_northpolemap_str1(self):
        np_map = day20.NorthPoleMap(r'^ENWWW(NEEE|SSE(EE|N))$')
        # Add | doors.
        np_map._add_door(Coord(-2, +2), Coord(-1, +2))
        np_map._add_door(Coord(-1, +2), Coord(+0, +2))
        np_map._add_door(Coord(+0, +2), Coord(+1, +2))

        np_map._add_door(Coord(-2, +1), Coord(-1, +1))
        np_map._add_door(Coord(-1, +1), Coord(-0, +1))
        np_map._add_door(Coord(+0, +1), Coord(+1, +1))

        np_map._add_door(Coord(+0, +0), Coord(+1, +0))

        np_map._add_door(Coord(-2, -1), Coord(-1, -1))
        np_map._add_door(Coord(-1, -1), Coord(+0, -1))
        np_map._add_door(Coord(+0, -1), Coord(+1, -1))

        # Add - doors.
        np_map._add_door(Coord(-2, +2), Coord(-2, +1))

        np_map._add_door(Coord(-2, +1), Coord(-2, +0))
        np_map._add_door(Coord(+1, +1), Coord(+1, +0))

        np_map._add_door(Coord(-2, +0), Coord(-2, -1))
        np_map._add_door(Coord(-1, +0), Coord(-1, -1))

        self.assertEqual('\n'.join(self.example_map2), str(np_map))

    def test_generate_map1(self):
        np_map = day20.NorthPoleMap(self.example_regex1)
        np_map.generate_map()
        self.assertEqual('\n'.join(self.example_map1), str(np_map))

    def test_generate_map2(self):
        np_map = day20.NorthPoleMap(self.example_regex2)
        np_map.generate_map()
        self.assertEqual('\n'.join(self.example_map2), str(np_map))

    def test_generate_map3(self):
        np_map = day20.NorthPoleMap(self.example_regex3)
        np_map.generate_map()
        self.assertEqual('\n'.join(self.example_map3), str(np_map))

    def test_generate_map4(self):
        np_map = day20.NorthPoleMap(self.example_regex4)
        np_map.generate_map()
        self.assertEqual('\n'.join(self.example_map4), str(np_map))

    def test_generate_map5(self):
        np_map = day20.NorthPoleMap(self.example_regex5)
        np_map.generate_map()
        self.assertEqual('\n'.join(self.example_map5), str(np_map))

    def test_part1_example1(self):
        np_map = day20.NorthPoleMap(self.example_regex1)
        np_map.generate_map()
        self.assertEqual(3, np_map.find_furthest_room()[0])

    def test_part1_example2(self):
        np_map = day20.NorthPoleMap(self.example_regex2)
        np_map.generate_map()
        self.assertEqual(10, np_map.find_furthest_room()[0])

    def test_part1_example3(self):
        np_map = day20.NorthPoleMap(self.example_regex3)
        np_map.generate_map()
        self.assertEqual(18, np_map.find_furthest_room()[0])

    def test_part1_example4(self):
        np_map = day20.NorthPoleMap(self.example_regex4)
        np_map.generate_map()
        self.assertEqual(23, np_map.find_furthest_room()[0])

    def test_part1_example5(self):
        np_map = day20.NorthPoleMap(self.example_regex5)
        np_map.generate_map()
        self.assertEqual(31, np_map.find_furthest_room()[0])

    def test_part1_input(self):
        result = day20.part1(aoc.read_input('day20.input'))
        self.assertEqual(3644, result)

    def test_part2_input(self):
        result = day20.part2(aoc.read_input('day20.input'))
        self.assertEqual(8523, result)


if __name__ == '__main__':
    unittest.main()
