//Escreva um programa que leia dois valores L1 e L2, que representam os lados de um retângulo e mostre o perímetro do mesmo.

#include <stdio.h>
 
int main() {
  long long int a;
  long long int b;
  long long int p;
  scanf("%lld", &a);
  scanf("%lld", &b);
  p = (a + b) * 2;
  printf("%lld", p);
}
