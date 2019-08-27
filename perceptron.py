import matplotlib.pyplot as plt
import random
import numpy as np


def act_fun(val):
    return 1 if val > 0 else 0


entradas = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
D = [0, 0, 0, 1]

umbral = 1.5
etha = 0.5
peso1 = random.uniform(-1, 1)
peso2 = random.uniform(-1, 1)
print(peso1, peso2)
errors = [False, False, False, False]
salidas = [0, 0, 0, 0]
converge = False
idx = 0
while False in errors:  # until converge
    # val = np.dot([peso1, peso2], entradas[idx])
    prod_punto = entradas[idx][0]*peso1 + entradas[idx][1]*peso2 - umbral
    print("El resultado del producto punto es: ", prod_punto)
    y = act_fun(prod_punto)
    salidas[idx] = y

    print("Deseado: ", D[idx])
    print("Obtenido: ", y)
    error = D[idx] - y
    if error != 0:
        print("Recalculando pesos...")
        peso1 = peso1 + error * entradas[idx][0]
        peso2 = peso2 + error * entradas[idx][1]
        umbral = umbral + etha*error
        print(peso1, peso2, umbral)
        errors[idx] = False
    else:
        errors[idx] = True
    idx += 1
    if idx >= len(entradas):
        m = peso1/peso2
        b = umbral / peso2
        graph = [[x + 0, b - x*m]for x in D]
        print(y)
        print(graph)
        for entrada, step in zip(entradas, D):
            plt.scatter(entrada[0], entrada[1],
                        color="blue" if step else "red")
        plt.plot(graph[0], graph[3])
        idx = 0

print("Entrenamiento terminado, se obtuvo: ", salidas)


plt.show()
