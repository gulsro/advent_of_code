def day1_2(data):
    line_left = [pair[0] for pair in data]
    line_right = [pair[1] for pair in data]
    
    occurance_count_left = {elem:line_right.count(elem) for elem in line_left}
    list_sim_score = [int(k) * int(v) for k, v in occurance_count_left.items()]
    return sum(list_sim_score)

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        str_list = file.read().strip().split("\n")
        data = [str_pair.split() for str_pair in str_list]
    print(day1_2(data))