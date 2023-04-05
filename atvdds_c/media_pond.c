//Escreva um programa para calcular a média de uma disciplina que possui duas notas, com pesos 2 e 3 respectivamente, 
//considerando as notas valores inteiros entre 0 (zero) e 100 (cem), inclusive.

#include <stdio.h>
 
int main() {
  int a;
  int b;
  int media;
  scanf("%d", &a);
  scanf("%d", &b);
  media = (a * 2 + b * 3)/5;
  printf("%d", media);
}
