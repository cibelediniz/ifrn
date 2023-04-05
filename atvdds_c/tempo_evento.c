//Escreva um programa que leia a hora de início e de fim de um evento e mostre o tempo do evento no formato "HH:MM".
//A hora de início e fim é dada em minutos desde o início do dia.

#include <stdio.h>
 
int main() {
  int inicio;
  int fim;
  int tempo;
  int horas;
  int min;
  scanf("%d", &inicio);
  scanf("%d", &fim);
      tempo = fim - inicio;
      horas = tempo/60;
      min = tempo%60;
     if (horas <= 10){
      printf("0");
      }
  printf("%d", horas);
  printf(":");
  printf("%d", min);
}
