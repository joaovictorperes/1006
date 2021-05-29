"""Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago."""

num1,quantidade1,preco1 = input().split(" ") # pega 3 valores na mesma linha e atribui a variáveis
num2,quantidade2,preco2 = input().split(" ") # pega 3 valores na mesma linha e atribui a variáveis

# Converte o valor para os tipos necessários 
num1 = int(num1)
quantidade1 = int(quantidade1)
preco1 = float(preco1) 

num2 = int(num2)
quantidade2 = int(quantidade2)
preco2 = float(preco2) 

valor1 = quantidade1 * preco1
valor2 = quantidade2 * preco2
valorTotal = valor1 + valor2

print("VALOR A PAGAR: R$ %.2f" % valorTotal)