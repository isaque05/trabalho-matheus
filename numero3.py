def calcular_perimetro_retangulo(comprimento, largura):
    """
    Calcula o perímetro de um retângulo dado o comprimento e a largura.
    """
    perimetro = 2 * (comprimento + largura)
    return perimetro

def calcular_area_retangulo(comprimento, largura):
    """
    Calcula a área de um retângulo dado o comprimento e a largura.
    """
    area = comprimento * largura
    return area

# Solicitar ao usuário o comprimento e a largura do retângulo
comprimento = float(input("Digite o comprimento do retângulo: "))
largura = float(input("Digite a largura do retângulo: "))

# Calcular o perímetro e a área
perimetro = calcular_perimetro_retangulo(comprimento, largura)
area = calcular_area_retangulo(comprimento, largura)

# Exibir o resultado
print(f"O perímetro do retângulo é {perimetro:.2f} unidades.")
print(f"A área do retângulo é {area:.2f} unidades quadradas.")