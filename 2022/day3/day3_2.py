import fileinput
import string

list_item = [line for line in fileinput.input()]
list_of_sets = []
for i in range(len(list_item)):
    list_of_sets.append(set(list_item[i]))

i = 0
common_item_list = []
for i in range(0, len(list_of_sets) - 2, 3):
    if (list_of_sets[i] & list_of_sets[i + 1] & list_of_sets[i + 2]):
       common_item_list.append(list_of_sets[i] & list_of_sets[i + 1] & list_of_sets[i + 2])

item_all = list(string.ascii_lowercase) + list(string.ascii_uppercase)
prio_points = list(range(1, 53))

lst = []
for index in range(len(common_item_list)):
    common_item_list[index].remove('\n')
    lst.append(list(common_item_list[index]))

prio_points_list = []
for i in range(len(lst)):
    for j in range(len(item_all)):
        if lst[i][0] == item_all[j]:
            prio_points_list.append(prio_points[j])
print(sum(prio_points_list))

