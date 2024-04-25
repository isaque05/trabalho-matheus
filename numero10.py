numero = float(input("digite um número"))

if numero > 0 and numero % 2 == 0:
        print ("O número é positivo e par.")
elif numero > 0 and numero % 3 == 0:
        print("O número é positivo e múltiplo de 3.")
elif numero < 0 and numero % 2 != 0:
        print ("O número é negativo e ímpar.")
elif numero == 0:
        print ("O número é zero.")
else:
        print ("O número não se enquadra em nenhuma das condições especificas")