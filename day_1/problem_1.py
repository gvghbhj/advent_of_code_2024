def main():
    sum = 0
    location_id_list_1 = []
    location_id_list_2 = []
    with open("list1.txt") as list_1:
        for line in list_1:
            location_id_list_1.append(int(line))
    with open("list2.txt") as list_2:
        for line in list_2:
            location_id_list_2.append(int(line))

    location_id_list_1.sort()
    location_id_list_2.sort()

    for i in range(len(location_id_list_1)):
        sum += absolute_value(location_id_list_1[i] - location_id_list_2[i])

    print(sum)
        

def absolute_value(x):
    if x >= 0:
        return x
    else:
        return -x

if __name__ == "__main__":
    main()
