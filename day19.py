#!/usr/bin/env python3

import aoc
from time_computer import TimeComputer


def part1(input_list):
    computer = TimeComputer(input_list)
    computer.run()
    registers = computer.get_registers()
    return registers[0]


def main_loop_simulator(reg5):
    """
    Analysis of program.

    0  addi 2 16 2 r2 += 16         Goto initialization routine at 17

    1  seti 1 0 1  r1 = 1           Initialize loop variables output loop index
    2  seti 1 4 3  r3 = 1           Initialize loop variables inner loop index

    3  mulr 1 3 4  r4 = r1 * r3     Start of inner loop
    4  eqrr 4 5 4  r4 = r4 == r5
    5  addr 4 2 2  r2 += r4         Jump to 7 if r4 == r5  r5 is constant
    6  addi 2 1 2  r2++             Jump to 8
    7  addr 1 0 0  r0 += r1         Accumulate r1 into r0  if r4 == r5
    8  addi 3 1 3  r3++
    9  gtrr 3 5 4  r4 = r3 > r5
    10 addr 2 4 2  r2 += r4         Branch to 12 if r3 > r5
    11 seti 2 5 2  r2 = 2           Branch to 3

    12 addi 1 1 1  r1++             Outer loop logic
    13 gtrr 1 5 4  r4 = r1 > r5
    14 addr 4 2 2  r2 += r4         Branch to 16 if r1 > r5
    15 seti 1 1 2  r2 = 1           Goto 2

    16 mulr 2 2 2  r2 *= r2         r2 = 256 Branch outside of program

    17 addi 5 2 5  r5 += 2          Initialization part 1 & 2
    18 mulr 5 5 5  r5 *= r5         Initialization part 1 & 2
    19 mulr 2 5 5  r5 *= r2         Initialization part 1 & 2
    20 muli 5 11 5 r5 *= 11         Initialization part 1 & 2
    21 addi 4 5 4  r4 += 5          Initialization part 1 & 2
    22 mulr 4 2 4  r4 *= r2         Initialization part 1 & 2
    23 addi 4 9 4  r4 += 9          Initialization part 1 & 2
    24 addr 5 4 5  r5 += r4         Initialization part 1 & 2
    25 addr 2 0 2  r2 += r0         Initialization part 1 & 2
    26 seti 0 0 2  r2 = 0           Goto 1

    27 setr 2 3 4  r4 = r2          Initialization part 2
    28 mulr 4 2 4  r4 *= r2         Initialization part 2
    29 addr 2 4 4  r4 += r2         Initialization part 2
    30 mulr 2 4 4  r4 *= r2         Initialization part 2
    31 muli 4 14 4 r4 *= 14         Initialization part 2
    32 mulr 4 2 4  r4 *= r2         Initialization part 2
    33 addr 5 4 5  r5 += r4         Initialization part 2
    34 seti 0 6 0  r0 = 0           Initialization part 2
    35 seti 0 3 2  r2 = 0           Goto 1

    The program performs this operation.  This will take a very long time.

    int main1(long r5) {
        long r0=0, r1=0, r3=0;

        for (r1 = 1; r1 <= r5; r1++) {
            for (r3 = 1; r3 <= r5; r3++) {
                long var = r1 * r3;
                if (var == r5) {
                    r0 += r1;
                }
            }
        }
        printf("%lu\n", r0);
    }

    This is an equivalent C program that removes the inner loop.

    int main2(long r5) {
        long r0=0, r1=0;

        for (r1 = 1; r1 <= r5; r1++) {
            # Accumulate if r5 / r1 has no remainder.
            long var = r5 / r1;
            if ( r5 == var * r1 ) {
                r0 += r1;
            }
        }
        printf("%lu\n", r0);
    }

    This function simulates the output based on the r5 initialization.
    """

    reg0 = 0
    for reg1 in range(1, reg5 + 1):
        # Accumulate if reg5 / reg1 has no remainder.
        if reg5 == reg5 // reg1 * reg1:
            reg0 += reg1

    return reg0


def part2(input_list):
    registers = [1,0,0,0,0,0]
    computer = TimeComputer(input_list, registers)

    # Simulate until reg5 initialization is completed.
    while computer.get_ip() != 1:
        computer.step()

    # Compute reg0 using faster algorithm.
    reg5 = computer.get_registers()[5]
    return main_loop_simulator(reg5)


if __name__ == "__main__":
    aoc.main(part1, part2)
