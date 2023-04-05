//Escreva um programa que leia um número inteiro n e mostre os divisores de n, incluindo ele mesmo.

#include <stdio.h>
 
int main() {
  int n,i;
  scanf("%d",&n);
  i=0;
  while (i<=n){
    if (n%++i==0){
      printf("%d ",i);
    }
  }
  printf("\n");
 
  return 0;
}
