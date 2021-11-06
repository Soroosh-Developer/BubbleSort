def bubbleSort(list):
    n = len(list)
    is_swapped = False
    for i in range(n):
        for j in range(n - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                is_swapped = True
        if not is_swapped:
            break
    return list


myList = [-3, 53, 54, 26, 93, 17, 77, 31, 44, 55, 8978, 521, 254, 654, 32, 41, 5, 54, 56, 20]
bubbleSort(myList)
print(myList)
