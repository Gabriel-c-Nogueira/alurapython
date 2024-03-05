
 
idade = int(input('digite sua idade: '))

if idade < 12: 
    print('criança')
elif idade >= 12 and idade < 18:
    print('adolescente')
else:
    print("adulto")