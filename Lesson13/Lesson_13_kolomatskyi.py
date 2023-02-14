#TASK_1

def check_string(string):
    for char in string:
        if not char.isalnum() or char.isupper():
            return False
    return True

my_string = "abc123def"
if check_string(my_string):
    print("String is valid")
else:
    print("String is not valid")


#TASK_2

import re

# Визначення регулярного виразу для перевірки URL-адрес
url_pattern = re.compile(r'https?://\S+')

# Зразок тексту стрічки
feed_text = "Check out this cool website: https://www.python.com"

# Пошук URL-адрес в стрічці
urls = re.findall(url_pattern, feed_text)

# Вивести URL-адреси, знайдені у стрічці
print(urls)

#TASK_3

string_list = ["example(.com)", "github(.com)", "stackoverflow(.com)"]

for i in range(len(string_list)):
    string_list[i] = string_list[i].split('(')[0]

print(string_list)


#TASK_4

string = "YouWearGuiltLikeShacklesOnYourFeetLikeAHaloInReverse (c) DepecheMode"
new_string = ""
for char in string:
    if char.isupper() and new_string != "":
        new_string += " "
    new_string += char
print(new_string)


