def main():
    sum = 0
    location_id_list_1 = []
    location_id_list_2 = []
    num_occurences = {}
    with open("list1.txt") as list_1:
        for line in list_1:
            location_id_list_1.append(int(line))
    with open("list2.txt") as list_2:
        for line in list_2:
            location_id_list_2.append(int(line))
    
    for number in location_id_list_2:
        try:
            num_occurences[number] += 1
        except:
            num_occurences[number] = 1

    for value in location_id_list_1:
        try:
            sum += (value * num_occurences[value])
        except:
            pass
    print(sum)

if __name__ == "__main__":
    main()
