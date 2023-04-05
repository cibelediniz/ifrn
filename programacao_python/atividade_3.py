#Escreva um programa que leia um número inteiro, que corresponde a uma sequencia de chamada em uma
#fila de espera, e mostre a mensagem Proximo: 001, onde o número deve ser mostrado com 3 algarismos, 
#preenchido com zeros à esquerda.

x = int(input())
seq = "{:03d}".format(x)
print("Próximo:",(seq))


#Escreva um programa que calcule o valor de um salário após um reajuste. O programa deve ler da 
#entrada padrão o valor atual do salário mínimo percentual de reajuste, também um número real. O programa deve
#calcular o percentual do novo valor do salário e mostrar o valor atual e o novo valor após o reajuste.

salario = float(input())
reajuste = float(input())
regra3 = salario * reajuste
regra3_2 = regra3/100
novo = salario + regra3_2
novo1 = "{:.02f}".format(novo)
print("Atual: {}\n Novo: {}".format(salario, novo1))


#Escreva um programa que leia o raio de um círculo e mostre a área da circunferência do mesmo, com
#exatamente 4 casas decimais. Considere o valor de π = 3.14159

raio = float(input())
pi = 3.14159
circunf = pi * raio * raio
print("{:.4f}".format(circunf))


#Escreva um programa que leia o valor final de venda de um automóvel e calcule seu preço sem
#impostos, os valores pagos para cada tipo de imposto e imprima os resultados. Considere que, para automóveis populares,
#o ICMS (Imposto sobre Circulação de Mercadorias e Serviços) é de 18%; o IPI (Imposto sobre Produtos Industrializados) é
#de 13%; o PIS (Programa de Integração Social) é de 1,4%; e a Cofins (Contribuição para o Financiamento da Seguridade
#Social) é de 7,6%. Todos os impostos são calculados sobre o valor de custo do automóvel. Todos os valores devem ser
#mostrados com 2 (duas) casas decimais.

valor0 = float(input())
regra3 = valor0 * 40
valor_imps = regra3/140
v_sem = valor0 - valor_imps
icms = valor0 * 18/140
ipi = valor0 * 13/140
pis = valor0 * 1.4/140
cofins = valor0 * 7.6/140
print("ICMS: {}\n IPI: {}\n PIS: {}\n Cofins: {}\n Valor sem impostos: {}".format(icms, ipi, pis, cofins, v_sem))
