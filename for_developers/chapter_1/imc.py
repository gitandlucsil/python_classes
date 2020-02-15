#IMC.py
def indice(altura,peso):
    imc = peso/(altura**2)
    return imc

def estado(imc):
    if imc < 24.9:
        print("Normal")
    elif 24.9 <= imc < 29.9:
        print("Peso a mais")
    elif 29.9 <= imc < 40:
        print("Ligeira obesidade")
    elif imc >= 40:
        print("Obesidade")
    else:
        print("Magro demais")

def pesoideal(altura,peso):
    a = 20*(altura**2)
    b = 24.9*(altura**2)
    print("Seu peso ideal se encontra entre %.2f e %.2f"%(a,b))