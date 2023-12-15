import re

# Создаем список слов
words = ["ac", "abc", "bac", "abac", "bcc", "aaa"]

# Определяем регулярное выражение
pattern = re.compile(r'a(?=c)')

# Фильтруем слова по заданному шаблону
result_words = list(filter(pattern.search, words))

# Выводим результат
print("Слова, в которых за 'а' следует 'с':", result_words)
