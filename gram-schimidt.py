import time

def metodo_gram_schmidt(matriz_utilizada):
    num_vetor = len(matriz_utilizada)
    tam_vetor = len(matriz_utilizada[0])

    vetores_ortogonalizados = [vetor[:] for vetor in matriz_utilizada]

    for i in range(num_vetor):
        for j in range(i):
            produto_escalar = sum(vetores_ortogonalizados[j][k] * matriz_utilizada[i][k] for k in range(tam_vetor))
            norma = sum(vetores_ortogonalizados[j][k] ** 2 for k in range(tam_vetor))
            escalar = produto_escalar / norma

            for k in range(tam_vetor):
                vetores_ortogonalizados[i][k] -= escalar * vetores_ortogonalizados[j][k]

    print("Vetores ortogonalizados:")
    for i in range(num_vetor):
        for j in range(tam_vetor):
            print(vetores_ortogonalizados[i][j], end=" ")
        print()

if __name__ == "__main__":
    start_time = time.time()
    matriz_utilizada = [
        [23.4522, 3.2982, 67.8308],
        [730.2251, 2.8308, 55.1269],
        [67.8308, 0.1269, 59.8605]
    ]
    
    metodo_gram_schmidt(matriz_utilizada)
    end_time = time.time()

    tempo_gasto = (end_time - start_time) * 1000.0
    print(f"Tempo gasto: {tempo_gasto:.4f} ms.")
