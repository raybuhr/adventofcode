from collections import defaultdict


class Intcode:
    def __init__(self, data, input_queue):
        self.position = 0
        self.relative_base = 0
        self.data = self.parse_data(data)
        self.input_queue = input_queue
        self.output_queue = []
        self.steps_processed = 0

    class Halt(Exception):
        pass

    @staticmethod
    def parse_data(data):
        d = [int(d) for d in data.split(",")]
        return defaultdict(int, enumerate(d))

    @staticmethod
    def parse_op_code(op_code):
        op = str(op_code).rjust(5, "0")
        code = int(op[3:])
        modes = [int(m) for m in op[:3][::-1]]
        return (code, modes)

    def print_state(self):
        print("opcode:", self.data[self.position])
        print("position:", self.position)
        print("relative_base:", self.relative_base)
        print("input_queue:", self.input_queue)
        print("output_queue:", self.output_queue)

    def step(self, verbose=False):
        self.steps_processed += 1
        op, modes = self.parse_op_code(self.data[self.position])
        param_pointers = {}
        for i, mode in enumerate(modes, start=1):
            if mode == 0:  # position
                param_pointers[i] = self.data[self.position + i]
            if mode == 1:  # immediate
                param_pointers[i] = self.position + i
            if mode == 2:  # relative
                param_pointers[i] = self.data[self.position + i] + self.relative_base
        if verbose:
            print("-----Step-----")
            self.print_state()
            print("opcode:", op)
            print("modes:", modes)
            print("param pointers:", list(param_pointers.values()))
        if op == 99:  # halt
            raise Intcode.Halt
        elif op == 1:  # add
            a, b, c = param_pointers[1], param_pointers[2], param_pointers[3]
            self.data[c] = self.data[a] + self.data[b]
            self.position += 4
        elif op == 2:  # multiply
            a, b, c = param_pointers[1], param_pointers[2], param_pointers[3]
            self.data[c] = self.data[a] * self.data[b]
            self.position += 4
        elif op == 3:  # input
            a, b, c = param_pointers[1], param_pointers[2], param_pointers[3]
            try:
                new_val = self.input_queue.pop(0)
                self.data[a] = new_val
                self.position += 2
            except:
                raise Intcode.Halt
        elif op == 4:  # output
            a, b, c = param_pointers[1], param_pointers[2], param_pointers[3]
            self.output_queue.append(self.data[a])
            self.position += 2
        elif op == 5:  # jump-if-true
            a, b, c = param_pointers[1], param_pointers[2], param_pointers[3]
            if self.data[a] != 0:
                self.position = self.data[b]
            else:
                self.position += 3
        elif op == 6:  # jump-if-false
            a, b, c = param_pointers[1], param_pointers[2], param_pointers[3]
            if self.data[a] == 0:
                self.position = self.data[b]
            else:
                self.position += 3
        elif op == 7:  # less than
            a, b, c = param_pointers[1], param_pointers[2], param_pointers[3]
            if self.data[a] < self.data[b]:
                self.data[c] = 1
            else:
                self.data[c] = 0
            self.position += 4
        elif op == 8:  # equals
            a, b, c = param_pointers[1], param_pointers[2], param_pointers[3]
            if self.data[a] == self.data[b]:
                self.data[c] = 1
            else:
                self.data[c] = 0
            self.position += 4
        elif op == 9:  # change relative base
            a, b, c = param_pointers[1], param_pointers[2], param_pointers[3]
            self.relative_base += self.data[a]
            self.position += 2
        else:
            raise Intcode.Halt

    def run(self, verbose=False):
        while True:
            try:
                self.step(verbose=verbose)
            except:
                break
