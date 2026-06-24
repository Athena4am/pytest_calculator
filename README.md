hdhd# Calculadora con Pytest

Proyecto simple en Python que implementa operaciones básicas de una calculadora
y demuestra cómo usar **pytest** para pruebas automatizadas.

## 🚀 Instalación y uso

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Athena4am/calculadora-pytest.git
   cd calculadora-pytest
   ```

   

2. Crear entorno virtual e instalar dependencias:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
   pip install pytest
   ```

   

3. Ejecutar las pruebas:

   ```bash
   pytest
   ```

   Ejemplo de código

   ```python
   # calculadora.py
   def suma(a, b):
       return a + b
   ```

   ```python
   # test_calculadora.py
   from calculadora import suma
   
   def test_suma():
       assert suma(2, 3) == 5
   ```

   