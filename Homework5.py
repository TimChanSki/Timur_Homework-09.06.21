#Task_1
number = int(35000003)
number = str(number)
min_number = min(number)
counter = number.count(min_number)
print("Количество нулей в вашем числе = ",counter)
#####################################
#Task_2
number_task2 = int(1002000000)
countzero = 0
while (number_task2 % 10 == 0):
    number_task2 //= 10
    countzero += 1
print("Количество 0 в конце числа = ",countzero)
#####################################
#Task_3
my_list1 = [1,2,3,4,5,6]
my_list2 = [7,8,90,1,4,6,8]
my_result = []
for index, symbol in enumerate(my_list1):
    if index % 2:
        symbol = my_list1[index]
        my_result.append(symbol)
for index, symbol in enumerate(my_list2):
    if not index % 2:
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
value1 = meine_string.find(l_limit)
value2 = meine_string.find(r_limit,8,12)
sub_str = meine_string[value1+1:value2:]
print("Найбольшая часть строки между o и g =  ",sub_str)
#####################################
#Task_8
str_my = "abcdefght"
result = (list(map(''.join, zip(*[iter(str_my + '_')]*2))))
print("Значения ",result)
#####################################
#Task_9
a = [2, 4, 1, 5, 3, 9, 0, 7]
values = (sum([a[i-1] < a[i] > a[i+1] for i in range(1, len(a)-1)]))
print("Количество элементов,которые больше двух своих соседей  ",values)






