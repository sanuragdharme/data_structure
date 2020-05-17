# For Binary Search : List has to in sorted order
# Find given number in the list

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

