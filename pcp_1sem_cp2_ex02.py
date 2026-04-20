def função(a,b,c):
    if a >= (b + c):
        print('NÃO FORMA TRIÂNGULO')
    elif a == b == c:
        print('FORMA TRIÂNGULO EQUILÁTERO')
    elif (a * 2) == (b * 2) + (c ** 2):
        print('FORMA TRIÂNGULO RETÂNGULO')
    elif(a*2) > (b * 2) > (c*2):
        print('FORMA TRIÂNGULO OBTUSÂNGULO')
    elif (a*2) > (b * 2) + (c*2):
        print('FORMA TRIÂNGULO OBTUSÂNGULO')
    elif (a*2) < (b * 2) + (c*2):
        print('FORMA TRIÂNGULO ACUTÂNGULO')
    return a,b,c



a = float(input('Lado A do triângulo: '))
b = float(input('Lado B do triângulo: '))
c = float(input('Lado C do triângulo: '))
função(a,b,c)