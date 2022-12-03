import fileinput
import string
def my_func(content_list):
    start = 0
    len_list = len(content_list)
    half = len_list // 2
    for start in range(len_list // 2):
        for half in range(len_list // 2, len_list):
            if content_list[start] == content_list[half]:
                return (content_list[start])

list_item = [list(line) for line in fileinput.input()]

item = [my_func(list_item[i]) for i in range(len(list_item))]
item_all = list(string.ascii_lowercase) + list(string.ascii_uppercase)
prio_points = list(range(1, 53))
prio_points_list = []
for i in range(len(item)):
    for j in range(len(item_all)):
        if item[i] == item_all[j]:
           prio_points_list.append(prio_points[j])
print(sum(prio_points_list))

