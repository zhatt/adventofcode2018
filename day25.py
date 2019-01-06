#!/usr/bin/env python3

import aoc


def parse_input(input_list):
    points = []

    for line in input_list:
        point = tuple(map(int, line.split(',')))
        points.append(point)

    return points


def distance(point1, point2):
    dist = 0
    for one, two in zip(point1, point2):
        dist += abs(two - one)
    return dist


def part1(input_list):
    points = parse_input(input_list)

    point_set = set(points)

    constellations = []

    while point_set:
        point = point_set.pop()
        constellation = {point}

        while constellation:
            points_to_add = []
            for point in point_set:
                for con_point in constellation:
                    if distance(con_point, point) <= 3:
                        points_to_add.append(point)
                        break

            for point in points_to_add:
                point_set.remove(point)
                constellation.add(point)

            if not points_to_add:
                constellations.append(constellation)
                constellation = None

    return len(constellations)


def part2(input_list):
    if input_list:
        pass
    return True


if __name__ == "__main__":
    aoc.main(part1, part2)
