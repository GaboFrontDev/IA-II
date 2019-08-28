import matplotlib.pyplot as plt
import random
import numpy as np


def act_fun(val):
    return 1 if val > 0 else 0


entradas = [
    [0, 0],
    [1, 0],
    [0, 1],
    [1, 1]
]
D = [0, 0, 0, 1]
# D = [0, 1, 1, 1]

umbral = 0
etha = 0.01
peso1 = random.uniform(-1, 1)
peso2 = random.uniform(-1, 1)
did_error = [True, True, True, True]
salidas = [0, 1, 1, 0]
idx = 0


while True in did_error:  # until converge
    prod_punto = (entradas[idx][0]*peso1 + entradas[idx][1]*peso2) + umbral
    y = act_fun(prod_punto)
    salidas[idx] = y
    error = D[idx] - y
    if error != 0:
        print("Recalculando pesos...")
        peso1 = peso1 + etha * error * entradas[idx][0]
        peso2 = peso2 + etha * error * entradas[idx][1]
        umbral = umbral + etha*error
        did_error[idx] = True
    else:
        did_error[idx] = False
    idx += 1
    if idx >= len(entradas):
        x1 = np.linspace(-3, 3, 20)
        x2 = (-peso1/peso2) * x1 - (umbral / peso2)
        # print("salida: ", y)
        for entrada, step in zip(entradas, D):
            plt.scatter(entrada[0], entrada[1],
                        color="blue" if step else "red")

        plt.plot(x1, x2, color="red")
        plt.pause(0.00005)
        idx = 0
        ax = plt.gca()
        del ax.lines[0]


x1 = np.linspace(-3, 3, 20)
x2 = (-peso1/peso2) * x1 - (umbral / peso2)
plt.plot(x1, x2, color="blue")
plt.show()
