//Escreva um programa que leia dois números inteiros a e b e mostre a soma dos mesmos.

#include <stdio.h>
 
int soma(int a, int b) {
  int r;
  r = a + b;
  return r;
}
 
int main() {
  int a, b, s;
  scanf("%d", &a);
  scanf("%d", &b);
  s = soma(a, b);
  printf("%d\n", s);
  return 0;
}
