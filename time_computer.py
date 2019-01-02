#!/usr/bin/env python3

import re

class TimeComputer:

    def __init__(self, input_list, registers=None):
        self._registers = registers if registers else [0, 0, 0, 0, 0, 0]
        self._program = list()
        self._ip_registers = [0]
        self._ip_register_number = 0
        self._halted = False

        self.load_program(input_list)

    @classmethod
    def get_opcodes(cls):
        return cls._ops_by_name.keys()

    def get_registers(self):
        return tuple(self._registers)

    def get_registers_reference(self):
        """
        Get a reference to the register list.  This should not normally be used.
        It can be used to modify the registers when hacking.
        """
        return self._registers

    def get_ip(self):
        return self._ip_registers[self._ip_register_number]

    def set_ip(self, new_ip):
        self._ip_registers[self._ip_register_number] = new_ip

    def is_halted(self):
        return self._halted

    def _inc_ip(self):
        ip_value = self.get_ip()
        if 0 <= ip_value + 1 < len(self._program):
            self.set_ip(ip_value + 1)
        else:
            self._halted = True

    def _execute(self, instruction):
        self._ops_by_name[instruction[0]](self, instruction)

    _ops_by_name = dict()

    def _op_addr(self, instruction):
        self._registers[instruction[3]] = self._registers[instruction[1]] + \
                                          self._registers[instruction[2]]
    _ops_by_name['addr'] = _op_addr

    def _op_addi(self, instruction):
        self._registers[instruction[3]] = self._registers[instruction[1]] + \
                                          instruction[2]
    _ops_by_name['addi'] = _op_addi

    def _op_mulr(self, instruction):
        self._registers[instruction[3]] = self._registers[instruction[1]] * \
                                          self._registers[instruction[2]]
    _ops_by_name['mulr'] = _op_mulr

    def _op_muli(self, instruction):
        self._registers[instruction[3]] = self._registers[instruction[1]] * \
                                          instruction[2]
    _ops_by_name['muli'] = _op_muli

    def _op_banr(self, instruction):
        self._registers[instruction[3]] = self._registers[instruction[1]] & \
                                          self._registers[instruction[2]]
    _ops_by_name['banr'] = _op_banr

    def _op_bani(self, instruction):
        self._registers[instruction[3]] = self._registers[instruction[1]] & \
                                          instruction[2]
    _ops_by_name['bani'] = _op_bani

    def _op_borr(self, instruction):
        self._registers[instruction[3]] = self._registers[instruction[1]] | \
                                          self._registers[instruction[2]]
    _ops_by_name['borr'] = _op_borr

    def _op_bori(self, instruction):
        self._registers[instruction[3]] = self._registers[instruction[1]] | \
                                          instruction[2]
    _ops_by_name['bori'] = _op_bori

    def _op_setr(self, instruction):
        self._registers[instruction[3]] = self._registers[instruction[1]]
    _ops_by_name['setr'] = _op_setr

    def _op_seti(self, instruction):
        self._registers[instruction[3]] = instruction[1]
    _ops_by_name['seti'] = _op_seti

    def _op_gtir(self, instruction):
        self._registers[instruction[3]] = 1 if instruction[1] > \
                                               self._registers[instruction[2]] else 0
    _ops_by_name['gtir'] = _op_gtir

    def _op_gtri(self, instruction):
        self._registers[instruction[3]] = 1 if self._registers[instruction[1]] > \
                                               instruction[2] else 0
    _ops_by_name['gtri'] = _op_gtri

    def _op_gtrr(self, instruction):
        self._registers[instruction[3]] = 1 if self._registers[instruction[1]] > \
                                               self._registers[instruction[2]] else 0
    _ops_by_name['gtrr'] = _op_gtrr

    def _op_eqir(self, instruction):
        self._registers[instruction[3]] = 1 if instruction[1] == \
                                               self._registers[instruction[2]] else 0
    _ops_by_name['eqir'] = _op_eqir

    def _op_eqri(self, instruction):
        self._registers[instruction[3]] = 1 if self._registers[instruction[1]] \
                                               == instruction[2] else 0
    _ops_by_name['eqri'] = _op_eqri

    def _op_eqrr(self, instruction):
        self._registers[instruction[3]] = 1 if self._registers[instruction[1]] \
                                               == self._registers[instruction[2]] else 0
    _ops_by_name['eqrr'] = _op_eqrr

    def load_program(self, input_list):
        self._program = list()

        re_ip = re.compile(r'#ip (\d+)')
        re_instruction = re.compile(r'(\D+) (\d+) (\d+) (\d+)')


        for line in input_list:
            match = re_ip.fullmatch(line)
            if match:
                self._ip_register_number = int(match.group(1))
                self._ip_registers = self._registers
                continue

            match = re_instruction.fullmatch(line)
            if match:
                self._program.append((match.group(1), int(match.group(2)),
                                      int(match.group(3)), int(match.group(4))))
                continue

            assert False


    def step(self, max_steps=1):
        for _ in range(max_steps):
            if self._halted:
                break

            ip_value = self.get_ip()
            self._execute(self._program[ip_value])
            self._inc_ip()

    def run(self):
        self._halted = False
        while not self._halted:
            self.step()


if __name__ == "__main__":
    pass
