import time
import math

def metodo_householder(matriz_a, matriz_v, num_linhas, num_colunas):
    for i in range(num_colunas):
        # Define matriz_v[i] como um subvetor matriz_a[i][i:num_linhas]
        for j in range(num_linhas - i):
            matriz_v[i][j] = matriz_a[i][i + j]

        # Soma dos quadrados restantes de matriz_v[i]
        soma_quadrados_restantes_v = sum(matriz_v[i][j] ** 2 for j in range(1, num_linhas - i))

        # Define matriz_v[i][0] como matriz_v[i][0] + sinal(matriz_v[i][0]) * ||matriz_v[i]||
        norma_v = math.sqrt(matriz_v[i][0] ** 2 + soma_quadrados_restantes_v)
        matriz_v[i][0] += norma_v if matriz_v[i][0] >= 0 else -norma_v

        # Normaliza matriz_v[i]
        norma_v = math.sqrt(matriz_v[i][0] ** 2 + soma_quadrados_restantes_v)
        for j in range(num_linhas - i):
            matriz_v[i][j] /= norma_v

        for j in range(i, num_colunas):
            # Atualiza matriz_a[j][i:num_linhas] = matriz_a[j][i:num_linhas] - 2 * (matriz_v[i]^T matriz_a[j][i:num_linhas]) * matriz_v[i]
            produto_interno_v_a = sum(matriz_v[i][k] * matriz_a[j][i + k] for k in range(num_linhas - i))
            produto_interno_v_a *= 2
            for k in range(num_linhas - i):
                matriz_a[j][i + k] -= produto_interno_v_a * matriz_v[i][k]

def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print("{:9.6g}".format(elemento), end=" ")
        print()

if __name__ == "__main__":
    MarcacoesTempo = [0, 0]
    MarcacoesTempo[0] = time.time()

    # Matriz exemplo fornecida
    matriz_utilizada = [
        [23.4522, 3.2982, 67.8308],
        [730.2251, 2.8308, 55.1269],
        [67.8308, 0.1269, 59.8605]
    ]

    num_linhas = len(matriz_utilizada)
    num_colunas = len(matriz_utilizada[0])

    # Alocar memória para matriz_a e as matrizes_v
    matriz_a = [[0.0] * num_linhas for _ in range(num_colunas)]
    matriz_v = [[0.0] * (num_linhas - i) for i in range(num_colunas)]

    # Inicializar os valores na matriz_a
    for i in range(num_colunas):
        for j in range(num_linhas):
            matriz_a[i][j] = matriz_utilizada[i][j]

    # Chama o método Householder
    metodo_householder(matriz_a, matriz_v, num_linhas, num_colunas)

    # Imprimir a matriz resultado formatada
    print("Matriz Resultado:")
    imprimir_matriz(matriz_a)

    # Liberar memória
    MarcacoesTempo[1] = time.time()
    Tempo = (MarcacoesTempo[1] - MarcacoesTempo[0]) * 1000.0
    print("Tempo gasto: {:.4f} ms.".format(Tempo))