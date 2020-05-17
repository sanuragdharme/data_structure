# Bubble Sort


def bubble(iterate_list):
    for i in range(len(iterate_list) - 1, 0, -1):
        for j in range(i):
            if iterate_list[j] > iterate_list[j+1]:
                iterate_list[j], iterate_list[j+1] = iterate_list[j+1], iterate_list[j]
            print(iterate_list)
        print(" ")


number_list = [5, 3, 8, 6, 7, 2]
bubble(number_list)
print("Sorted List: ", number_list)
