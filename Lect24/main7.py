import re 


mails = "vasya@yandex.ru -  petya@mail.ru, bob@gmail.com"

result = re.findall(r'@\w+.\w+', mails)
print(result)