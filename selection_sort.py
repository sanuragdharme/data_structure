# Selection Sort


def selection(iteration_list):
    for i in range(len(iteration_list) - 1):
        min_position = i
        for j in range(i, len(iteration_list)):
            if iteration_list[j] < iteration_list[min_position]:
                min_position = j

        iteration_list[i], iteration_list[min_position] = iteration_list[min_position], iteration_list[i]


number_list = [5, 3, 8, 6, 7, 2]
selection(number_list)
print("Sorted List: ", number_list)
