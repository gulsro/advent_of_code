import re

def day3_1(str_):
    pattern = r"mul\(\d{1,3},\s?\d{1,3}\)"

    muls = re.findall(pattern, str_)
    mixed_list = [mul.strip("mul()").split(",") for mul in muls]
    mult_list = [int(pair[0])* int(pair[1]) for pair in mixed_list]
    print(sum(mult_list))

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        str_ = file.read().strip()
    day3_1(str_)
