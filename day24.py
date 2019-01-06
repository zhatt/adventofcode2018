#!/usr/bin/env python3

import re

import aoc


def parse_strengths_and_weaknesses(strengths_and_weaknesses):
    immune_to = None
    weak_to = None
    if strengths_and_weaknesses:
        for s_or_w in strengths_and_weaknesses.split('; '):
            tokens = s_or_w.split()
            tag = tokens[0]
            assert tokens[1] == 'to'
            tagvalues = [token.rstrip(',') for token in tokens[2:]]

            if not immune_to and tag == 'immune':
                immune_to = tagvalues
            elif not weak_to and tag == 'weak':
                weak_to = tagvalues
            else:
                assert False
    return immune_to, weak_to


def parse_input(input_list, boost=0):

    regex = r'^' \
            r'(\d+) units each with (\d+) hit points ' \
            r'(\(.+\) )?' \
            r'with an attack that does (\d+) (.+) damage at initiative (\d+)' \
            r'$'

    parser = re.compile(regex)

    in_immune_system_groups = False
    in_infection_groups = False

    immune_system_groups = set()
    infection_groups = set()

    for line in input_list:

        if line == 'Immune System:':
            in_immune_system_groups = True
            in_infection_groups = False
            group_name = 'Immune System'
            group_number = 1
            group_boost = boost

        elif line == 'Infection:':
            in_infection_groups = True
            in_immune_system_groups = False
            group_name = 'Infection'
            group_number = 1
            group_boost = 0

        elif line == '':
            pass  # There is a blank line between groups.

        else:
            match = parser.fullmatch(line)
            assert match
            num_units = int(match.group(1))
            hit_points = int(match.group(2))
            strengths_and_weaknesses = match.group(3)
            if strengths_and_weaknesses is not None:
                strengths_and_weaknesses = strengths_and_weaknesses[1:-2]
            damage = int(match.group(4)) + group_boost
            damage_type = match.group(5)
            initiative = int(match.group(6))

            immune_to, weak_to = parse_strengths_and_weaknesses(strengths_and_weaknesses)

            name = group_name + ' ' + str(group_number)
            group_number += 1
            group = Group(name=name,
                          num_units=num_units, hit_points=hit_points,
                          damage=damage, damage_type=damage_type,
                          initiative=initiative,
                          immune_to=immune_to, weak_to=weak_to)

            if in_immune_system_groups:
                immune_system_groups.add(group)
            elif in_infection_groups:
                infection_groups.add(group)
            else:
                assert False

    return immune_system_groups, infection_groups


class Group:
    def __init__(self, name, num_units, hit_points, damage, damage_type, initiative,
                 immune_to=None, weak_to=None):
        self._name = name
        self._num_units = num_units
        self._hit_points = hit_points
        self._damage = damage
        self._damage_type = damage_type
        self._initiative = initiative
        self._immune_to = immune_to if immune_to else []
        self._weak_to = weak_to if weak_to else []

    def damage_type(self):
        return self._damage_type

    def immune_to(self):
        return self._immune_to

    def weak_to(self):
        return self._weak_to

    def effective_power(self):
        return self._num_units * self._damage

    def initiative(self):
        return self._initiative

    def damage_possible(self, defender):
        damage = self._num_units * self._damage

        if self._damage_type in defender.immune_to():
            damage = 0

        elif self._damage_type in defender.weak_to():
            damage *= 2

        return damage

    def defend(self, attacker):
        assert attacker.damage_type() not in self.immune_to()

        power = attacker.effective_power()
        if attacker.damage_type() in self.weak_to():
            power *= 2

        units_killed = power // self._hit_points
        if units_killed > self._num_units:
            units_killed = self._num_units
        self._num_units -= units_killed

        return units_killed


    def is_dead(self):
        return self._num_units == 0

    def num_units(self):
        return self._num_units


class Battle:
    def __init__(self, immune_system_groups, infection_groups):
        self._immune_system_groups = immune_system_groups
        self._infection_groups = infection_groups

    def _get_selection_order(self):
        selection_order_immune_system = list(self._immune_system_groups)
        selection_order_infection = list(self._infection_groups)

        key_func=lambda group: (group.effective_power(), group.initiative())
        selection_order_immune_system.sort(reverse=True, key=key_func)
        selection_order_infection.sort(reverse=True, key=key_func)

        return selection_order_immune_system, selection_order_infection

    @staticmethod
    def _get_battle_targets(attacking_group, defending_group_in):
        targets = {}
        defending_group = defending_group_in.copy()

        for attacker in attacking_group:
            max_damage = 0
            possible_targets = []
            for defender in defending_group:
                damage = attacker.damage_possible(defender)
                if damage == 0:
                    continue

                if damage > max_damage:
                    max_damage = damage
                    possible_targets = []

                if damage == max_damage:
                    possible_targets.append((defender.effective_power(),
                                             defender.initiative(), defender))

            if possible_targets:
                possible_targets.sort(reverse=True)
                target = possible_targets[0][2]
                targets[attacker] = target
                defending_group.remove(target)

        return targets

    def _get_battle_order(self):
        order = list()
        order.extend(self._immune_system_groups)
        order.extend(self._infection_groups)
        order.sort(reverse=True, key=lambda group: group.initiative())
        return order

    def simulate(self):
        while self._immune_system_groups and self._infection_groups:
            immune_system_selection_order, infection_selection_order = self._get_selection_order()
            targets = {}
            targets.update(self._get_battle_targets(immune_system_selection_order,
                                                    self._infection_groups))
            targets.update(self._get_battle_targets(infection_selection_order,
                                                    self._immune_system_groups))

            battle_order = self._get_battle_order()

            num_killed = 0
            for attacker in battle_order:
                if not attacker.is_dead() and attacker in targets:
                    defender = targets[attacker]
                    num_killed += defender.defend(attacker)
                    if defender.is_dead():
                        # We don't keep track of which group so try to remove from both groups.
                        self._immune_system_groups.discard(defender)
                        self._infection_groups.discard(defender)

            if num_killed == 0:
                # Won't be a winner.
                break


        immune_system_num_units = 0
        infection_num_units = 0
        for group in self._immune_system_groups:
            immune_system_num_units += group.num_units()
        for group in self._infection_groups:
            infection_num_units += group.num_units()

        return immune_system_num_units, infection_num_units


def part1(input_list):
    immune_system_groups, infection_groups = parse_input(input_list)
    battle = Battle(immune_system_groups, infection_groups)
    return sum(battle.simulate())


def part2(input_list):
    boost = 0
    while True:
        boost += 1
        immune_system_groups, infection_groups = parse_input(input_list, boost)
        battle = Battle(immune_system_groups, infection_groups)

        immune_system_num_units, infection_num_units = battle.simulate()

        if infection_num_units == 0:
            break

    return immune_system_num_units


if __name__ == "__main__":
    aoc.main(part1, part2)
