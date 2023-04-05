#Escreva um programa que leia dois números inteiros e mostre a soma dos mesmos.

a = int(input())
b = int(input())
soma = a+b
print(soma)


#Escreva um programa que leia dois números reais e mostre a média aritmética dos mesmos.

x = float(input())
y = float(input())
media = (x+y)/2
print(media)


#Escreva um programa que leia duas notas e mostre a média obtida a partir das mesmas, de acordo com as regras do IFRN

nota1 = int(input())
nota2 = int(input())
media_ifrn = (nota1*2+nota2*3)/5
print(media_ifrn)


#Escreva um programa que leia três (3) números e mostre o produto dos mesmos.

bibi1 = int(input())
bibi2 = int(input())
bibi3 = int(input())
produto_bibi = bibi1*bibi2*bibi3


#Escreva um programa que leia a hora de início e de fim de um evento e mostre o tempo do evento no
#formato HH:MM. A hora de início e fim é dada em minutos desde o início do dia.

h_inicio = int(input())
h_fim = int(input())
tempo = h_fim-h_inicio
horas = tempo//60
minutos = (tempo%60)
tempo_evento = print(horas,minutos,sep=":")


#Escreva um programa que leia a quantidade de dias desde o início do ano e mostre quantas semanas e 
#quantos dias já se passaram desde do dia primeiro de janeiro.

qtd_dias = int(input())
semanas = qtd_dias//7
dias = qtd_dias%7
print("{} semana(s)\n{} dia(s)".format(semanas, dias))


#Escreva um programa que leia o valor de um item a venda, a quantidade de itens que você vai 
#comprar e o valor que você tem para pagar. Todos os valores são inteiros. O programa deve então 
#informar o valor total a ser pago e o valor do troco que você vai receber.

valor_item = int(input())
qtd_compra = int(input())
meu_valor = int(input())
valor = valor_item*qtd_compra
troco = meu_valor-valor
print("A pagar: {}\n Troco: {}".format(valor, troco))


#Escreva um programa que leia a distância entre duas cidades A e B, em kilômetros, a velocidade, em km/h, 
#do carro e mostre qual o tempo da viagem entre A e B, no formato HH:MM. Os segundos devem ser desprezados.

distancia = int(input())
vel = int(input())
horas = (distancia//vel)
minutos = int(((distancia/vel) - horas) * 60)
tempo_viagem = print(horas,minutos,sep=":")


#Escreva um programa que calcule a quantidade de postes a serem colocados em uma rua. O programa deve ler a
#distância do início ao fim da rua, em quilômetros, e a distância entre dois (2) postes, em metros. Seu programa deve
#mostrar a quantidade de postes e a distância entre os dois últimos postes. Lembre-se que há sempre um poste no início 
#da rua e outro no final. A distância entre cada par de postes é o valor, em metros, lido pelo programa, com exceção
#da distância entre os dois últimos postes da rua.

from math import ceil
dist_rua = int(input())*1000
entre_postes = int(input())
qtd_postes = dist_rua/entre_postes + 1
qtd_postes1 = ceil(qtd_postes)
ult_postes = dist_rua%entre_postes
print("{} poste(s)\n{} metro(s)".format(qtd_postes1, ult_postes))
