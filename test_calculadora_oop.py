import pytest
from calculadora_oop import calculadora


def test_sumar_oop():
    calc = calculadora()
    calc.suma(5, 5)
    assert calc.resultado == 10


def test_sumar_cero_oop():
    calc = calculadora()
    calc.suma(5, 0)
    assert calc.resultado == 5


def test_sumar_negativos_oop():
    calc = calculadora()
    calc.suma(-5, -5)
    assert calc.resultado == -10


def test_sumar_positivo_negativo():
    calc = calculadora()
    calc.suma(5, -2)
    assert calc.resultado == 3


def test_sumar_decimales_oop():
    calc = calculadora()
    calc.suma(10.5, 10.5)
    assert calc.resultado == 21


def test_sumar_numero_string_oop():
    calc = calculadora()
    with pytest.raises(TypeError):
        calc.suma(5, "suma")


def test_sumar_listas_oop():
    calc = calculadora()
    with pytest.raises(TypeError):
        calc.suma(5, [])


# test para funcion restar


def test_restar_oop():
    calc = calculadora()
    calc.resta(5, 5)
    assert calc.resultado == 0


def test_restar_cero_oop():
    calc = calculadora()
    calc.resta(5, 0)
    assert calc.resultado == 5


def test_resta_negativos_oop():
    calc = calculadora()
    calc.resta(-5, -5)
    assert calc.resultado == 0


def test_resta_positivo_negativo():
    calc = calculadora()
    calc.resta(5, -2)
    assert calc.resultado == 7


def test_resta_decimales_oop():
    calc = calculadora()
    calc.resta(10.5, 10.5)
    assert calc.resultado == 0


def test_resta_numero_string_oop():
    calc = calculadora()
    with pytest.raises(TypeError):
        calc.resta(5, "suma")


def test_resta_listas_oop():
    calc = calculadora()
    with pytest.raises(TypeError):
        calc.resta(5, [])


# test para multiplicacion
def test_multiplicar_oop():
    calc = calculadora()
    calc.multiplicacion(5, 5)
    assert calc.resultado == 25


def test_multiplicar_cero_oop():
    calc = calculadora()
    calc.multiplicacion(5, 0)
    assert calc.resultado == 0


def test_multiplicar_negativos_oop():
    calc = calculadora()
    calc.multiplicacion(-5, -5)
    assert calc.resultado == 25


def test_multiplicar_positivos_negativos_oop():
    calc = calculadora()
    calc.multiplicacion(5, -5)
    assert calc.resultado == -25


def test_multiplicar_decimales_oop():
    calc = calculadora()
    calc.multiplicacion(5.25, 5.25)
    assert calc.resultado == 27.5625


def test_multiplicar_string_oop():
    calc = calculadora()
    with pytest.raises(TypeError):
        calc.multiplicacion(5, "Hola")


def test_multiplicar_lista_oop():
    calc = calculadora()
    with pytest.raises(TypeError):
        calc.multiplicacion(5, [])
