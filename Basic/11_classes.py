# Classes
class Person():
  pass

print(Person)

# Creating an Object
p = Person()
print(p)

# Class Constructor
class Person():
  def __init__(self, name):
    self.name = name

p = Person('Juan')
print(p.name)
print(p)

class Person():
  def __init__(self, first_name, last_name, age, country, city):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.country = country
    self.city = city

p = Person('Juan', 'Lopera', 24, 'Colombia', 'Medellín')
print(p.first_name)
print(p.last_name)
print(p.age)
print(p.country)
print(p.city)

class Person():
  def __init__(self, first_name, last_name, age, country, city):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.country = country
    self.city = city
  def person_info(self):
    return f'{self.first_name} {self.last_name} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Juan', 'Lopera', 24, 'Colombia', 'Medellín')
print(p.person_info())

# Method to Modify Class Default Values
class Person():
  def __init__(self, first_name='Juan', last_name='Lopera', age=24, city='Medellín', country='Colombia'):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.city = city
    self.country = country
    self.skills = []
  def person_info(self):
    return f'{self.first_name} {self.last_name} is {self.age} years old. He lives in {self.city}, {self.country}'
  def add_skill(self, skill):
    self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')

p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

# Inheritance
class Student(Person):
  pass

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

# Overriding parent method
class Student(Person):
  def __init__(self, first_name='Juan', last_name='Lopera', age=24, city='Medellín', country='Colombia', gender='Male'):
    self.gender = gender
    super().__init__(first_name, last_name, age, country, city)
  def person_info(self):
    gender = 'He' if self.gender == 'male' else 'she'
    return f'{self.first_name} {self.last_name} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
