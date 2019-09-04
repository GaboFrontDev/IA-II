from neurona_base import Neurona
import sys
import os


def act_fun(val):
    return 1 if val > 0 else 0


data = [
    [0, 0],
    [1, 0],
    [0, 1],
    [1, 1]
]

D = [[0, 0, 0, 1], [0, 1, 1, 0]]


def read_entries(fileobj):
    for line in fileobj:
        entry = []
        for token in line.split():
            entry.append(int(token))
        if entry:
            yield entry
        else:
            pass


def has_error(neuronas):

    for neurona in neuronas:
        if neurona.did_error:
            return True
    return False


def main():
    entrada = open(sys.argv[1])
    maestro = open(sys.argv[2])
    data = []
    D = []
    for entry in read_entries(entrada):
        data.append(entry)
    for token in read_entries(maestro):
        D.append(token)

    print(data)
    print(D)
    neuronas = []
    index = 0
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
                D[entrySegment][desiredSegment], data[entrySegment], act_fun)
            desiredSegment += 1
            if neuronas[neuronaIdx].did_error:
                entrySegment = 0
            neuronaIdx += 1
        print("Segmento", entrySegment,  "terminado")
        entrySegment += 1


if __name__ == "__main__":
    if os.path.exists(sys.argv[1]) and os.path.exists(sys.argv[2]):
        main()
    else:
        print("File does not exists")
