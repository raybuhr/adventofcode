from copy import deepcopy
from dataclasses import dataclass, field


@dataclass
class HandHoldGameConsole:
    data: str
    accumulator: int = 0
    position: int = 0
    instructions: list = field(default_factory=list)

    def parse_data(self):
        self.instructions = [d.split() for d in self.data.splitlines()]

    def step(self):
        inst, val = self.instructions[self.position]
        val = int(val)
        if inst == "acc":
            self.accumulator += val
            self.position += 1
        elif inst == "jmp":
            self.position += val
        elif inst == "nop":
            self.position += 1

    def run(self, log_jump_locs=False):
        seen = []
        if log_jump_locs:
            jump_locs = []
        while self.position not in seen:
            seen += [self.position]
            try:
                self.step()
                if log_jump_locs and "jmp" in self.instructions[self.position]:
                    jump_locs += [self.position]
            except IndexError:
                print(self.accumulator)
                break
        if log_jump_locs:
            return jump_locs

    def replace_instructions(self, position):
        self.parse_data()
        self.instructions[position][0] = 'nop'

