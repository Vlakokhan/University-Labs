def main():
    # Запит на вибір режиму роботи
    mode = input("Тип роботи (1 - шифрування / 2 - дешифрування): ")
    match mode:
        case "1":
            # Читання тексту для шифрування з файлу
            text = readFile("encryption_input.txt")
            # Отримання ключа
            K = input('Введіть ключ: ')
            # Шифрування тексту
            C = encrypt(text, K)
            # Запис зашифрованого тексту у файл
            writeFile(C, "encryption_output.txt")
        case "2":
            # Читання зашифрованого тексту з файлу
            text = readFile("encryption_output.txt")
            # Отримання ключа
            K = input('Введіть ключ: ')
            # Дешифрування тексту
            M = decrypt(text, K)
            # Запис розшифрованого тексту у файл
            writeFile(M, "decryption_output.txt")
        case _:
            # Повідомлення про неправильний вибір режиму
            print("Неправильний вибір")
    return

# Функція для шифрування повідомлення
def encrypt(M, K):
    encrypted = []
    keyLength = len(K)
    for count, char in enumerate(M):
        # Використання операції XOR для шифрування
        encrypted_char = chr((ord(char) ^ ord(K[count % keyLength])))
        encrypted.append(encrypted_char)
    return ''.join(encrypted)

# Функція для дешифрування повідомлення
def decrypt(C, K):
    decrypted = []
    keyLength = len(K)
    for count, char in enumerate(C):
        # Використання операції XOR для дешифрування
        decrypted_char = chr((ord(char) ^ ord(K[count % keyLength])))
        decrypted.append(decrypted_char)
    return ''.join(decrypted)

# Функція для читання файлу
def readFile(filename):
    with open(filename, encoding='utf-8', mode="r") as file:
        text = file.read()
    return text

# Функція для запису у файл
def writeFile(text, filename):
    with open(filename, encoding='utf-8', mode="w") as file:
        file.write(text)

# Виконання головної функції
if __name__ == "__main__":
    main()
