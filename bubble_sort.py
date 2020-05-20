# Bubble Sort
# Complexity of Bubble Sort - O(n2)
# It is a stable sort
# Number of Swaps - O(n)


def bubble(iterate_list):
    for i in range(len(iterate_list) - 1, 0, -1):
        for j in range(i):
            if iterate_list[j] > iterate_list[j+1]:
                iterate_list[j], iterate_list[j+1] = iterate_list[j+1], iterate_list[j]
            print(iterate_list)
        print(" ")


number_list = [5, 3, 8, 6, 7, 5, 2]
bubble(number_list)
print("Sorted List: ", number_list)
print(sorted(number_list))
number_list.sort()
print(number_list)