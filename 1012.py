"""Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B. """

a,b,c = input().split(" ")

a = float(a)
b = float(b)
c = float(c)

areaTriangulo = (a * c)/2
areaCirculo = 3.14159 * (c ** 2)
areaTrapezio = ((a+b)*c)/2
areaQuadrado = b ** 2
areaRetangulo = a * b

print("TRIANGULO: %.3f" % areaTriangulo)
print("CIRCULO: %.3f" % areaCirculo)
print("TRAPEZIO: %.3f" % areaTrapezio)
print("QUADRADO: %.3f" % areaQuadrado)
print("RETANGULO: %.3f" % areaRetangulo)