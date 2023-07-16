import numpy as np
# aqui eu montei a matriz dos coeficientes
def gerarMatrizCoeficientes(num_pontos,λ):
    matriz_coeficiente = np.zeros((num_pontos,num_pontos),dtype=float)
    a  = 1 + 2*λ
    b = -λ
    row, column = matriz_coeficiente.shape
    for i in range(row):
        for j in range(column):
            if i == j:
                matriz_coeficiente[i][j] = a
                if i != 0:
                    matriz_coeficiente[i][j-1] = b
                try:
                    matriz_coeficiente[i][j+1] = b
                except IndexError:
                    pass
    return matriz_coeficiente

def gerarMatrizAmpliada(num_pontos,contorno,variavel,λ):
    matriz_ampliada = np.zeros((num_pontos,1),dtype=float)
    for i in range(num_pontos):
        if i == 0:
            matriz_ampliada[i] = variavel[i] + λ*contorno[0]
            continue
        matriz_ampliada[i] = variavel[i]
        if i == num_pontos-1:
            matriz_ampliada[i] = variavel[i] + λ*contorno[1]
    
    return matriz_ampliada
