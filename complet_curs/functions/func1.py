def sum(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def isOdd(num):
    if num % 2 != 0:
        return True
    else:
        return False

def isEvenorOdd(num):
    if isEven(num) is True:
        return "Even!"
    elif isOdd(num) is True:
        return "Odd!"
    else:
        return "Problem!"

print("6 + 5: ",sum(6,5))
print("6 - 5: ",sub(6,5))
print("6 * 5: ",mul(6,5))
print("6 / 5: ",div(6,5))
print("5 is even?, ", isEven(5))
print("5 is odd?, ", isOdd(5))
print("5 is even or odd?, 5 is ",isEvenorOdd(5))