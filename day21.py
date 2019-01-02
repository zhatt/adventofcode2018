#!/usr/bin/env python3

import aoc
from time_computer import TimeComputer

#
# Analysis of program
# * = branch target
#
# #ip 3
#
# 0   seti 123 0 5	r5 = 0x7b      (  0111_1011)
# 1*  bani 5 456 5	r5 &= 0x1c8    (1_1100_1000)  = 0100_1000
# 2   eqri 5 72 5		r5 = r5 == 0x48  (0100_1000)
# 3   addr 5 3 3		r5 branch to 5 if r5 == 0x48
# 4   seti 0 0 3		goto 1
#
# 5*  seti 0 5 5		r5 = 0
# 6   bori 5 65536 2	r2 = r5 | 0x10000 (1_0000_0000_0000_0000)
#
# 7*  seti 10362650 3 5	r5 = 0x9e1f1a
#
# 8   bani 2 255 4	r4 = r2 & 0xff
# 9   addr 5 4 5		r5 += r4
# 10  bani 5 16777215 5	r5 &= 0xffffff
# 11  muli 5 65899 5	r5 *= 0x1016b
# 12  bani 5 16777215 5	r5 &= 0xffffff
# 13  gtir 256 2 4	r4 = 0x100 > r2
# 14  addr 4 3 3		branch to 16 (really 7) if 0x100 > r2
# 			This never happens
#
# [15  addi 3 1 3		goto 17]
# [16* seti 27 4 3	goto 27]
#
#
# This is the main inner loop.
# for (r4 = 0;  ; r4++ )
# (r4 + 1) * 0x100 > r2 exits loop
#
# 17* seti 0 3 4		r4 = 0
# 18* addi 4 1 1		r1 = r4 + 1
# 19  muli 1 256 1	r1 *= 0x100
# 20  gtrr 1 2 1		r1 = r1 > r2
# 21  addr 1 3 3		branch to 23 (really 26) if r1 > r2
# 22  addi 3 1 3		goto 24
# 23* seti 25 2 3		goto 26
# 24* addi 4 1 4		r4++
# 25  seti 17 7 3		goto 18
#
# 26* setr 4 0 2		r2 = r4
# 27* seti 7 8 3		goto 7
# 28  eqrr 5 0 4		r4 = r0 == r5
# 29  addr 4 3 3		branch to 31 if r0 == r5
# 30  seti 5 1 3		goto 5
#

def part1(input_list):
    computer = TimeComputer(input_list)

    # The program exits when r0 == r5.  r0 is not modified by the program
    # so we can just run the program to instruction 28 and get the value
    # of r5.  If the program is started with that value in r0 it will
    # give the shortest run.
    while True:
        if computer.get_ip() == 28:
            break

        computer.step()

        if computer.is_halted():
            assert False

    registers = computer.get_registers()
    return registers[5]


def part2(input_list):
    computer = TimeComputer(input_list)
    reg5_values = set()
    last_reg5 = 0

    # We assume that there is a loop in the sequence of r5 values.  We want to
    # find the last value of r5 before the sequence repeats.  If that value
    # is used for r0 it will give the longest run time that is not infinite.
    while True:
        if computer.get_ip() == 18:
            # Force r4 to value to exit loop.
            registers = computer.get_registers_reference()
            registers[4] = registers[2] // 256  # Also -1 + 1 in equation.

        if computer.get_ip() == 28:
            reg5 = computer.get_registers()[5]
            if reg5 in reg5_values:
                break

            reg5_values.add(reg5)
            last_reg5 = reg5

        computer.step()

        if computer.is_halted():
            assert False

    return last_reg5


if __name__ == "__main__":
    aoc.main(part1, part2)
