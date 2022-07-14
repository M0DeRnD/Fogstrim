# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


# words = "Measuring programming progress by lines of code is like measuring aircraft building progress by weight."
# temp = list(words)
# del temp[2::3]
# result = "".join(temp)
#
#
# print(result)


# a = input("Введите число а: ")
# b = input("Введите число b: ")
#
# if a>b:
#     print("a>b")
# else:
#     print("a<b")


# x1 = 31.16763283472605
# x2 = 95.74722237090143
# y1 = 45.60092056377414
# y2 = -18.73510183270119
#
# def area(x1, y1, x2, y2):
#     k1 = x2 - x1
#     k2 = y2 - y1
#     square = k1 * k2 / 2
#     return round(square.__abs__(),1)
#
# print(area(-1,-1,-3,-3))
import math
from typing import Any

# def is_pow(x):
#     answer = 0
#     for i in range(2,10):
#         temp = pow(x,1/i)
#         if temp.is_integer():
#             answer += 1
#     if answer >= 1:
#         return True
#     else:
#         return False
#
#
# print(is_pow(5))


#########################################################################

# list_goods = ['молоко Хорская Буренка:70:5\n', 'молоко Фермерское:55:10\n', 'молоко Простоквашино:66:5\n',
#               'хлеб серый хлебозавод:30:20\n', 'яйцо 1 кат.:30:40\n', 'яйцо 2 кат.:30:40\n', 'яйцо 3 кат.:30:40\n',
#               'макароны Макфа,рожки:30:10\n', 'макароны Макфа,спагетти:30:10\n', 'сахар 1кг:40:30\n',
#               'соль 1 кг:35:30\n', 'масло сливочное:100:20\n', 'масло подсолнечное:100:20\n', 'говядина 1кг:250:10\n',
#               'свинина 1кг:220:10\n', 'баранина 1кг:210:10\n', 'филе куриное 1кг:200:10\n',
#               'грудка куриная 1кг:225:10\n', 'голень куриная 1кг:230:10\n', 'крылышки куриные 1кг:180:10\n',
#               'рыба мороженая, Кета 1кг:400:5\n', 'рыба мороженая, Треска 1кг:300:5\n',
#               'рыба мороженая, Горбуша 1кг:300:5\n', 'рыба мороженая, Окунь 1кг:300:5\n',
#               'чай черный Greenfield 10 пак.:50:20\n', 'Чай черный Lipton 10 пак.:60:20\n',
#               'чай зеленый Greenfield 10 пак.:50:20\n', 'Чай зеленый Lipton 10 пак.:60:20\n',
#               'мука пшеничная Весёлый мельник 1кг.:40:20\n', 'мука пшеничная Весёлый мельник 2кг.:60:10\n',
#               'хлеб ржаной хлебозавод:50:20\n', 'сушки 1кг.:45:20\n', 'пряники 1кг.:55:20\n', 'булочки плюшки:30:10\n',
#               'пирожки с брусникой:30:10\n', 'пирожки с картошкой:30:2\n', 'пирожки с вишней:30:10\n',
#               'рис шлифованный 1кг:40:10\n', 'рис круглозерный 1кг:45:10\n', 'пшено 1кг:50:30\n',
#               'крупа гречневая 1кг:60:30\n', 'вермишель Макфа 1кг:45:20\n', 'картофель 1кг:60:50\n',
#               'капуста белокочаная 1кг:60:50\n', 'лук репчатый 1кг:40:50\n', 'морковь 1кг:55:50\n',
#               'яблоки Новая Зеландия 1кг:60:120']
# mean = 0
# count_all = 0
# summ = 0
# max_int = 0
# min_int = 1000
# set_goods = set()
#
# for good in list_goods:
#     price = int(good.split(':')[1])
#     summ += price
#     count_all += 1
#
#     if price > 100:
#         set_goods.add(good)
#
# dict_goods = {}
# dict_goods['mean'] = summ / count_all
# dict_goods['count all'] = count_all
# dict_goods['summa'] = summ
#
# print(dict_goods)
#
#
# def work_with_list(list_goods, is_max_min):
#     '''Функция возвращает максимальную или минимальную стоимость товаров'''
#
#     list_result = []
#     max = 0
#     min = 1000
#
#     for good in list_goods:
#         price = int(good.split(':')[1])
#
#         if price > max:
#             max = price
#         if price < min:
#             min = price
#
#     if is_max_min:
#         for good in list_goods:
#             price = int(good.split(':')[1])
#             name = good.split(':')[0]
#             if price == max:
#                 list_result.append(name)
#     else:
#         for good in list_goods:
#             price = int(good.split(':')[1])
#             name = good.split(':')[0]
#             if price == min:
#                 list_result.append(name)
#
#     return list_result
#
# list_max = work_with_list(list_goods,is_max_min=True)
# list_min = work_with_list(list_goods,is_max_min=False)
# print(list_max)
# print(list_min)



# list_number = [1,2,3,4]
# print(list_number)
# list_number.append(5)
# result = list_number.copy()
# print(result)



# primer = {"a": 4, "b": 6, "c": 7, "d": 9}
#
# print(primer.keys())
# answer = 0
# for value in primer.values():
#     temp = value
#     answer += temp
# print(answer)


# set_test = set('qwerty')
# set_test.add('l')
#
# # frozen_set_test = frozenset('qwerty')
# # frozen_set_test.add('l')
#
# print(set_test)


# spisok = [1, 2, 3, 4, 5]
#
# for count,value in enumerate(spisok):
#     print(count,value)
#
# mnojestvo = set(spisok)
#
# print(mnojestvo,type(mnojestvo))


# test_string = "1 2 3 4 5"
#
# print(list(test_string.split()))

# test_list = ['hello', 'my', 'freind']
# a = ' '.join(test_list)
# print(a)

# list_test = [1, 3, 4, 'hello', 4, 5, 'Python']
# for i in list_test:
#     print(f"Сейчас будет {i}.")



# class Animal:
#     def __init__(self, name="",food=""):
#         self.name = name
#         self.food = food
#
#     def eat(self):
#         print(self.name, "Покушал")
#
# class Cat(Animal):
#     def __init__(self,name="",tail=True):
#         super().__init__(name,"хищник")
#         self.tail = tail
#
#     def meow(self):
#         print("Я", self.name, "meow")
#
# vasya = Cat("Васька",False)
#
# vasya.meow()


from datetime import datetime
from datetime import timedelta
from exception import EndingExpirationDate

class Good:
  '''Класс товара'''

  def __init__(self, name, count, price, production_date, expiration_day):
      self.name = name
      self.count = count
      self.price = price
      self.production_date = datetime.strptime(production_date, '%Y-%m-%d')
      self.expiration_day = expiration_day

  def __str__(self):
      return f'{self.name}'

  def check_expiration_date(self):
      '''Проверка срока годности товара'''

      date_now = datetime.now()
      date_ending_expiration = self.production_date + timedelta(days=int(self.expiration_day))

      if date_ending_expiration > date_now:
          return True
      else:
          raise EndingExpirationDate
class GoodList:
  '''Класс со списком товаров'''
  def __init__(self):
      self.good_list = []
  def add_good_in_list(self, good: Good):
      '''Добавляем товар в список'''
      try:
          good.check_expiration_date()
          self.good_list.append(good)
      except EndingExpirationDate:
          print(f"Товар {good} с истекшим сроком годности")
          return None
  def remove_good_from_list(self, name: str):
      '''Удаляем товар из списка по имени (первый найденный)'''
      for index, good in enumerate(self.good_list):
          if good.name == name:
              del self.good_list[index]
              break
  def clear_by_expiration_date(self):
      '''Очищает по сроку годности'''
      for good in self.good_list:
          try:
              good.check_expiration_date()
          except EndingExpirationDate:
              self.remove_good_from_list(good.name)
  def get_mean_price(self):
      '''Получаем среднюю цену товаров'''
      sum_price = 0
      sum_count = 0
      for good in self.good_list:
          sum_price += int(good.price)
          sum_count += int(good.count)
      print(f'sum goods = {sum_price}')
      print(f'sum count = {sum_count}')
      mean = 0
      if sum_count != 0:
          mean = sum_price / sum_count
      return mean
  def get_good_with_max_price(self):
      '''Получаем товар с максимальной ценой'''
      name = ''
      max_price = 0
      for good in self.good_list:
          if good.price > max_price:
              max_price = good.price
              name = good.name
      return name
  def get_good_with_min_price(self):
      '''Получаем товар с минимальной ценой'''
      name = ''
      min_price = 10000
      for good in self.good_list:
          if good.price < min_price:
              min_price = good.price
              name = good.name
      return name
  def get_good_with_max_count(self):
      '''Получаем товар с максимальным количеством'''
      name = ''
      max_count = 0
      for good in list_with_goods:
          if good.count > max_count:
              max_count = good.count
              name = good.name
      return name
  def get_good_with_min_count(self):
      '''Получаем товар с максимальным количеством'''
      name = ''
      min_count = 0
      for good in list_with_goods:
          if good.count < min_count:
              min_count = good.count
              name = good.name
      return name
good_list = GoodList()
with open('file.txt', 'r') as file:
  list_with_goods = file.readlines()
  for str_good in list_with_goods:
      list_good = str_good.split(':')
      name = list_good[0]
      price = list_good[1]
      count = list_good[2]
      production_date = list_good[3]
      expiration_day = list_good[4]
      good_list.add_good_in_list(Good(name, price, count, production_date, expiration_day))
      good_list.get_mean_price()

