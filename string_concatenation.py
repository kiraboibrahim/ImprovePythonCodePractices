import timeit


str_1 = "A"*1000
str_2 = "B"*2000

def concat_with_plus(str_1, str_2):
    return str_1 + str_2

def concat_with_format(str_1, str_2):
    return "%s%s".format(str_1, str_2)


print("Concatenation with plus takes ", timeit.timeit("concat_with_plus(str_1, str_2)", "from  __main__ import concat_with_plus, str_1, str_2"), "seconds")

print("Concatenation with format ", timeit.timeit("concat_with_format(str_1, str_2)", "from  __main__ import concat_with_format, str_1, str_2"), "seconds")
