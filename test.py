# import matplotlib.pyplot as plt
from neurona_base import Neurona


def act_fun(val):
    return 1 if val > 0 else 0


data = [
    [0, 0],
    [1, 0],
    [0, 1],
    [1, 1],
    [0, 1],
]
D = [0, 0, 0, 1, 0]

i = 0
neurona = Neurona(len(data[i]), etha=0.5)
while neurona.did_error:
    neurona.did_error = False
    while i < len(data):
        neurona.evaluate_error(D[i], data[i], act_fun)
        i += 1
    i = 0
