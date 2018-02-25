import matplotlib.pyplot as plt
import numpy as np
from random import randint
from sys import exit


# Entrada do conjunto de pontos
# Entrada da função fi(x) a ser ajustada
from exemplo3 import *
QTD_PONTOS = len(pontos[0])


# Criando a matriz
QTD_G = len(G)
matriz = []
vetor  = []
for linha in range(QTD_G):
    linha = [0]*QTD_G
    matriz.append(linha)
    vetor.append([0])


# Aplicação do Método dos Mínimos Quadrados
for linha in range(QTD_G):
    for coluna in range(QTD_G):
        ''' matriz[linha][coluna] = "∑fi_"+str(coluna)+"(Xi)*fi_"+str(linha)+"(Xi)" '''
        somatorio = 0.0
        for X in range(QTD_PONTOS):
            somatorio += G[coluna](pontos[0][X]) * G[linha](pontos[0][X])
        matriz[linha][coluna] = somatorio
    ''' vetor[linha] = "∑f(Xi)*fi_"+str(linha)+"(Xi)" '''
    somatorio=0.0
    for X in range(QTD_PONTOS):
        somatorio += pontos[1][X] * G[linha](pontos[0][X])
    vetor[linha] = somatorio

# Imprimindo a matriz
for linha in range(QTD_G):
    print(str(matriz[linha])+" "+str(vetor[linha]))





##############################################
# Aplicação do Método de Eliminação de Gauss #
##############################################
n= QTD_G
qtd_linhas = n
qtd_colunas = n

for pivo in range(n-1): #Percorre os pivôs
    # print ("\nAnalisando o pivo: "+ str(pivo))

    # Pivoteamento
    linha_do_maior_elemento = pivo # indice da linha do maior elemento no momento
    for elemento in range(pivo+1,qtd_linhas): # Encontra linha para troca
        if abs(matriz[elemento][pivo]) > abs(matriz[linha_do_maior_elemento][pivo]):
            linha_do_maior_elemento = elemento # Atualiza com o indice da linha do maior elemento no momento

    # print("\tA linha do maior |elemento| é: "+str(linha_do_maior_elemento))

    # print("\n\tEstado Atual")
    # print("\t"+"Matriz "+str(matriz))
    # print("\t"+"Vetor "+str(vetor))

    # Encontrou o maior elemento, agora temos que trocas as qtd_linhas
    if abs(matriz[pivo][pivo]) != abs(matriz[linha_do_maior_elemento][pivo]): # Se precisa trocar linha
        linha_aux = matriz[pivo].copy()
        var_aux = vetor[pivo]
        matriz[pivo] = matriz[linha_do_maior_elemento]
        vetor[pivo] = vetor[linha_do_maior_elemento]
        matriz[linha_do_maior_elemento] = linha_aux
        vetor[linha_do_maior_elemento] = var_aux

        # print("\n\tDepois da troca de linha")
        # print("\t"+"Matriz "+str(matriz))
        # print("\t"+"Vetor "+str(vetor))
    # else:
        # print('\n\tNão precisa de troca de linha')


    # print("\n\tZerando elementos abaixo do pivô "+ str(pivo)+"...")

    for linha in range((pivo+1), qtd_linhas): # Percorre as linhas
        m = matriz[linha][pivo] / matriz[pivo][pivo]
        for k in range(pivo, n):
            matriz[linha][k] = matriz[linha][k] - m * matriz[pivo][k]
        vetor[linha] = vetor[linha] - m * vetor[pivo]


# print("\nMatriz Triangular Superior:")
# print("\t"+"Matriz "+str(matriz))
# print("\t"+"Vetor "+str(vetor))


#alterar esses testes

# Verificando a qtd de soluções
# if matriz[qtd_linhas-1][qtd_colunas-1] != 0:
#     print("\n\tSistema com solução única.")
# else:
#     if vetor[qtd_colunas-1] == 0:
#         print("\n\tSistema com infinitas soluções.")
#     else:
#         print("\n\tSistema com nenhuma solução.")
#     exit(0) # Encerra o programa


# Resolvendo o sistema (Retrosubstituição)
vetor_solucao = np.zeros((qtd_colunas))

vetor_solucao[n-1] = vetor[qtd_linhas-1] / matriz[qtd_linhas-1][qtd_colunas-1]

for linha in range(qtd_linhas-1-1, -1, -1): # Laço para as variáveis
    # print ("linha =" +str(linha))
    acumulador = 0
    for coluna in range(linha+1, n):
        # print ("coluna =" +str(coluna))
        acumulador = acumulador + matriz[linha][coluna] * vetor_solucao[coluna]
    vetor_solucao[linha] = (vetor[linha]-acumulador) / matriz[linha][linha]

print("\nVetor solução = "+str(vetor_solucao))
#######################################
# Fim da Aplicação do Método de Gauss #
#######################################


# Recebo os valores de a1, a2, a3, ... ; Substituo na equação fi(x) e ploto o polinômio
espaco = 1.3
ponto_a = pontos[0][0]*espaco
ponto_b = pontos[0][-1]*espaco
n_pontos = 1000
# Cria n_pontos igualmente espaçados no intervalo [ponto_a,ponto_b]
x = np.linspace(ponto_a, ponto_b, n_pontos)

fi_x = 0
for variavel in range(QTD_G):
    fi_x += vetor_solucao[variavel] * G[variavel](x)

''' fi_x = a1 * g1(x) + a2 * g2(x) + a3 * g13(x) + ... + an * gn(x) '''

fig, ax = plt.subplots()
ax.plot(x, fi_x, color='green')
ax.scatter(pontos[0],pontos[1])

plt.show()
