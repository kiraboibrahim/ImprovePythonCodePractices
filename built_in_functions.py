import timeit

numbers = range(1, 1000)

def custom_sum():
    total = 0
    for number in numbers:
        total += number
    return total

def built_in_sum():
    total = sum(numbers)
    return total

print("Custom sum() function takes ", timeit.timeit("custom_sum()", "from __main__ import custom_sum, numbers"), "seconds.")
print("Built In sum() function takes ", timeit.timeit("built_in_sum()", "from __main__ import built_in_sum, numbers"), "seconds.")
