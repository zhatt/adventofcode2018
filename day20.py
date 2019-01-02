#!/usr/bin/env python3

from collections import deque
from collections import namedtuple
import sys

import regex

import aoc
from aoc import Coord


class NorthPoleMap:
    direction_mapping = {
        # Direction : Coord to add to current location to move that direction.
        'N': Coord(0, 1),
        'E': Coord(1, 0),
        'S': Coord(0, -1),
        'W': Coord(-1, 0)
    }

    def __init__(self, map_regex_with_detours):
        sys.setrecursionlimit(10000)  # Needed to compile the complex regex.

        map_regex, self._longest_detour = self._remove_detours_from_regex(map_regex_with_detours)

        self._map_regex_with_detours = regex.compile(map_regex_with_detours)
        self._map_regex = regex.compile(map_regex)
        # Store the map as a sparse dictionary of doors which will be '-' or '|'.
        self._map_data = dict()
        self._min_coord = Coord(0, 0)
        self._max_coord = Coord(0, 0)

    def __str__(self):
        output = list()

        # Add bottom.
        output += '#' * (((self._max_coord.x_val - self._min_coord.x_val + 1) * 2) + 1) + '\n'

        for y_val in range(self._max_coord.y_val, self._min_coord.y_val - 1, -1):

            # Draw row containing '|' doors
            output += '#.'
            for x_val in range(self._min_coord.x_val, self._max_coord.x_val):
                coord1 = Coord(x_val, y_val)
                coord2 = Coord(x_val+1, y_val)
                output += self._map_data.get((coord1, coord2), '#')
                if coord2 == Coord(0, 0):
                    output += 'X'
                else:
                    output += '.'
            output += '#\n'

            # Draw row containing '-' doors.  This will also draw the bottom perimeter wall because
            # it goes one index past self._min_coord.y.
            output += '#'
            for x_val in range(self._min_coord.x_val, self._max_coord.x_val + 1):
                coord1 = Coord(x_val, y_val-1)
                coord2 = Coord(x_val, y_val)
                output += self._map_data.get((coord1, coord2), '#')
                output += '#'
            output += '\n'

        # Strip final '\n' from output.
        return ''.join(output[:-1])

    @staticmethod
    def _remove_detours_from_regex(regex_route):
        longest_detour = 0

        while True:
            # Detours end in '|)'
            index_end = regex_route.find('|)')
            if index_end == -1:
                break

            index_begin = regex_route.rfind('(', 0, index_end)
            # We assume that all detours don't have sub-patterns or multiple paths.
            assert index_begin != -1
            assert -1 == regex_route.rfind(')', index_begin+1, index_end-1)
            assert -1 == regex_route.rfind('|', index_begin+1, index_end-1)

            longest_detour = max(longest_detour, index_end - index_begin - 1)

            regex_route = regex_route[:index_begin] + regex_route[index_end + 2:]

        return regex_route, longest_detour


    def _add_door(self, coord1, coord2):
        if coord2 < coord1:
            coord1, coord2 = coord2, coord1
        assert coord1 != coord2
        assert coord1.x_val == coord2.x_val and coord1.y_val == coord2.y_val - 1 or \
               coord1.x_val == coord2.x_val - 1 and coord1.y_val == coord2.y_val

        self._min_coord = aoc.min_bound_coord(self._min_coord, coord1, coord2)
        self._max_coord = aoc.max_bound_coord(self._max_coord, coord1, coord2)

        if coord1.x_val == coord2.x_val:
            door_type = '-'
        else:
            door_type = '|'
        self._map_data[(coord1, coord2)] = door_type

    def _is_door(self, coord1, coord2):
        if coord2 < coord1:
            coord1, coord2 = coord2, coord1
        assert coord1 != coord2
        assert coord1.x_val == coord2.x_val and coord1.y_val == coord2.y_val - 1 or \
               coord1.x_val == coord2.x_val - 1 and coord1.y_val == coord2.y_val

        return Coord(coord1, coord2) in self._map_data

    def _find_paths(self, seed_coord, seed_path, max_depth=-1, take_detours=False):
        # Perform a breadth first search of valid paths to discover the doors.

        PathData = namedtuple( 'PathData', ['current_coord', 'current_path'] )

        paths = deque([PathData(seed_coord, seed_path)])
        final_paths = []

        while paths and max_depth != 0:
            max_depth -= 1

            path_data = paths.popleft()

            path_was_extended = False
            for direction, increment in self.direction_mapping.items():
                new_coord = aoc.add_coords(path_data.current_coord, increment)
                new_path = path_data.current_path + direction

                if take_detours:
                    match = self._map_regex_with_detours.fullmatch(new_path, partial=True)
                else:
                    match = self._map_regex.fullmatch(new_path, partial=True)

                if match:
                    paths.append(PathData(new_coord, new_path))
                    path_was_extended = True
                    self._add_door(path_data.current_coord, new_coord)

            if not path_was_extended:
                final_paths.append(path_data.current_path)

        return final_paths


    def generate_map(self):
        final_paths = self._find_paths(Coord(0,0), '')

        paths_simulated = set()

        # Re-walk the final_paths taking detours.
        for path in final_paths:
            new_path = ''
            coord = Coord(0,0)
            for char in path:
                new_path += char
                coord = aoc.add_coords(coord, self.direction_mapping[char])

                if new_path not in paths_simulated:
                    self._find_paths(coord, new_path, max_depth=self._longest_detour,
                                     take_detours=True)
                    paths_simulated.add(new_path)

    def find_furthest_room(self):
        # Perform a breadth first search.
        paths = deque([(Coord(0,0), '')])
        rooms_visited = set(Coord(0,0))

        num_doors = 0
        num_doors_is_1000_or_more = 0

        while paths:
            current_coord, current_path = paths.popleft()

            for direction, increment in self.direction_mapping.items():
                next_coord = aoc.add_coords(current_coord, increment)
                if next_coord in rooms_visited:
                    continue

                if self._is_door(current_coord, next_coord):
                    next_path = current_path + direction
                    paths.append((next_coord, next_path))
                    num_doors = max(num_doors, len(next_path))

                    # Most of these paths have common beginnings to we only need to re-simulate
                    # if we haven't done next_path already when simulating a previous path.
                    if next_coord not in rooms_visited:
                        rooms_visited.add(next_coord)
                        if num_doors >= 1000:
                            num_doors_is_1000_or_more += 1

        return num_doors, num_doors_is_1000_or_more


def part1(input_list):
    route_regex = input_list[0]
    np_map = NorthPoleMap(route_regex)
    np_map.generate_map()
    return np_map.find_furthest_room()[0]


def part2(input_list):
    route_regex = input_list[0]
    np_map = NorthPoleMap(route_regex)
    np_map.generate_map()
    return np_map.find_furthest_room()[1]


if __name__ == "__main__":
    aoc.main(part1, part2)
