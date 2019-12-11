import itertools
from aocd import get_data


def parse_data(data, width, height):
    size = width * height
    length = len(data)
    chunks = [data[i : i + size] for i in range(0, length, size)]
    chunks = [[chunk[i : i + width] for i in range(0, size, width)] for chunk in chunks]
    return chunks


def count_thing(layer, thing):
    return sum(1 for row in layer for i in row if i == thing)


def find_layer_with_least_zeroes(layers):
    zeroes = [count_thing(layer, "0") for layer in layers]
    least = min(zeroes)
    return layers[zeroes.index(least)]


def solve_part1(data):
    layers = parse_data(data, 25, 6)
    layer = find_layer_with_least_zeroes(layers)
    ones = count_thing(layer, "1")
    twos = count_thing(layer, "2")
    return ones * twos


def get_pixels(data, width, height):
    size = width * height
    return [data[i::size] for i in range(size)]


def pick_top_layer(pixels):
    for i in pixels:
        if i != "2":
            return i
    return "2"


def decode_messgae(pixels, width, height):
    msg = "".join(pixels).replace("0", " ").replace("1", "#").replace("2", " ")
    return [msg[i : i + width] for i in range(0, width * height, width)]


def solve_part2(data):
    pixels = get_pixels(data, 25, 6)
    merged_layers = [pick_top_layer(p) for p in pixels]
    msg = decode_messgae(merged_layers, 25, 6)
    for m in msg:
        print(m)


if __name__ == "__main__":
    data = get_data(year=2019, day=8)
    print("-" * 20, "Part 1:", "-" * 20)
    print(solve_part1(data), "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    solve_part2(data)
