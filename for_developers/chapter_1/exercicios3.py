#1.Fazer uma calculadora que execute operacoes de adicao, subtracao, multiplicacao, divisao, quadrado, cubo, raiz quadrada,
#  seno, cosseno, tangente.
print("----Inicio exercicio 1----")
import math
def calculadora(funcao,arg1,arg2):
    return funcao(arg1,arg2)

def somar(arg1,arg2):
    return arg1+arg2
def subtrair(arg1,arg2):
    return arg1-arg2
def multiplicar(arg1,arg2):
    return arg1*arg2
def dividir(arg1,arg2):
    return arg1/arg2
def quadrado(arg1,arg2):
    return arg1**2
def raizquadrada(arg1,arg2):
    return math.sqrt(arg1)
def seno(arg1,arg2):
    return math.sin(arg1)
def cosseno(arg1,arg2):
    return math.cos(arg1)
def tangente(arg1,arg2):
    return math.tan(arg1)

print(calculadora(somar,1,2))
print(calculadora(subtrair,1,2))
print(calculadora(multiplicar,5,2))
print(calculadora(dividir,6,2))
print(calculadora(quadrado,6,0))
print(calculadora(raizquadrada,6,0))
print(calculadora(seno,6,0))
print(calculadora(cosseno,6,0))
print(calculadora(tangente,6,0))
#2.Faca um programa que ao receber um valor de raio, retorne a area e perımetro do cırculo
print("----Inicio exercicio 2----")
raio = float(input("Informe o valor do raio: "))
area = math.pi * raio**2
perimetro = math.pi * raio * 2
print("A area tem o valor de: %.2f"%(area))
print("O perimetro tem o valor de: %.2f"%(perimetro))