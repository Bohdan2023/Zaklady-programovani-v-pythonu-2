def mocnina1(base, exponent):
    result = 1
    for i in range(exponent):
        result = result * base
    return result

#print(mocnina1(2,0))


def dvojkovasoustava5(number):
    seznam = ""
    while number > 0:
        seznam = str(number % 2) + seznam
        number = number // 2
    print(seznam)
    
#dvojkovasoustava5(2)


def matica3(number):
    seznam = []
    seznam1 = []
    counter = number
    for i in range(number):
        counter = counter - 1
        for j in range(number):
            if j != counter:
                seznam1.append(0)
            else:
                seznam1.append(1)
        seznam.append(seznam1)
        seznam1 = []

    for items in seznam:
        print(items)
        
# matica3(7)


def seznamy4(a, b):
    if len(a) == len(b):
        timer = 0
        seznam1 = a
        seznam2 = b
        for prvek1 in seznam1:
            for prvek2 in seznam2:
                if prvek1 == prvek2:
                    timer = timer + 1
        if timer < len(seznam1):
            print("seznamy neobsahuji stejni prvky")
        else:
            print("seznamy obsahuji stejni prvky")
    else:
        print("seznamy nejsou stejne delky")
    
    
#seznamy4([1, 2, 5],[1, 5, 2, 1])

def seznamyy4(list1 = [], list2 = []):
    from collections import Counter

    if Counter(list1) == Counter(list2):
        print("True")
    else:
        print("False")

# seznamyy4([1, 2, 3],[1, 2, 3])


def opakujiciprvky(arr1, arr2):
    result = []
    timer = 0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                for g in range(len(result)):
                    if result[g] == arr1[i]:
                        timer = timer + 1
                if timer == 0:
                    result.append(arr1[i])
                timer = 0
                break
    return result
        
#print(opakujiciprvky([7, 2, 5, 3, 5, 3], [7, 2, 5, 4, 6, 3, 5, 3]))


"""
word = "abc"
letter_to_replace = "a"
new_letter = "v"

word_list = list(word)
indexes = []

for i, letter in enumerate(word_list):
    if letter == letter_to_replace:
        indexes.append(i)
        
for index in indexes:
    word_list[index] = new_letter
new_word = "".join(word_list)
print(new_word)


def shift_alphabet(alphabet, shift):
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    return shifted_alphabet

indexes = []
word = "abc"
letter_to_replace = "abcdefghijklmnopqrstuvwxyz"
letter_to_replace_list = list(letter_to_replace)
word_list = list(word)
shift = 1
for _ in range(25):
    original_alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = shift_alphabet(original_alphabet, shift)
    new_letter = list(shifted_alphabet)
    shift = shift + 1
    for i in new_letter:
        for j in word_list:
            if j == i:
                indexes.append(i)
print(indexes)
"""


def caesar_decrypt(sifrovany_text, shift):
    desifrovany_text = ""
    for symbol in sifrovany_text:
        shifted = ord(symbol) - shift
        if shifted < ord('a'):
            shifted = shifted + 26
        desifrovany_text = desifrovany_text + chr(shifted)
    return desifrovany_text

def brute_force_caesar(sifrovany_text):
    for i in range(26):
        text = caesar_decrypt(sifrovany_text, i)
        print(i, text)

text = "Axeeh Phkew"

# brute_force_caesar(text)
