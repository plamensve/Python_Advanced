# def palindrome(word, index):
#     first_part = ''
#     middle = ''
#     second_part = ''
#
#     length = len(word)
#     first_part += word[:length // 2]
#     middle += word[length // 2]
#     second_part += word[length // 2 + 1:]
#
#     if first_part == second_part[::-1]:
#         return f'{word} is a palindrome'
#     else:
#         return f'{word} is not a palindrome'
#
#
# print(palindrome("peter", 0))


# SOLUTION 2

# def palindrome(word, idx):
#     if idx == len(word) // 2:
#         return f"{word} is a palindrome"
#
#     if word[idx] != word[-idx-1]:
#         return f"{word} is not a palindrome"
#
#     result = palindrome(word, idx+1)
#
#     return result
#
#
# print(palindrome("abcba", 0))


# SOLUTION 3

def palindrome(word, idx):
    if word[idx] != word[-idx-1]:
        return f"{word} is not a palindrome"

    if idx == len(word) // 2:
        return f"{word} is a palindrome"

    return palindrome(word, idx + 1)


print(palindrome("abcba", 0))