//Para se preparar para os outros problemas, vamos fazer um teste. Dado um número X, retorne o menor número par maior do que X.

#include <stdio.h>
 
int main() {
  int x,s_par;
  scanf("%d",&x);
  if (x%2==0){
    s_par = x+2;
  } else {
    s_par = x+1;
  }
  printf("%d\n",s_par);
 
  return 0;
}
