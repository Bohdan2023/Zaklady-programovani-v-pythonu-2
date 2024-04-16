def odeber_ze_seznamu1(seznam, x):
    if seznam == []:
        return []
    elif seznam[0] == x:
        return seznam[1]
    else:
        seznam[1] = odeber_ze_seznamu1(seznam[1], x)
        return seznam
    
# spojovy_seznam = [1, [2, [3, [4, [5, [6, []]]]]]]
# print(odeber_ze_seznamu1(spojovy_seznam, 6))
# print(spojovy_seznam)
# spojovy_seznam = odeber_ze_seznamu1(spojovy_seznam, 5)
# print(spojovy_seznam)
# spojovy_seznam = odeber_ze_seznamu1(spojovy_seznam, 4)
# print(spojovy_seznam)
# spojovy_seznam = odeber_ze_seznamu1(spojovy_seznam, 3)
# print(spojovy_seznam)
# spojovy_seznam = odeber_ze_seznamu1(spojovy_seznam, 2)
# print(spojovy_seznam)
# spojovy_seznam = odeber_ze_seznamu1(spojovy_seznam, 1)
# print(spojovy_seznam)



def pridej_do_obousmerneho_seznamu(seznam, x):
    predchozi_prvek = []
    while seznam:
       predchozi_prvek = seznam
       seznam = seznam[DALSI_PRVEK]
    seznam.extend([predchozi_prvek, x, []])
    return seznam
        
def odeber_z_obousmerneho_prvni(seznam):
    if seznam[DALSI_PRVEK] == []:
        seznam[DALSI_PRVEK][PREDCHOZI_PRVEK] = []
    return seznam[DALSI_PRVEK]

def odeber_z_obousmerneho_posledni(seznam):
    if seznam[DALSI_PRVEK] == []:
        seznam[PREDCHOZI_PRVEK][DALSI_PRVEK] = []
        return seznam[PREDCHOZI_PRVEK]
        
def odeber_z_obousmerneho_seznamu(seznam, x):
    if seznam == []:
        return []
    if seznam[PREDCHOZI_PRVEK] == [] and seznam[DALSI_PRVEK] == []:
        return []
    if seznam[HODNOTA] == x:
        if seznam[PREDCHOZI_PRVEK] == []:
            return odeber_z_obousmerneho_prvni(seznam)
        elif seznam[DALSI_PRVEK] == []:
            return odeber_z_obousmerneho_posledni(seznam)
        else:
            seznam[PREDCHOZI_PRVEK][DALSI_PRVEK] = seznam[DALSI_PRVEK]
            seznam[DALSI_PRVEK][PREDCHOZI_PRVEK] = seznam[PREDCHOZI_PRVEK]
            return seznam[DALSI_PRVEK]
    seznam[DALSI_PRVEK] = odeber_z_obousmerneho_seznamu(seznam[DALSI_PRVEK], x)
    return seznam

PREDCHOZI_PRVEK = 0
HODNOTA = 1
DALSI_PRVEK = 2



# seznam = []
# pridej_do_obousmerneho_seznamu(seznam, 1)
# pridej_do_obousmerneho_seznamu(seznam, 2)
# pridej_do_obousmerneho_seznamu(seznam, 5)
# pridej_do_obousmerneho_seznamu(seznam, 8)
# pridej_do_obousmerneho_seznamu(seznam, 9)
# print(seznam)
# seznam = odeber_z_obousmerneho_seznamu(seznam, 2)
# print(seznam)
# seznam = odeber_z_obousmerneho_seznamu(seznam, 5)
# print(seznam)
# seznam = odeber_z_obousmerneho_seznamu(seznam, 8)
# print(seznam)
# seznam = odeber_z_obousmerneho_seznamu(seznam, 1)
# print(seznam)


def pridej_do_fronty(fronta, hodnota):
    if not fronta:
        fronta = [hodnota, []]
        return fronta
    uzel = fronta
    predchozi = uzel
    while uzel:
        predchozi = uzel
        uzel = uzel[1]
    predchozi[1] = [hodnota, []]
    return fronta

def odeber_z_fronty(seznam):
    if seznam == []:
        return []
    print("Odebrali jste z fronty:", seznam[0])
    return seznam[1]

fronta = None
fronta = pridej_do_fronty(fronta, 1)
print(fronta)
fronta = pridej_do_fronty(fronta, 2)
print(fronta)
fronta = pridej_do_fronty(fronta, 3)
print(fronta)
# fronta = odeber_z_fronty(fronta)
# fronta = odeber_z_fronty(fronta)
# print(fronta)
# fronta = odeber_z_fronty(fronta)
# print(fronta)
# fronta = odeber_z_fronty(fronta)
# print(fronta)
# fronta = pridej_do_fronty(fronta, 1)
# print(fronta)
# fronta = pridej_do_fronty(fronta, 2)
# print(fronta)


def pop(seznam):
    promnenna = seznam[0]
    if seznam[1] != []:
        return pop(seznam[1])
    odeber_ze_seznamu1(fronta, promnenna)
    return promnenna

print("Odebrali jste ze zasobniku:", pop(fronta))
print("Odebrali jste ze zasobniku:", pop(fronta))
print("Odebrali jste ze zasobniku:", pop(fronta))
print("Odebrali jste ze zasobniku:", pop(fronta))
print(fronta)