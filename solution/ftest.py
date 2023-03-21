import math

import time

start = time.time()
# do something

x = math.factorial(100000)
end = time.time()
delta = end - start
print(x)
end2 = time.time()
delta2 = end2 - end
delta3 = end2 - start
print("calc took %.2f seconds to process" % delta)
print("print took %.2f seconds to process" % delta2)
print("all took %.2f seconds to process" % delta3)