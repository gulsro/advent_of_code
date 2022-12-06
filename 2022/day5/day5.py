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

stack_list = [[], [[R], [P], [C], [D], [B]], [[H], [V], [G]], [[N], [S], [Q], [D], [J]], [[], [], [], [], []],  
#directive_list = []
#for i in range(len(lines)):
#    directive_list.append(lines[])
for i in range(len(lines)):
    lines[i] =  lines[i].split()
    lines[i].remove(lines[i][0])
    lines[i].remove(lines[i][1])
    lines[i].remove(lines[i][2])
print(lines)
print(len(lines))

#for i in range(len(lines)):
#    for j in range(0, len(lines[i]), 2):
#        lines[i].remove(lines[i][j])

print(lines)
