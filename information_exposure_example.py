# Función que expone información sensible (vulnerable a exposición de información sensible)
def sensitive_operation():
    try:
        # Alguna operación sensible que podría lanzar una excepción
        result = 1 / 0  # Simulación de error para demostrar información sensible
        print("Result:", result)
    except Exception as e:
        print("Error:", str(e))


# Ejemplo de uso
if __name__ == "__main__":
    sensitive_operation()
