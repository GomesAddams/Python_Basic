#TASK_1

import json

data = [
    {
        "name": "John Doe",
        "age": 32,
        "email": "johndoe@example.com",
        "address": "123 Main St, Anytown USA",
        "phone": "555-555-5555"
    },
    {
        "name": "Jane Doe",
        "age": 29,
        "email": "janedoe@example.com",
        "address": "456 Main St, Anytown USA",
        "phone": "555-555-5556"
    },
    {
        "name": "Jim Smith",
        "age": 45,
        "email": "jimsmith@example.com",
        "address": "789 Main St, Anytown USA",
        "phone": "555-555-5557"
    },
    {
        "name": "Sarah Connor",
        "age": 38,
        "email": "sarahconnor@example.com",
        "address": "111 Main St, Anytown USA",
        "phone": "555-555-5558"
    },
    {
        "name": "Tom Wilson",
        "age": 25,
        "email": "tomwilson@example.com",
        "address": "222 Main St, Anytown USA",
        "phone": "555-555-5559"
    },
    {
        "name": "Emily Davis",
        "age": 40,
        "email": "emilydavis@example.com",
        "address": "333 Main St, Anytown USA",
        "phone": "555-555-5560"
    },
    {
        "name": "Bruce Willis",
        "age": 35,
        "email": "brucewillis@example.com",
        "address": "444 Main St, Anytown USA",
        "phone": "555-555-5561"
    },
    {
        "name": "Russel Peters",
        "age": 28,
        "email": "russelpeters@example.com",
        "address": "555 Main St, Toronto Canada",
        "phone": "555-555-5562"
    },
    {
        "name": "Jennifer Gardner",
        "age": 33,
        "email": "jennifergardner@example.com",
        "address": "666 Main St, Anytown USA",
        "phone": "555-555-5563"
    },
    {
        "name": "Wednesday Addams",
        "age": 26,
        "email": "wednesdayaddams@example.com",
        "address": "777 Main St, Anytown USA",
        "phone": "555-555-5564"
    }
]

with open('database.json', 'w') as f:
    json.dump(data, f, indent=4)


#TASK_2


import csv

def parse_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        students = []
        for row in reader:
            student = {}
            for i, header in enumerate(headers):
                student[header] = row[i]
            students.append(student)
        return students


students = parse_csv('students.csv')
print(students)


#TASK_3

import csv
import datetime

def generate_csv(a_list):
    header = ['temperature', 'date', 'locations', 'weather']
    filename = "results.csv"

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for data in a_list:
            row = []
            for key, value in data:
                if isinstance(value, datetime.date):
                    value = value.strftime("%m/%d/%Y")
                elif isinstance(value, tuple):
                    value = ",".join(value)
                row.append(value)
            writer.writerow(row)
    print(f"CSV file '{filename}' has been generated.")

meteo = [(('temperature', 42),
   ('date', datetime.date(2017, 1, 22)),
   ('locations', ('Berlin', 'Paris')),
   ('weather', 'sunny')),
  (('temperature', -42),
   ('date', datetime.date(2017, 1, 22)),
   ('locations', ('Marseille', 'Moscow')),
   ('weather', 'cloudy'))]

generate_csv(meteo)
