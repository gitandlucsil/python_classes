import sys

_file = open("test.txt", "r")
print("File: ", _file.name)
for line in _file.readlines():
    sys.stdout.write(line)
_file.close()