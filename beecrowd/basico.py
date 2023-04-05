#1921 - Guilherme e suas pipas

n = int(input())
b = ((n-3) * n)//2
print(b)


#2413 - Busca na Internet

t = int(input())
t2 = t*2
t1 = t2*2
print(t1)


#2416 - Corrida

c, n = map(int,input().split())
resto = c%n
print(resto)


#1930 - Tomada

t1, t2, t3, t4 = map(int,input().split())
soma = t1 + t2 + t3 + t4 - 3
print(soma)


#1959 - Polígonos Regulares Simples

n, l = map(int, input().split())
p = n*l
print(p)


#1019 - Conversão de Tempo

t_evento = int(input())
horas = t_evento//3600
mins = (t_evento%3600)//60
segs = (t_evento%3600)%60
print("{}:{}:{}".format(horas,mins,segs))


#1963 - O filme

a, b = map(float,input().split())
c = b - a
x = (100 * c)/a
print("{:.2f}".format(x),"%",sep="")


#2234 - Cachorros-quentes

h, p = map(int,input().split())
calc = h/p
print("{:.2f}".format(calc))


#2374 - PNEU

n = int(input())
m = int(input())
pressao = n - m
print(pressao)


#1020 - Idade em Dias

a = int(input())
ano = a//365
mes = (a%365)//30
dias = (a%365)%30
print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(ano,mes,dias))


#2377 - Pedágio

l, d = map(int,input().split())
k, p = map(int,input().split())
km = k * l
pedagios = l//d
custo_p = pedagios * p
custo_t = custo_p + km
print(custo_t)


#2395 - Transporte de Contêineres

a, b, c = map(int,input().split())
x, y, z = map(int,input().split())
tudo = (x//a) * (z//c) * (y//b) 
print(tudo)


#2786 - Piso da Escola

l = int(input())
c = int(input())
a = l*c
q1 = a + (l - 1) * (c - 1)
q2 = (c - 1) * 2 + (l - 1) * 2
print(q1)
print(q2)


#1008 - Salário

number = int(input())
hours = int(input())
value_h = float(input())
salary = hours * value_h
print("NUMBER = {}\nSALARY = U$ {:.2f}".format(number,salary))


#1010 - Cálculo simples

x, y, z = map(float,input().split())
a, b, c = map(float,input().split())
value1 = y * z
value2 = b * c
soma = value1 + value2
print("VALOR A PAGAR: R$ {:.02f}".format(soma))


#1011 - Esfera

R = int(input())
vol = (4.0/3) * 3.14159 * (R**3)
print("VOLUME = {:.3f}".format(vol))


#1014 - Consumo

dist = int(input())
gas = float(input())
gasto = dist / gas
print("{:.3f}".format(gasto),"km/l")


#1017 - Gasto de Combustível

tempo = int(input())
vel = int(input())
calc = (tempo * vel) / 12
print("{:.3f}".format(calc))


#1018 - Cédulas

a = int(input())
print(a)
print('{} nota(s) de R$ 100,00'.format(a//100))
a = a - (a//100)*100
print('{} nota(s) de R$ 50,00'.format(a//50))
a = a - (a//50)*50
print('{} nota(s) de R$ 20,00'.format(a//20))
a = a - (a//20)*20
print('{} nota(s) de R$ 10,00'.format(a//10))
a = a - (a//10)*10
print('{} nota(s) de R$ 5,00'.format(a//5))
a = a - (a//5)*5
print('{} nota(s) de R$ 2,00'.format(a//2))
a = a - (a//2)*2
print('{} nota(s) de R$ 1,00'.format(a//1))


#1021 - Notas e Moedas

valor = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
  qt_notas = int(valor / nota)
  print('{} nota(s) de R$ {:.2f}'.format(qt_notas, nota))
  valor -= qt_notas * nota

print('MOEDAS:')
for moeda in moedas:
  valor = round(valor, 2)
  qt_moedas = int(valor / moeda)
  print('{} moeda(s) de R$ {:.2f}'.format(qt_moedas, moeda))
  valor -= qt_moedas * moeda
