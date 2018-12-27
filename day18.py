#!/usr/bin/env python3

import aoc
from aoc import Coord

class LumberMap:
    def __init__(self, input_list):
        line_num = 0
        self.lumber_map = dict()

        x_val = 0  # Make pylint happy.

        for line in input_list:
            for x_val, contents in enumerate(line):
                self.lumber_map[Coord(x_val, line_num)] = contents
            line_num += 1

        self.map_size = Coord(x_val + 1, line_num)

    def get_stats(self):
        tree_acres = 0
        lumberyard_acres = 0

        for y_index in range(self.map_size.y_val):
            for x_index in range(self.map_size.x_val):
                contents = self.lumber_map[Coord(x_index, y_index)]
                if contents == '#':
                    lumberyard_acres += 1
                elif contents == '|':
                    tree_acres += 1

        return tree_acres, lumberyard_acres

    def count_neighbors(self, coord):
        tree_neighbors = 0
        lumberyard_neighbors = 0

        for y_index in range(coord.y_val-1, coord.y_val + 2):
            for x_index in range(coord.x_val-1, coord.x_val + 2):
                neighbor_coord = Coord(x_index, y_index)
                if neighbor_coord == coord:
                    continue

                neighbor_contents = self.lumber_map.get(neighbor_coord)
                if neighbor_contents == '|':
                    tree_neighbors += 1

                elif neighbor_contents == '#':
                    lumberyard_neighbors += 1

        return tree_neighbors, lumberyard_neighbors


    def simulate(self):
        new_lumber_map = dict()

        for y_index in range(self.map_size.y_val):
            for x_index in range(self.map_size.x_val):
                coord = Coord(x_index, y_index)
                ( tree_neighbors, lumberyard_neighbors) = self.count_neighbors(coord)
                current_contents = self.lumber_map[coord]
                new_contents = current_contents
                if current_contents == '.':
                    if tree_neighbors >= 3:
                        new_contents = '|'

                elif current_contents == '|':
                    if lumberyard_neighbors >= 3:
                        new_contents = '#'

                elif current_contents == '#':
                    if lumberyard_neighbors < 1 or tree_neighbors < 1:
                        new_contents = '.'

                else:
                    assert False

                new_lumber_map[coord] = new_contents

        self.lumber_map = new_lumber_map

    def __str__(self):
        output = ''

        for y_index in range(self.map_size.y_val):
            for x_index in range(self.map_size.x_val):
                output += self.lumber_map[Coord(x_index, y_index)]
            output += '\n'

        # Strip final newline.
        return output[:-1]


def part1(input_list):
    lumber_map = LumberMap(input_list)

    for _ in range(10):
        lumber_map.simulate()

    tree_acres, lumberyard_acres = lumber_map.get_stats()

    return tree_acres * lumberyard_acres


def part2(input_list):
    lumber_map = LumberMap(input_list)
    maps_seen = set()

    minute = 0

    # Find a cycle in the simulation and accelerate the rest of the simulation.
    while minute < 1_000_000_000:
        lumber_map.simulate()
        contents = str(lumber_map)
        if contents in maps_seen:
            minute = 1_000_000_000 - (1_000_000_000 % minute)

        maps_seen.add(contents)
        minute += 1

    tree_acres, lumberyard_acres = lumber_map.get_stats()

    return tree_acres * lumberyard_acres


if __name__ == "__main__":
    aoc.main(part1, part2)
