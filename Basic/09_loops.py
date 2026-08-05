# Loops
#? While Loop
count = 0
while count < 5:
  print(count)
  count = count + 1
# Prints from 0 to 4

count = 0
while count < 5:
  print(count)
  count = count + 1
else:
  print(count)

# Break and Continue - Part 1
#TODO Break
count = 0
while count < 5:
  print(count)
  count = count + 1
  if count == 3:
    break

#TODO Continue
count = 0
while count < 5:
  if count == 3:
    count += 1
    continue
  print(count)
  count = count + 1

#? For Loop
# Using For loop on list
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
  print(number)      # the numbers will be printed line by line, from 0 to 5

# Using For loop on string
language = 'Python'
for letter in language:
  print(letter)


for i in range(len(language)):
  print(language[i])

# Using For loop on tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
  print(number)

# For loop with dictionary Looping through a dictionary gives you the key of the dictionary.
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
for key in person:
  print(key)

for key, value in person.items():
  print(key, value) # this way we get both keys and values printed out

# Using For Loop in set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
  print(company)

# The Range Function
'''
  The range() function is used to return a list of numbers.
  The range(start, end, step) takes three parameters: starting, ending and increment
'''
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# for backward from start to end 
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]

for number in range(11):
  print(number)   # prints 0 to 10, not including 11

# Nested For Loop
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
for key in person:
  if key == 'skills':
    for skill in person['skills']:
      print(skill)

# For Else
for number in range(11):
  print(number)   # prints 0 to 10, not including 11
else:
  print('The loop stops at', number)

# Pass
for number in range(6):
  pass