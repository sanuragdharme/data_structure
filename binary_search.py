# For Binary Search : List has to in sorted order
# Find given number in the list
# Complexity is O(n)
# Worst Case - Complexity is O(log N)
# Search faster than Linear Search

position = -1


def get_binary_search(search_list, search_num):
    search_list = sorted(search_list)
    lower_bound = 0
    upper_bound = len(search_list)
    print("Sorted List: ", search_list)

    while lower_bound <= upper_bound:
        # To get the integer value in return use //
        mid_value = (lower_bound + upper_bound) // 2
        if search_list[mid_value] == search_num:
            globals()['position'] = mid_value
            return True
        else:
            if search_list[mid_value] < search_num:
                lower_bound = mid_value + 1
            else:
                upper_bound = mid_value - 1

    return False


number_list = [5, 8, 4, 6, 9, 2, 34, 12, 45, 87, 1, 456, 23]
num = 12

if get_binary_search(number_list, num):
    print("Found the number {} at iteration {}".format(num, position))
else:
    print("Number is not available")


def binary_search(sorted_list, key):
    min_index = 0
    max_index = len(sorted_list) - 1

    while min_index <= max_index:
        mid = (min_index + max_index) // 2

        if sorted_list[mid] == key:
            return mid
        elif sorted_list[mid] < key:
            min_index = mid + 1
        else:
            max_index = mid - 1

    return -1


numbers_list = [25, 29, 32, 34, 37, 43, 45, 49, 55, 66, 78, 89, 99]
print("Binary Search: ", binary_search(numbers_list, 49))
