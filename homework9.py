# Task 1


def reverse_gen(some_list: list):
    new_str_list = []
    for index, symbol in enumerate(some_list):
        if index % 2:
            new_str_list.append(symbol[::-1])
        else:
            new_str_list.append(symbol)
    return new_str_list


str_list = ['qwee', 'rftew', "werf"]
result = reverse_gen(str_list)
print(result)


#####################################################
# Task 2

def letter_a_checker(some_list: list):
    new_str_list = []
    for index, symbol in enumerate(some_list):
        if symbol[0] == 'a':
            new_str_list.append(symbol)
    return new_str_list


str_list = ['aferg', 'hyasg', "asftw"]
result = letter_a_checker(str_list)
print(result)


#####################################################
# Task 3


def check_for_a(some_list: list):
    new_str_list = []
    for index, value in enumerate(some_list):
        if 'a' in value:
            new_str_list.append(value)
    return new_str_list


str_list = ["dfgwera","gdfgsdfg",'dfgwasdaa']
result = check_for_a(str_list)
print(result)


#####################################################
# Task 4


def str_list_check(some_list: list):
    new_list = []
    for index, symbol in enumerate(some_list):
        if isinstance(symbol, str):
            new_list.append(symbol)
    return new_list


my_list = [7.2,52,"4,",4,'7']
result = str_list_check(my_list)
print(result)


#####################################################
# Task 5

def unique_symbols(some_str: str):
    new_list = []
    for index, symbol in enumerate(set(some_str)):
        if some_str.count(symbol) == 1:
            new_list.append(symbol)
    return new_list


my_str = 'bbrgbtg,bpfvfevkermgkodcasdghtr'
result = unique_symbols(my_str)
print(result)


#####################################################
# Task 6

def str_intersection(some_str_1: str, some_str_2: str):
    new_list = list(set(some_str_1).intersection(set(some_str_2)))
    return new_list


my_str_1 = 'rgbtg,bpfvfevkermgkodcasdghtr'
my_str_2 = 'kfdombgofgmokwmdfschtywedasczx'
result = str_intersection(my_str_1, my_str_2)
print(result)


#####################################################
# Task 7

def symbols_in_both_str(some_str_1: str, some_str_2: str):
    new_list = []
    some_list = list(set(some_str_1).intersection(set(some_str_2)))
    for index, symbol in enumerate(some_list):
        if some_str_1.count(symbol) == 1 and some_str_2.count(symbol) == 1:
            new_list.append(symbol)
    return new_list


my_str_1 = 'rgbtg,bpfvfevkermgkodcasdghtr'
my_str_2 = 'kfdombgofgmokwmdfschtywedasczx'
result = symbols_in_both_str(my_str_1, my_str_2)
print(result)
#####################################################
# Task 8

import random
import string

names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]


def email_generator(names_list: list, domains_list: list):
    random_name = random.choice(names_list).lower()
    random_number = random.randint(100, 999)
    letters = string.ascii_lowercase
    random_letters_list = []
    for count in range(random.randint(5, 7)):
        random_letter = random.choice(letters)
        random_letters_list.append(random_letter)
    random_letter_str = ''.join(random_letters_list)
    random_domain = random.choice(domains_list)
    email = f'{random_name}.{random_number}@{random_letter_str}.{random_domain}'
    return email


random_email = email_generator(names, domains)
print(random_email)
