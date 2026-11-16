import pytest
from main import calcular_area


def test_area_valores_enteros():
    assert calcular_area(5, 4) == 20


def test_area_valores_decimales():
    assert calcular_area(2.5, 4.0) == pytest.approx(10.0)


def test_base_invalida():
    with pytest.raises(ValueError):
        calcular_area(0, 5)
    with pytest.raises(ValueError):
        calcular_area(-3, 5)


def test_altura_invalida():
    with pytest.raises(ValueError):
        calcular_area(5, 0)
    with pytest.raises(ValueError):
        calcular_area(5, -2)