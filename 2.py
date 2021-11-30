from random import randint
print("Доброго времени суток! Вас приветствует бот Big Dick Bot. Задавайте свои вопросы!!!")
list_request = ["Я ничего не понял!", "Хэй, у меня нет вариантов!", "Поясни пожалуйста получше!", "Что за херню ты несёшь?????","Говори на русском блять!"]
a = 0
while True:
    z = input()
    z = z.split()
    slovo = ""
    for i in z:     
        slovo  = slovo + i
    with open("1.txt", "r") as inf:
        for line in inf:
            line = line.strip()
            line = line.split(":")
            if line[0]==slovo:
                print(line[1])
                a = -1
            elif slovo == "Отпустипрошу":
                a = -1
                break
    a = a + 1
    if slovo == "Отпустипрошу":
        print("Ладно, ты всё ровно неинтересный фу")
        break
    elif a == 1:
        break
if a == 1:
    print(list_request[randint(0, 4)])
    k = input()
    print("Окей понял, ", k)
    dobav = slovo + ":" + k
    with open("1.txt", "a") as ist:
        ist.write(dobav + '\n')
    
