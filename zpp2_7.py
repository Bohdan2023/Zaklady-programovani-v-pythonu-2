def mocnina1(base, exponent):
    try:
        if not isinstance(exponent, int):
            raise TypeError("Exponent neni cele cislo")
        if exponent < 0:
            raise ValueError("Exponent je mensi 0")
        if exponent >= 100:
            raise OverflowError("Exponent je prilis velky")
        
    except TypeError as eror:
        return eror
    except ValueError as eror:
        return eror
    except OverflowError as eror:
        return eror
    except Exception as eror:
        return f"neocekavana chyba: {eror}"
    
    result = 1
    for i in range(exponent):
        result = result * base
    return result

# zaklad = 2
# exponent = 0.5

# print(mocnina1(zaklad, exponent))


# def deleni_prvku_v_seznamu(seznam, index, deleni):
#     delka_seznamu = len(seznam)
#     try:
#         if index > delka_seznamu - 1:
#             raise IndexError("Index je mimo rozsah")
#         if deleni == 0:
#             raise ZeroDivisionError("Nemuzete delit na nulu")
        
#     except IndexError as eror:
#         return eror
#     except ZeroDivisionError as eror:
#         return eror
#     result = seznam[index] // deleni
#     return result
    
# seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9]    
# print(deleni_prvku_v_seznamu(seznam, 3, 2))


def faktorial(cislo):
    result = 1
    for i in range(1, cislo + 1):
        result = result * i
    return result

def pascal(n, k):#n=hloubka; k=index
    try:
        if not (isinstance(n, (int)) and isinstance(k, (int))):
            raise TypeError("n a k musi byt int")
        
    
    except TypeError as eror:
        return eror
    
    faktorial_n = faktorial(n)
    faktorial_k = faktorial(k)
    faktorial_n_k = faktorial(n - k)
    result = faktorial_n // (faktorial_k * (faktorial_n_k))
    return result
        
# print(pascal("abc", 3))


def test_all_1(f, sekvence):
    try:
        if not isinstance(sekvence, (list)):
            raise TypeError("sekvence musi byt listem")
    
    except TypeError as eror:
        return eror
    
    counter = 0
    for i in sekvence:
        if f(i) == True:
            counter = counter + 1
    if counter == len(sekvence):
        return True
    else:
        return False
    
funkce = lambda x: x % 2 == 0
sekvence = 1 #[8, 2, 4]

# print(test_all_1(funkce, sekvence))


def aplikuj(f, sekvence):
    try:
        if not isinstance(sekvence, (list)):
            raise TypeError("sekvence musi byt listem")
        
    except TypeError as eror:
        return eror
    
    x = 0
    for item in sekvence:
        x = f(x, item)
    return x      

sekvence3 = 1
f = lambda x, y: x + y

print(aplikuj(f, sekvence3))


def odeber_ze_seznamu1(seznam, x):
    try:
        if not isinstance(seznam, (list)):
            raise TypeError("musi to byt seznam")
        
    except TypeError as eror:
        return eror
    
    if seznam == []:
        return []
    elif seznam[0] == x:
        return seznam[1]
    else:
        seznam[1] = odeber_ze_seznamu1(seznam[1], x)
        return seznam
    
spojovy_seznam = 1 #[1, [2, [3, [4, [5, [6, []]]]]]]
# print(odeber_ze_seznamu1(spojovy_seznam, 6))