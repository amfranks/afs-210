import random

array = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

# Print array before shuffle.
print("\nBefore Shuffle:\n")
print(f"{array}\n")

def shuffle(list):

    length_of_list = len(list)
    last_index = len(list) -1

    for i in range(0, length_of_list):
        random_index = random.randint(0, last_index)
        list[i], list[random_index] = list[random_index], list[i]

    return list

print("Shuffled:\n")
print(shuffle(array))
print(shuffle(array))
print(shuffle(array))
print(shuffle(array))
print(shuffle(array))

# The time complexity of this algorithm is O(n), because it iterates
# through our list once, and increases the amount of iterations
# linearly based upon how many elements are in our list.