import matplotlib.pyplot as plt
entradas = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
umbral = 1.5

""" PESOS PARA AND """
peso1 = 1
peso2 = 1
""" PESOS PARA OR """
# peso1 = 2
# peso2 = 2

prod_punto = [a[0]*peso1 + a[1]*peso2 - umbral for a in entradas]
steps = [(a > 0) for a in prod_punto]

m = peso1/peso2
b = umbral / peso2
graph = [[x + 0, b - x*m]for x in steps]
print(steps)
print(graph)
for entrada, step in zip(entradas, steps):
    plt.scatter(entrada[0], entrada[1], color="blue" if step else "red")

plt.plot(graph[0], graph[3])
plt.show()
