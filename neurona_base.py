import random
import numpy as np
import matplotlib.pyplot as plt


class Neurona:
    W = []
    etha = 0
    error = 0
    umbral = 0
    did_error = True

    def __init__(self, len, etha):
        i = 0
        self.etha = etha
        while i < len:
            self.W.append(random.uniform(-1, 1))
            i += 1
        self.W = np.array(self.W)

    def recalc_w(self, data):
        sl = self
        print("recalculando pesos...")
        print("Pesos iniciales", sl.W)
        output = sl.etha * sl.error * np.array(data)
        sl.W = np.array([sum(x) for x in zip(sl.W, output)])
        sl.umbral = sl.umbral + sl.etha * sl.error
        print("Pesos actualizados", sl.W)

    def evaluate_error(self, D, data, act_fun):
        dot = self.dot(data)
        self.error = D - act_fun(dot)
        if self.error != 0:
            self.did_error = True
            self.recalc_w(data)

    def dot(self, input):
        i = 0
        val = 0
        while i < len(input):
            val += input[i]*self.W[i]
            i += 1
        return val + self.umbral
