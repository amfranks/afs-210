def binary_search(ordered_list, term):

    size_of_list = len(ordered_list) - 1

    index_of_first_element = 0
    index_of_last_element = size_of_list

    while index_of_first_element <= index_of_last_element:
        mid_point = (index_of_first_element + index_of_last_element) / 2

        if ordered_list[int(mid_point)] == term:
            return True

        if term > ordered_list[int(mid_point)]:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1

    if index_of_first_element > index_of_last_element:
        return False

print(binary_search([7, 20, 26, 31, 40, 51, 55, 63, 74, 81], 31))
print(binary_search([7, 20, 26, 31, 40, 51, 55, 63, 74, 81], 77))
print(binary_search(["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"], "Delta"))