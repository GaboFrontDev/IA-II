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

D = [[1], [0], [0], [1]]


def read_entries(fileobj):
    for line in fileobj:
        entry = []
        for token in line.split():
            entry.append(int(token))
        if entry:
            yield entry


def main():
    print("Abriendo archivos")
    entrada = open(sys.argv[1])
    maestro = open(sys.argv[2])
    data = []
    D = []
    for entry in read_entries(entrada):
        data.append(entry)
    for token in read_entries(maestro):
        D.append(token)

    print("información cargada")
    print("Maestro: ", D)
    print("Entradas: ", data)
    neuronas = []
    index = 0
    # Carga inicial
    while index < len(D[0]):
        neuronas.append(Neurona(len(data[0]), etha=0.1))
        index += 1
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


if __name__ == "__main__":
    if os.path.exists(sys.argv[1]) and os.path.exists(sys.argv[2]):
        main()
    else:
        print("File does not exists")
