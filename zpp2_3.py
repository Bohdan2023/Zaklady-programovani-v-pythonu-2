def test_all_1(f, sekvence):
    counter = 0
    for i in sekvence:
        if f(i) == True:
            counter = counter + 1
    if counter == len(sekvence):
        return True
    else:
        return False
funkce = lambda x: x % 2 == 0
sekvence = [2, 4, 7, 8]
#print(test_all_1(funkce, sekvence))


def test_any_2(f, sekvence):
    counter = 0
    for i in sekvence:
        if f(i) == True:
            counter = counter + 1
    if counter >= 1:
        return True
    else:
        return False
funkce1 = lambda x: x % 2 == 0
sekvence1 = [1, 5, 3, 5, 7]
#print(test_any_2(funkce1, sekvence1))


def mapovani(f, sekvence):
    seznam = []
    for item in sekvence:
        seznam.append(f(item))
    return seznam
funkce2 = lambda x: x + x  
sekvence2 = [1, 2, 3, 5, 7]
#print(mapovani(funkce2, sekvence2))


def aplikuj(f, sekvence):
    x = 0
    for item in sekvence:
        x = f(x, item)
    return x      
sekvence3 = [1, 2, 3, 4, 5, 6]
f = lambda x, y: x + y
print(aplikuj(f, sekvence3))