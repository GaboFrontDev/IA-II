from neurona_base import Neurona
import matplotlib.pyplot as plt
import sys
import os
import numpy as np
from imc import IMC_Data
from imc import es_gordito
def act_fun(val):
    return 1 if val > 0 else 0


pesoDict  = {
    "mininum": 40,
    "maximum": 90
}
alturaDict = {
    "mininum":1.40, 
    "maximum": 1.90
}

def main():
    data =[]
    D  =[]
    for i in range(50):
        data.append(IMC_Data(pesoDict,alturaDict))
    data = np.array(data)
    for dato in data:
        D.append([es_gordito(dato[0]/(pow(dato[1],2)))])
    data = (data - data.min()) / (data.max() - data.min() )
    for dato, step in zip(data, D):
        plt.scatter(dato[0], dato[1],
                    color="red" if step[0] else "blue")    
    plt.pause(0.5)
    neuronas = []
    index = 0

    # Carga inicial
    while index < len(D[0]):
        neuronas.append(Neurona(len(data[0]), etha=0.1))
        index += 1

    print("información cargada")
    print("Maestro: ", D)
    print("Entradas: ", data)
    entrySegment = 0
    error = False
    # Entrenamiento por fila de entradas
    while entrySegment < len(data):
        neuronaIdx = 0
        # Entrenamiento de cada neurona con el indice de fila correspondiente
        while neuronaIdx < len(neuronas):
            neuronas[neuronaIdx].evaluate_error(
                D[entrySegment][neuronaIdx], data[entrySegment], act_fun)
            if neuronas[neuronaIdx].did_error:
                error = True
                entrySegment = 0
                break
            else:
                error = False
            neuronaIdx += 1
        if not error:
            entrySegment += 1

    peso1= neuronas[0].W[0]
    peso2= neuronas[0].W[1]
    umbral = neuronas[0].umbral
    x1 = np.linspace(0.3, 1, 20)
    x2 = ((-peso1/peso2) * x1 - (umbral / peso2))
    ln = plt.plot(x1, x2, color="blue")



if __name__ == "__main__":
    main()
    print("end")
    plt.show()
