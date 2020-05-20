# Shell Sort
# Follows Divide and Conquer
# It uses Insertion Sort and the entire list is divided and those sublist are sorted
# Complexity of Shell Sort - Between O(n) and O(n2) Average - O(n3/2)
# It is an adaptive sort


def shell(iterate_list):
    length = len(iterate_list)
    gap = length // 2

    while gap > 0:
        for i in range(gap, length):
            temp = iterate_list[i]
            j = i

            while j >= gap and iterate_list[j-gap] > temp:
                iterate_list[j] = iterate_list[j-gap]
                j -= gap

            iterate_list[j] = temp

            print("Gap: ", gap)
            print("Iterable List: ", iterate_list)

        gap = gap // 2


number_list = [10, 5, 7, 2, 8, 3, 9, 6, 1, 4]
shell(number_list)