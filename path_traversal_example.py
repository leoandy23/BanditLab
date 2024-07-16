import os


# Función para leer un archivo (vulnerable a traversal de ruta)
def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content


# Ejemplo de uso
if __name__ == "__main__":
    file_path = input("Enter file path: ")
    file_content = read_file(file_path)
    print("File content:")
    print(file_content)
