#Questão 1

print("Escreva um programa que leia uma lista de números e mostre o primeiro número na lista.")
l = list(map(int,input().split()))
print(l[0])


#Questão 2

print("Escreva um programa que leia uma lista de números e troque o primeiro elemento com o segundo. Depois mostre a nova lista.")
l = list(map(int,input().split()))
a = l[0]
l[0] = l[1]
l[1] = a
print(l)


#Questão 3

print("Escreva um programa que leia uma lista de 5 (cinco) números inteiros e mostre o primeiro e o último número.")
l = list(map(int,input().split()))
print(l[0],l[4])


#Questão 4

print("Escreva um programa que leia uma lista de 8 números e troque de lugar o primeiro número e o último número. Mostre a lista modificada.")
l = list(map(int,input().split()))
a = l[0]
l[0] = l[7]
l[7] = a
print(l)


#Questão 5

print('''Escreva um programa que leia uma lista de números inteiros em uma linha, depois leia um número inteiro e adicione o número lido ao final da lista.
Mostre a nova lista na tela.''')
l = list(map(int,input().split()))
l.append(int(input()))
print(l)


#Questão 6

print("Escreva um programa que leia uma lista de números, separados por espaço, e mostre a quantidade de números lidos.")
l = list(map(int,input().split()))
print(len(l))


#Questão 7

print("Escreva um programa que leia uma lista de números, separados por espaço, mostre a quantidade de números lidos, o primeiro número e o último número da lista.")
l = list(map(int,input().split()))
print(len(l),l[0],l[-1])


#Questão 8

print("Escreva um programa que leia uma lista de números inteiros e mostre o menor número e o maior número da lista.")
l = list(map(int,input().split()))
print(min(l),max(l))


#Questão 9

print("Escreva um programa que leia uma lista de números inteiros e mostre se a soma dos números é par ou ímpar.")
l = list(map(int,input().split()))
if sum(l)%2 == 0: print("Par")
else: print("Impar")


#Questão 10

print("Escreva um programa que leia uma lista de números inteiros e mostre se a soma dos números é divisível pela quantidade de números lidos.")
l = list(map(int,input().split()))
if sum(l)%len(l) == 0: print("Sim")
else: print("Nao")


#Questão 11

print('''Escreva um programa que leia uma lista de números, separados por espaço, e mostre o número localizado no meio da lista. 
Caso a lista tenha uma quantidade par de números, o programa mostra a média dos dois números do meio.''')
l = list(map(int,input().split()))

if len(l) % 2 == 0: 
  print((l[(len(l)//2)-1] + l[len(l)//2])/2)
else: 
  print(l[len(l)//2])


#Questão 12

print("Escreva um programa que leia uma string e mostre quantas palavras existem na string.")
l = input().split()
print(len(l))
