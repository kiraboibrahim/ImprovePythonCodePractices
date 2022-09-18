import time

import factorial


start = time.time()
factorial.factorial(100)
end = time.time()

duration = end - start
print("Python took {} seconds".format(duration))
