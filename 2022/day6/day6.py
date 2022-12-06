with open('input', 'r') as f:
    inpt = f.read()

set_list = []
for i in range(0, len(inpt), 4):
    set_list.append(set(inpt[i:(i+4)]))

sum_list = []        
for i in range(len(set_list)):
    sum_list.append(len(set_list[i]))
    if len(set_list[i]) == 4:  
        print(i)
        break

count = 0
for i in range(len(sum_list)):
    count += sum_list[i]
print(count)

#hrbbjkm
