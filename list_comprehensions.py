import timeit
<<<<<<< HEAD
=======
import dis
>>>>>>> d29113f (init)


def get_even_numbers_less_100():
    even_numbers = []
    for number in range(1, 100):
        if number%2 == 0:
            even_numbers.append(number)
    return even_numbers


def get_even_numbers_less_100_lc():
    even_numbers = [number for number in range(1, 100) if number%2 == 0] 
    return even_numbers


print("List comprehension takes ", timeit.timeit("get_even_numbers_less_100_lc()", "from __main__ import get_even_numbers_less_100_lc"), "seconds.") 
print("List construction with append and conditionals takes ", timeit.timeit("get_even_numbers_less_100()", "from __main__ import get_even_numbers_less_100"), "seconds.")