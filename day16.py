#!/usr/bin/env python3

from collections import namedtuple
import re

import aoc
from time_computer import TimeComputer

Sample = namedtuple('Sample', ['registers_before', 'instruction', 'registers_after'])

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
            sample =  Sample(registers_before=before, instruction=instruction,
                             registers_after=after)
            samples.add(sample)

            before = None
            instruction = None
            continue

        assert line == ''

    return samples, program

def how_many_opcodes_match(sample, opcodes=None):

    if opcodes is None:
        opcodes = TimeComputer.get_opcodes()

    matches = set()
    for opcode in opcodes:
        regs = list(sample.registers_before)
        instruction = '%s %d %d %d' % (opcode, sample.instruction[1], sample.instruction[2],
                                       sample.instruction[3])
        program = [instruction]
        computer = TimeComputer(program, regs)
        computer.step()

        if sample.registers_after == computer.get_registers():
            matches.add(opcode)
    return matches


def part1(input_list):
    three_or_more_count = 0
    samples, _ = parse_input(input_list)
    for sample in samples:
        matches = how_many_opcodes_match(sample)

        if len(matches) >= 3:
            three_or_more_count += 1
    return three_or_more_count


def part2(input_list):
    samples, program_with_opnums = parse_input(input_list)

    opcode_map = dict()

    remaining_opcodes = set(TimeComputer.get_opcodes())

    # Figure out the opcode number to name mapping by running the samples on every
    # opcode that we haven't yet mapped.  Each iteration should map one number to
    # an opcode.
    while remaining_opcodes:
        opcode_number = None
        for sample in samples:
            matches = how_many_opcodes_match(sample, remaining_opcodes)
            if len(matches) == 1:
                opcode_number = sample.instruction[0]
                opcode_name = matches.pop()
                opcode_map[opcode_number] = opcode_name
                remaining_opcodes.remove(opcode_name)
                break

        assert opcode_number is not None  # Indicates bug in input data.
        if opcode_number is not None:
            samples_to_delete = set()
            for sample in samples:
                if sample.instruction[0] == opcode_number:
                    samples_to_delete.add(sample)

            samples -= samples_to_delete

    # Remap opcode numbers to name in the program.
    program = []
    for instruction in program_with_opnums:
        instruction_text = '%s %d %d %d' % (opcode_map[instruction[0]], instruction[1],
                                            instruction[2], instruction[3])
        program.append(instruction_text)

    computer = TimeComputer(program)
    computer.run()

    registers = computer.get_registers()
    return registers[0]


if __name__ == "__main__":
    aoc.main(part1, part2)
