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

#arr = [45, 456,"",75, 34]
buffer = []
sums = []
#arr = [line for line in fileinput.input()]
for line in fileinput.input():
    if line != '\n':
        buffer.append(line)
    else:
        sums.append(sum([int(num.replace('\n', "")) for num in buffer]))
        buffer = []
print(max(sums))
#import pdb;pdb.set_trace()
#i = 0
#while i < len(arr):
#    if arr[i] == '\n':
#        arr[i] = 0
#    i += 1
#my_lst = [int(arr) for line in arr]
#print(arr)
#arr = [int(line) for line in fileinput.input()]
#my_func(arr)
