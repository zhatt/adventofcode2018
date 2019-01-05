#!/usr/bin/env python3

from collections import namedtuple
import re
import z3

import aoc

Coord3 = namedtuple('Coord3', ['x_val', 'y_val', 'z_val'])
NanoBot = namedtuple('NanoBot', ['coord', 'radius'])


def parse_input(input_list):

    parser = re.compile(r'^pos=<(.+),(.+),(.+)>, r=(.+)$')
    nanobots = set()

    for line in  input_list:
        match = parser.fullmatch(line)
        assert match
        x_val = int(match.group(1))
        y_val = int(match.group(2))
        z_val = int(match.group(3))
        r_val = int(match.group(4))

        nanobots.add(NanoBot(Coord3(x_val, y_val, z_val), r_val))

    return nanobots


def part1(input_list):
    nanobots = parse_input(input_list)

    largest_nanobot = NanoBot(Coord3(0,0,0), 0)
    for nanobot in nanobots:
        if nanobot.radius > largest_nanobot.radius:
            largest_nanobot = nanobot

    num_nanobots = 0
    for nanobot in nanobots:
        distance = abs(nanobot.coord.x_val - largest_nanobot.coord.x_val) + \
                   abs(nanobot.coord.y_val - largest_nanobot.coord.y_val) + \
                   abs(nanobot.coord.z_val - largest_nanobot.coord.z_val)

        if distance <= largest_nanobot.radius:
            num_nanobots += 1

    return num_nanobots


def z3_abs(value):
    return z3.If(value >= 0, value, -value)

def z3_dist(coord1, coord2):
    return z3_abs(coord1[0] - coord2[0]) + \
           z3_abs(coord1[1] - coord2[1]) + \
           z3_abs(coord1[2] - coord2[2])

def part2(input_list):
    # Use z3 to find x,y,z that maximizes number_of_nearby_bots(x,y,z).
    # Based on https://github.com/msullivan's solution.

    nanobots = parse_input(input_list)

    z3_x_val = z3.Int('x')
    z3_y_val = z3.Int('y')
    z3_z_val = z3.Int('z')

    best_location = (z3_x_val, z3_y_val, z3_z_val)

    z3_number_of_bots = z3.Int('number_of_bots')

    z3_number_of_nearby_bots = z3_x_val * 0
    for nanobot in nanobots:
        z3_number_of_nearby_bots += z3.If(z3_dist(best_location, nanobot[0]) <= nanobot[1], 1, 0)

    optimize = z3.Optimize()
    optimize.add(z3_number_of_bots == z3_number_of_nearby_bots)
    optimize.maximize(z3_number_of_bots)
    optimize.minimize(z3_dist((0,0,0), (z3_x_val, z3_y_val, z3_z_val)))

    optimize.check()

    model = optimize.model()

    position = (model[z3_x_val].as_long(),
                model[z3_y_val].as_long(),
                model[z3_z_val].as_long())

    distance = abs(position[0]) + abs(position[1]) + abs(position[2])
    return distance

if __name__ == "__main__":
    aoc.main(part1, part2)
