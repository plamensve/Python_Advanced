import os
import re


words_file_path = os.path.join('..', 'test', 'words.txt')
input_file_path = os.path.join('..', 'test', 'input.txt')
output_file_path = os.path.join('..', 'test', 'output.txt')

with open(words_file_path, 'r') as file:
    searched_words_text = file.read()
    searched_words = [word for word in searched_words_text.split()]


with open(input_file_path) as file:
    content = file.read().lower()

words_count = {}
for searched_word in searched_words:
    pattern = re.compile(rf'\b{searched_word}\b')
    result = re.findall(pattern, content)
    words_count[searched_word] = len(result)

sorted_words_count = sorted(words_count.items(), key=lambda kvp: -kvp[1])

with open(output_file_path, 'a') as file:
    for word, count in sorted_words_count:
        file.write(f"{word} - {count}\n")