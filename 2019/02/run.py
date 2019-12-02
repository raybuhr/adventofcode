def parse_data(data):
    return [int(d) for d in data.strip().split(",")]


def process_instruction(instruction, data):
    if len(instruction) < 4:
        return "done", data
    op_code, in1, in2, out = instruction
    if op_code == 99:
        return "done", data
    elif op_code == 1:
        data[out] = data[in1] + data[in2]
        return "running", data
    elif op_code == 2:
        data[out] = data[in1] * data[in2]
        return "running", data
    else:
        raise ValueError("Unknown op_code")


def run_intcode(data):
    start = 0
    status = "running"
    while status != "done":
        status, data = process_instruction(data[start:(start+4)], data)
        start += 4
    return data


def test_run_intcode():
    data = parse_data("1,9,10,3,2,3,11,0,99,30,40,50")
    expect = parse_data("3500,9,10,70,2,3,11,0,99,30,40,50")
    got = run_intcode(data)
    assert expect == got
    data = parse_data("1,0,0,0,99")
    expect = parse_data("2,0,0,0,99")
    got = run_intcode(data)
    assert expect == got
    data = parse_data("2,3,0,3,99")
    expect = parse_data("2,3,0,6,99")
    got = run_intcode(data)
    assert expect == got
    data = parse_data("2,4,4,5,99,0")
    expect = parse_data("2,4,4,5,99,9801")
    got = run_intcode(data)
    assert expect == got
    data = parse_data("1,1,1,4,99,5,6,0,99")
    expect = parse_data("30,1,1,4,2,5,6,0,99")
    got = run_intcode(data)
    assert expect == got


def replace_program(data, noun, verb):
    data[1] = noun
    data[2] = verb
    return data


def replace_and_run(data, noun, verb):
    data = replace_program(data, noun, verb)
    output = run_intcode(data)
    return output[0]


def solve_pt2(program):
    goal = 19690720
    
    def guess_noun_and_verb(program, noun, verb):
        data = parse_data(program)
        output = replace_and_run(data, noun, verb)
        return output

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
    with open("2019/02/input.txt") as fp:
        program = fp.read()
    
    print("Part 1:")
    data = parse_data(program)
    # replace position 1 with the value 12 and replace position 2 with the value 2
    output = replace_and_run(data, 12, 2)
    print(output)

    print("Part 2:")
    noun, verb = solve_pt2(program)
    print(100 * noun + verb)
