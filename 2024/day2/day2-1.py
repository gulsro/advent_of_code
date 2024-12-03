def check_des(line):
    return all(line[i] < line[i+1] for i in range(len(line) - 1))
    
def check_asc(line):
    return all(line[i] > line[i+1] for i in range(len(line) - 1))

def check_dif(line):
    return all(abs(line[i]-line[i+1]) <= 3 for i in range(len(line) - 1))

def day2_1(data):
    new = [line for line in data if (check_des(line) or check_asc(line)) and check_dif(line)]
    return len(new)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        str_list = file.read().strip().split("\n")
        data = [[int(num) for num in str_report.split()] for str_report in str_list]
    print(day2_1(data))