#truncate always come from the maths library
import math

a = 2.87593469856390563

#truncate tends to remove all the values after the decimal points

a = math.trunc(a)
print(f"The value return without the single decimal point {a}")