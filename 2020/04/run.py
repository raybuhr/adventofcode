from aocd import get_data


FIELDS = {
    "byr": "(Birth Year)",
    "iyr": "(Issue Year)",
    "eyr": "(Expiration Year)",
    "hgt": "(Height)",
    "hcl": "(Hair Color)",
    "ecl": "(Eye Color)",
    "pid": "(Passport ID)",
    "cid": "(Country ID)",
}


def parse_data(data):
    lines = data.replace("\n", " ").split("  ")
    passports = [{f.split(":")[0]: f.split(":")[1] for f in l.split()} for l in lines]
    return passports


def is_passport_valid(passport):
    return all(f in passport for f in FIELDS if f != "cid")


def check_byr(byr):
    if not byr:
        return False
    return int(byr) >= 1920 and int(byr) <= 2002


def check_iyr(iyr):
    if not iyr:
        return False
    return int(iyr) >= 2010 and int(iyr) <= 2020


def check_eyr(eyr):
    if not eyr:
        return False
    return int(eyr) >= 2020 and int(eyr) <= 2030


def check_hgt(hgt):
    if not hgt:
        return False
    if hgt[-2:] not in ("cm", "in"):
        return False
    if "cm" in hgt:
        h = int(hgt.replace("cm", ""))
        if not (h >= 150 and h <= 193):
            return False
    if "in" in hgt:
        h = int(hgt.replace("in", ""))
        if not (h >= 59 and h <= 76):
            return False
    return True


def check_hcl(hcl):
    if not hcl:
        return False
    if len(hcl) != 7:
        return False
    if not hcl.startswith("#"):
        return False
    if not all(c in "0123456789abcdef" for c in hcl[1:]):
        return False
    return True


def check_ecl(ecl):
    if not ecl:
        return False
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def check_pid(pid):
    if not pid:
        return False
    if len(pid) != 9:
        return False
    if not all(p in "0123456789" for p in pid):
        return False
    return True


def is_passport_super_valid(passport):
    rules = {}
    rules["basic_valid"] = is_passport_valid(passport)
    rules["byr"] = check_byr(passport.get("byr"))
    rules["iyr"] = check_iyr(passport.get("iyr"))
    rules["eyr"] = check_eyr(passport.get("eyr"))
    rules["hgt"] = check_hgt(passport.get("hgt"))
    rules["hcl"] = check_hcl(passport.get("hcl"))
    rules["ecl"] = check_ecl(passport.get("ecl"))
    rules["pid"] = check_pid(passport.get("pid"))
    return all(rules.values())


def solve_pt1(data):
    passports = parse_data(data)
    return sum(is_passport_valid(p) for p in passports)


def solve_pt2(data):
    passports = parse_data(data)
    return sum(is_passport_super_valid(p) for p in passports)


if __name__ == "__main__":
    data = get_data(year=2020, day=4)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = solve_pt1(data)
    print(pt_1, "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve_pt2(data)
    print(pt_2, "\n")
