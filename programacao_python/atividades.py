#LISTA ORDENADA
print("Escreva uma função recursiva que verifique se uma lista de números inteiros está ordenada.")

def listord(l):
  if len(l) == 1 or len(l) == 0:
    return True
  return l[0] <= l[1] and listord(l[1:])
  
lista = list(map(int,input().split()))
if listord(lista):
  print("Ordenada")
else:
  print("Não ordenada")


#FATORES PRIMOS
print("Escreva uma função recursiva que receba um número inteiro e retorne uma lista com os fatores primos de n:")

def fatora_r(n, d):
  if n == d: return [n]
  if n % d == 0: 
    n = n//d
    divisores = fatora_r(n, d)
    divisores.append(d)
    return divisores
  else: return fatora_r(n, d+1)

def fatora(n):
  return fatora_r(n, 2)

n = int(input())
fatores = fatora(n)[::-1]
mul = "x".join(map(str, fatores)) #bota um x em vez dos espaços
print(f"{n}={mul}")
