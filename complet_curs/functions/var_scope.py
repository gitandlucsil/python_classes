def printName():
    global name
    print(name)
    name = "andre"
    print(name)

def sumList(list_num):
    global sumvalue
    for num in list_num:
        if type(num) is list:
            sumList(num)
        else:
            sumvalue += num
    return sumvalue

name = "jose"
printName()
sumvalue = 0
print(sumList([5,7,2,3,8]))
print(sumList([[5,7],[2,3,8]]))