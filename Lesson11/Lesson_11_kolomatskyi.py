#TASK_1

def calculate_gpa(hours, quality_points):
    return quality_points / hours

def academic_warning(hours, gpa):
    if hours < 30 and gpa < 1.5:
        return True
    elif hours < 60 and gpa < 1.75:
        return True
    elif hours >= 60 and gpa < 2.0:
        return True
    else:
        return False

filename = "students_data.txt"
try:
    with open(filename, 'r') as f:
        students_data = f.readlines()
except FileNotFoundError:
    print("Error: The file '" + filename + "' does not exist.")
    exit(1)

warned_students = []
for student_data in students_data:
    student_data = student_data.strip().split(" ")
    try:
        name = student_data[0]
        hours = int(student_data[1])
        quality_points = float(student_data[2])
    except (ValueError, IndexError):
        print("Error: Invalid input format for student '" + name + "'")
        continue

    gpa = calculate_gpa(hours, quality_points)
    if academic_warning(hours, gpa):
        warned_students.append(name)

if warned_students:
    print("Students on academic warning:")
    for student in warned_students:
        print(student)
else:
    print("No students on academic warning.")


#TASK_2

class ExceptionLineTooLong(Exception):
    pass

def read_file_with_line_limit(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if len(line) > 80:
                raise ExceptionLineTooLong("Line {} is too long".format(i + 1))
        return lines

try:
    lines = read_file_with_line_limit("test.txt")
    print("Lines in the file:")
    print(*lines, sep='\n')
except ExceptionLineTooLong as e:
    print(e)
except Exception as e:
    print("An error occurred:", e)


#TASK_3

import os

class FileUtils:
    @staticmethod
    def fileExists(filename):
        try:
            return os.path.exists(filename)
        except:
            return False

    @staticmethod
    def isInt(string):
        try:
            int(string)
            return True
        except:
            return False

    @staticmethod
    def isDouble(string):
        try:
            float(string)
            return True
        except:
            return False
