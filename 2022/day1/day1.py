import fileinput
def my_func(arr):
    result = 0
    i = 0
    sum_list = []
    my_list = []
    while i < len(arr):
        while (i < len(arr) and arr[i] != '\n'):   
            my_list.append(arr[i])
            i += 1
        sum_list.append(sum(my_list))
        my_list.clear()
        i += 1
    result = max(sum_list)
    print(result)
    return result

buffer = []
sums = []
for line in fileinput.input():
    if line != '\n':
        buffer.append(line)
    else:
        sums.append(sum([int(num.replace('\n', "")) for num in buffer]))
        buffer = []
print(max(sums))

