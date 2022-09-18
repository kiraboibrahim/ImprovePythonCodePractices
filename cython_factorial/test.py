import factorial
import time

start = time.time()
factorial.factorial(100)
end = time.time()

duration = end - start
print("Cython took {} seconds".format(duration))
