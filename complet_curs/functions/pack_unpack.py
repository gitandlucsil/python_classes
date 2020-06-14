def sum_numbers(num1, num2):
    return num1 + num2

def sum_unpack(*nums):
    return sum(nums)

print("6 + 5: ",sum_numbers(6,5))

list_number = [6, 5, 7, 10]
print("Sum of the list is: ", sum_unpack(*list_number))