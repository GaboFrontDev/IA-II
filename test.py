from neurona_base import Neurona
import sys
import os


def act_fun(val):
    return 1 if val > 0 else 0


data = [
    [
        [0, 0, 0],
        [1, 0, 1],
        [0, 1, 0],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ], [
        [0, 0, 0],
        [1, 0, 1],
        [0, 1, 0],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ], [
        [0, 0, 0],
        [1, 0, 1],
        [0, 1, 0],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]

]

D = [[0, 0, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1]]


def read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token


def main():
    entrada = open(sys.argv[1])
    maestro = open(sys.argv[2])
    for token in read_by_tokens(entrada):
        print(token)
    for token in read_by_tokens(maestro):
        print(token)
    segmentIdx = 0
    for segment in data:
        i = 0
        neurona = Neurona(len(segment[i]), etha=0.5)
        while neurona.did_error:
            neurona.did_error = False
            while i < len(segment):
                neurona.evaluate_error(D[segmentIdx][i], segment[i], act_fun)
                i += 1
            i = 0
        print("termina el entrenamiento")


if __name__ == "__main__":
    if os.path.exists(sys.argv[1]) and os.path.exists(sys.argv[2]):
        main()
    else:
        print("File does not exists")
