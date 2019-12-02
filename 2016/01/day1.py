# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '2016/day1'))
	print(os.getcwd())
except:
	pass
# %% [markdown]
# --- Day 1: No Time for a Taxicab ---
# 
# Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.
# 
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
# 
# You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.
# 
# The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.
# 
# There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?
# 
# For example:
# ```
# Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
# R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
# R5, L5, R5, R3 leaves you 12 blocks away.
# ```
# How many blocks away is Easter Bunny HQ?

# %%
with open('input.txt') as f:
    instructions = f.read().strip("\n")


# %%
steps = instructions.split(", ")


# %%
def turn(step, current_direction):
    step_direction = step[0]
    if current_direction == "N":
        if step_direction == "L":
            new_direction = "W"
        elif step_direction == "R":
            new_direction = "E"
    elif current_direction == "S":
        if step_direction == "L":
            new_direction = "E"
        elif step_direction == "R":
             new_direction = "W"
    elif current_direction == "E":
        if step_direction == "L":
            new_direction = "N"
        elif step_direction == "R":
            new_direction = "S"
    elif current_direction == "W":
        if step_direction == "L":
            new_direction = "S"
        elif step_direction == "R":
            new_direction = "N"
    return new_direction


# %%
def move(step, current_direction):
    dist = int(step[1:])
    new_direction = turn(step, current_direction)
    if new_direction == "W":
        coord = (-dist, 0)
    if new_direction == "S":
        coord = (0, -dist)
    if new_direction == "E":
        coord = (dist, 0)
    if new_direction == "N":
        coord = (0, dist)
    return coord


# %%
def add_coords(coord1, coord2):
    coord = (coord1[0]+coord2[0], coord1[1]+coord2[1])
    return coord


# %%
current = "N"
coord = (0, 0)


# %%
for step in steps:
    change = move(step, current)
    current = turn(step, current)
    coord = add_coords(coord, change)


# %%
print(coord)
print(abs(coord[0]) + abs(coord[1]))
# %% [markdown]
# The first half of this puzzle is complete! It provides one gold star: *
# %% [markdown]
# --- Part Two ---
# 
# Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.
# 
# For example, if your instructions are `R8, R4, R4, R8`, the first location you visit twice is 4 blocks away, due East.
# 
# How many blocks away is the first location you visit twice?

# %%
coords_visited = []


# %%
current = "N"
coord = (0, 0)
coords_visited.append(coord)
for step in steps:
    change = move(step, current)
    current = turn(step, current)
    coord = add_coords(coord, change)
    coords_visited.append(coord)


# %%
coords_visited[0:3]


# %%
def find_coords_between(coord1, coord2):
    visited = []
    if coord1[0] == coord2[0]:
        if coord2[1] < 0:
            dist = range(coord1[1], coord2[1], -1)
        elif coord2[1] >= 0:
            dist = range(coord1[1], coord2[1])
        for i in dist:
            new_coord = (coord1[0], i)
            if new_coord not in visited:
                visited.append(new_coord)
    if coord1[1] == coord2[1]:
        if coord1[0] < 0:
            dist = range(coord1[0], coord2[0], -1)
        elif coord1[0] >= 0:
            dist = range(coord1[0], coord2[0])
        for i in dist:
            new_coord = (i, coord1[1])
            if new_coord not in visited:
                visited.append(new_coord)
    return visited

# %%
from itertools import product

# %%
def find_all_coords_between(coord1, coord2):
    coords = []
    x1, y1 = coord1
    x2, y2 = coord2
    if x1 != x2:
        xs = [x for x in range(min(x1, x2), max(x1, x2))]
    else:
        xs = [x1]
    if y1 != y2:
        ys = [y for y in range(min(y1, y2), max(y1, y2))]
    else:
        ys = [y1]
    xys = list(product(xs, ys))
    return [c for c in xys if c not in [coord1, coord2]]


# %%
find_all_coords_between(coords_visited[0], coords_visited[1])


# %%
all_coords = []
done = False
i = 0
while not done:
    new_visits = [coords_visited[i]]
    new_visits += find_all_coords_between(coords_visited[i], coords_visited[i+1])
    for v in new_visits:
        if v in all_coords:
            print(v)
            print(sum(abs(c) for c in v)) 
            done = True
            break
        else:
            all_coords.append(v)
    i += 1

# %% [markdown]
# That's the right answer! You are one gold star closer to fixing the sleigh.
# 
# You have completed Day 1!

# %%



