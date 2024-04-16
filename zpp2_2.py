def faktorial3(n):
    if n < 0:
        return print("zadejte čislo větši než nula")
    if n == 0:
        return 1
    else:
        return n * faktorial3(n - 1)
#print(faktorial3(3))


def faktorialkonec4(n, akumulator):
    if n < 0:
        return print("zadejte čislo větši než nula")
    if n == 0:
        return akumulator
    else:
        return faktorialkonec4(n - 1, akumulator * n)
#print(faktorialkonec4(5, 1))#akumulator vždy 1


def hloupafunk2(start, end):
    if start <= end:
        result = 0
        for i in range(start, end + 1):
            result = result + i
        return result
#print(hloupafunk2(1, 4))

def delkaseznamu5(seznam):
    if not seznam:
        return 0
    else:
        return 1 + delkaseznamu5(seznam[1:])
    
#print(delkaseznamu5([1, 2, 3]))


def mocnina_rekurzivni_1(zaklad, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return zaklad
    else:
        return zaklad * mocnina_rekurzivni_1(zaklad, exponent - 1)
#print(mocnina_rekurzivni_1(2, 3))


def mocnina_rekurzivni_koncova_1(zaklad, exponent, akumulator):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return akumulator * zaklad
    else:
        return mocnina_rekurzivni_koncova_1(zaklad, exponent - 1, akumulator * zaklad)
#print(mocnina_rekurzivni_koncova_1(2, 3, 1))#akumulator vždy 1


def faktorial(cislo):
    result = 1
    for i in range(1, cislo + 1):
        result = result * i
    return result

def pascal(n, k):#n=hloubka; k=index
    faktorial_n = faktorial(n)
    faktorial_k = faktorial(k)
    faktorial_n_k = faktorial(n - k)
    result = faktorial_n // (faktorial_k * (faktorial_n_k))
    return result
        
print(pascal(0, 0))