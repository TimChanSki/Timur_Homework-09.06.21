import json
#Task 1

def reader(filename):
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        return data

####################################################
#Task 2
def sort_name(path):
    dicts_list = reader(path)
    for dict in dicts_list:
        split_nam = dict['name'].split(' ')
        dict['name'] = split_nam

    sort_last_nam = sorted(dicts_list, key=lambda x: (x['name'][-1], x['name'][0]))
    for dict in sort_last_nam:
        joined_name = ' '.join(dict['name'])
        dict['name'] = joined_name
    return sort_last_nam

####################################################
#Task 3
def sort_year(path):
    dicts_list = reader(path)
    for dict in dicts_list:
        split_year = dict['years'].split(' ')
        dict['years'] = split_year
        if dict['years'][-1] == 'BC.':
            dict['years'][-2] = f'-{dict["years"][-2]}'
            dict['years'].pop(-1)

    sorted_by_year = sorted(dicts_list, key=lambda x: float(x['years'][-1]))
    for dict in sorted_by_year:
        if float(dict['years'][-1]) < 0:
            dict['years'][-1] = dict['years'][-1].replace('-', '')
            dict['years'].append('BC.')
        joined_year = ' '.join(dict['years'])
        dict['years'] = joined_year
    return sorted_by_year

####################################################
#Task 4

def sort_numbers(path):
    dicts_list = reader(path)
    for dict in dicts_list:
        splited_text = dict['text'].split(' ')
        dict['text'] = splited_text
    sort_numbers_list = sorted(dicts_list, key=lambda x: len(x.get('text')))
    for dict in sort_numbers_list:
        joined_text = ' '.join(dict['text'])
        dict['text'] = joined_text
    return sort_numbers_list
