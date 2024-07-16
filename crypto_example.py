from Crypto.Cipher import DES


# Función para cifrar datos usando DES (vulnerable por uso de algoritmo criptográfico inseguro)
def encrypt_data(data):
    cipher = DES.new("8bytekey", DES.MODE_ECB)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data


# Ejemplo de uso
if __name__ == "__main__":
    data = input("Enter data to encrypt: ")
    encrypted_data = encrypt_data(data)
    print("Encrypted data:", encrypted_data)
