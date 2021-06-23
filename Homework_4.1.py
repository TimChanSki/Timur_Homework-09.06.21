#Task_1
from random import randint
my_list = [randint(0,199) for i in range(10)]### решил завести в список 10 рандомных чисел, надеюсь не ошибка)
for number_more_hungred in my_list:
    if number_more_hungred > 100:
        print(f"Значения в списке,которые больше 100:",number_more_hungred)
#######################################
#Task_2
my_result = []
for numbers in my_list:
    if numbers > 100:
        my_result.append(numbers)
print(my_result)
#######################################
#Task_3
my_list1 = [5,2]
lenth = len(my_list1)
if lenth < 2:
    my_list1.append(0)
else:
    value_1 = my_list1[-1]
    value_2 = my_list1[-2]
    sum_index = value_1 + value_2
    my_list1.append(sum_index)
print(my_list1)
#######################################
#Task_4
value = input("Введите число с затятой: ")
try:
    value = float(value)
    result = value ** -1
except ValueError:
    print("Число не может быть приведено к типу float")
    result = 0
except ZeroDivisionError:
    print("Ноль не может быть привидено к типу float")
    result = -1
print(result)

###Не знаю как сделать проверку на точку.Через if '.' in value?
#######################################
#Task_5
my_string_1 = "0123456789"
my_listik = []
for symb_1 in my_string_1:
    for symb_2 in my_string_1:
        sum_symb = symb_1 + symb_2
        sum_symb = int(sum_symb)
        my_listik.append(sum_symb)
print(my_listik)
