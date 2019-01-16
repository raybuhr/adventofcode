#%%
data = '320851'


#%%
def create_recipes(scores, num_recipes):
    elf_one = 0
    elf_two = 1
    recipes = [int(r) for r in str(scores)]
    while num_recipes > 0:
        next_recipe = str(recipes[elf_one] + recipes[elf_two])
        recipes += [int(r) for r in next_recipe]
        elf_one_steps = recipes[elf_one] + 1
        elf_two_steps = recipes[elf_two] + 1
        elf_one = (elf_one + elf_one_steps) % len(recipes)
        elf_two = (elf_two + elf_two_steps) % len(recipes)
        num_recipes -= 1
    return ''.join([str(r) for r in recipes])


#%%
test_cases = [
    (9, '5158916779'),
    (5, '0124515891'),
    (18, '9251071085'),
    (2018, '5941429882')
]


#%%
for tc in test_cases:
    ans = create_recipes('37', tc[0]+10)
    assert tc[1] == ans[tc[0]:tc[0]+10]


#%%
get_ipython().run_cell_magic('time', '', 'pt1 = create_recipes(\'37\', int(data)+10)\nprint("Part One:", pt1[int(data):int(data)+10])')


#%%
def find_recipe(scores, recipe):
    elf_one = 0
    elf_two = 1
    while recipe not in scores[-(len(recipe)+1):]:
        scores += str(int(scores[elf_one]) + int(scores[elf_two]))
        elf_one = (elf_one + int(scores[elf_one]) + 1) % len(scores)
        elf_two = (elf_two + int(scores[elf_two]) + 1) % len(scores)
    return scores


#%%
test_cases2 = [
    ('51589', 9),
    ('01245', 5),
    ('92510', 18),
    ('59414', 2018)
]


#%%
get_ipython().run_cell_magic('time', '', "for tc in test_cases2:\n    ans = find_recipe('37', tc[0])\n    print('Expected', tc[1], 'and got', ans.index(tc[0]))\n    assert ans.index(tc[0]) == tc[1]")


#%%
get_ipython().run_cell_magic('time', '', "pt2 = find_recipe('37', data)")


#%%
print("Part Two:", pt2.index(data))




#%%
