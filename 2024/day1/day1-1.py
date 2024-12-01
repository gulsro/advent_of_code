def day1_1(data):
    sorted_firsts = sorted(data)
    sorted_seconds = sorted([elem[1] for elem in sorted_firsts])
    all_sorted = [[sorted_firsts[i][0], sorted_seconds[i]] for i in range(len(data))]

    distance_list = [abs(int(pair[0]) - int(pair[1])) for pair in all_sorted]
    return sum(distance_list)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        str_list = file.read().strip().split("\n")
        data = [str_pair.split() for str_pair in str_list]
    print(day1_1(data))
