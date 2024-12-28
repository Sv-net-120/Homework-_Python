
# Разместить файлы в порядке увеличения количества строк
# text_2
# 1
# Строка номер 1 файла номер 2
# text_1
# 2
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 2

with open('text_1.txt', encoding='utf-8-sig') as f_1:

    f_1_list = f_1.readlines()
    str_1 = len(f_1_list)
    num_f1 = 1

with open('text_2.txt', encoding='utf-8-sig') as f_2:

    f_2_list = f_2.readlines()
    str_2 = len(f_2_list)
    num_f2 = 2

with open('text_3.txt', encoding='utf-8-sig') as f_3:

    f_3_list = f_3.readlines()
    str_3 = len(f_3_list)
    num_f3=3

spisok_str = [str_1,str_2,str_3]
spisok_num = [ num_f1, num_f2, num_f3]
spisok_text = [f_1_list, f_2_list, f_3_list]
zip_spisok = sorted(zip(spisok_str, spisok_num, spisok_text), key = lambda x: (x[0], len(x[2])))
print_txt = list(zip_spisok)

print(f' text_{print_txt[0][1]}\n 1 \n Строка номер 1 файла номер {print_txt[0][1]}\n {''.join(print_txt[0][2])}\n')
print(f" text_{print_txt[1][1]}\n 2 \n "
      f"Строка номер 1 файла номер {print_txt[1][1]}\n {''.join(print_txt[1][2][0])}"
      f" Строка номер 2\n {''.join(print_txt[1][2][1])}")
print(f" text_{print_txt[2][1]}\n 3 \n "
      f"Строка номер 1 файла номер {print_txt[2][1]}\n {''.join(print_txt[2][2][0])}"
      f" Строка номер 2\n {''.join(print_txt[2][2][1])}"
      f" Строка номер 3\n {''.join(print_txt[2][2][2])}")

# Результат выполнения кода
# text_2
#  1
#  Строка номер 1 файла номер 2
#  Тревога началась в тринадцать часов ноль две минуты.
#
#  text_1
#  2
#  Строка номер 1 файла номер 1
#  Начальник  полиции
#  Строка номер 2
#  лично позвонил в шестнадцатый участок. А спустя  одну минуту тридцать секунд
#
#  text_3
#  3
#  Строка номер 1 файла номер 3
#   В  это время  дня  машины текли сплошным  блестящим  потоком,  а  среди
#  Строка номер 2
#  потока, будто  колонны из бетона  и стекла, высились  здания. Здесь,  в мире
#  Строка номер 3
#  резких граней,  люди  на тротуарах  выглядели  несчастными и  неприкаянными.