#!/usr/bin/env python3

import re

import aoc
from aoc import Coord

class GroundMap:
    spring_coord = Coord(500,0)
    just_below_spring_coord = Coord(500,1)

    def __init__(self, input_list):
        # Initialize the map with the spring.
        self._ground_map = dict({self.spring_coord : '+'})
        self._amount_of_water_resting = 0
        self._amount_of_water_flowing = 0

        re_x = re.compile(r'^x=(\d+), y=(\d+)..(\d+)$')
        re_y = re.compile(r'^y=(\d+), x=(\d+)..(\d+)$')

        for line_num, line in enumerate(input_list):
            match = re_x.search(line)
            if match:
                xstart = int(match.group(1))
                xend = int(match.group(1)) + 1
                ystart = int(match.group(2))
                yend = int(match.group(3)) + 1

            match = re_y.search(line)
            if match:
                ystart = int(match.group(1))
                yend = int(match.group(1)) + 1
                xstart = int(match.group(2))
                xend = int(match.group(3)) + 1

            if line_num == 0:
                min_coord_x = xstart
                max_coord_x = xend - 1
                min_coord_y = ystart
                max_coord_y = yend - 1
            else:
                min_coord_x = min(min_coord_x, xstart)
                max_coord_x = max(max_coord_x, xend)
                min_coord_y = min(min_coord_y, ystart)
                max_coord_y = max(max_coord_y, yend)

            for x_coord in range(xstart, xend):
                for y_coord in range(ystart, yend):
                    self._ground_map[Coord(x_coord, y_coord)] = '#'

        # Add a column of output padding for water flow.
        self._min_coord = Coord(min_coord_x - 1, min_coord_y)
        self._max_coord = Coord(max_coord_x, max_coord_y - 1)

    def __str__(self):
        output = ''
        row_label_length = len("%d" % self._max_coord.y_val)
        col_label_length = len("%d" % self._max_coord.x_val)
        for y_index in range(0, col_label_length):
            output += "%*s" % ( row_label_length + 1, ' ')
            for x_index in range(self._min_coord.x_val, self._max_coord.x_val + 1):
                col_label = "%*d" % (col_label_length, x_index)
                output += col_label[y_index]
            output += '\n'

        for y_index in range(0, self._max_coord.y_val + 2):
            output += "%*d " % (row_label_length, y_index)
            for x_index in range(self._min_coord.x_val, self._max_coord.x_val + 1):
                coord = Coord(x_index, y_index)
                output += self._ground_map.get(coord, '.')
            output += '\n'

        return output[0:-1]  # Strip final newline.

    def _coord_is_in_reservoir(self, coord):
        # We can only check coordinates that aren't yet mapped that are mapped below.
        assert self._ground_map.get(coord) is None
        assert coord.y_val == self._max_coord.y_val or \
            self._ground_map.get(Coord(coord.x_val, coord.y_val + 1)) is not None

        # Check by extending the region to the left and then to the right.
        for increment in (-1, 1):
            current_coord = coord
            while True:
                next_coord = Coord(current_coord.x_val + increment, current_coord.y_val)
                if not self._min_coord.x_val < next_coord.x_val < self._max_coord.x_val:
                    return False

                coord_below = Coord(next_coord.x_val, next_coord.y_val + 1)
                contents = self._ground_map.get(coord_below)
                # There not clay below or resting water below (which has clay below it).
                if contents not in ('#', '~'):
                    return False

                contents = self._ground_map.get(next_coord)
                # There is clay in this direction.
                if contents in ('#', '~'):
                    break

                # Flowing water only happens outside of reservoirs.
                if contents == '|':
                    return False

                current_coord = next_coord

        return True

    def _can_add_water_below(self, coord, side):
        assert self._ground_map.get(coord) is None
        assert coord.y_val == self._max_coord.y_val or \
               self._ground_map.get(Coord(coord.x_val, coord.y_val + 1)) is not None

        if side == 'left':
            increment = -1
        elif side == 'right':
            increment = 1
        else:
            assert False

        current_coord = coord
        while True:
            next_coord = Coord(current_coord.x_val + increment, current_coord.y_val)
            next_coord_below = Coord(current_coord.x_val + increment, current_coord.y_val + 1)
            if next_coord in self._ground_map:
                return False

            content_below = self._ground_map.get(next_coord_below)
            if content_below is None:
                return True

            if content_below == '|':
                return False

            # Keep moving and checking.
            current_coord = next_coord


    def add_some_water(self):
        start_coord = type(self).spring_coord
        current_coord = start_coord
        last_lr_coord = start_coord
        done_with_this_drop = False
        while not done_with_this_drop:
            # Go down
            while True:
                next_coord = Coord(current_coord.x_val, current_coord.y_val + 1)
                # Something is below this coordinate.
                if next_coord in self._ground_map:
                    break

                # Too deep.
                if next_coord.y_val > self._max_coord.y_val:
                    done_with_this_drop = True
                    break

                current_coord = next_coord

            if done_with_this_drop:
                break

            coord_below = Coord(current_coord.x_val, current_coord.y_val + 1)
            if self._ground_map.get(coord_below) == '|':
                done_with_this_drop = True

            else:
                # Check left and right.  We only move one step and then we will try
                # to go down again.
                next_coord_left = Coord(current_coord.x_val - 1, current_coord.y_val)
                next_coord_right = Coord(current_coord.x_val + 1, current_coord.y_val)

                if self._can_add_water_below(current_coord, 'left'):
                    last_lr_coord = current_coord
                    current_coord = next_coord_left

                elif self._can_add_water_below(current_coord, 'right'):
                    last_lr_coord = current_coord
                    current_coord = next_coord_right

                elif self._coord_is_in_reservoir(current_coord):
                    while self._ground_map.get(next_coord_left) is None:
                        next_coord_left = Coord(next_coord_left.x_val - 1, next_coord_left.y_val)
                    while self._ground_map.get(next_coord_right) is None:
                        next_coord_right = Coord(next_coord_right.x_val + 1, next_coord_right.y_val)

                    for x_index in range(next_coord_left.x_val + 1, next_coord_right.x_val ):
                        self._ground_map[Coord(x_index, next_coord_right.y_val)] = '~'
                        self._amount_of_water_resting += 1

                    # FIXME logic below will add this back.
                    del self._ground_map[current_coord]
                    self._amount_of_water_resting -= 1

                    done_with_this_drop = True

                # FIXME I can't read this anymore
                elif next_coord_left not in self._ground_map and next_coord_left != last_lr_coord:
                    last_lr_coord = current_coord
                    current_coord = next_coord_left

                elif next_coord_right not in self._ground_map and next_coord_right != last_lr_coord:
                    last_lr_coord = current_coord
                    current_coord = next_coord_right

                else:
                    done_with_this_drop = True

        if self._coord_is_in_reservoir(current_coord):
            self._ground_map[current_coord] = '~'
            self._amount_of_water_resting += 1
        else:
            self._ground_map[current_coord] = '|'
            if self._min_coord.y_val <= current_coord.y_val <= self._max_coord.y_val:
                self._amount_of_water_flowing += 1

    def full_of_water(self):
        # We are full if the coordinate below the spring contains a value.
        return self._ground_map.get(type(self).just_below_spring_coord) is not None

    def simulate(self):
        while not self.full_of_water():
            self.add_some_water()
            #print(self)

        #print(self)

    def get_amount_of_water_resting(self):
        return self._amount_of_water_resting

    def get_amount_of_water_flowing(self):
        return self._amount_of_water_flowing



def part1(input_list):
    ground_map = GroundMap(input_list)
    ground_map.simulate()
    return ground_map.get_amount_of_water_resting() + ground_map.get_amount_of_water_flowing()


def part2(input_list):
    ground_map = GroundMap(input_list)
    ground_map.simulate()
    return ground_map.get_amount_of_water_resting()


if __name__ == "__main__":
    aoc.main(part1, part2)
