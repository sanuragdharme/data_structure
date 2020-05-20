# Selection Sort
# Complexity of Selection Sort - O(n2)
# Number of Swaps - O(n)
# It is not a stable sort


def selection(iteration_list):
    length = len(iteration_list)
    for i in range(length - 1):
        min_position = i
        for j in range(i, length):
            if iteration_list[j] < iteration_list[min_position]:
                min_position = j

        iteration_list[i], iteration_list[min_position] = iteration_list[min_position], iteration_list[i]


number_list = [5, 3, 8, 6, 5, 2]
selection(number_list)
print("Sorted List: ", number_list)
