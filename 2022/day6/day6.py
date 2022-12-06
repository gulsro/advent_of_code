with open('input', 'r') as f:
    inpt = f.read()

set_list = []
for i in range(len(inpt)):
    set_list.append(set(inpt[i:(i+4)]))

count = 4 #first check for 4-char-set
for i in range(len(set_list)):
    #sum_list.append(len(set_list[i]))
    if len(set_list[i]) == 4:
        print(i)
        break
    count+= 1
print(count)
