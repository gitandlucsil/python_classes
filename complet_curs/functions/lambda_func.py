def sum_numbers(num1, num2):
    return num1 + num2
    
sum_lambda = lambda num1,num2 : sum_numbers(num1, num2)

print("6 + 5: ",sum_lambda(6,5))