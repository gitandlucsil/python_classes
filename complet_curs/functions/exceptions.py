def divide(num1, num2):
    result = ""
    try:
        result = num1/num2
    except ZeroDivisionError:
        result = "Error!"
    finally:
        return result

print(divide(6, 3))
print(divide(6, 0))