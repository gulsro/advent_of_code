import fileinput
buffer = []
sums = []
#arr = [line for line in fileinput.input()]
for line in fileinput.input():
    if line != '\n':
        buffer.append(line)
    else:
        sums.append(sum([int(num.replace('\n', "")) for num in buffer]))
        buffer = []

sums.sort()
print(max(sums))

print(sums[len(sums) - 1] + sums[len(sums) - 2] + sums[len(sums) - 3])

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
