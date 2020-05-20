# Merge Sort
# Follows Divide and Conquer with Recursion
# Complexity of Merge Sort - nlog(n)
# It is a stable sort


def merge(iterate_list):
    if len(iterate_list) <= 1:
        return

    middle = len(iterate_list) // 2
    left_half = iterate_list[:middle]
    right_half = iterate_list[middle:]

    merge(left_half)
    print(left_half)

    merge(right_half)
    print(right_half)

    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            iterate_list[k] = left_half[i]
            i += 1
        else:
            iterate_list[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        iterate_list[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        iterate_list[k] = right_half[j]
        j += 1
        k += 1

    print(iterate_list)


number_list = [54, 26, 93, 17, 77, 44, 55, 20, 13, 2, 100, 66]
merge(number_list)

