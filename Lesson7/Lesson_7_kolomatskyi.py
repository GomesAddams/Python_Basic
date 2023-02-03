#TASK_1


def get_domain_names(file_name):
    with open(file_name, 'r') as f:
        domain_list = [line.strip().replace('.', '') for line in f]
    return domain_list

domains = get_domain_names("domains.txt")
print(domains)


#TASK_2

with open("names.txt", "w") as file:
    file.write("1,Шевченко,UKR\n")
    file.write("2,Orwell,UK\n")
    file.write("3,Williams,Australia\n")
    file.write("4,Gretski,Canada\n")
    file.write("5,Brown,New Zealand\n")

def get_surnames(file_name):
    surnames = []
    with open(file_name, 'r') as file:
        for line in file:
# Розділіть рядок комою
            parts = line.split(',')
# Додавання прізвище (індекс 1) до списку прізвищ
            surnames.append(parts[1])
    return surnames

# Приклад використання:
surnames = get_surnames('names.txt')
print(surnames)


#TASK_3

import re
from datetime import datetime

def get_dates(file_name):
    dates = []
    with open(file_name, 'r') as file:
        for line in file:
# Використовуйте регулярний вираз для пошуку дат у форматі  "ddth mmm yyyy"
            match = re.search(r'\d{1,2}(st|nd|rd|th)\s\w+\s\d{4}', line)
            if match:
                date_str = match.group()
# Розбір рядка дати в об'єкт datetime
                date = datetime.strptime(date_str, '%d%s %B %Y')
# Додавання дату як словник до списку дат
                dates.append({"date": date.strftime('%d %B %Y')})
    return dates

# Приклад використання:
dates = get_dates('authors.txt')
print(dates)



#TASK_4

def sort_file_by_length(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines.sort(key=len)
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line)

# fklndvkl
