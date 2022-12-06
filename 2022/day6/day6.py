with open('input', 'r') as f:
    inpt = f.read()

lst = []
for index in range(len(inpt)):
    for i in range(4):
        for j in range(4):
            j = i + 1
            if inpt[i] == inpt[j]:
                break
            lst[i] = lst.append(inpt[i:j])

            #lst.append(j)
    #print(j)       

print(lst)


#hrbbjkm
