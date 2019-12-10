from aocd.models import Puzzle
import pytest
from intcode import Intcode

def get_data():
    puzzle = Puzzle(year=2019, day=2)
    data = puzzle.input_data
    return data


def run(data, input_queue, verbose=False):
    intcode = Intcode(data=data, input_queue=input_queue)
    while True:
        try:
            intcode.step(verbose=verbose)
        except:
            break
    return intcode


test_cases = [
    ("1,9,10,3,2,3,11,0,99,30,40,50", "3500,9,10,70,2,3,11,0,99,30,40,50"),
    ("1,0,0,0,99", "2,0,0,0,99"),
    ("2,3,0,3,99", "2,3,0,6,99"),
    ("2,4,4,5,99,0", "2,4,4,5,99,9801"),
    ("1,1,1,4,99,5,6,0,99", "30,1,1,4,2,5,6,0,99"),
]

@pytest.mark.parametrize("test_data,expected", test_cases)
def test_run_intcode(test_data, expected):
    intcode = run(test_data, [])
    got = ",".join(str(i) for i in intcode.data.values())
    assert expected == got[:len(expected)]


def replace_program(data, noun, verb):
    d = [int(d) for d in data.strip().split(",")]
    d[1] = noun
    d[2] = verb
    return ",".join(str(i) for i in d)


def replace_and_run(data, noun, verb):
    data = replace_program(data, noun, verb)
    output = run(data, [])
    return output


def solve_pt2(program):
    goal = 19690720
    
    def guess_noun_and_verb(program, noun, verb):
        output = replace_and_run(program, noun, verb)
        return output.data[0]

    noun = 0
    verb = 0
    guess = guess_noun_and_verb(program, noun, verb)
    while guess < goal:
        noun += 1
        guess = guess_noun_and_verb(program, noun, verb)
    
    noun -= 1
    guess = guess_noun_and_verb(program, noun, verb)
    while guess < goal:
        verb += 1
        guess = guess_noun_and_verb(program, noun, verb)

    return noun, verb


if __name__ == "__main__":
    program = get_data()
    
    print("-"*30)
    print("Part 1:")
    # replace position 1 with the value 12 and replace position 2 with the value 2
    output = replace_and_run(program, 12, 2)
    print(output.data[0])
    print("-"*30)
    print("Part 2:")
    print("-"*30)
    noun, verb = solve_pt2(program)
    print(100 * noun + verb)
    print("-"*30)
