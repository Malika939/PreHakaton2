b = int(input("введите ваш вес"))
if b < 50: 
    print("вам нужно набрать вес")
    d = 50 - b
    print(d, "кг веса вам нехватет")
elif b > 80:
    print("вам нужно сбросить вес")
    g = b - 80 
    print(g, "кг вам нужно сбросить")
else:
    print("у вас правильный вес")

a = int(input("введите ваш рост"))   
if a < 150:
    print("вы низкий")
elif a > 170:
    print("вы высокий")
else:
    print("у вас средний рост")