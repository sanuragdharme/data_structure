# In Linear Search, we check given number in sequential manner
# Find given number in the list

number_list = [5, 3, 8, 6, 7, 2]
num = 5

# Method 1
count = 0
for i in number_list:
    count += 1
    if i == num:
        print("Method 1: Found the number {} with {} iteration".format(i, count))

# Method 2
if num in number_list:
    print("Method 2: Number {} is available".format(num))

# Method 3
search = 0
while search < len(number_list):
    if number_list[search] == num:
        print("Method 3: Found the number {} with {} iteration".format(num, search))
    search += 1

