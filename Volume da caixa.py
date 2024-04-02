def volume_caixa(comprimento, largura, altura):
    volume = comprimento * largura * altura
    return volume

def calcular():
    comprimento = int(input(" Qual é o comprimento da caixa? "))
    largura = int(input(" Qual é a largura da caixa? "))
    altura = int(input(" Qual é a altura da caixa? "))
    volume = volume_caixa(comprimento, largura, altura)
    volume_caixa(comprimento, largura, altura)
    print(f"O volume da caixa é:{volume}")

calcular()