# geneticky kod priserky 0 az 9 a je to 5 cisel napr. [0, 5, 8, 9, 1]
# najkrajsia je [1,1,1,1,1]
# budu aj mutacie 7%

import random

monsters = []
lenght = 5
cage = []


def create_monster():
    temp = []
    for i in range(5):
        temp.append(random.randint(0, 9))
    return temp


def iq_test(monster: list) -> int:
    return monster.count(1)


def sex(monster1, monster2):
    new_monster = []
    for i in range(lenght):
        percent = random.randint(1, 100)
        if percent <= 7:
            new_monster.append(random.randint(0, 9))
        else:
            percent1 = random.randint(1, 100)
            if percent1 > 50:
                new_monster.append(monster1[i])
            else:
                new_monster.append(monster2[i])
    return new_monster


def bubble_sort(c):
    for i in range(len(c), 0, -1):
        for j in range(i-1):
            if iq_test(c[j]) > iq_test(c[j + 1]):
                c[j], c[j + 1] = c[j + 1], c[j]
    return c


for x in range(10):
    cage.append(create_monster())

for a in range(100):
    bubble_sort(cage)
    cage = cage[len(cage)//2::]
    for y in range(len(cage)):
        cage.append(sex(cage[random.randint(0, 4)], cage[random.randint(0, 4)]))
    print(cage[::-1])
