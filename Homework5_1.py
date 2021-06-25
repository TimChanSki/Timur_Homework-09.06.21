#Task_1
number = int(12130141510)
find_all_zero = str(number).count('0')
print("Количество нулей в вашем числе = ",find_all_zero)
#####################################
#Task_2
number_task2 = int(1014105500000)
number_task2 = str(number_task2)
revers_task = number_task2[::-1]
count = 0
for i in revers_task:# for i in str(number_task2)[::-1]
    if i == '0':
        count += 1
    else:
        break
print("Количество 0 в конце числа = ",count)
#####################################
#Task_3
my_list1 = [1,2,3,4,5,6]
my_list2 = [7,8,90,1,4,6,8]
my_result = []
for index, symbol in enumerate(my_list1):
    if not index % 2:
        symbol = my_list1[index]
        my_result.append(symbol)
for index, symbol in enumerate(my_list2):
    if  index % 2:
        symbol = my_list2[index]
        my_result.append(symbol)
print('Список из 2 списков = ',my_result)
#####################################
#Task_4
my_listik = [7,2,3,4]
first_elem = my_listik[0]
new_listik = my_listik[1:].copy()
new_listik.append(first_elem)
print("Список new_list с 1 елементом в конце = ",new_listik)
#####################################
#Task_5
spisok_my_list = [1,2,3,4,5,6,7]
perviy_element_spiska = spisok_my_list.pop(0)
spisok_my_list.append(perviy_element_spiska)
print('Task_5 = ',spisok_my_list)
#####################################
#Task_6
my_str =  '43 больше чем 34 но меньше чем  56 и равно 43'
my_splited_str = my_str.split()
my_str_numbers = []
for number in my_splited_str:
    if number.isnumeric():
        my_str_numbers.append(int(number))
sum_of_numbers = sum((my_str_numbers))
print("Сума чисел из строки = ", sum_of_numbers)
#####################################
#Task_7
meine_string = "My long string"
l_limit = 'o'
r_limit = 'g'
limit_of_left_position = (meine_string.rfind(l_limit,0,16))
limit_of_right_position = (meine_string.rfind(r_limit,0,16))
print("Найбольшая часть строки между o и g = ",meine_string[limit_of_left_position + 1:limit_of_right_position])
# value1 = meine_string.find(l_limit)
# value2 = meine_string.find(r_limit,8,12)
# sub_str = meine_string[value1+1:value2:]
# print("Найбольшая часть строки между o и g =  ",sub_str)
#####################################
#Task_8
str_my = "abcdefght"
empty_list = []
for i,j in enumerate(str_my):
    if i % 2==0:
        if len(k:=str_my[i:i+2])>1:
            empty_list.append(k)
        else:
            empty_list.append(k+'_')
print(empty_list)
#####################################
#Task_9
list_of_values = [2, 4, 1, 5, 3, 9, 0, 7]
counter = 0
for i in range(1, len(list_of_values) - 1):
    if list_of_values[i - 1] < list_of_values[i] > list_of_values[i + 1]:
        counter += 1
print("Количество элементов,которые больше двух своих соседей  ",counter)







