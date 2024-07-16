# Función para validar una contraseña (vulnerable a validación inadecuada de entrada)
def check_password(password):
    if password == "admin":
        print("Access granted")
    else:
        print("Access denied")


# Ejemplo de uso
if __name__ == "__main__":
    password = input("Enter password: ")
    check_password(password)
