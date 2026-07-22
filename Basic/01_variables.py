# Variables

# Snake case variable names.
first_name = 'Juan'
last_name = 'Lopera'
country = 'Colombia'
city = 'Medellin'
age = 24
is_married = False
skills = ['Python', 'JavaScript', 'HTML', 'CSS', 'SQL']
person_info = {
    'first_name': 'Juan',
    'last_name': 'Lopera',
    'country': 'Colombia',
    'city': 'Medellin'
  }

# Printing the values of the variables.
print('First Name:', first_name)  # print() --> print the value of the variable.
print(len(first_name))            # len() --> print the length of the variable. (4)
print('Last Name:', last_name)
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in a line.
first_name, last_name, country, age, is_married = 'Juan', 'Lopera', 'Colombia', 24, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

first_name = input('What is your first name?: ')  # input() --> get the value from the user.
age = input('What is your age?: ')

print(first_name)
print(age)

# Casting data types.
# int to float
num_int = 28
print('num_int', num_int)     # 28
num_float = float(num_int)
print('num_float', num_float) # 28.0

# float to int
gravity = 9.81
print(int(gravity)) # 9

# int to str
num_int = 10
print(num_int)  # 10
num_str = str(num_int)
print(num_str)  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)            # Convert the string to a float first
num_int = int(num_float)              # Then convert the float to an integer
print('num_int', int(num_str))        # 10
print('num_float', float(num_str))    # 10.6
num_int = int(num_float)
print('num_int', int(num_int))        # 10

# str to list
first_name = 'Juan'
print(first_name)                     # 'Juan'
first_name_to_list = list(first_name)
print(first_name_to_list)             # ['J', 'u', 'a', 'n']