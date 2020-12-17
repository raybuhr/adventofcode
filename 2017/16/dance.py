import sys


class Dance:
    def __init__(self, programs, steps):
        self.programs = programs
        self.steps = steps

    def spin(self, x):
        """takes the first x elements and puts them at the end"""
        x = int(x)
        start = self.programs[-x:]
        end = self.programs[:-x]
        self.programs = start + end

    def exchange(self, x):
        """takes an input of x like A/B representing the positions
        and swaps the positions of A and B"""
        a_idx = int(x.split("/")[0])
        b_idx = int(x.split("/")[1])
        a = self.programs[a_idx]
        b = self.programs[b_idx]
        self.programs[a_idx], self.programs[b_idx] = b, a

    def partner(self, x):
        """takes an input of like A/B and swaps the positions"""
        a = x.split("/")[0]
        b = x.split("/")[1]
        a_idx, b_idx = self.programs.index(a), self.programs.index(b)
        self.programs[a_idx], self.programs[b_idx] = b, a

    def dance(self, x):
        """look at step x and figure out which function to apply"""
        fun = x[0]
        fun_input = x[1:]
        if fun == "s":
            self.spin(fun_input)
        if fun == "x":
            self.exchange(fun_input)
        if fun == "p":
            self.partner(fun_input)


def test():
    dance = Dance(programs=list("abcde"), steps="s1,x3/4,pe/b".split(","))
    for step in dance.steps:
        dance.dance(step)
    return "".join(dance.programs)


def main():
    programs = list("abcdefghijklmnop")
    with open("16/input.txt") as f:
        steps = f.read().split(",")
    dance = Dance(programs=programs, steps=steps)
    dances_seen = []
    for i in range(100):  # guess at repetition
        for step in dance.steps:
            dance.dance(step)
        result = "".join(dance.programs)
        if result not in dances_seen:
            dances_seen.append(result)
    idx = 1000000000 % len(dances_seen)
    print("A:", dances_seen[0])
    print("B:", dances_seen[idx - 1])


if __name__ == "__main__":
    assert test() == "baedc"
    main()
