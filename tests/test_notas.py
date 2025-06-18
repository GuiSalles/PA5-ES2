from src.notas import (
    calcular_media,
    calcular_mediana,
    nota_maxima,
    nota_minima,
    classificar_nota,
)

def test_media():
    assert calcular_media([7, 8, 9]) == 8

def test_mediana_impar():
    assert calcular_mediana([5, 1, 9]) == 5

def test_mediana_par():
    assert calcular_mediana([5, 1, 9, 7]) == 6.0

def test_max_min():
    notas = [3, 10, 6, 8]
    assert nota_maxima(notas) == 10
    assert nota_minima(notas) == 3

def test_classificacao():
    assert classificar_nota(9.5) == "A"
    assert classificar_nota(7.1) == "B"
    assert classificar_nota(5.5) == "C"
    assert classificar_nota(3.2) == "D"
