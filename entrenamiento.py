# CORRECCION DEL ERROR
# Función de entrenamiento para encontrar los pesos que obedezcan a la salida deseada
# Tenemos que calcular el error para encontrar la salida deseada " D "
# E = D_i - Y
# Lo que nosotros queremos hacer es minimizar el vector de error cambiando nuestro
# vector de pesos W.s
# ------------------------
# W_i(k + 1) = W_i(k) + E(k)*X_i(k)
# 1. iniciar vector W con valores aleatorios que
#	 estén entre -1 y 1. EX:  W = [rand,rand]
#
# 2. Por cada entrada x en nuestros patrones
# 	 de entrenamiento.
# 	 Primero vamos a  calcular el error, después
# 	 nuestros pesos nuevos.
# 	 W[i] = W[i] + X[i]*e
# 3. Si e != 0, regresamos a paso 2.
D = [0, 0, 0, 1]  # Salida deseada


# graph = [[x + 0, b - x*m]for x in steps]
# for entrada, step in zip(entradas, steps):
#     plt.scatter(entrada[0], entrada[1], color="blue" if step else "red")

# m = peso1/peso2
# b = umbral / peso2

# plt.plot(graph[0], graph[3])
# plt.show()
