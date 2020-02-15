soma = lambda num1, num2: num1+num2
subtracao = lambda num1, num2: num1-num2
multiplicacao = lambda num1,num2: num1*num2
divisao = lambda num1, num2: num1/num2

def calculadora(function,num1,num2):
    print(function(num1,num2))

calculadora(soma,2,2)
calculadora(subtracao,4,2)
calculadora(multiplicacao,8,2)
calculadora(divisao,10,2)