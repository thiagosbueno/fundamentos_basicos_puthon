# -*- coding: utf-8 -*-
import random
from functools import reduce
# Permitir assentos na palavras

# Primeiro comentário
print("Olá Mundo!")

"""
comentários
de
várias linhas
"""
print("Segunda linha: Olá Mundo!")

# Operações matématicas
print("Operações matématicas:")
print(2 + 2)
print(2 - 2)
print(2 * 2)
print(10 / 3)
print(10 % 3)

#Variáveis
print("Variáveis:")
var1 = "Olá Mundo!" #string
var2 = 1 #integer
var3 = 1.1 #float
var4 = True #boolean

print(var1)
print(var2)
print(var3)
print(var4)

#Operadores Relacionais
x = 2
y = 3

soma = x + y

print("Operadores Relacionais:")
print(x == y)
print(x != y)
print(soma > y)
print(soma >= y)
print(soma < y)
print(soma <= y)

#Operadores Lógicos
x = 3
y = 3
z = 4
soma = x + y

print("Operadores Lógicos:")
print(x == y and x == soma)
print(x == y and x == z)
print(x == y or x == z)
print(x == y or x == z and z == y)
print(z == y and x  == y or x == z)

#Estruturas Condicionais
x = 1
y = 1000000

print("Estruturas Condicionais:")

if x > y:
	print("x é maior que y")	
else:	
	print("y é maior que x")

x = 1
y = 2

if x > y:
	print("x é maior que y")	
if y > x: 
	print("y é maior que x")
if y > x: 
	print("tem valor diferentes")
else:	
	print("x e y tem o mesmo valor!")

if x > y:
	print("x é maior que y")	
elif y > x: 
	print("y é maior que x")
else:	
	print("x e y tem o mesmo valor!")

#Estruturas de repetição

print("Estruturas de repetição:")
#Comando While
print("while:")
i = 0
while i <= 10:
	print(i)
	i += 1

#Comando For
print("for:")

lista1 = [1,2,3,4,5]
lista2 = ["ola", "mundo", "!"]
lista3 = [0, "ola", "biscoito", "bolacha", 9.99, True]

for i in lista3:
	print(i)

#Comando For range
print("for range:")

for i in range(10):
	print(i)

for i in range(10,20):
	print(i)

for i in range(10,20,2):
	print(i)

#Strings
print("Strings:")

a = "Thiago"
b = "Bueno"

print(a + b)
print(a + " " + b)

concatenar = a + " " + b

tamanho = len(concatenar)
print(tamanho)

letra = concatenar[0]
print(letra)

letra = concatenar[0:6]
print(letra)

letra = concatenar[0:]
print(letra)

print(concatenar.lower())
print(concatenar.upper())

minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split()
print(minha_lista)

minha_lista = minha_string.split("r")
print(minha_lista)

minha_lista = minha_string.lower().split("r")
print(minha_lista)

busca = minha_string.find(" ")
print(busca)

busca = minha_string.find("rei")
print(busca)

print(minha_string[busca:])

busca = minha_string.find("rainha")
print(busca)

minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)

#Funções
print("Funções:")

def soma(x, y):
	print(x + y)

def somaRetornada(x, y):
	return(x + y)

soma(2,2)
soma = somaRetornada(2,3)
print(soma)

#Manipulando arquivos
print("Manipulando arquivos:")

arquivo = open("arquivo.txt")

linhas = arquivo.readlines();
print(linhas)

for i in linhas:
	print(i)

textoCompleto = arquivo.read();
print(textoCompleto)

w = open("arquivo2.txt", "w")
w.write("Esse é o meu arquivo")
w.close()

w = open("arquivo2.txt", "a")
w.write("Esse é o meu arquivo")
w.close()


#Listas e dicionários
print("Listas e dicionários:")

minha_lista = ["abacaxi", "melancia", "abacate", "morango", "banana"]
print(minha_lista)

minha_lista.append("limão")
print(minha_lista)

if "melancia" in minha_lista:
	minha_lista.remove("melancia")
	print(minha_lista)

del minha_lista[2:]
print(minha_lista)

lista = [12,345,43,5,2,3,9,4,571,63,8,432]
print(lista)

lista.sort() #Ou pode ser usado dessa forma lista = sorted(lista)
print(lista)

lista.sort(reverse = True)
print(lista)

lista.reverse()
print(lista)

meu_dicionario = {"A": "Ameixa", "B" : "Banana", "C" : "Carambola"}
print(meu_dicionario)
print(meu_dicionario["A"])
print(meu_dicionario["B"])
print(meu_dicionario["C"])

for chave in meu_dicionario:
	print(chave + ": " + meu_dicionario[chave])

for item in meu_dicionario.items():
	print(item)

for valor in meu_dicionario.values():
	print(valor)



#Random
# Fazer o import random no começo do projeto
print("Random:")

numero = random.randint(0,10) #numero aleatorio de 0 a 10
print(numero)

lista = [0,32,321,5456,1243,546,45,3,5123,543,6]
numero = random.choice(lista) #pega valor aleatorio dentro da lista
print(numero)


#Exceções
print("Exceções:")

a = 2
b = 0

try:
	print(a / b)
except:
	print("Não é permitido divisão por 0")

#Exercícios
"""
Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.   

Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.   

Escreva um programa que resolva uma equação de segundo grau.   

Escreva um programa que ordene uma lista numérica com três elementos.   

Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.
"""

#List Comprehension
print("List Comprehension:")

x = [1, 2, 3, 4, 5]
y = []

for i in x:
	y.append(i**3)

print(y)

y = [i**2 for i in x]
print(y)

z = [i for i in x if i % 2 == 1]
print(z)

#Enumerate
print("Enumerate:")

lista = ["abacate", "bola", "cachorro"]

for i in lista:
	print(i)

for i in range(len(lista)):
	print(i, lista[i])

for i, nome in enumerate(lista):
	print(i, nome)


#Map
print("Map:")

def dobro(x):
	return x * 2

valor = [1, 2, 3, 4, 5]
valor_dobrado = map(dobro, valor)
valor_dobrado = list(valor_dobrado)
print(valor_dobrado)

#Reduce
#Fazer o from functools import reduce
print("Reduce:")

def soma(x,y):
	return x + y

lista = [1, 2, 3, 4, 5]
soma = reduce(soma, lista)
print(soma)


#Zip
print("Zip:")

lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]

for numero,nome in zip(lista1, lista2):
	print(numero,nome)