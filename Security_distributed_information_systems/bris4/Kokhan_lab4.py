# Загальна кількість літер в англійському алфавіті
n = 26
# Функція, яка реалізує алгоритм Евкліда для знаходження НСД (найбільшого спільного дільника)
def euclidean_algorithm(a, b):
    if a == 0:
        return b, 0, 1
        # Рекурсивний виклик для обчислення НСД та коефіцієнтів x1 і y1
    gcd, x1, y1 = euclidean_algorithm(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Функція для знаходження оберненого елемента по модулю
def inversed_mod(number, mod):
      # Використання алгоритму Евкліда для знаходження оберненого елемента
    return euclidean_algorithm(number, mod)[1] % mod

# Функція для шифрування повідомлення
def encrypt_message(a, s, message):
        # Створення списку для збереження зашифрованого тексту
    encrypted = []
    # Проходження по кожному символу у вхідному повідомленні
    for char in message:
         # Перевірка, чи є символ літерою
        if char.isalpha():
            # Перевірка, чи є символ літерою
            E = chr(((a * (ord(char.upper()) - ord('A')) + s) % n) + ord('A'))
            # Якщо символ був нижнім регістром, додати зашифрований символ у нижньому регістрі
            encrypted.append(E.lower() if char.islower() else E)
        else:
             # Якщо символ не є літерою, додати його до списку без змін
            encrypted.append(char)
            # Об'єднання списку в рядок і повернення зашифрованого повідомлення
    return ''.join(encrypted)

# Функція для дешифрування повідомлення
def decrypt_message(a, s, message):
    decrypted = []
    inv_a = inversed_mod(a, n)
    for char in message:
        if char.isalpha():
               # Формула для дешифрування символу
            D = chr(((inv_a * (ord(char.upper()) - ord('A') - s)) % n) + ord('A'))
            decrypted.append(D.lower() if char.islower() else D)
        else:
            decrypted.append(char)
    return ''.join(decrypted)

# Функція для отримання коректних значень 'a' та 's'
def get_valid_inputs():
    while True:
          # Введення значення 'a'
        a = int(input("Введіть a (менше 26, і НСД(a, n) = 1): "))
         # Перевірка умови НСД та чи a менше 26
        if euclidean_algorithm(a, n)[0] == 1 and a < 26:
            break
        print("Некоректне a. Спробуйте ще раз.")
    
    while True:
        s = int(input("Введіть s (менше 26): "))
         # Перевірка, чи s менше 26
        if s < 26:
            break
        print("Некоректне s. Спробуйте ще раз.")
        # Повернення коректних значень 'a' та 's'
    return a, s

# Функція для процесу шифрування
def handle_encryption():
     # Читання повідомлення з файлу
    with open('encryption_input.txt', encoding='utf-8') as f:
        message = f.read()
         # Отримання коректних значень 'a' та 's'
    a, s = get_valid_inputs()
    # Шифрування повідомлення
    encrypted_message = encrypt_message(a, s, message)
    # Запис зашифрованого повідомлення у файл
    with open('encryption_output.txt', 'w', encoding='utf-8') as fw:
        fw.write(encrypted_message)
    print("Текст успішно зашифровано")

# Функція для процесу дешифрування
def handle_decryption():
    with open('encryption_output.txt', encoding='utf-8') as f:
        encrypted_message = f.read()
    a, s = get_valid_inputs()
    decrypted_message = decrypt_message(a, s, encrypted_message)
    with open('decryption_output.txt', 'w', encoding='utf-8') as fw:
        fw.write(decrypted_message)
    print("Текст успішно розшифровано")

# Головна функція для запуску програми
def main():
     # Нескінченний цикл для вибору режиму роботи програми
    while True:
        mode = input("Введіть 'e' для шифрування або 'd' для дешифрування повідомлення: ").strip().lower()
        if mode == 'e':
            handle_encryption()
        elif mode == 'd':
            handle_decryption()
        else:
            print("Некоректний режим! Введіть 'e' для шифрування або 'd' для дешифрування.")

# Run the main function
if __name__ == "__main__":
    main()
