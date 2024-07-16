import logging

# Configuración básica de logging
logging.basicConfig(level=logging.INFO)


# Función que registra información sensible (vulnerable a inserción de información sensible en logs)
def log_sensitive_data(password):
    logging.info(f"User password: {password}")


# Ejemplo de uso
if __name__ == "__main__":
    password = input("Enter password: ")
    log_sensitive_data(password)
