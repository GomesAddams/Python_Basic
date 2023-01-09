#TASK_1

print("Введіть першу межу діапазона: ")

a = input()

if not a:

    a = 0

print("Введіть другу межу діапазона: ")

b = input()

range_x = range(int(a), int(b))

print("Введіть будьяке число: ")

x = input()

if int(x) in range_x:

    print(x, bool(x))

else:

    print(x, bool(False))


#TASK_2

arithmetic = {"a": 4, "b": 5}

def summ(a, b):

    return a + b

print(summ(**arithmetic))

def subtraction(a, b):

    return a - b

print(subtraction(**arithmetic))

def multiplication(a, b):

    return a * b

print(multiplication(**arithmetic))

def division(a, b):

    return a / b

print(division(**arithmetic))

def modulus(a, b):

    return a % b

print(modulus(**arithmetic))

def exponentiation(a, b):

    return a ** b

print(exponentiation(**arithmetic))

def floor_division(a, b):

    return a // b

print(floor_division(**arithmetic))

#TASK_3


print("Введіть будьяке слово: ")

word = input()

if str(word) == str(word)[::-1]:

    print("Palindrome")

else:

    print("Not Palindrome")


#TASK_4

print("Введіть будьяку стрічку: ")

word_str = input()

if __name__ == '__main__':

    s = word_str

    chars = "@#$%~*"

    res = s.translate(str.maketrans('', '', chars))
    print(res)



