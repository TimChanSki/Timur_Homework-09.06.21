# Task 1
my_list = ["artr", "dfagdf", "sdafwq", "ergdew", "aterwrqew", "fhraatherw"]
new_my_list = []
for index, stroka in enumerate(my_list):
    if not index % 2:
        new_my_list.append(stroka[::-1])
    else:
        new_my_list.append(stroka)
print(new_my_list)
###########################################
# Task 2
list_with_letter_a = []
for value in (my_list):
    if "a" in value[0]:
        list_with_letter_a.append(value)
print(list_with_letter_a)
###########################################
# Task 3
list_with_letter_a_anywhere = []
for value in (my_list):
    if "a" in value:
        list_with_letter_a_anywhere.append(value)
print(list_with_letter_a_anywhere)
###########################################
# Task 4
my_combinated_list = ["1", "2", '3', 4, 5, 6]
print(my_combinated_list)
str_list = []

for value in my_combinated_list:
    if type(value) == str:
        str_list.append(value)
print(str_list)
###########################################
# Task 5
my_str = "Набор НепонятныйХ "
new_list = []
for symbol in my_str:
    if my_str.count(symbol) == 1:
        new_list.append(symbol)
print(new_list)
###########################################
# Task 6
my_str1 = "8,5,41,4,57,7,64,45,7,5,6,"
my_str2 = "6,6,1,8,2,6,4"
my_set = list(set(my_str1) & set(my_str2))
print(my_set)
###########################################
# Task 7
str1 = "Это строка под номером 1"
str2 = "А вот данная строка под номером 2"
new_wish_list = []
for value in str1:
    values = str1.find(value) - str1.rfind(value)
    if values == 0:
        if value in str2 and str2.find(value) - str2.rfind(value) == 0:
            new_wish_list.append(value)
print(new_wish_list)
###########################################
# Task 8
person = {"Person_info": {"Surname": "Solonovich", "Name": "Dmitriy", "Age": 37},
          "Place of living": {"Country": "Ukraine", "City": "Dnipro", "Street": "Central"},
          "Work": {"Availability": "yes", "Post": " General Manenger"}}
print(person)
###########################################
# Task 9
cake = {"Components": {"Cups": {"Flour": 40, "Milk": 30, "Butter": 100, "Egs": 3}},
        {"Cream": {"Sugar": 120, "Butter": 50, " Vanil": 10, "Sour Cream": 15}}:
            {"Glazyr": {"Coke": 15, "Sugar": 100, "Butter": 100}}}
print(cake)
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло
