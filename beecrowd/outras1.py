#1001 - Extremamente Básico

def f(a,b):
  x = a + b
  return x

a = int(input())
b = int(input())
print("X = {}".format(f(a,b)))


#1002 - Área do Círculo

def f(r):
  area = 3.14159 * (r**2)
  return area

r = float(input())
print("A={:.4f}".format(f(r)))


#1005 - Média 1

def f(a,b):
  media = (a * 3.5 + b * 7.5)/11
  return media

a = float(input())
b = float(input())
print("MEDIA = {:.5f}".format(f(a,b)))


#1013 - O Maior

a, b, c = map(int,input().split())

maior = a
if b > maior and b > c:
  print("{} eh o maior".format(b))
elif c > maior and c > b:
  print("{} eh o maior".format(c))
else:
  print("{} eh o maior".format(a))


#1012 - Área

def f1(a,c):
  areatri = (a * c)/2
  return areatri

def f2(a):
  areaci = 3.14159 * (a**2)
  return areaci

def f3(a,b,c):
  areatra = ((a + b) * c)/2
  return areatra

def f4(a):
  areaqua = a**2
  return areaqua

def f5(a,b):
  arearet = a * b
  return arearet

a, b, c = map(float,input().split())

print("TRIANGULO: {:.3f}".format(f1(a,c)))
print("CIRCULO: {:.3f}".format(f2(c)))
print("TRAPEZIO: {:.3f}".format(f3(a,b,c)))
print("QUADRADO: {:.3f}".format(f4(b)))
print("RETANGULO: {:.3f}".format(f5(a,b)))
