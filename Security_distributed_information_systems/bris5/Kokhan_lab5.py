import random  

def is_prime(num):  # Функція для перевірки, чи є число простим
    if num <= 1:  # Якщо число менше або дорівнює 1, то воно не є простим
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Перевіряємо дільники до квадратного кореня числа
        if num % i == 0:
            return False
    return True  # Якщо дільників не знайдено, число є простим

def euclidean_algorithm(a, b):  # Функція, яка реалізує алгоритм Евкліда для знаходження НСД та коефіцієнтів x і y
    if a == 0:  
        return b, 0, 1
    gcd, x1, y1 = euclidean_algorithm(b % a, a)
    x = y1 - (b // a) * x1  
    y = x1 
    return gcd, x, y  

def mod_inverse(a, m):  # Функція для знаходження оберненого елемента за модулем
    gcd, x, _ = euclidean_algorithm(a, m)
    if gcd != 1:
        raise ValueError("Inverse does not exist")
    return x % m

def key_creation(p, q):  # Функція для генерації ключів RSA
    n = p * q 
    phi = (p - 1) * (q - 1) 
    e = random.randint(2, phi - 1) 
    while euclidean_algorithm(e, phi)[0] != 1:  
        e = random.randint(2, phi - 1)  
    d = mod_inverse(e, phi)  
    public_key = (e, n)  # Встановлюємо відкритий ключ (e, n)
    private_key = (d, n)  # Встановлюємо таємний ключ (d, n)
    return public_key, private_key 

def encrypt(message, public_key):  # Функція для шифрування повідомлення
    e, n = public_key  
    return [pow(ord(char), e, n) for char in message]  # Шифруємо кожен символ повідомлення

def decrypt(ciphertext, private_key):  # Функція для дешифрування повідомлення
    d, n = private_key 
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])  # Розшифровуємо кожен символ криптотексту

def main():  # Головна функція
    while True:  # Починаємо нескінченний цикл для вибору режиму роботи
        mode = input("Enter 'e' - encrypt, 'd' - decrypt message, 'g' - generate keys: ")

        if mode == 'g':  # Генерація ключів
            p = int(input("Enter p: ")) 
            while not is_prime(p):  # Перевірка, чи є p простим числом
                p = int(input("Enter a prime number for p: "))  
            
            q = int(input("Enter q: "))
            while not is_prime(q):  # Перевірка, чи є q простим числом
                q = int(input("Enter a prime number for q: "))

            public_key, private_key = key_creation(p, q)  # Генерація ключів
            print("Public key:", public_key)  
            print("Private key:", private_key) 

        elif mode == 'e':  # Шифрування
            with open('encryption_input.txt', encoding='utf-8', mode='r') as f:
                message = f.read()  # Читання повідомлення з файлу
            
            public_key = (int(input("Enter 1st element of public key: ")),  # Введення першого елементу відкритого ключа
                          int(input("Enter 2nd element of public key: ")))  # Введення другого елементу відкритого ключа

            encrypt_result = encrypt(message, public_key)  # Шифрування повідомлення
            encryption_result_sep = ", ".join(str(x) for x in encrypt_result)  # Перетворення зашифрованого тексту до формату блоків, розділених комами

            with open('encryption_output.txt', encoding='utf-8', mode='w') as fw:
                fw.write(encryption_result_sep)  # Запис зашифрованого тексту до файлу

        elif mode == 'd':  # Дешифрування
            with open('encryption_output.txt', encoding='utf-8', mode='r') as f:
                ciphertext = f.read()  # Читання зашифрованого тексту з файлу

            private_key = (int(input("Enter 1st element of private key: ")),  # Введення першого елементу таємного ключа
                           int(input("Enter 2nd element of private key: ")))  # Введення другого елементу таємного ключа

            ciphertext_array = list(map(int, ciphertext.split(", ")))  # Перетворення зашифрованого тексту в масив елементів
            decrypt_result = decrypt(ciphertext_array, private_key)  # Розшифрування тексту

            with open('decryption_output.txt', encoding='utf-8', mode='w') as fw:
                fw.write(decrypt_result)  # Запис розшифрованого тексту до файлу

        else:
            print("Invalid mode entered!")

if __name__ == "__main__":
    main()
