//Escreva um programa que leia dois números inteiros a e b e mostre o MDC (Máximo Divisor Comum) entre a e b.

#include <stdio.h>
 
int main() {
    int m, n, aux;
    scanf("%d %d", &m, &n);
    while (n > 0) {
        aux = n;
        n = m % n;
        m = aux;
    }
 
    printf("%d\n", m);
    return 0;
}
