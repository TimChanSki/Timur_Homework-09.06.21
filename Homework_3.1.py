#Task 1
value = input("Введите значение value для манипуляций:  ")

value = int(value)

new_value = value // 2 if value < 100 else -value

print("Значения из Task 1 :", new_value)
######################################
#Task 2
new_value2 =  1 if value < 100 else 0

print("Значения из Task 2 :", new_value2)
######################################
#Task 3
new_value3 =  True if value == 1 else False

print("Значения из Task 3 :", new_value3)
######################################
#Task 4
my_str = input("Введите значение my_str для манипуляций:  ")

my_str = my_str.upper()

print("Значения из Task 4 :",my_str)
#######################################
#Task 5
my_str2 = my_str.lower()

print("Значения из Task 5 :",my_str2)
#######################################
#Task 6

lenth_str = len(my_str)

if lenth_str < 5:
    print("Значения из Task 6 :",my_str * 2)
else:
    print("Значения из Task 6 :",my_str)
#######################################
#Task 7

lenth_str1 = len(my_str)

if lenth_str1 < 5:
    print("Значения из Task 7 :",my_str + my_str[::-1])
else:
    print("Значения из Task 7 :", my_str)

