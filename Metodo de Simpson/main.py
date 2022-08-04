#Criacao da funcao que funciona como f(x)
def func(x):
    from math import sqrt, exp, sin ,log
    #f = exp(x)
    #f = 4/(pow(x,2)+1)
    f =  pow(x, 2)+1
    return f
#Criacao do algoritmo
def simpson(a, b, n):
    h = (b-a)/n
    x = []
    #Definicao do primeiro primeiro ponto depois de a
    pm = a+h
    #Lista "geral" de itens
    x.append(round(pm, 1))
    #Lista de itens em posicoes impares
    x_impar = []
    #Lista de itens em posicoes pares
    x_par = []
    #somatorio da lista de itens pares na funcao
    soma_par = 0
    #somatorio da lista de itens impares na funcao
    soma_impar = 0
    #Resultado da integral numérica
    result = 0
    count = 0
    #Insere os itens na lista geral
    for i in range(1, n-1, 1):
        x.append(x[i-1]+h)
    #Insere os itens nas posicoes impares na lista de itens impares
    for i in range(0, n-1, 2):
        x_impar.append(x[i])
        soma_impar += func(x_impar[count])
        count += 1
    count = 0
    #Insere os itens nas posicoes pares na lista de itens pares
    for i in range(1, n-1, 2):
        x_par.append(x[i])
        soma_par += func(x_par[count])
        count += 1
    #Formula
    result = (h/3)*(func(a)+2*(soma_par)+4*(soma_impar)+func(b))

    print('resultado =', result)

simpson(0, 1, 1000)