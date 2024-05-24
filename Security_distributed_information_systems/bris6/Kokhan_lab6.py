import random

def is_prime(num):  # Функція для перевірки, чи є число простим
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Перевіряємо дільники до квадратного кореня числа
        if num % i == 0:  
            return False
    return True  # Якщо дільників не знайдено, число є простим

def euclidean_algorithm(a, b):  # Функція, яка реалізує алгоритм Евкліда для знаходження НСД та коефіцієнтів x і y
    if a == 0:  # Якщо a дорівнює нулю, НСД дорівнює b
        return b, 0, 1
    gcd, x1, y1 = euclidean_algorithm(b % a, a)  
    x = y1 - (b // a) * x1  
    y = x1 
    return gcd, x, y  

def key_creation(p, q):  # Функція для генерації ключів
    n = p * q  
    return n, (p, q)  # Повертаємо відкритий ключ (n) та таємний ключ (p, q)

def encryption(public_key, message):  # Функція для шифрування повідомлення
    n = public_key  
    return [pow(ord(char), 2, n) for char in message]  # Шифруємо кожен символ повідомлення

def decryption(private_key, element):  # Функція для дешифрування повідомлення
    p, q = private_key  
    n = p * q  
    gcd, yp, yq = euclidean_algorithm(p, q)  # Використовуємо алгоритм Евкліда для обчислення НСД та коефіцієнтів
    p1 = pow(element, (p + 1) // 4, p)  # Обчислення першого кореня за модулем p
    p2 = p - p1  # Обчислення другого кореня за модулем p
    q1 = pow(element, (q + 1) // 4, q)  # Обчислення першого кореня за модулем q
    q2 = q - q1  # Обчислення другого кореня за модулем q
    r1 = (yp * p * q1 + yq * q * p1) % n  # Обчислення першого можливого розшифрованого варіанту
    r2 = (yp * p * q2 + yq * q * p1) % n  # Обчислення другого можливого розшифрованого варіанту
    r3 = (yp * p * q1 + yq * q * p2) % n  # Обчислення третього можливого розшифрованого варіанту
    r4 = (yp * p * q2 + yq * q * p2) % n  # Обчислення четвертого можливого розшифрованого варіанту
    return [r1, r2, r3, r4]  

def main():  # Головна функція програми
    while True:  # Безкінечний цикл для обробки команд користувача
        mode = input("Enter 'e' - encrypt, 'd' - decrypt message, 'g' - generate keys: ")  # Вибір режиму роботи

        if mode == 'g':  # Якщо обрано генерацію ключів
            while True:  
                p = int(input("Enter p: "))  
                if is_prime(p):  
                    break 
                else:
                    print("p isn't prime. ")  

            while True: 
                q = int(input("Enter q: ")) 
                if is_prime(q): 
                    break
                else:
                    print("q isn't prime. ")  

            public_key, private_key = key_creation(p, q)  # Генерація ключів
            print("Public key:", public_key) 
            print("Private key:", private_key)  

        elif mode == 'e':  # Якщо обрано шифрування
            with open('encryption_input.txt', encoding='utf-8', mode='r') as f:  # Відкриття файлу з текстом для шифрування
                message = f.read() 

            public_key = int(input("Enter public key (n): ")) 
            encrypt_result = encryption(public_key, message) 
            encryption_result_sep = ", ".join(str(x) for x in encrypt_result)  # Форматування зашифрованого тексту

            with open('encryption_output.txt', encoding='utf-8', mode='w') as fw:  # Запис зашифрованого тексту у файл
                fw.write(encryption_result_sep)  
            
            print("Text encrypted successfully") 

        elif mode == 'd':  # Якщо обрано дешифрування
            with open('encryption_output.txt', encoding='utf-8', mode='r') as f:  # Відкриття файлу з зашифрованим текстом
                input_values = f.read()  

            private_key = tuple(int(input(f"Enter {i+1} element of private key: ")) for i in range(2))  # Введення таємного ключа
            input_array = input_values.split(", ")  # Розділення зашифрованого тексту на окремі елементи
            array_without_spaces = [int(value.strip()) for value in input_array]  # Видалення пробілів і перетворення в цілі числа
            decrypt_result = []  # Ініціалізація списку для результату дешифрування

            for element in array_without_spaces:  # Дешифрування кожного елемента
                calc_blocks = decryption(private_key, element)  # Виклик функції дешифрування для кожного елемента
                for letter in calc_blocks:  # Перебір можливих розшифрованих значень
                    if 32 <= letter <= 122 or letter == 10 or letter == 13:  # Перевірка, чи є значення допустимим символом
                        decrypt_result.append(chr(letter))  # Додавання символу до результату дешифрування

            with open('decryption_output.txt', encoding='utf-8', mode='w') as fw:  # Запис дешифрованого тексту у файл
                fw.write(''.join(decrypt_result))  
            
            print("Text decrypted successfully")  

        else:  
            print("Invalid mode entered!")  

if __name__ == "__main__":  
    main()  
