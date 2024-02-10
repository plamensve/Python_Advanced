def words_sorting(*words):
    result = {}
    total_value = 0
    for word in words:
        current_word = word
        sum_of_chars = 0
        for char in word:
            sum_of_chars += ord(char)
        total_value += sum_of_chars
        result[current_word] = sum_of_chars

    final_result = []
    if total_value % 2 == 0:
        sorted_dict = sorted(result.items(), key=lambda x: x)
        for word, value in sorted_dict:
            final_result.append(f"{word} - {value}")
    else:
        sorted_dict = sorted(result.items(), key=lambda x: -x[1])
        for word, value in sorted_dict:
            final_result.append(f"{word} - {value}")

    return '\n'.join(final_result)


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))








