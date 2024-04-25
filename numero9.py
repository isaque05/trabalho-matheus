# CONVERSOR DE MEDIDAS 

num = float(input("digite o valor:"))
unidade = float(input("digite a unidade de medida,que sao metro, centimetro, quilometro, polegada, pés ou milha: "))
cmtom = num /100
cmtokm = num / 100000
cmtopolegada = num / 2.54
cmtope = num / 30.48
cmtomilha = num / 160900
mtocm = num / 100
mtokm = num / 1000
mtopolegada = num * 39.37
mtope = num * 3.281
mtomilha = num / 1609
kmtocm = num * 100000
kmtom = num * 1000
kmtopolegada = num * 39370
kmtope = num * 3281
kmtomilha = num / 1.609
polegadatocm = num * 2.54
polegadatom = num / 39.37
polegadatokm = num / 39370
polegadatope = num / 12
polegadatomilha = num / 63360
petocm = num * 30.48
petom = num / 3.281 
petokm = num / 3281
petopolegada = num * 12
petomilha = num / 5289
milhatocm = num * 160900
milhatom = num * 1609
milhatokm = num * 1.609
petocm = num * 30.48
petom = num / 3.281
petokm = num / 3281
petopolegada = num * 12
petomilha = num / 5280
milhatocm = num * 160900
milhatom = num * 1.609
milhatokm = num * 63360
milhatope = num * 5280

if unidade == "cintimetro":
    print("%f %s pode ser convertido em %f metros, %f quilometros, %f polegadas, %f pés, %f milhas." %(num, unidade, cmtom, cmtokm, cmtopolegada, cmtope, cmtomilha))
elif unidade == "metro":
    print("%f %s pode ser convertido em %f centimetros, %f quilometros, %f polegadas, %f pés %f milhas." %(num, unidade, mtokm, mtopolegada, ))
elif unidade == "quilometro":
    print("%f %s pode ser convertido em %f centimetros, %f metros, %f polegadas, %f pés %f milhas."%(num, unidade, kmtocm, kmtom, kmtopolegada,kmtope))
elif unidade == "polegada":
    print("%f %s pode ser convertido em %f centimetros, %f metros, %f quilometros, %f pés %f milhas. " %(num, unidade, polegadatocm, polegadatokm))
elif unidade == "pé":
    print("%f %s pode ser convertido em %f centimetros, %f metros, %f quilometros, %f polegadas, %f milhas."%(num, unidade, petocm, petom, petokm, petomilha))
elif unidade == "milha":
    print("%F %s pode ser convertido em %f centimetros, %f metros, %f quilometros, %f  polegadas, %f miljas,"%(num, unidade, milhatocm, milhatom, milhatokm,))
else:
    print("Erro voce digitou um valor de unidade que nao é válido")