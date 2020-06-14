import time

interval = 10000

def factorial(num):
    f = 1
    while num > 1:
        f *= num
        num -= 1
    return f

def factorial_recursive(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursive(num-1)

time1_begin = time.time()
for index in range(interval):
    factorial(index)
    #print("Factorial of %s is: %s" % (index, factorial(index)))
time1_end = time.time()
diff_1 = time1_end - time1_begin

"""
time2_begin = time.time()
for index in range(interval):
    factorial_recursive(index)
    #print("Factorial of %s is: %s" % (index, factorial_recursive(index)))
time2_end = time.time()
diff_2 = time2_end - time2_begin
"""
print("Time to non-recursive: ",diff_1)
#print("Time to recursive: ",diff_2)
