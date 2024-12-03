import re

def day3_1(str_):
    pattern = r"(?:mul|do|don't)\((?:\d{1,3},\s?\d{1,3})?\)"

    muls = re.findall(pattern, str_)
    mixed_list = [mul.strip("mul()").split(",") for mul in muls]
    #print(mixed_list)

    mult_list = [int(pair[0])* int(pair[1]) if len(pair) == 2 else pair[0] for pair in mixed_list]
    total = 0
    flag = True
    for i in mult_list:
        if i == "don't":
            flag = False
        elif i == "do":
            flag = True
        elif flag and isinstance(i, int):
            total += i
        
    print(total)

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        str_ = file.read().strip()
    day3_1(str_)
