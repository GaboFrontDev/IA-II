from neurona_base import Neurona
import matplotlib.pyplot as plt
import sys
import os
import numpy as np
from imc import IMC_Data
from imc import es_gordito


def act_fun(val):
    return val


pesoDict = {
    "mininum": 40,
    "maximum": 90
}
alturaDict = {
    "mininum": 1.40,
    "maximum": 1.90
}


def main():
    neurona = []
    D = []
    pesos = np.random.randint(40, 90, size=50)
    alturas = np.random.randint(140, 190, size=50)/100
    data = np.vstack((pesos, alturas)).T
    D = np.array([1 if x[0]/pow(x[1], 2) >= 25 else 0 for x in data])
    for dato, step in zip(data, D):
        plt.scatter(dato[0], dato[1],
                    color="red" if step else "blue")
    epoch = 100
    neurona = Neurona(learn_rate=0.001, iterations=epoch)
    neurona.fit(data, D)
    return neurona


if __name__ == "__main__":
    classifier = main()
    plt.plot(range(1, len(classifier.cost) + 1), classifier.cost)

    plt.title("Visualisation of errors")
    plt.xlabel('Epochs')
    plt.ylabel('Errors')
    plt.show()
