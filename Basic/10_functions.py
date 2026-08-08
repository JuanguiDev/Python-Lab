# Functions
#? Function without Paremeters
def generate_full_name():
  first_name = 'Juan'
  last_name = 'Lopera'
  space = ' '
  full_name = first_name + space + last_name
  print(full_name)

generate_full_name()

def add_two_numbers ():
  num_one = 2
  num_two = 3
  total = num_one + num_two
  print(total)
add_two_numbers()

#? Function Returning a Value
def generate_full_name():
  first_name = 'Juan'
  last_name = 'Lopera'
  space = ' '
  full_name = first_name + space + last_name
  return full_name
print(generate_full_name())

# Function with parameters
#? Single Parameter
def greeting(name):
  message = name + ', welcome to Python!!'
  return message
print(greeting('Juan'))

def square_number(x):
  return x * x
print(square_number(2))

def area_of_circle (r):
  PI = 3.14
  area = PI * r ** 2
  return area
print(area_of_circle(10))

#? Two Parameters
def generate_full_name(first_name, last_name):
  space = ' '
  full_name = first_name + space + last_name
  return full_name
print(generate_full_name('Juan', 'Lopera'))

def sum_two_numbers (num_one, num_two):
  sum = num_one + num_two
  return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
  age = current_year - birth_year
  return age
print('Age: ', calculate_age(2026, 2002))

# Function with Default Parameters
def greetings (name = 'Peter'):
  message = name + ', welcome to Python for Everyone!'
  return message
print(greetings())
print(greetings('Juan'))

# Arbitrary Number of Arguments
def sum_all_nums(*nums):
  total = 0
  for num in nums:
    total += num     # same as total = total + num 
  return total
print(sum_all_nums(2, 3, 5)) # 10


# Default and Arbitrary Number of Parameters in Functions
def generate_groups (team,*args):
  print(team)
  for i in args:
    print(i) 
generate_groups('Team-1','Juan','Brook','David','Eyob')

# Dictionary unpacking
# Define a function that takes two arguments: 'name' and 'location'
def greet(name, location):
  # Print a greeting message using the provided arguments
  print("Hi there", name, "how is the weather in", location)

# Create a dictionary with keys matching the function's parameter names
my_dict = {"name": "Alice", "location": "New York"}
greet(**my_dict)

# Function as a Parameter of Another Function
#You can pass functions around as parameters
def square_number (n):
  return n ** n

def do_something(f, x):
  return f(x)
print(do_something(square_number, 3)) # 27