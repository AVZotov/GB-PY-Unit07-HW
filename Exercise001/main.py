input_string = "пара-ра-рам рам-пам-папам па-ра-па-да"
is_true = "Парам пам-пам"
is_false = "Пам парам"
letter = 'а'


result = len(set(map(lambda x: x.count(letter), input_string.split())))
print(is_true if result == 1 else is_false)
