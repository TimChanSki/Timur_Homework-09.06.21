#Task 1
persons = [{"name": "Sam", "age": 10}, {"name": "Jackky", "age": 47}, {"name": "Mal", "age": 12}]
ages = []
youngest_pers = []
oldest_pers = []
for person in persons:
    ages.append(person.get('age'))

for person in persons:
    if person['age'] == min(ages):
        youngest_pers.append(person['name'])
    if person['age'] == max(ages):
        oldest_pers.append(person['name'])
#####################################################
#Task 2
my_dict_1 = {'key_': 'value1','key_1': 'value1','key2_': 'value2','key_3': 'value_2','_key_3': 'value_3',}
my_dict_2 = {'key_4': '_value_4','key_1': 'value_3','key_2': 'value_2','key_5': 'value_5','_key_6': '_value6',}
my_dict_1_keys = [key_1 for key_1 in my_dict_1.keys()]
my_dict_2_keys = [key_2 for key_2 in my_dict_2.keys()]

my_dict_1_set = set(my_dict_1_keys)
my_dict_2_set = set(my_dict_2_keys)
both_dicts_keys = list(my_dict_1_set.intersection(my_dict_2_set))

my_dict1_keys_unique = list(my_dict_1_set.difference(my_dict_2_set))
new_dict = {}
for first_dict_key in my_dict1_keys_unique:
    new_dict[first_dict_key] = my_dict_1[first_dict_key]

result_dict = {}
value_list = []
keys_union = my_dict_1_set.union(my_dict_2_set)
new_list = []
for key_from_union in keys_union:
    if key_from_union in my_dict_1_keys and key_from_union in my_dict_2_keys:
        result_dict[key_from_union] = [my_dict_1[key_from_union], my_dict_2[key_from_union]]
    elif key_from_union in my_dict_1_keys:
        result_dict[key_from_union] = my_dict_1[key_from_union]
    else:
        result_dict[key_from_union] = my_dict_2[key_from_union]


