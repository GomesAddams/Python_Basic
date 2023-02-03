#TASK_1

def check_range(num_x, from_num=0):
    if num_x in range(from_num, to_num):
        return (bool(num_x))
    else:
        return (bool(num_x))
print("Введіть першу межу діапазона: ")
from_num = input()
print("Введіть другу межу діапазона: ")
to_num = input()
print("Введіть будьяке число: ")
num_x = input()
print(bool(num_x))



#TASK_2

def arithmetic(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    elif operation == '**':
        return a ** b
    elif operation == '%':
        return a % b
    elif operation == '//':
        return a // b
    else:
        return 'Operation cannot be reversed'

print(arithmetic(a=2, b=3, operation='+'))
print(arithmetic(a=2, b=3, operation='-'))
print(arithmetic(a=2, b=3, operation='*'))
print(arithmetic(a=2, b=3, operation='/'))
print(arithmetic(a=2, b=3, operation='**'))
print(arithmetic(a=2, b=3, operation='%'))
print(arithmetic(a=2, b=3, operation='//'))
print(arithmetic(a=2, b=3, operation='^'))

#TASK_3


print("Введіть будьяке слово: ")

word_x = input()

def is_palindrome(word_x):

    if str(word_x) == str(word_x)[::-1]:

        print("Palindrome")

    else:

        print("Not Palindrome")


#TASK_4

print("Введіть будьяку стрічку: ")

word_str = input()

def spec_char(word_str):

if __name__ == '__main__':

    s = word_str

    chars = "@#$%~*"

    res = s.translate(str.maketrans('', '', chars))
    print(res)



