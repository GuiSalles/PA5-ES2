def calcular_media(notas):
    return sum(notas) / len(notas) if notas else 0

def calcular_mediana(notas):
    notas_ordenadas = sorted(notas)
    n = len(notas)
    if n == 0:
        return 0
    meio = n // 2
    return notas_ordenadas[meio] if n % 2 != 0 else (notas_ordenadas[meio - 1] + notas_ordenadas[meio]) / 2

def nota_maxima(notas):
    return max(notas) if notas else 0

def nota_minima(notas):
    return min(notas) if notas else 0

def classificar_nota(nota):
    if nota >= 9:
        return "A"
    elif nota >= 7:
        return "B"
    elif nota >= 5:
        return "C"
    else:
        return "D"
