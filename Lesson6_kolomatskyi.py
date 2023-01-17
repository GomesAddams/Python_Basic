#TASK_1

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_elements = list(filter(lambda x: x in list1, list2))
common_elements.sort()
print(common_elements)

#TASK_2

cars_data = {"BMW": 21, "Mercedes": 18, "VW": 17, "Toyota": 15, "Honda": 16, "Nissan": 20}

# Визначення середної витрати бензину
total_points = 0
for cars in cars_data:
    total_points += cars_data[cars]
average_score = total_points / len(cars_data)

# Відображаються назви автомобілів які мають витрату вище середнього
above_average = []
for cars in cars_data:
    if cars_data[cars] > average_score:
        above_average.append(cars)

print("The average gasoline consumption is: ", average_score)
print("The car above average is : ", above_average)

#TASK_3

task_list = [1, 2, 3, 2, 4, 2, 5, 3, 6, 1]

# Перетворення списку на множину, щоб видалити дублікати
unique_values = set(task_list)

# Визначення кількості різних величин
num_unique_values = len(unique_values)

print("The number of different values is: ", num_unique_values)


#TASK_4

list1 = [int(x) for x in input("Enter the numbers for list1 : ").split()]
list2 = [int(x) for x in input("Enter the numbers for list2 : ").split()]

# Перетворення списку на множину
set1 = set(list1)
set2 = set(list2)

# Знаходження перетин множин
intersection = set1.intersection(set2)

# Перетворення множини зворотньо у список і сортування його
intersection_list = list(intersection)
intersection_list.sort()

print("The numbers that are included in both lists in ascending order are: ", intersection_list)


#TASK_5

text = input("Enter the line of text: ")

# Створення порожнього словника для зберігання частоти з'явлення слів
word_frequencies = {}

# Розділення тексту на слова
words = text.split(" ")

# Повтерення через кожне слово
for word in words:
    # Перевірка, чи є слово вже у словнику
    if word in word_frequencies:
        # Якщо так, то збільшити кількість
        word_frequencies[word] += 1
    else:
        # Якщо ні, доавання до словника з кількістю рівної 1
        word_frequencies[word] = 1

# Друк слів з іхньою кількістю
for word in word_frequencies:
    print("{}: {}".format(word, word_frequencies[word]))
