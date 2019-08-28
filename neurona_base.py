class Neurona:
    "This is my second class"
    pesos = []
    etha = 0.5
    error = 0
    umbral = 0
    did_error = False

    def set_error(self):
        return 0

    def recalc_pesos(self, entradas):
        print("recalculando pesos...")
        sf = self
        sf.did_error = True
        sf.pesos = sf.pesos + sf.etha * sf.error * entradas
        sf.umbral = sf.umbral + sf.etha * sf.error

    def func(self):
        print('running')
