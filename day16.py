#!/usr/bin/env python3

import re

import aoc

class Computer:

    def __init__(self, registers):
        self._registers = registers

    def get_registers(self):
        return tuple(self._registers)

    def execute_as(self, operation, instruction):
        self.ops_by_name[operation](self, instruction)

    def execute(self, instruction):
        self.ops_by_number[instruction[0]](self, instruction)

    ops_by_name = dict()

    def op_addr(self, instruction):
        self._registers[instruction[3]] = self._registers[instruction[1]] + \
                                          self._registers[instruction[2]]
    ops_by_name['addr'] = op_addr

    def op_addi(self, instruction):
        self._registers[instruction[3]] = self._registers[instruction[1]] + \
                                          instruction[2]
    ops_by_name['addi'] = op_addi

    def op_mulr(self, instruction):
        self._registers[instruction[3]] = self._registers[instruction[1]] * \
                                          self._registers[instruction[2]]
    ops_by_name['mulr'] = op_mulr

    def op_muli(self, instruction):
        self._registers[instruction[3]] = self._registers[instruction[1]] * \
                                          instruction[2]
    ops_by_name['muli'] = op_muli

    def op_banr(self, instruction):
        self._registers[instruction[3]] = self._registers[instruction[1]] & \
                                          self._registers[instruction[2]]
    ops_by_name['banr'] = op_banr

    def op_bani(self, instruction):
        self._registers[instruction[3]] = self._registers[instruction[1]] & \
                                          instruction[2]
    ops_by_name['bani'] = op_bani

    def op_borr(self, instruction):
        self._registers[instruction[3]] = self._registers[instruction[1]] | \
                                          self._registers[instruction[2]]
    ops_by_name['borr'] = op_borr

    def op_bori(self, instruction):
        self._registers[instruction[3]] = self._registers[instruction[1]] | \
                                          instruction[2]
    ops_by_name['bori'] = op_bori

    def op_setr(self, instruction):
        self._registers[instruction[3]] = self._registers[instruction[1]]
    ops_by_name['setr'] = op_setr

    def op_seti(self, instruction):
        self._registers[instruction[3]] = instruction[1]
    ops_by_name['seti'] = op_seti

    def op_gtir(self, instruction):
        self._registers[instruction[3]] = 1 if instruction[1] > \
                                               self._registers[instruction[2]] else 0
    ops_by_name['gtir'] = op_gtir

    def op_gtri(self, instruction):
        self._registers[instruction[3]] = 1 if self._registers[instruction[1]] > \
                                               instruction[2] else 0
    ops_by_name['gtri'] = op_gtri

    def op_gtrr(self, instruction):
        self._registers[instruction[3]] = 1 if self._registers[instruction[1]] > \
                                               self._registers[instruction[2]] else 0
    ops_by_name['gtrr'] = op_gtrr

    def op_eqir(self, instruction):
        self._registers[instruction[3]] = 1 if instruction[1] == \
                                               self._registers[instruction[2]] else 0
    ops_by_name['eqir'] = op_eqir

    def op_eqri(self, instruction):
        self._registers[instruction[3]] = 1 if self._registers[instruction[1]] \
                                               == instruction[2] else 0
    ops_by_name['eqri'] = op_eqri

    def op_eqrr(self, instruction):
        self._registers[instruction[3]] = 1 if self._registers[instruction[1]] \
                                               == self._registers[instruction[2]] else 0
    ops_by_name['eqrr'] = op_eqrr

    ops_by_number = list( [None] * len(ops_by_name))

    def set_op_number(self, op_name, op_number):
        self.ops_by_number[op_number] = self.ops_by_name[op_name]

def parse_input(input_list):
    samples = set()
    program = list()

    re_before = re.compile(r'Before: \[(\d+), (\d+), (\d+), (\d+)]')
    re_after = re.compile(r'After:  \[(\d+), (\d+), (\d+), (\d+)]')
    re_instruction = re.compile(r'(\d+) (\d+) (\d+) (\d+)')

    before = None
    instruction = None

    for line in input_list:
        match = re_before.search(line)
        if match:
            before = (int(match.group(1)), int(match.group(2)), int(match.group(3)),
                      int(match.group(4)))
            continue

        match = re_instruction.search(line)
        if match:
            if before:
                instruction = (int(match.group(1)), int(match.group(2)), int(match.group(3)),
                               int(match.group(4)))
            else:
                program.append((int(match.group(1)), int(match.group(2)), int(match.group(3)),
                                int(match.group(4))))
            continue

        match = re_after.search(line)
        if match:
            after = (int(match.group(1)), int(match.group(2)), int(match.group(3)),
                     int(match.group(4)))
            sample = (before, instruction, after)
            samples.add(sample)

            before = None
            instruction = None
            continue

        assert line == ''

    return samples, program

def what_many_opcodes_match(sample, opcodes=Computer.ops_by_name):
    matches = set()
    for opcode in opcodes:
        regs = list(sample[0])
        computer = Computer(regs)
        computer.execute_as(opcode, sample[1])
        if sample[2] == computer.get_registers():
            matches.add(opcode)
    return matches


def part1(input_list):
    three_or_more_count = 0
    samples, _ = parse_input(input_list)
    for sample in samples:
        matches = what_many_opcodes_match(sample)

        if len(matches) >= 3:
            three_or_more_count += 1
    return three_or_more_count


def part2(input_list):
    registers = list((0,0,0,0))
    computer = Computer(registers)

    remaining_opcodes = set(Computer.ops_by_name)
    samples, program = parse_input(input_list)

    while remaining_opcodes:
        opcode_number = None
        for sample in samples:
            matches = what_many_opcodes_match(sample, remaining_opcodes)
            if len(matches) == 1:
                opcode_number = sample[1][0]
                opcode_name = matches.pop()
                computer.set_op_number(opcode_name, opcode_number)
                remaining_opcodes.remove(opcode_name)
                break

        assert opcode_number is not None  # Indicates bug in input data.
        if opcode_number is not None:
            samples_to_delete = set()
            for sample in samples:
                if sample[1][0] == opcode_number:
                    samples_to_delete.add(sample)

            samples -= samples_to_delete


    for instruction in program:
        computer.execute(instruction)

    registers = computer.get_registers()

    return registers[0]


if __name__ == "__main__":
    aoc.main(part1, part2)
