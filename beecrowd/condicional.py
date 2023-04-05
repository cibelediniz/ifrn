#2006 - Identificando o Chá

n1 = int(input())
n2 = list(map(int, input().split()))
print(n2.count(n1))


#1044 - Múltiplos

a, b = map(int,input().split())
if b%a == 0 or a%b == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")


#1046 - Tempo de Jogo

a, b = map(int,input().split())
duracao = 24 - (24 + a - b)%24
if a == b:
    print("O JOGO DUROU 24 HORA(S)")
else:
    print("O JOGO DUROU {} HORA(S)".format(duracao))


#1794 - Lavanderia

n = int(input())
la, lb = map(int,input().split())
sa, sb = map(int,input().split())
if n >= la and n >= sa and n <= lb and n <= sb:
    print("possivel")
else:
    print ("impossivel")


#2235 - Andando no Tempo

a, b, c = map(int,input().split())
if a + b == c or a + c == b or b + c == a:
    print("S")
elif a == b or a == c or b == c:
  print("S")
else:
  print("N")


#1893 - Fases da Lua

a, b = map(int,input().split())
if a >= 0 and b <= 2:
  print("nova")
elif b > a and b <= 96:
  print("crescente")
elif a >= b and b <= 96:
  print("minguante")
else:
  print("cheia")


#1038 - Lanche

a, c = map(float,input().split())
if a == 1:
  b = 4.0
elif a == 2:
  b = 4.5
elif a == 3:
  b = 5.0
elif a == 4:
  b = 2.0
elif a == 5:
  b = 1.5
total = b * c
print("Total: R$ {:.2f}".format(total))


#1040 - Média 3

a, b, c, d = map(float,input().split())
media = ((a*2) + (b*3) + (c*4) + (d*1))/10
print("Media: {:.1f}".format(media))
if media >= 7:
  print("Aluno aprovado.")
elif media < 5:
  print("Aluno reprovado.")
elif media >= 5 and media <= 6.9:
  print("Aluno em exame.")
  e = float(input())
  media2 = (e + media)/2
  print("Nota do exame: {:.1f}".format(e))
  if media2 >= 5:
    print("Aluno aprovado.\nMedia final: {:.1f}".format(media2))
  elif media2 < 5:
    print("Aluno reprovado.\nMedia final: {:.1f}".format(media2))


#1041 - Coordenadas de um Ponto

x, y = map(float,input().split())
if x == 0 and y == 0:
  print("Origem")
elif x > 0 and y > 0:
  print("Q1")
elif x < 0 and y > 0:
  print("Q2")
elif x < 0 and y < 0:
  print("Q3")
elif x > 0 and y < 0:
  print("Q4")
elif x == 0:
  print("Eixo Y")
elif y == 0:
  print("Eixo X")


#1042 - Sort Simples

a, b, c = map(int,input().split())
if a > b and a > c:
    d = a
    if b > c:
        e = b
        f = c
    else:
        e = c
        f = b
if b > a and b > c:
    d = b
    if a > c:
        e = a
        f = c
    else:
        e = c
        f = a
if c > a and c > b:
    d = c
    if a > b:
        e = a
        f = b
    else:
        f = a
        e = b
print("{}\n{}\n{}\n".format(f,e,d))
print("{}\n{}\n{}".format(a,b,c))


#2369 - Conta de Água

n = int(input())
basico = 7
if n <= 10:
    print(basico)
elif n >= 11 and n <= 30:
    x = n - 10
    print(basico + x)
elif n >= 31 and n <= 100:
    x = n - 30
    print(basico + 20 + (2 * x))
elif n >= 101:
    x = n - 100
    print(basico + 20 + 140 + (5 * x))


#2295 - Frota de Táxi

pa, pg, ra, rg = map(float,input().split())
if ra/pa < rg/pg:
	print("G")
elif rg/pg < ra/pa:
	print("A")
elif rg/pg == ra/pa:
	print("G")


#1929 - Triângulo

a, b, c, d = map(int,input().split())
if a + b > c and b + c > a and a + c > b:
    print("S")
elif b + c > d and c + d > b and b + d > c:
    print("S")
elif a + c > d and c + d > a and a + d > c:
    print("S")
elif a + b > d and b + d > a and a + d > b:
    print("S")
else:
    print("N")
 

#2424 - Tira-teima

x, y = map(int,input().split())
if x <= 432 and y <= 468 and x >= 0 and y >= 0:
    print("dentro")
else:
    print("fora")


#2375 - Sedex

n = int(input())
a, l, p = map(int,input().split())
if n <= a and n <= l and n <= p:
    print("S")
else:
    print("N")


#2397 - Triângulos

listatri = list(map(int,input().split()))
listaord = sorted(listatri)
if listaord[0] + listaord[1] > listaord[2]:
    if listaord[2]**2 == listaord[1]**2 + listaord[0]**2:
        print("r")
    elif listaord[2]**2 > listaord[1]**2 + listaord[0]**2:
        print("o")
    elif listaord[2]**2 < listaord[1]**2 + listaord[0]**2:
        print("a")
else:
    print("n")


2454 - Flíper

p, r = map(int,input().split())
if p == 0 and r == 0:
    print("C")
elif p == 0 and r == 1:
    print("C")
elif p == 1 and r == 0:
    print("B")
else:
    print("A")


#2409 - Colchão

a, b, c = map(int, input().split())
h, l = map(int, input().split())
if a <= h and b <= l or a <= h and c <= l:
  print("S")
elif b <= h and a <= l or b <= h and c <= l:
  print("S")
elif c <= h and a <= l or c <= h and b <= l:
  print("S")
else:
  print("N")


#2455 - Gangorra

p1, c1, p2, c2 = map(int,input().split())
if p1 * c1 == p2 * c2:
    print(0)
elif p1 * c1 > p2 * c2:
    print(-1)
elif p1 * c1 < p2 * c2:
    print(1)
    
    
#1035 - Teste de Seleção 1

a, b, c, d = map(int,input().split())
if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a%2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")


#2787 - Xadrez

l = int(input())
c = int(input())
if (l%2 == c%2):
    print("1")
else:
    print("0")


#2780 - Basquete de Robôs

a = int(input())
if a <= 800:
    print(1)
elif a > 800 and a <= 1400:
    print(2)
elif a > 1400 and a <= 2000:
    print(3)


#2717 - Tempo do Duende

n = int(input())
a, b = map(int,input().split())
x = a + b
if x > n:
    print("Deixa para amanha!")
elif x <= n:
    print("Farei hoje!")


#2679 - Sucessor Par

n = int(input())
if n%2 == 0:
    print(n+2)
else:
    print(n+1)
   
   
#2437 - Distância de Manhattan

xm, ym, xr, yr = map(int,input().split())
if xm > xr:
    if ym > yr:
        dist = (xm - xr) + (ym - yr)
    elif yr > ym:
        dist = (xm - xr) + (yr - ym)
    elif yr == ym:
        dist = (xm - xr)

elif xm < xr:
    if ym > yr:
        dist = (xr - xm) + (ym - yr)
    elif yr > ym:
        dist = (xr - xm) + (yr - ym)
    elif yr == ym:
        dist = (xr - xm)

elif xm == xr:
    if ym > yr:
        dist = (ym - yr)
    elif yr > ym:
        dist =(yr - ym)
print(dist)


#2670 - Máquina de Café

piso1 = int(input())
piso2 = int(input())
piso3 = int(input())

t1 = piso2 * 2 + piso3 * 4
t2 = piso1 * 2 + piso3 * 2
t3 = piso1 * 4 + piso2 * 2

if t1 <= t2 and t1 <= t3:
    print(t1)
elif t2 <= t1 and t2 <= t3:
    print(t2)
elif t3 <= t1 and t3 <= t2:
    print(t3)


#2702 - Escolha Difícil

a, b, c = map(int,input().split()) #refeiçoes disponiveis
d, e, f = map(int,input().split()) #refeiçoes requisitadas
frango = d - a
bife = e - b
massa = f - c
if d > a and e <= b and f <=c:
    print(frango)
elif e > b and d <= a and f <= c:
    print(bife)
elif f > c and d <=a and e <= b:
    print(massa)
elif f > c and d > a and e <= b:
    print(massa + frango)
elif f <= c and d > a and e > b:
    print(frango + bife)
elif f > c and d <= a and e > b:
    print(massa + bife)
elif f > c and d > a and e > b:
    print(massa + bife + frango)
else:
    print("0")


#1051 - Imposto de Renda

a = float(input())
if a >= 0 and a <= 2000:
    print("Isento")

elif a >= 2000.01 and a <= 3000:
    valor = a - 2000
    i = (valor * 8)/100
    print("R$ {:.2f}".format(i))

elif a >= 3000.01 and a <= 4500:
    valor2 = a - 3000
    valor = a - 2000 - valor2
    i = (valor * 8)/100
    i2 = (valor2 * 18)/100
    print("R$ {:.2f}".format(i + i2))

elif a > 4500:
    valor3 = a - 4500
    valor2 = a - 3000 - valor3
    valor = a - 2000 - valor2 - valor3
    i = (valor * 8)/100
    i2 = (valor2 * 18)/100
    i3 = (valor3 * 28)/100
    print("R$ {:.2f}".format(i + i2 + i3))


#1048 - Aumento de Salário

a = float(input())
if a >= 0 and a <= 400:
    novo = ((a*15)/100) + a
    reajuste = novo - a
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 15 %".format(novo, reajuste))

elif a >= 400.01 and a <= 800:
    novo = ((a * 12)/100) + a
    reajuste = novo - a
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 12 %".format(novo, reajuste))

elif a >= 800.01 and a <= 1200:
    novo = ((a * 10)/100) + a
    reajuste = novo - a
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 10 %".format(novo, reajuste))

elif a >= 1200.01 and a <= 2000:
    novo = ((a * 7)/100) + a
    reajuste = novo - a
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 7 %".format(novo, reajuste))

elif a > 2000:
    novo = ((a * 4)/100) + a
    reajuste = novo - a
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 4 %".format(novo, reajuste))


#1037 - Intervalo

a = float(input())
if a >=0 and a <= 25.00:
  print("Intervalo [0,25]")

elif a >= 25 and a <= 50:
  print("Intervalo (25,50]")

elif a >= 50 and a <= 75:
  print("Intervalo (50,75]")

elif a >= 75 and a <= 100:
  print("Intervalo (75,100]")

else:
  print("Fora de intervalo")
