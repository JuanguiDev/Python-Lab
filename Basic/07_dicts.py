# Dictionaries
# Syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

person = {
  'first_name':'Juan',
  'last_name':'Lopera',
  'age':24,
  'country':'Colombia',
  'is_marred':False,
  'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
  'address':{
    'street':'Space street',
    'zipcode':'02210'
  }
}

# Dictionary Length
person = {
  'first_name':'Juan',
  'last_name':'Lopera',
  'age':24,
  'country':'Colombia',
  'is_marred':False,
  'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
  'address':{
    'street':'Space street',
    'zipcode':'02210'
  }
}
print(len(person))

# Accessing Dictionary Items
person = {
  'first_name':'Juan',
  'last_name':'Lopera',
  'age':24,
  'country':'Colombia',
  'is_marred':False,
  'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
  'address':{
    'street':'Space street',
    'zipcode':'02210'
  }
}

print(person['first_name']) # Juan
print(person['country'])    # Colombia
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
# print(person['city'])       # Error

print(person.get('first_name')) # Juan
print(person.get('country'))    # Colombia
print(person.get('skills')) #['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None

# Adding Items to a Dictionary
person = {
  'first_name':'Juan',
  'last_name':'Lopera',
  'age':24,
  'country':'Colombia',
  'is_marred':False,
  'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
  'address':{
    'street':'Space street',
    'zipcode':'02210'
  }
}

person['job_title'] = 'Developer'
person['skills'].append('HTML')
print(person)

# Modifying Items in a Dictionary
person = {
  'first_name':'Juan',
  'last_name':'Lopera',
  'age':24,
  'country':'Colombia',
  'is_marred':False,
  'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
  'address':{
    'street':'Space street',
    'zipcode':'02210'
  }
}

person['first_name'] = 'Guillermo'
person['age'] = 25

# Checking Keys in a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False

# Removing Key and Value Pairs from a Dictionary
person = {
  'first_name':'Juan',
  'last_name':'Lopera',
  'age':24,
  'country':'Colombia',
  'is_marred':False,
  'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
  'address':{
    'street':'Space street',
    'zipcode':'02210'
  }
}

person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item

# Changing Dictionary to a List of Items
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

# Deleting a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

# Copy a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# Getting Dictionary Keys as a List
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

# Getting Dictionary Values as a List
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])