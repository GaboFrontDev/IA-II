from neurona_base import Neurona
import sys
import os
import numpy as np
from imc import IMC_Data
from imc import es_gordito


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
    for i in range(2):
        data.append(IMC_Data(pesoDict,alturaDict))
    data = np.array(data)
    for dato in data:
        D.append([es_gordito(dato[0]/(pow(dato[1],2)))])
    normalizacion = data / np.linalg.norm(data)
    neuronas = []
    index = 0
    print(D)
    # Carga inicial
    while index < len(D[0]):
        neuronas.append(Neurona(len(data[index]), etha=0.5))
        index += 1
    entrySegment = 0

    # Entrenamiento por fila de entradas
    while entrySegment < len(data):
        neuronaIdx = 0
        desiredSegment = 0
        while neuronaIdx < len(neuronas):
            neuronas[neuronaIdx].did_error = False
            neuronas[neuronaIdx].evaluate_error(
                D[entrySegment][desiredSegment], data[entrySegment], es_gordito)
            desiredSegment += 1
            if neuronas[neuronaIdx].did_error:
                entrySegment = 0
            neuronaIdx += 1
        print("Segmento", entrySegment,  "terminado")
        entrySegment += 1


if __name__ == "__main__":
    main()