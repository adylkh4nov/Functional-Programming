"""Ex 1"""
def count_skills(resume: str) -> int:
    """
    Функция принимает строку (резюме) и возвращает количество навыков/умений, перечисленных в резюме.
    """
    skills = resume.split(',')  # разделяем строку на элементы по запятой
    return len(skills)  # возвращаем количество элементов

def print_resume(resume: str):
    """
    Функция принимает строку (резюме) и выводит ее на экран.
    """
    print(resume)


"""resume = 'Актвиность, ответственность, отзывчивость'
print(count_skills(resume))"""



"""Ex 2"""
def func(person):
    list=['Oleg','Volodya']
    for i in list:
        if i == person:
          return 'Студент '+person+' есть в списке'   
        else:
          return 'Студента '+person+' нет в списке'

"""person='Leha'
print(func(person))"""


"""
Ex 3
"""

"""from functools import reduce
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Применяем функцию map для умножения каждого элемента на 2
mapped_nums = list(map(lambda x: x * 2, nums))
print(mapped_nums)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Применяем функцию filter для выбора только четных элементов
filtered_nums = list(filter(lambda x: x % 2 == 0, nums))
print(filtered_nums)  # [2, 4, 6, 8, 10]

# Применяем функцию reduce для нахождения произведения всех элементов
reduced_num = reduce(lambda x, y: x * y, nums)
print(reduced_num)  # 3628800
"""

"""
Ex 4
"""

def calculate_delivery_cost(street_name: str, item_price: float) -> float:
    # список улиц, на которых доставка бесплатна
    free_delivery_streets = ['Аль-Фараби', 'Саина', 'Ташенова', 'Достык']

    # список улиц, на которых стоимость доставки зависит от цены товара
    variable_delivery_streets = ['Абая', 'Манаса', 'Фурманова']

    # определяем стоимость доставки для каждой улицы
    if street_name in free_delivery_streets:
        delivery_cost = 0
    elif street_name in variable_delivery_streets:
        if item_price < 10000:
            delivery_cost = 1000
        else:
            delivery_cost = item_price * 0.1
    else:
        delivery_cost = 500

    return delivery_cost

print(calculate_delivery_cost('Аль',500))

"""
Ex 5
"""

def compose(f, g):
    """
    Принимает на вход две функции f и g и возвращает новую функцию h(x),
    которая является композицией функций f(g(x)).
    """
    def h(x):
        return f(g(x))
    return h

def f(x):
    return x + 1

def g(x):
    return x * 2

h = compose(f, g)
print(h(3))  # результат: 7 (f(g(3)) = f(6) = 7)
