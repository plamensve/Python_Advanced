from collections import deque

vowels = deque([v for v in input().split()])  # -> first symbol
consonants = deque([c for c in input().split()])  # -> last symbol
words = {
    'rose': [],
    'lotus': [],
    'daffodil': [],
    'tulip': [],
}
find_word = False
while True:
    if not vowels or not consonants:
        break

    if find_word:
        break

    current_vowel = vowels.popleft()
    current_consonants = consonants.pop()

    for k, v in words.items():
        current_word = k

        if current_vowel in current_word and current_vowel not in words[current_word]:
            count = current_word.count(current_vowel)
            if count == 1:
                words[k].append(current_vowel)
            elif count > 1:
                words[k].append(current_vowel)
                words[k].append(current_vowel)
            if len(current_word) == len(words[k]):
                print(f"Word found: {k}")
                find_word = True
                break

        if current_consonants in current_word and current_consonants not in words[current_word]:
            count = current_word.count(current_consonants)
            if count == 1:
                words[k].append(current_consonants)
            elif count > 1:
                words[k].append(current_consonants)
                words[k].append(current_consonants)
            if len(current_word) == len(words[k]):
                print(f"Word found: {k}")
                find_word = True
                break

if not find_word:
    print(f"Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
