def pi(valor):
    resultado = valor * 3.14159265
    return resultado

def calculo_circunferencia():
    valor = int(input("Informe um valor: "))
    valor = valor ** 2
    print(pi(valor))

calculo_circunferencia()