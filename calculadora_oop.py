class calculadora:
    # una clase de una calculadora simple, guarda el ultimo resultado
    # el constructor
    def __init__(self):
        self.resultado = 0
        print("calculadora creada, lista para operar")

    # Funciones
    def suma(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            self.resultado = a + b
            return self.resultado
        else:
            raise TypeError("los argumentos deben ser numeros")

    def resta(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            self.resultado = a - b
            return self.resultado
        else:
            raise TypeError("los argumentos deben ser numeros")

    def multiplicacion(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            self.resultado = a * b
            return self.resultado
        else:
            raise TypeError("los argumentos debens ser numeros")
