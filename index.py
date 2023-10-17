l1 = float(input('Digite o comprimento do primeiro lado: '))
l2 = float(input('Digite o comprimento do segundo lado: '))
l3 = float(input('Digite o comprimento do terceiro lado: '))

if l1 < l2+l3 or l2 < l1+l3 or l3 < l2+l1 and l1 > l2-l3 or l2 > l1-l3 or l3 > l2-l1:
    if l1 == l2 and l2 == l3:
        print('Triângulo Equilátero!')

    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('Triângulo Isósceles!')

    else:
        print('Triângulo Escaleno!')
else:
    print('Não é possível criar um triângulo!.\n Tente novamente.')