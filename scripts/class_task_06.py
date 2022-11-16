# Поиск самых высокооплачиваемых работников с помощью спискового включения

# нужно найти всех сотрудников, 
# зарабатывающих по крайней мере 100 000 долларов в год

employees = {'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121}



for name, salary in employees.items():
    if salary >= 100000:
        print(name)
