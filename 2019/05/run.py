def read_data(filepath):
    with open(filepath) as fp:
        data = fp.read()
    return data


def parse_data(data):
    return [int(d) for d in data.strip().split(",")]


def parse_op_code(op_code):
    op = str(op_code)
    if len(op) < 5:
        op = op.rjust(5, "0")
    code = int(op[3:])
    third, second, first = int(op[0]), int(op[1]), int(op[2])
    return (code, first, second, third)


def run_intcode(data, input_value):
    position = 0
    done = False
    while not done:
        instructions = parse_op_code(data[position])
        op, mode1, mode2, mode3 = instructions
        params = data[position + 1 :]
        if op == 99:
            done = True

        elif op == 1:
            out = params[2]
            data[out] = (data[params[0]] if mode1 == 0 else params[0]) + (
                data[params[1]] if mode2 == 0 else params[1]
            )
            position += 4

        elif op == 2:
            out = params[2]
            data[out] = (data[params[0]] if mode1 == 0 else params[0]) * (
                data[params[1]] if mode2 == 0 else params[1]
            )
            position += 4

        elif op == 3:
            out = params[0]
            data[out] = input_value
            position += 2

        elif op == 4:
            out = params[0]
            print(data[out])
            position += 2

        elif op == 5:  # jump-if-true
            first = data[params[0]] if mode1 == 0 else params[0]
            second = data[params[1]] if mode2 == 0 else params[1]
            if first != 0:
                position = second
            else:
                position += 3

        elif op == 6:  # jump-if-false
            first = data[params[0]] if mode1 == 0 else params[0]
            second = data[params[1]] if mode2 == 0 else params[1]
            if first == 0:
                position = second
            else:
                position += 3

        elif op == 7:  # less than
            first = data[params[0]] if mode1 == 0 else params[0]
            second = data[params[1]] if mode2 == 0 else params[1]
            if first < second:
                data[params[2]] = 1
            else:
                data[params[2]] = 0
            position += 4

        elif op == 8:  # equals
            first = data[params[0]] if mode1 == 0 else params[0]
            second = data[params[1]] if mode2 == 0 else params[1]
            if first == second:
                data[params[2]] = 1
            else:
                data[params[2]] = 0
            position += 4

        else:
            raise ValueError(
                "Unknown op_code",
                data[position],
                position,
                op,
                mode1,
                mode2,
                mode3,
                params[:4],
            )
    return data


def solve_part_1():
    data = parse_data(read_data("2019/05/input.txt"))
    run_intcode(data, input_value=1)


def solve_part_2():
    data = parse_data(read_data("2019/05/input.txt"))
    run_intcode(data, input_value=5)


if __name__ == "__main__":
    print("-" * 10 + "Part 1: " + "-" * 10)
    solve_part_1()
    print("\n" + "-" * 10 + "Part 2: " + "-" * 10)
    solve_part_2()
