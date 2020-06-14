import random
import string

for num in range(10):
    print(random.randint(1, 10))

for num in range(10):
    print(random.random())

for num in range(10):
    print(random.uniform(1,10))

print(random.choice(string.ascii_lowercase))