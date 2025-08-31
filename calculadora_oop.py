class calculadora:
    # una clase de una calculadora simple, guarda el ultimo resultado
    # el constructor
    def __init__(self):
        self.resultado = 0
        print("calculadora creada, lista para operar")

    # metodos
    def suma(self, a, b):
        if not isinstance(a, (int, float) or not isinstance(b, (int, float))):
            raise TypeError("los argumentos deben ser numeros")

        self.resultado = a + b
        return self.resultado

    def resta(self, a, b):
        if not isinstance(a, (int, float) or not isinstance(b, (int, float))):
            raise TypeError("los argumentos debens ser numeros")

        self.resultado = a - b
        return self.resultado
