//Escreva um programa que leia dois números reais a e b e mostre a média entre os dois.

#include <stdio.h>
 
int main() {
  float a;
  float b;
  float media;
  scanf("%f", &a);
  scanf("%f", &b);
  media = (a + b)/2;
  printf("%f", media);
}
