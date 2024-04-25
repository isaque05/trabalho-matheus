# scrip para determinar se um ano é bissexto 
print ('bom dia')

ano = int(input('ano: '))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('bisexto')
else:
    print('não é bissexto')