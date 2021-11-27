# string message = "hello";
from sys import getsizeof
message = "hello"

print(message)
print(type(message))

counter =  0 # 0  # 100 # 2**64
size  = getsizeof(counter)
print(size)
