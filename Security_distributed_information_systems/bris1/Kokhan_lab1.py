alphabet = ['А','Б','В','Г','Ґ','Д','Е','Є','Ж','З','И','І','Ї','Й','К',
'Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ь','Ю','Я'
] #ініціалізація алфавіту
n = len(alphabet) #довжина алфавіту
key = input("Введіть ключ: ").upper() #ініціалізація ключа
m = len(key)
def encrypt(): #функція, що шифрує текст
    with open('input.txt', encoding = 'utf-8', mode = 'r') as f: #відкриття файлу в режимі читання
        textNew = f.read()  #читання вмісту файлу і зберігання
    textCypher= [] #порожній список, що буде використовуватися для зберігання зашифрованих символів
    ordM = 0
    ordK = 0
    j = 0
    for letter in textNew: #початок циклу для всіх символів тексту
        if letter.upper() in alphabet: #перевірка кожного символу чи є він літерою алфавіту
            ordM = alphabet.index(letter.upper())  #індекс символу тексту в алфавіті
            ordK = alphabet.index(key[j].upper()) #індекс символу ключа на поточній позиції
            if not letter.isupper(): #перевірка регістру
                textCypher.append(alphabet[( ordM + ordK) % n].lower()) #знаходження зашифрованого символу в алфавіті і перетворення його в нижній регістр
            else:
                textCypher.append(alphabet[( ordM + ordK) % n]) #знаходження зашифрованого символу в алфавіті, але без перетворення
        else:
            textCypher.append(letter)  #додавання не буквеного символу в список
        j += 1
        if j == m:
            j=0
    textOld = ''.join(str(letter) for letter in textCypher)  #об'єднання зашифрованих символів в тексту
    with open('output.txt', encoding = 'utf-8', mode = 'w') as fw: #відкриття файлу в режимі запису
        fw.write(textOld) #запис зашифрованого тексту
        print("Текст успішно зашифровано")
def decrypt():  #функція, що розшифровує текс
    with open('output.txt', encoding = 'utf-8', mode = 'r') as f:   #Читання зашифрованого тексту з файлу
        textOld = f.read() #Ініціалізація списку для розшифрованого тексту
    ordC = 0 
    ordKn = 0
    i = 0
    textDecypher = []  #Ініціалізація списку для розшифрованого тексту
    for symbol in textOld: #початок циклу для всіх символів зашифрованого тексту
        if symbol.upper() in alphabet: #перевірка кожного символу чи є він літерою алфавіту
            ordC = alphabet.index(symbol.upper()) # індексація символу в алфавіт
            ordKn = (n-alphabet.index((key[i].upper()))) % n #індекс символу ключа дешифрування на поточній позиції
            if not symbol.isupper():
                textDecypher.append(alphabet[(ordC + ordKn) % n].lower())  #знаходження розшифрованого символу в алфавіті і перетворення його в нижній регістр
            else:
                textDecypher.append(alphabet[(ordC + ordKn) % n]) #знаходження розшифрованого символу в алфавіті, але без перетворення
        else:
            textDecypher.append(symbol) #додавання не буквеного символу в список
        i+=1
        if i == m:
            i=0
    textNew = ''.join(str(symbol) for symbol in textDecypher) #об'єднання розшифрованого тексту
    with open('decryption_output.txt', encoding = 'utf-8', mode = 'w') as fw: #Запис дешифрованого тексту до файлу
        fw.write(textNew)
    print("Текст успішно розшифровано")
mode = input("Введіть 1, щоб зашифрувати, або 2, щоб розшифрувати: ")
if mode == '1':
     encrypt()
if mode == '2':
    decrypt()
