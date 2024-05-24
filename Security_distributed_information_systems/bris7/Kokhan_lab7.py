import random

# Функція для перевірки, чи є число простим
def is_prime(num): 
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Перевіряємо дільники до квадратного кореня числа
        if num % i == 0:
            return False
    return True  

# Функція для генерації ключів
def generate_keys(p, g):
    a = random.randint(1, p-1)  # Випадкове число a в діапазоні від 1 до p-1
    h = pow(g, a, p)  
    public_key = (p, g, h)  
    private_key = a  
    return public_key, private_key  

# Функція для шифрування тексту
def encrypt_message(public_key, message):
    p, g, h = public_key  
    encrypted_message = []  # Список для збереження зашифрованих пар (c1, c2)
    
    for char in message:
       
        r = random.randint(1, p-1)  # Випадкове число r в діапазоні від 1 до p-1
        c1 = pow(g, r, p) 
        c2 = (ord(char) * pow(h, r, p)) % p
        encrypted_message.append((c1, c2))  # Додавання пари (c1, c2) до списку зашифрованих повідомлень
    
    return encrypted_message 

# Функція для дешифрування тексту
def decrypt_message(p, private_key, encrypted_message):
    decrypted_text = []  # Список для збереження розшифрованих символів
    a = private_key 
    
    for c1, c2 in encrypted_message:
        s = pow(c1, p-1-a, p)
        M = (c2 * s) % p  
        decrypted_text.append(chr(M))  # Перетворення M на символ і додавання до списку
    
    return ''.join(decrypted_text)  # Повернення розшифрованого тексту як рядка

# Основний цикл програми
def main():
    while True:
        mode = input("Enter 'e' to encrypt, 'd' to decrypt message, 'g' to generate keys: ")  # Вибір режиму
        
        if mode == 'g':
            while True:
                p = int(input("Enter p: "))  
                if is_prime(p):  # Перевірка, чи є p простим
                    break
                else:
                    print("p isn't prime.")
            
            while True:
                g = int(input("Enter g: "))  
                if is_prime(g) and g < p-1:  # Перевірка, чи є g простим і меншим за p-1
                    break
                else:
                    print("g isn't prime or greater than p-1.")
            
            public_key, private_key = generate_keys(p, g)  # Генерація ключів
            print("Public key:", public_key)  
            print("Private key:", private_key) 
        
        elif mode == 'e':
            with open('encryption_input.txt', encoding='utf-8', mode='r') as f:  # Відкриття файлу для читання
                message = f.read()  # Зчитування тексту
            
            p = int(input("Enter 1st element of public key (p): "))  
            g = int(input("Enter 2nd element of public key (g): "))  
            h = int(input("Enter 3rd element of public key (h): "))  
            public_key = (p, g, h)  # Формування відкритого ключа
            
            encrypted_message = encrypt_message(public_key, message)  # Шифрування повідомлення
            encrypted_message_str = "; ".join(str(pair) for pair in encrypted_message)  # Перетворення зашифрованих пар на рядок
            
            with open('encryption_output.txt', encoding='utf-8', mode='w') as fw:  
                fw.write(encrypted_message_str) 
            
            print("Text encrypted successfully.")
        
        elif mode == 'd':
            with open('encryption_output.txt', encoding='utf-8', mode='r') as f: 
                encrypted_message_str = f.read() 
            
            p = int(input("Enter 1st element of public key (p): "))  
            a = int(input("Enter 1st element of private key (a): "))  
            private_key = a  
            
            encrypted_message = [tuple(map(int, pair.strip(" ()").split(","))) for pair in encrypted_message_str.split(";")]  # Розділення рядка на пари чисел
            decrypted_message = decrypt_message(p, private_key, encrypted_message)  # Дешифрування повідомлення
            
            with open('decryption_output.txt', encoding='utf-8', mode='w') as fw:  
                fw.write(decrypted_message)  
            
            print("Text decrypted successfully.")
        
        else:
            print("Invalid mode entered!")  

if __name__ == "__main__":
    main()  
