import numpy as np

# Визначення функції для розкодування QR-коду
def scanner(qrcode):
    # Ініціалізуємо список для зберігання значень QR-коду
    qr_code_indeces = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(21)
    
    # Проходимо по вхідному QR-коду
    for i, row in enumerate(qrcode):
        for j, val in enumerate(row):
            # Змінюємо значення в залежності від його позиції
            if (i + j) % 2 == 0:
                val = 1 - val
            qr_code_indeces[i][j] = val
    
    # Перетворюємо список в масив NumPy
    qr_code = np.array(qr_code_indeces)
    
    # Відділяємо перші 9 рядків
    qr_code = qr_code[9:]
    
    # Ініціалізуємо змінні для подальшої обробки
    odd, output = 0, []
    
    # Ітеруємося через конкретні стовпці
    for i in [19, 17, 15, 13]:
        columns = qr_code[:, [i, i + 1]]
        if odd == 1:
            direction = 1
        else:
            direction = -1
            
        # Додаємо значення з обраних стовпців до виводу
        for row in columns[::direction]:
            output += row.tolist()[::-1]
        odd = 1 - odd
    
    # Перетворюємо вивід в бінарний рядок
    output = ''.join(list(map(str, output[4:])))
    
    # Витягуємо кількість літер з бінарного рядка
    letter_count = int(output[:8], 2)
    output = output[8:]
    
    # Ініціалізуємо пустий рядок для слів
    word = ''
    print(letter_count)
    
    # Ітеруємося через бінарний рядок для вилучення символів
    for i in range(0, (letter_count * 8) + 11, 8):
        word += chr(int(output[i:i+8], 2))
        if len(word) == letter_count:
            return word  # Повертаємо розкодоване слово
