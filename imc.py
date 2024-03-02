

def calcular_imc(peso, altura):
    "Calcula el Índice de Masa Corporal (IMC) dado el peso en kilogramos y la altura en metros."
    return peso / (altura ** 2)

def estado_nutricional(imc):
    """
    Determina el estado nutricional de acuerdo al IMC.
    """
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad tipo I"
    elif 35 <= imc < 40:
        return "Obesidad tipo II"
    else:
        return "Obesidad tipo III (mórbida)"

def main():
    # Solicitar datos al usuario
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))

    # Calcular el IMC
    imc = calcular_imc(peso, altura)

    # Determinar el estado nutricional
    estado = estado_nutricional(imc)

    # Mostrar resultados
    print(f"Su IMC es: {imc:.2f}")
    print(f"Su calificacion OMS es: {estado}")

if __name__ == "__main__":
    main()
