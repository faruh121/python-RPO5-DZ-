# Пользователь вводит с клавиатуры строку. Проверьте
# является ли введенная строка палиндромом. Палиндром — слово или текст, которое читается одинаково
# слева направо и справа налево. Например, кок; А роза
# упала на лапу Азора; доход; А буду я у дуба.

predl = input("Введеите предложение: ")
x = len(predl)
cnt = 0
x = x - 1
k = 0
while x - cnt >= cnt:
    if predl[x - cnt] == predl[cnt]:
        cnt += 1
    else:
        k = 1
        break
if k == 1:
  print("Да, является")
else:
  print("Нет, не является")

# # Пользователь вводит с клавиатуры некоторый текст,
# # после чего пользователь вводит список зарезервированных
# # слов. Необходимо найти в тексте все зарезервированные
# # слова и изменить их регистр на верхний. Вывести на
# # экран измененный текст. 

# txt = input("Введите текст: ")
# slova = input("Введите зарезервированые слова через пробел: ").split(' ')
# for i in slova:
#   txt = txt.replace(i,i.upper())
# print(txt)


# Задание 3
# Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученный
# результат.
text = input("Введите предложения: ")
words = text.split()
count = 0
for word in words:
    if word.endswith(".") or word.endswith("!") or word.endswith("?") :
        count += 1
print(count)