from collections import Counter
import json


def count_symbols(text: str) -> list:
    '''
    Подсчет количества символов и добавление их в словарь в порядке возрастания частоты появления
    :param text: изначальный текст
    '''
    symbols = Counter(text)
    key_dict = {}
    for item in symbols:
        symbols[item] = symbols[item] / len(text)
        key_dict[item] = symbols[item]
    key_dict = dict(sorted(key_dict.items(), key=lambda x: -x[1]))
    x = list(key_dict.keys())
    return x


if __name__ == '__main__':
    with open("cod2.txt", "r", encoding="utf-8") as fp:
        text = fp.read()
    symbol_list = count_symbols(text)
    print(f"Буквы исходного текста по убыванию частоты появления: {symbol_list}")

    with open("key2.json", "r", encoding="utf-8") as f:
        key = json.load(f)
    decrypted_text = text.translate(str.maketrans(key))

    print(f"Исходный текст: {text}")
    print(f"Дешифрованный текст: {decrypted_text}")

    with open("decrypted.txt", "w", encoding="utf-8") as f:
        f.write(decrypted_text)
