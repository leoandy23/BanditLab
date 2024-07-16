import sqlite3


# Función para buscar usuarios por nombre (vulnerable a SQL injection)
def find_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    users = cursor.fetchall()
    conn.close()
    return users


# Ejemplo de uso
if __name__ == "__main__":
    username = input("Enter username: ")
    result = find_user(username)
    print(result)
