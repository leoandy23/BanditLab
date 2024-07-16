import os


# Función para ejecutar un comando del sistema (vulnerable a inyección de comandos)
def run_command(user_input):
    os.system("echo " + user_input)


# Ejemplo de uso
if __name__ == "__main__":
    command = input("Enter command: ")
    run_command(command)
