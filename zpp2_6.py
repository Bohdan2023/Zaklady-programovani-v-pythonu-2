def vytvor_matici(pocet_radku, pocet_sloupcu):
    matici = [[pocet_radku], [pocet_sloupcu]]
    
    #vytvarime spojovy seznam(radky) a vkladame index radku
    zasobnik = [[0], [], None]
    zasobnik[2] = zasobnik
    for i in range(1, pocet_radku):
        vytvor_radky_sloupci(zasobnik, i)
    matici.append(zasobnik)
    
    #vytvarime spojovy seznam(sloupci) a vkladame index radku
    zasobnik = [[0], [], None]
    zasobnik[2] = zasobnik
    for j in range(1, pocet_sloupcu):
        vytvor_radky_sloupci(zasobnik, j)
    matici.append(zasobnik)
    
    #vkladame odkaz na matici v posledni seznam(radky)
    radky_v_matici = matici[2]
    sloupci_v_matici = matici[3]
    while radky_v_matici:
        radky_v_matici = radky_v_matici[1]
    radky_v_matici.append(matici)
    
    #vkladame odkaz na matici v posledni seznam(sloupci)
    while sloupci_v_matici:
        sloupci_v_matici = sloupci_v_matici[1]
    sloupci_v_matici.append(matici)
    
    #vytvarime strukturu ktera bude obsahovat stejni daty jako matici ale budeme mit pristup k nim mnohem jednodusi
    zasobnik = []
    zasobnik = jednoduchi_vypis(pocet_radku, pocet_sloupcu)
    matici.append(zasobnik)
    return matici
    
#vytvarime tady spojovy seznam pro matici
def vytvor_radky_sloupci(seznam, i):
    if seznam[1] == []:
        seznam[1].extend([[i], [], seznam[1]])
        return seznam
    else:
        return vytvor_radky_sloupci(seznam[1], i)
    
#funkce pro vytvareni jednoduche struktury pomoci ktere budeme vypisovat daty kteri obsahuje matice
def jednoduchi_vypis(pocet_radku, pocet_sloupcu):
    vypis = []
    zasobnik = []
    for i in range(pocet_radku):
        for j in range(pocet_sloupcu):
            zasobnik.append(0)
        vypis.append(zasobnik)
        zasobnik = []
    return vypis


def vloz_prvek(matici, prvek, index_radku, index_sloupcu):
    radky_v_matici = matici[2]
    sloupci_v_matici = matici[3]
    
    #prochazime tady struktutu ktera obsahuje radky a vkladame prvek
    if matici[4][index_radku][index_sloupcu] == 0:
        matici[4][index_radku][index_sloupcu] = prvek
        odkaz = radky_v_matici
        stop = 0
        while radky_v_matici:
            if stop == 0:
                if radky_v_matici[0][0] == index_radku:
                    stop = 1
                    if radky_v_matici[2] == odkaz:
                        radky_v_matici[2] = []
                        radky_v_matici[2].extend([[prvek], [index_radku], [index_sloupcu], odkaz])
                    else:
                        prvky = radky_v_matici[2]
                        while prvky:
                            if prvky[3] == odkaz:
                                prvky[3] = []
                                prvky[3].extend([[prvek], [index_radku], [index_sloupcu], odkaz])
                                break
                            else:
                                prvky = prvky[3]
                else:
                    odkaz = radky_v_matici[1]
                    radky_v_matici = radky_v_matici[1]
            else:
                break
        
        #prochazime tady struktutu ktera obsahuje sloupci a vkladame prvek
        odkaz = sloupci_v_matici
        stop = 0
        odkaz = sloupci_v_matici
        while sloupci_v_matici:
            if stop == 0:
                if sloupci_v_matici[0][0] == index_sloupcu:
                    stop = 1
                    if sloupci_v_matici[2] == odkaz:
                        sloupci_v_matici[2] = []
                        sloupci_v_matici[2].extend([[prvek], [index_radku], [index_sloupcu], odkaz])
                    else:
                        prvky = sloupci_v_matici[2]
                        while prvky:
                            if prvky[3] == odkaz:
                                prvky[3] = []
                                prvky[3].extend([[prvek], [index_radku], [index_sloupcu], odkaz])
                                break
                            else:
                                prvky = prvky[3]
                else:
                    odkaz = sloupci_v_matici[1]
                    sloupci_v_matici = sloupci_v_matici[1]
            else:
                break
    else:
        print("misto je obsazene jinym prvkem")
    return matici

# pomoci jednoduche strukture kteru jsme vytvorili na zacatku vypisujeme prvky kteri obsahuje matici bez prochazeni matici do vnitra
def zobraz_matici(matici):
    for i in matici[4]:
        print(*i)



matici = []
matici = vytvor_matici(3, 3)
vloz_prvek(matici, 1, 0, 0)
vloz_prvek(matici, 9, 0, 1)
vloz_prvek(matici, 8, 1, 0)
vloz_prvek(matici, 3, 1, 1)
zobraz_matici(matici)
