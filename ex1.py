import re

def text_statistics():
    print("АНАЛИЗАТОР ТЕКСТОВОЙ СТАТИСТИКИ")
    text = input("Введите текст для анализа: ")

    # Количество символов (включая пробелы и знаки)
    num_chars = len(text)

    # Количество слов (разделение по пробелам)
    words = text.split()
    num_words = len(words)

    # Количество предложений (делим по ., !, ? и убираем пустые кусочки)
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]
    num_sentences = len(sentences)

    # Выводим результат
    print("=== СТАТИСТИКА ТЕКСТА ===")
    print(f"Общее количество символов: {num_chars}")
    print(f"Количество слов: {num_words}")
    print(f"Количество предложений: {num_sentences}")

if __name__ == "__main__":
    text_statistics()


ptint ("Hello world")

