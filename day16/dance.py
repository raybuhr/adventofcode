import sys

def spin(x):
    "takes the first x elements and puts them at the end"
    global programs
    x = int(x)
    start = programs[-x:]
    end = programs[:-x]
    programs = start + end

def exchange(x):
    """takes an input of x like A/B representing the positions
    and swaps the positions of A and B"""
    global programs
    a_idx = int(x.split("/")[0])
    b_idx = int(x.split("/")[1])
    a = programs[a_idx]
    b = programs[b_idx]
    programs[a_idx], programs[b_idx] = b, a

def partner(x):
    "takes an input of like A/B and swaps the positions"
    global programs
    a = x.split("/")[0]
    b = x.split("/")[1]
    a_idx, b_idx = programs.index(a), programs.index(b)
    programs[a_idx], programs[b_idx] = b, a

def dance(x):
    "look at step x and figure out which function to apply"
    fun = x[0]
    fun_input = x[1:]
    if fun == "s":
        spin(fun_input)
    if fun == "x":
        exchange(fun_input)
    if fun == "p":
        partner(fun_input)

if len(sys.argv) > 1:
    programs = list("abcdefghijklmnop")
    with open("input.txt") as f:
        steps = f.read()
else:
    programs = list("abcde")
    with open("test_input.txt") as f:
        steps = f.read()
    print("Starting with:", programs)

steps = steps.split(",")

for step in steps:
    dance(step)

print("".join(programs))
