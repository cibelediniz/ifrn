// Escreva um programa que leia um número natural n e informe se o mesmo é primo.

#include <stdio.h>
 
    int main(){
        int n, aux, primo = 1;
        scanf("%d", &n);
        
        for (aux = 2; aux <= n/2; aux++)
            if ((n % aux) == 0)
                primo = 0;
            if (n == 1)
                primo = 0;
        
        if (primo)
            printf("Sim\n");
        else
            printf("Nao\n");
        return 0;
}
