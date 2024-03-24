# task 1
squares = [x ** 2 for x in range(1, 11)]
print("List of squares from 1 to 10:", squares)


def range_of_nums_squares(s, e):
    return [x ** 2 for x in range(s, e + 1)]


start = 1
end = 10
squares_list = range_of_nums_squares(start, end)
print(f"List of squares from {start} to {end}: {squares_list}")

