def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def potencia(a, b):
    return a ** b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

if __name__ == "__Calculadora_basica.py__":
    print("Suma: 2 + 3 =", suma(2, 3))
    print("Resta: 5 - 2 =", resta(5, 2))
    print("Potencia: 2 ** 3 =", potencia(2, 3))
    print("Multiplicar: 4 * 5 =", multiplicar(4, 5))
    print("Dividir: 10 / 2 =", dividir(10, 2))