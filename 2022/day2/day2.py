import fileinput
def my_func(i, j):    
    while i == 'A':
        if j == 'X':
            return 4
        elif j == 'Y':
            return 8
        elif j == 'Z':
            return 3
    while i == 'B':
        if j == 'X':
            return 1
        elif j == 'Y':
            return 5
        elif j == 'Z':
            return 9
    while i == 'C':
        if j == 'X':
            return 7
        elif j == 'Y':
            return 2
        elif j == 'Z':
            return 6
lst = []
arr = [line.split() for line in fileinput.input()]
index = 0
for index in range(len(arr)):
    i = arr[index][0]
    j = arr[index][1]
    lst.append(my_func(i, j))
print(sum(lst))

