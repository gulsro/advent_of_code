import fileinput
buffer = []
sums = []
for line in fileinput.input():
    if line != '\n':
        buffer.append(line)
    else:
        sums.append(sum([int(num.replace('\n', "")) for num in buffer]))
        buffer = []

sums.sort()
print(max(sums))

print(sums[len(sums) - 1] + sums[len(sums) - 2] + sums[len(sums) - 3])

