from collections import Counter
from string import ascii_lowercase


def extract_letters_from_room(room):
    letters = [
        l for l in
        room.split("[")[0]
        if l in ascii_lowercase
    ]
    return letters


def extract_checksum_from_room(room):
    checksum = room.split("[")[-1].replace("]", "")
    return checksum


def find_top_five_letters(room):
    keep = []
    letters = extract_letters_from_room(room)
    letter_count = Counter(letters)
    top = sorted(letter_count.most_common(), reverse=True, key=lambda c: (c[1], c[0]))
    return "".join([t[0] for t in top[:5]])

def is_real_room(room):
    letters = find_top_five_letters(room)
    checksum = extract_checksum_from_room(room)
    return letters == checksum


def test_is_real_room():
    got = find_top_five_letters("aaaaa-bbb-z-y-x-123[abxyz]")
    expect = "abxyz"
    assert got == expect
    assert is_real_room("a-b-c-d-e-f-g-h-987[abcde]") is True
    assert is_real_room("not-a-real-room-404[oarel]") is True
    assert is_real_room("totally-real-room-200[decoy]") is False


if __name__ == "__main__":
    with open("2016/04/input.txt") as fp:
        rooms = fp.read().split("\n")
    