"""
Конкурсный отбор
Напишите программу, кот. выводит список хорошистов и отличников в классе.

Формат входных данных
На вход подается натуральное число n, далее следует n строк с фамилией школьника и его оценкой на каждой из них.

Формат выходных данных
Программа должна вывести сначала все введённые строки с фамилиями и оценками учеников в том же порядке.
Затем следует пустая строка, а затем выводятся строки с фамилиями и оценками хорошистов и отличников (в том же порядке).

Примечание 1. Оценка ученика – это натуральное число от 1 до 5.
Примечание 2. Гарантируется, что в классе есть хотя бы один хорошист – обладатель оценки 4, или отличник – получивший 5.
"""

# n = int(input())
# students = [input() for _ in range(n)]

# print(*students, sep='\n')
# print()
# for i in students:
#     if i[-1] in ('4', '5'):
#         print(i)

# get input as list of tuples
# students = [tuple(input().split()) for _ in range(n)]  # [('Круглов', '4'), ('Кузнецов', '5'), ('Федин', '4'), ('Тарасов', '2'), ('Словецкий', '3')]

colors = ('red', 'green', 'blue', 'cyan')
a, b, _, _ = colors

# print(a)
# print(b)


# Recursion
def factorial(n):
    print(f'Factorial called with {n}.')
    if n < 2:
        print('Returning 1.')
        return 1
    result = n * factorial(n - 1)
    print(f'Returning {result} for factorial of {n}.')
    return result


# factorial(3)

# def is_power_of(number, base):
#     if number < base:
#         return number == base ** 0
#     return is_power_of(number / base, base)
#
#
# print(is_power_of(8,2)) # Should be True
# print(is_power_of(64,4)) # Should be True
# print(is_power_of(70,10)) # Should be False
# print(is_power_of(1000,10))

def even_numbers(maximum):

    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all even numbers
    # up to and including the "maximum" value, but excluding 0.
    for i in range(1, maximum + 1):

        # Complete the body of the loop by appending the even number
        # followed by a space to the "return_string" variable.
        if not i % 2:
            return_string += str(i) + ' '

    # This .strip command will remove the final " " space at the end of
    # the "return_string".
    return return_string.strip()

# print(even_numbers(6))  # Should be 2 4 6
# print(even_numbers(10)) # Should be 2 4 6 8 10
# print(even_numbers(1))  # No numbers displayed
# print(even_numbers(3))  # Should be 2
# print(even_numbers(0))  # No numbers displayed


# num1 = 0
# num2 = 0
#
# for x in range(5):
#     num1 = x
#     for y in range(14):
#         num2 = y + 3
#
# print(num1 + num2)

schedule = "Last year’s annual report will be released in March 2023"
old_date = '2023'
new_date = '2024'
p = len(old_date)
new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)
# print(schedule[:-p])
# print(schedule[-p:])
# print(schedule[:-p] + schedule[-p:])
# print(new_schedule)


def groups_per_user(group_dictionary):
    user_groups = {}

    for group, users in group_dictionary.items():
        for user in users:
            if user in user_groups:
                user_groups[user].append(group)
            else:
                user_groups[user] = [group]

    return user_groups


# print(groups_per_user({"local": ["admin", "userA"],
#                        "public": ["admin", "userB"],
#                        "administrator": ["admin"]}))


def invert_resource_dict(resource_dictionary):
    new_dictionary = {}

    for resource_group, resources in resource_dictionary.items():
        for resource in resources:
            if resource in new_dictionary:
                new_dictionary[resource].append(resource_group)
            else:
                new_dictionary[resource] = [resource_group]

    return(new_dictionary)


# print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
#         "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))
#
# wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# wardrobe.update(new_items)
# print(wardrobe)

# def sales_prices(item_and_price):
#     item = ""
#     price = ""
#
#     item_or_price = item_and_price.split()
#     for x in item_or_price:
#         if x.isalpha():
#             item += x + " "
#         else:
#             price = x
#
#     item = item.strip()
#
#     return "{} are on sale for ${}".format(item, price)
#
#
# print(sales_prices("Winter fleece jackets 49.99"))
#
#
# class City:
#     name = ""
#     country = ""
#     elevation = 0
#     population = 0
#
#
# city1 = City()
# city1.name = "Cusco"
# city1.country = "Peru"
# city1.elevation = 3_399
# city1.population = 358_052
#
# city2 = City()
# city2.name = "Sofia"
# city2.country = "Bulgaria"
# city2.elevation = 2_290
# city2.population = 1_241_675
#
# city3 = City()
# city3.name = "Seoul"
# city3.country = "South Korea"
# city3.elevation = 38
# city3.population = 9_733_509
#
#
# def max_elevation_city(min_population):
#     return_city = City()
#
#     if min_population < city1.population  < city2.population < city3.population:
#         return_city = city1
#
#     if city1.population < min_population < city2.population < city3.population:
#         return_city = city2
#
#     if city1.population < city2.population < min_population < city3.population:
#         return_city = city3
#
#     # Format the return string
#     if return_city.name:
#         return f'{return_city.name}, {return_city.country}'
#     else:
#         return ""
#
#
# print(max_elevation_city(100_000)) # Should print "Cusco, Peru"
# print(max_elevation_city(1_000_000)) # Should print "Sofia, Bulgaria"
# print(max_elevation_city(10_000_000)) # Should print ""
#
#
# class Clothing:
#     stock = {'name': [], 'material': [], 'amount': []}
#
#     def __init__(self, name):
#         material = ""
#         self.name = name
#
#     def add_item(self, name, material, amount):
#         Clothing.stock['name'].append(self.name)
#         Clothing.stock['material'].append(self.material)
#         Clothing.stock['amount'].append(amount)
#
#     def Stock_by_Material(self, material):
#         count = 0
#         n = 0
#         for item in Clothing.stock['material']:
#             if item == material:
#                 count += Clothing.stock['amount'][n]
#                 n += 1
#         return count
#
#
# class Shirt(Clothing):
#     material = "Cotton"
#
#
# class Pants(Clothing):
#     material = "Cotton"
#
#
# polo = Shirt("Polo")
# sweatpants = Pants("Sweatpants")
# polo.add_item(polo.name, polo.material, 4)
# sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
# current_stock = polo.Stock_by_Material("Cotton")
# print(current_stock)

import datetime

now = datetime.datetime.now()
print(now)

# print(now.year, now.day, now.month, now.second)

# Get my IP
# import requests
#
# response = requests.get('https://httpbin.org/ip')
# print(f'Your IP is {response.json()["origin"]}')


class Animal:
    name = ""
    category = ""

    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category


class Turtle(Animal):
    category = 'reptile'


class Snake(Animal):
    category = 'reptile'


class Zoo:
    def __init__(self):
        self.current_animals = {}

    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result


zoo = Zoo()


turtle = Turtle("Turtle")  # create an instance of the Turtle class
snake = Snake("Snake")  # create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile"))  # should be 2

import random
n = random.random()*10+1
print(n)
