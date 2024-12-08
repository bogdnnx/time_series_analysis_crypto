from random import *
import datetime
for _ in range(5):
    n = 10 ** 6
    count = 0
    start = datetime.datetime.now()
    #print('Время старта: ' + str(start))
    for _ in range(n):
        days_seen = set()
        for _ in range(30):
            day = randint(1, 365)
            if day in days_seen:
                count += 1  # Если есть совпадение, увеличиваем счетчик
                break
            days_seen.add(day)

    # Рассчитываем вероятность
    res = count / n
    finish = datetime.datetime.now()
    #print('Время окончания: ' + str(finish))
    print('Время работы: ' + str(finish - start))
    print(f"С вероятностью в {res*100}% у двух людей из 30 день рождения в один и тот же день")