# Задача 2
# Создайте список "города" с именами любых городов
# Количество элементов в списке "города" не меньше 3!

cities_list = ['Москва', 'Париж', 'Берлин']

# Создайте список списков населения перечисленных городов

people_list = [
    [cities_list[0], 12000000],
    [cities_list[1], 2000000],
    [cities_list[2], 3000000],
]

# Выведите на консоль население второго города в списке в формате
# Население Москвы - ХХ человек

print(f'Население Парижа - {people_list [1][1]} человек')

# Выведите на консоль общий размер населения перечисленных городов как сумму населения всех городов
# Итого размер населения - ХХ человек

total = people_list[0][1] + people_list[1][1] + people_list[2][1]
print(f'Итого размер населения - {total} человек')
