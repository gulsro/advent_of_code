#            [M] [S] [S]
#        [M] [N] [L] [T] [Q]
#[G]     [P] [C] [F] [G] [T]
#[B]     [J] [D] [P] [V] [F] [F]
#[D]     [D] [G] [C] [Z] [H] [B] [G]
#[C] [G] [Q] [L] [N] [D] [M] [D] [Q]
#[P] [V] [S] [S] [B] [B] [Z] [M] [C]
#[R] [H] [N] [P] [J] [Q] [B] [C] [F]
# 1   2   3   4   5   6   7   8   9

with open('input', 'r') as f:
    lines = f.read().splitlines()

QUANTITY = 0
FROM = 1
TO = 2

stack_list = [[],
              [['R'], ['P'], ['C'], ['D'], ['B'], ['G']],
              [['H'], ['V'], ['G']],
              [['N'], ['S'], ['Q'], ['D'], ['J'], ['P'], ['M']],
              [['P'], ['S'], ['L'], ['G'], ['D'], ['C'], ['N'], ['M']],
              [['J'], ['B'], ['N'], ['C'], ['P'], ['F'], ['L'], ['S']],
              [['Q'], ['B'], ['D'], ['Z'], ['V'], ['G'], ['T'], ['S']],
              [['B'], ['Z'], ['M'], ['H'], ['F'], ['T'], ['Q']],
              [['C'], ['M'], ['D'], ['B'], ['F']],
              [['F'], ['C'], ['Q'], ['G']]]

for i in range(len(lines)):
    lines[i] =  lines[i].split()
    lines[i].remove(lines[i][0])
    lines[i].remove(lines[i][1])
    lines[i].remove(lines[i][2])
    #_, q, _, f, _, t = line.split()

def move_crate(line, stack_list):
    how_many = int(line[QUANTITY])
    from_where = int(line[FROM])
    to_where = int(line[TO])
    for i in range(how_many):
        elem = stack_list[from_where].pop(i - how_many)
        stack_list[to_where].append(elem)

for line in lines:
    move_crate(line, stack_list)

print(len(stack_list))
for stack in stack_list:
    if stack:
        print(stack[-1])

