# Insertion Sort
# Complexity of Insertion Sort - O(n2)
# Number of Swaps - O(n2)
# It is a stable sort


def insertion(iterate_list):
    length = len(iterate_list)
    for i in range(0, length - 1):
        for j in range(i + 1, 0, -1):
            if iterate_list[j] < iterate_list[j-1]:
                iterate_list[j], iterate_list[j-1] = iterate_list[j-1], iterate_list[j]
            print(iterate_list)
        print(" ")


number_list = [10, 5, 7, 2, 8, 3, 9, 6, 1, 4]
insertion(number_list)
