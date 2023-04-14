def sort_last(tuples):
    return sorted(tuples, key=lambda x: x[-1])


input_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sorted_list = sort_last(input_list)

print(sorted_list)
