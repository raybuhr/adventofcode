from collections import defaultdict

with open("input.txt") as f:
    lines = f.read().splitlines()

max_size = 100_000
cur_dir = None
dir_sizes = defaultdict(int)
dirs = set()

for line in lines:
    if line.startswith("$ cd "):
        dir = line.replace("$ cd ", "")
        if dir == "/":
            cur_dir = dir
        elif dir not in ("/", ".."):
            if cur_dir != "/":
                cur_dir = f"{cur_dir}/{dir}"
            else:
                cur_dir += dir
        elif dir == "..":
            cur_dir = "/".join(cur_dir.split("/")[:-1])
            if not cur_dir:
                cur_dir = "/"
        else:
            raise ValueError("unrecognized dir")
        dirs.add(cur_dir)
        continue
    if line == "$ ls":
        continue
    if line.startswith("dir "):
        dir = line.replace("dir ", "")
        dirs.add(f"{cur_dir}/{dir}")
        continue
    if line.split(" ")[0].isdigit():
        size = int(line.split(" ")[0])
        dir_sizes[cur_dir] += size

for d in dirs:
    if d not in dir_sizes:
        dir_sizes[d] = 0

big_dir_sizes = defaultdict(int)
for dir, size in dir_sizes.items():
    big_dir_sizes[dir] += size
    parents = dir.split("/")[:-1]
    while parents:
        big_dir_sizes["/".join(parents)] += size
        parents.pop()

under = {k: v for k, v in big_dir_sizes.items() if v <= max_size}
print("part a:", sum(v for v in under.values()))

fs_size = 70000000
need = 30000000
used = big_dir_sizes[""]
unused = fs_size - used
del_size = need - unused

print("part b", min(v for v in big_dir_sizes.values() if v > del_size))
