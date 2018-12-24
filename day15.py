#!/usr/bin/env python3

import aoc
from aoc import Coord

class SquareData:
    def __init__(self, contains, enemy, coord, attack_power, hit_points):
        self.contains = contains
        self.coord = coord
        self.enemy = enemy
        self.hit_points = hit_points
        self.attack_power = attack_power

class MapData:
    def __init__(self):
        self.grid = dict()
        self.size = Coord(0,0)


def parse_input(input_list, elf_attack_power = 3):
    # Map is a dictionary with Coord keys.
    map_data = MapData()
    x_val = 0
    y_val = 0
    for y_val, line in enumerate(input_list):
        for x_val, char in enumerate(line):
            if char == '.':
                pass
            elif char == 'G':
                map_data.grid[Coord(x_val, y_val)] = \
                    SquareData('G', 'E', Coord(x_val, y_val), 3, 200)
            elif char == 'E':
                map_data.grid[Coord(x_val, y_val)] = \
                    SquareData('E', 'G', Coord(x_val, y_val), elf_attack_power, 200)
            elif char == '#':
                map_data.grid[Coord(x_val, y_val)] = \
                    SquareData('#', '#', Coord(x_val, y_val), 0, 0)
            else:
                assert False  # Bad input

    map_data.size = Coord(x_val + 1, y_val + 1)
    return map_data


def print_map(map_data, show_hitpoints=False):
    output = ''
    for y_val in range(map_data.size.y_val):
        hit_points = list()
        for x_val in range(map_data.size.x_val):
            square = map_data.grid.get(Coord(x_val, y_val))

            if square:
                output += square.contains
                if square.contains in 'GE':
                    hit_points.append("%s(%d)" % (square.contains, square.hit_points))
            else:
                output += '.'

        if hit_points and show_hitpoints:
            output += '   ' + ', '.join(hit_points)
        output += '\n'

    return output


def get_nearby_set(coord):
    return {
        Coord(coord.x_val, coord.y_val - 1),
        Coord(coord.x_val - 1, coord.y_val),
        Coord(coord.x_val + 1, coord.y_val),
        Coord(coord.x_val, coord.y_val + 1)
    }


def is_enemy_nearby(map_data, enemy, coord):
    enemy_list = []

    for neighbor_coord in get_nearby_set(coord):
        square = map_data.grid.get(neighbor_coord)

        if square and square.contains == enemy:
            enemy_list.append(square)

    if not enemy_list:
        return False

    min_hit_points = enemy_list[0].hit_points
    for square in enemy_list:
        min_hit_points = min(min_hit_points, square.hit_points)

    enemies_to_attack_coord = []
    for square in enemy_list:
        if square.hit_points == min_hit_points:
            enemies_to_attack_coord.append(square.coord)

    sort_coord_list_by_reading_order(enemies_to_attack_coord)
    return map_data.grid[enemies_to_attack_coord[0]]


def find_closest_enemy_paths(map_data, coord):
    # Perform breadth first search for enemies.
    # Returns a set of possible paths.  The paths all start at coord and end
    # at a coordinate that we can attack from.
    paths_set = set()  # set of path tuples
    paths_set.add((coord,))
    done = False
    have_path = set()

    # Continue searching while we are looking further and there are valid paths.
    while not done and paths_set:
        done = True
        can_extend_path_lengths = True
        new_paths_set = set()

        # First check if any of the path tips have an enemy nearby.  If so, then
        # we are done extending the paths.
        for path in paths_set:
            have_path.add(path[-1])
            if is_enemy_nearby(map_data, map_data.grid[path[0]].enemy, path[-1]):
                can_extend_path_lengths = False
                new_paths_set.add(path)

        if can_extend_path_lengths:
            # No enemies were found, try to extend the paths.
            for path in paths_set:
                for neighbor_coord in get_nearby_set(path[-1]):
                    # There is already a shorter path to this coord.
                    if neighbor_coord in have_path:
                        continue

                    # If the square is open, extend the list and add it to set
                    # of paths needing testing.  We only need to keep track of
                    # the first, second, and last square in the path because that
                    # is all that is used by the consumer of the list.  Doing
                    # this reduces the size of the paths_set we need to track.
                    # Without this optimization, the size and number of paths to
                    # compute is quite large.
                    if not neighbor_coord in map_data.grid:
                        if len(path) == 1:
                            new_path = (path[0], neighbor_coord)
                        else:
                            new_path = (path[0],path[1], neighbor_coord)
                        new_paths_set.add(new_path)
                        done = False

        paths_set = new_paths_set

    return paths_set


def choose_next_square_coord(path_set):
    # All paths are the same length.  Find the path end that is first in reading order.
    squares = list()
    for path in path_set:
        assert path
        squares.append(path[-1])
    sort_coord_list_by_reading_order(squares)
    chosen_square = squares[0]

    # There might be multiple paths to the chosen square.  Find the one where the first step
    # is first in reading order.  It doesn't matter if there are multiple paths that meet the
    # criteria because we will recalculate paths for the next step.
    next_squares = list()
    for path in path_set:
        if path[-1] == chosen_square:
            if len(path) > 1:
                next_squares.append(path[1])
            else:
                # Don't need to move.
                next_squares.append(path[0])
    sort_coord_list_by_reading_order(next_squares)

    return next_squares[0]


def sort_coord_list_by_reading_order(coord_list):
    coord_list.sort(key=lambda coord: (coord.y_val, coord.x_val))


def get_turn_order(map_data):
    order = []
    for coord, square in map_data.grid.items():
        if square.contains in 'GE':
            order.append(coord)

    sort_coord_list_by_reading_order(order)

    squares = []
    for coord in order:
        squares.append(map_data.grid[coord])

    return squares


def total_hit_points(map_data):
    total = 0
    for square in map_data.grid.values():
        total += square.hit_points
    return total


def attack(map_data, square):
    # Returns True if an elf was killed.

    square_to_attack = is_enemy_nearby(map_data, square.enemy, square.coord)
    if square_to_attack:
        square_to_attack.hit_points -= square.attack_power

        if square_to_attack.hit_points < 1:
            del map_data.grid[square_to_attack.coord]

            if square_to_attack.contains == 'E':
                return True

    return False

def combat(map_data, max_rounds=-1):
    # max_rounds is used for unit testing.

    last_round = 0
    done_battling = False
    elves_killed = 0

    while max_rounds and not done_battling:
        last_round += 1
        max_rounds -= 1
        order = get_turn_order(map_data)
        for square in order:
            if done_battling:
                continue

            count = 0
            for mapsquare in map_data.grid.values():
                if mapsquare.contains == square.enemy:
                    count += 1

            if count == 0:
                done_battling = True
                continue

            if square.hit_points <= 0:
                # This troop was already killed in this round he is no longer in the
                # map but is still in the battle order list.
                continue

            closest_enemy_paths = find_closest_enemy_paths(map_data,
                                                           square.coord)
            if not closest_enemy_paths:
                continue

            done_battling = False

            next_square_coord = choose_next_square_coord(closest_enemy_paths)
            del map_data.grid[square.coord]
            square.coord = next_square_coord
            map_data.grid[next_square_coord] = square

            an_elf_died = attack(map_data, square)
            if an_elf_died:
                elves_killed += 1

    last_total_hit_points = 0
    for square in map_data.grid.values():
        if square.contains in 'GE':
            last_total_hit_points += square.hit_points

    return (last_round-1) * last_total_hit_points, elves_killed


def part1(input_list):
    map_data = parse_input(input_list)
    final_sum, _ = combat(map_data)
    return final_sum


def part2(input_list):
    elf_attack_power = 4
    elves_killed = 1
    while elves_killed:
        map_data = parse_input(input_list, elf_attack_power)
        final_sum, elves_killed = combat(map_data)
        elf_attack_power += 1

    return final_sum


if __name__ == "__main__":
    aoc.main(part1, part2)
