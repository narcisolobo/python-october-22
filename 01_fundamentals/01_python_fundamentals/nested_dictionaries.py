""" 
Get Values From a List of Dictionaries
Create a function iterateDictionary2(key_name, some_list) that,
given a list of dictionaries and a key name, the function prints
the value stored in that key for each dictionary. For example,
iterateDictionary2('first_name', students) should output:
Michael
John
Mark
KB

And iterateDictionary2('last_name', students) should output:

Jordan
Rosales
Guillen
Tonel

"""


def iterate_dictionary2(key, lst_of_dicts):
    # iterate over list of dictionaries
    # for i in range(len(lst_of_dicts)):
    #     print(lst_of_dicts[i][key])
    for dict in lst_of_dicts:
        print(dict[key])


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

# iterate_dictionary2('first_name', students)

""" 
Iterate Through a Dictionary with List Values
Create a function printInfo(some_dict) that given a dictionary
whose values are all lists, prints the name of each key along
with the size of its list, and then prints the associated values
within each key's list. For example:
"""



dojo = {
    'locations': [
        'San Jose',
        'Seattle',
        'Dallas',
        'Chicago',
        'Tulsa',
        'DC',
        'Burbank'
    ],
    'instructors': [
        'Michael',
        'Amy',
        'Eduardo',
        'Josh',
        'Graham',
        'Patrick',
        'Minh',
        'Devon'
    ]
}

def print_info(dict_input):
    for key in dict_input.keys():
        print(f'{len(dict_input[key])} {key}')
        for element in dict_input[key]:
            print(element)

print_info(dojo)

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
