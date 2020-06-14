_file = open("test.txt", "w")
_file.write("#List of NBA Players:\n")
_file.write("@Lebron James\n")
_file.write("@James Harden\n")
_file.write("@Stephen Curry\n")
_file.write("%This not shoudl be printed!")
_file.flush()
print("Mode operation: ", _file.mode)
_file.close()

if _file.closed:
    _file = open("test.txt", "r")
    print("File: ", _file.name)
    for line in _file.readlines():
        if line[0] == "#":
            print(line[1:].center(80))
        elif line[0] == "@":
            print(line[1:].rjust(80))
        elif line[0] == "%":
            pass
    print("Mode operation: ", _file.mode)
    _file.close()
