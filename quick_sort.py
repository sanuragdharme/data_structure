# Quick Sort
# Follows Divide and Conquer with Recursion
# Complexity of Quick Sort - nlog(n)
# It is not a stable sort


def partition(iterate_list, start_index, end_index):
    curr_index = start_index
    pivot = iterate_list[end_index]

    for i in range(start_index, end_index):
        if iterate_list[i] <= pivot:
            iterate_list[curr_index], iterate_list[i] = iterate_list[i], iterate_list[curr_index]
            curr_index += 1

    iterate_list[curr_index], iterate_list[end_index] = iterate_list[end_index], iterate_list[curr_index]
    return curr_index


def quick_sort(iterate_list, start_index, end_index):
    if start_index >= end_index:
        return

    curr_index = partition(iterate_list, start_index, end_index)

    print("Element in the right place: ", iterate_list[curr_index])
    print(iterate_list)

    quick_sort(iterate_list, start_index, curr_index - 1)
    quick_sort(iterate_list, curr_index + 1, end_index)


number_list = [54, 26, 93, 17, 77, 44, 55, 20, 13, 2, 100, 66]
quick_sort(number_list, 0, len(number_list) -1)
