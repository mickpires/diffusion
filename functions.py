import numpy as np
# aqui eu montei a matriz dos coeficientes
class Implicito:
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
            if i == num_pontos-1:
                matriz_ampliada[i] = variavel[i] + λ*contorno[1]
                break
            matriz_ampliada[i] = variavel[i]
        
        return matriz_ampliada
    
class CrankNicolson:
    def gerarMatrizCoeficientes(num_pontos,λ):
        matriz_coeficiente = np.zeros((num_pontos,num_pontos),dtype=float)
        a  = 2*(1 + λ)
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
                matriz_ampliada[i] = λ*(variavel[i+1] + 2*contorno[0]) + 2*(1-λ)*variavel[i]
                continue
            if i == num_pontos-1:
                matriz_ampliada[i] = λ*(variavel[i-1] + 2*contorno[1]) + 2*(1-λ)*variavel[i]
                break
            matriz_ampliada[i] = λ*(variavel[i+1] +variavel[i-1]) + 2*(1-λ)*variavel[i]
        return matriz_ampliada