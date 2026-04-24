import math

a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

lados = (a, b, c)
lados = sorted(lados, reverse=True)

forma_tri = not lados[0] >= lados[1]+lados[2]

tri_ret =  lados[0]**2 == lados[1]**2 + lados[2]**2

tri_obtuso = lados[0]**2 > lados[1]**2 + lados[2]**2

tri_acu = lados[0]**2 < lados[1]**2 + lados[2]**2

tri_equi = lados[0] == lados[1] == lados[2]

tri_iso = lados[0] == lados[1] != lados[2] or lados[1] == lados[2] != lados[0] or lados[2] == lados[0] != lados[1]

if forma_tri:
    if tri_equi:
        print("TRIÂNGULO EQUILÁTERO")
    elif tri_iso:
        print("TRIÂNGULO ISÓSCELES")
    if tri_ret:
        print("TRIÂNGULO RETÂNGULO")
    elif tri_obtuso:
        print("TRIÂNGULO OBTUSÂNGULO")
    elif tri_acu:
        print("TRIÂNGULO ACUTÂNGULO")
else:
    print("NÃO FORMA TRIÂNGULO")