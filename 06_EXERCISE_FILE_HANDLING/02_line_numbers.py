import os
# from string import punctuation # use if ... in punctuation:

path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, "01_02_text.txt")
result_file_path = os.path.join(path_to_root, "02_result.txt")

punctuation_symbols = ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?" )

with open(file_path, "r") as f:
    data = f.read().split("\n")

with open(result_file_path, "a") as file:
    for i in range(len(data)):
        punc_count, letter_count = 0, 0

        for chr in data[i]:
            if chr in punctuation_symbols: punc_count += 1
            if chr.isalpha(): letter_count += 1

        file.write(f"Line {i+1}: " + data[i] + f" ({letter_count})({punc_count})")
        if i != len(data) - 1: file.write("\n")
        
# Alternative solution

# import os

# path_to_root = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(path_to_root, "01_even_lines.txt")

# punctuation_symbols = ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?" )
# result = []

# with open(file_path, "r") as f:
#     data = f.read().split("\n")
#     for i in range(len(data)):
#         punc_count, letter_count = 0, 0

#         for chr in data[i]:
#             if chr in punctuation_symbols: punc_count += 1
#             if chr.isalpha(): letter_count += 1

#         result.append(f"Line {i+1}: " + data[i] + f" ({letter_count})({punc_count})")
        
#     with open("result.txt", "a") as file:
#         file.write("\n".join(result))
    