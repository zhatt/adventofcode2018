#!/usr/bin/env python3

from collections import namedtuple
import enum
import heapq

import aoc
from aoc import Coord

class Cave:
    CaveData = namedtuple('CaveData', ['erosion_level', 'erosion_type'])

    class Type(enum.IntEnum):
        ROCKY = 0
        WET = 1
        NARROW = 2

    class Tools(enum.IntEnum):
        NEITHER = enum.auto()
        CLIMBING_GEAR = enum.auto()
        TORCH = enum.auto()

    allowed_tools = {
        Type.ROCKY : {Tools.CLIMBING_GEAR, Tools.TORCH},
        Type.WET : {Tools.NEITHER, Tools.CLIMBING_GEAR},
        Type.NARROW : {Tools.NEITHER, Tools.TORCH}
    }

    other_allowed_tool = {
        (Type.ROCKY, Tools.CLIMBING_GEAR) : Tools.TORCH,
        (Type.ROCKY, Tools.TORCH) : Tools.CLIMBING_GEAR,
        (Type.WET, Tools.NEITHER) : Tools.CLIMBING_GEAR,
        (Type.WET, Tools.CLIMBING_GEAR) : Tools.NEITHER,
        (Type.NARROW, Tools.NEITHER) : Tools.TORCH,
        (Type.NARROW, Tools.TORCH) : Tools.NEITHER
    }

    def __init__(self, depth, target_coord):
        self._depth = depth
        self._target_coord = target_coord
        self._map_data = dict()

    def __str__(self):
        output = list()

        for y_val in range(self._target_coord.y_val + 1):
            for x_val in range(self._target_coord.x_val + 1):
                coord = Coord(x_val, y_val)
                if coord == Coord(0, 0):
                    output += 'M'
                elif coord == self._target_coord:
                    output += 'T'
                else:
                    erosion_type = self.get_map_data(coord).erosion_type
                    if erosion_type == self.Type.ROCKY:
                        output += '.'
                    elif erosion_type == self.Type.WET:
                        output += '='
                    elif erosion_type == self.Type.NARROW:
                        output += '|'
                    else:
                        assert False

            output += '\n'

        # Strip final newline.
        return ''.join(output[:-1])

    def get_map_data(self, coord):
        data = self._map_data.get(coord)

        # Return cached data.
        if data:
            return data

        # Otherwise calculate data to cache.  This will use recursion to
        # calculate most data points.
        if coord == Coord(0,0):
            geologic_index = 0

        elif coord == self._target_coord:
            geologic_index = 0

        elif coord.y_val == 0:
            geologic_index = coord.x_val * 16807

        elif coord.x_val == 0:
            geologic_index = coord.y_val * 48271

        else:
            # Recursively calculate data.
            coord1 = aoc.add_coords(coord, Coord(-1,0))
            coord2 = aoc.add_coords(coord, Coord(0,-1))
            geologic_index = self.get_map_data(coord1).erosion_level * \
                             self.get_map_data(coord2).erosion_level

        erosion_level = (geologic_index + self._depth) % 20183
        erosion_type = self.Type(erosion_level % 3)
        self._map_data[coord] = self.CaveData(erosion_level=erosion_level,
                                              erosion_type=erosion_type)
        return self._map_data[coord]

    def risk_level(self):
        level = 0
        for y_val in range(self._target_coord.y_val + 1):
            for x_val in range(self._target_coord.x_val + 1):
                coord = Coord(x_val, y_val)
                level += self.get_map_data(coord).erosion_type
        return level

    def simulate_rescue(self):
        shortest_rescue_time = 0

        # Store active paths in heap.
        paths_heap = []
        heapq.heappush(paths_heap, (0, Coord(0,0), self.Tools.TORCH))

        # Store shortest time to arrive at this coord with a given tool.  We can
        # have one of two tools deployed in any location.  We keep track of the
        # fastest path to location arriving with each tool.  This effectively
        # makes them appear as two different locations but with the same
        # paths to the next location.
        visited = dict()
        visited[(Coord(0,0),self.Tools.TORCH)] = 0

        while paths_heap:
            (current_time, current_coord, current_tool) = heapq.heappop(paths_heap)
            current_data = self.get_map_data(current_coord)

            if current_coord == self._target_coord:
                arrival_time = current_time

                # Need to swap to torch to see target.
                if current_tool != self.Tools.TORCH:
                    current_time += 7

                if shortest_rescue_time == 0:
                    shortest_rescue_time = current_time
                else:
                    shortest_rescue_time = min(shortest_rescue_time, current_time)

                # We are not guaranteed to be done the first time we get here because
                # if we swapped the torch, there may be other shorter paths that arrive up to
                # 6 seconds later that don't need to swap the torch.
                #
                # We will continue until the arrival time is greater or equal to the fastest
                # rescue time.
                if arrival_time >= shortest_rescue_time:
                    # We are done.  Remove all paths to terminate simulation loop.
                    paths_heap = []

                continue


            for increment in (Coord(0,-1), Coord(-1,0), Coord(1, 0), Coord(0, 1)):
                next_coord = aoc.add_coords(current_coord, increment)
                if next_coord.x_val < 0 or next_coord.y_val < 0:
                    continue

                next_data = self.get_map_data(next_coord)
                next_allowed_tools = self.allowed_tools[next_data.erosion_type]
                if current_tool in next_allowed_tools:
                    # Proceed with current tool.
                    next_tool = current_tool
                    next_time = current_time + 1
                else:
                    # Swap tool and proceed.
                    next_tool = self.other_allowed_tool[(current_data.erosion_type, current_tool)]
                    next_time = current_time + 7 + 1

                visited_time = visited.get((next_coord,next_tool))
                if visited_time is not None and visited_time <= next_time:
                    # This route is now longer then the shortest path we have
                    # found to next_coord.  Abandon it.
                    continue

                visited[next_coord,next_tool] = next_time

                heapq.heappush(paths_heap, (next_time, next_coord, next_tool))

        return shortest_rescue_time


def parse_input(input_list):
    assert input_list[0][0:7] == 'depth: '
    assert input_list[1][0:8] == 'target: '

    index = input_list[0].find(' ')
    depth = int(input_list[0][index+1:])
    index = input_list[1].find(' ')
    index2 = input_list[1].find(',')
    x_val = int(input_list[1][index+1:index2])
    y_val = int(input_list[1][index2+1:])

    return depth, Coord(x_val, y_val)


def part1(input_list):
    depth, target_coord = parse_input(input_list)
    cave = Cave(depth, target_coord)
    return cave.risk_level()


def part2(input_list):
    depth, target_coord = parse_input(input_list)
    cave = Cave(depth, target_coord)

    rescue_time = cave.simulate_rescue()
    return rescue_time


if __name__ == "__main__":
    aoc.main(part1, part2)
