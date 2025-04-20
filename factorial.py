
def calcular_factorial(n):
    """Calcula el factorial de un número positivo"""
    if n < 0:
        return "Error: el número debe ser positivo"
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

# Solicita al usuario un número
try:
    numero = int(input("Ingrese un número entero positivo: "))
    resultado = calcular_factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
except ValueError:
    print("Por favor, ingrese un número válido.")
    