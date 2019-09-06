import numpy as np

def es_gordito(val):
    return 1 if val > 25 else 0


def IMC_Data(peso, altura):
    data = []
    altura = np.random.uniform(altura["mininum"],altura["maximum"]) 
    peso= np.random.uniform(peso["mininum"],peso["maximum"]) 
    data.append(peso)
    data.append(altura)
    return data