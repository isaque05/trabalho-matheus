print ("bom dia")
# calcule os lados da piramide

a= float(input('escreva o temanho do primeiro lado'))
b= float(input('escreva o tamanho do segundo lado'))
c= float(input('escreva o tamanho do terceiro lado'))

            #tipos de piramite 
if(a + b < c) or (a + c < b)or(b + c < a):
    print("nao e um triangulo ")
elif (a == b) and (a == c):
    print ("equilatero")
elif (a == b) or (a == c) or (b == c):
    print ("isosceles")
else:
    print ("escaleno")