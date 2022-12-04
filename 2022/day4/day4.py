with open('input', 'r') as f:
    pair_list = f.read().splitlines()
pairs = []
for i in range(len(pair_list)):
    single_pair = pair_list[i].split(",")
    pairs.append(single_pair)

no_dash_list = []
for i in range(len(pairs)):
    for j in range(len(pairs[i])):
        no_dash = pairs[i][j].split("-")
        no_dash_list.append(no_dash)
my_list = []
for i in range(len(no_dash_list)):
    for j in range(2):
        my_list.append(int(no_dash_list[i][j]))

set_list = []
for i in range(0, len(my_list), 2):
    set_list.append(set(range(my_list[i], my_list[i + 1] + 1)))
print(set_list)

count = 0
for i in range(0, len(set_list), 2):
    if set_list[i].issubset(set_list[i + 1]) or set_list[i + 1].issubset(set_list[i]):
        count += 1
print(count)
