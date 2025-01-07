

import os
os.chdir(r"C:\Users\white\Desktop\HOMEWORK")

text_dict = {}
for file_name in os.listdir():
    if  file_name.endswith('.txt'):
        f_list = []
        with open(file_name, encoding='utf-8-sig') as f:
            f_list = [lines.strip() for lines in f]
            text_dict[file_name] = f_list

text_dict_sorted = sorted(text_dict.items(), key= lambda item: item[1], reverse=True)

file_text = ''
for element in text_dict_sorted:
    str_text = ''
    str_text = str(f'{element[0]}:\n {'\n '.join(element[1])}\n')
    file_text += str_text

with open ('text_result.txt', 'w', encoding='utf-8-sig') as f_result:
    f_result.write(file_text)

