def keygen(step: int) -> dict:
    '''
    Генерирует ключ шифрования с заданным шагом
    :param step: шаг подстановки
    '''
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    key = {}
    for element in alphabet:
        position = alphabet.find(element)
        if position < len(alphabet)-step:
            key[alphabet[position]] = alphabet[position+step]
        else:
            key[alphabet[position]] = alphabet[step]
    print(key)
    with open('key1.txt', 'w', encoding='utf-8') as file:
        file.write(str(key))
    return key


if __name__ == '__main__':
    key = keygen(3)
    with open("original.txt", "r", encoding="utf-8") as fp:
        text = fp.read().upper()
    encrypted_text = text.translate(str.maketrans(key))

    print(f"Исходный текст: {text}")
    print(f"Зашифрованный текст: {encrypted_text}")
    with open("encrypted.txt", "w", encoding="utf-8") as f:
        f.write(encrypted_text)
