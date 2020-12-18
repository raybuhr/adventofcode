from aocd import get_data
import numpy as np


def simplify(formula, advanced=False):
    if "(" in formula:
        left, right = formula.split(")", 1)
        group = left.split("(")[-1]
        left = left.replace("("+group, "")
        if advanced:
            group = str(np.prod([eval(g) for g in group.split("*")]))
        else:
            group = group.split()
            while len(group) > 3:
                subtotal = eval("".join(group[:3]))
                group = [str(subtotal)] + group[3:]
            group = str(eval("".join(group)))
        formula = left + group + right
    return formula


def calc_simple(formula):
    while "(" in formula:
        formula = simplify(formula)
    formula = formula.split()
    while len(formula) > 3:
        subtotal = eval("".join(formula[:3]))
        formula = [str(subtotal)] + formula[3:]
    return eval("".join(formula))
 

def calc_advanced(formula):
    while "(" in formula:
        formula = simplify(formula, True)
    return np.prod([eval(f) for f in formula.split("*")])


def solve_pt1(data):
    return sum(calc_simple(formula) for formula in data.splitlines())


def solve_pt2(data):
    return sum(calc_advanced(formula) for formula in data.splitlines())


if __name__ == "__main__":
    data = get_data(year=2020, day=18)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = solve_pt1(data)
    print(pt_1, "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve_pt2(data)
    print(pt_2, "\n")
