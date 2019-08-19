import matplotlib.pyplot as plt
entradas = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
umbral = 1.5

""" PESOS PARA AND """
# peso1 = 1
# peso2 = 1
""" PESOS PARA OR """
peso1 = 2
peso2 = 2

prod_punto = [a[0]*peso1 + a[1]*peso2 - umbral for a in entradas]
steps = [(a > 0) for a in prod_punto]

m = peso1/peso2
b = umbral / peso2
graph = [[m*x+b, x + 0]for x in [steps[0], steps[1]]]
print(graph)
plt.plot(graph)
plt.show()
