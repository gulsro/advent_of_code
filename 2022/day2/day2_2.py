import fileinput
def my_func(i, j):
    while j == 'X':
        if i == 'A':
            return 3
        elif i == 'B':
            return 1
        elif i == 'C':
            return 2
    while j == 'Y':
        if i == 'A':
            return 4
        elif i == 'B':
            return 5
        elif i == 'C':
            return 6
    while j == 'Z':
        if i == 'A':
            return 8
        elif i == 'B':
            return 9
        elif i == 'C':
            return 7

lst = []
arr = [line.split() for line in fileinput.input()]
index = 0
for index in range(len(arr)):
    i = arr[index][0]
    j = arr[index][1]
    lst.append(my_func(i, j))
print(lst)
print(sum(lst))
