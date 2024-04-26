def save_matrix(data, filename):
    with open(filename, 'w') as csvfile:
        for row in data:
            csv_row = ','.join(map(str, row)) + '\n'
            csvfile.writelines(csv_row)

matrix = [[1, 22, 3], [4, 55, 6], [7, 8, 9]]
save_matrix(matrix, "text.csv")


def csv_reader(file):
    lines = []
    with open(file, newline="") as csvfile:
        for line in csvfile:
            lines.append(line.strip().split(','))
    return lines

def load_matrix(file):
    matrix = []
    for row in csv_reader(file):
        row = [int(x) for x in row]
        matrix.append(row)
    return matrix

print(load_matrix("text.csv"))

# def mapovani(f, sekvence):
#     seznam = []
#     for item in sekvence:
#         seznam.append(f(item))
#     return seznam
# funkce2 = lambda x: x + x  
# sekvence2 = [1, 2, 3, 5, 7]
# print(mapovani(funkce2, sekvence2))



# def cteni_souboru3(nazev_souboru):
#     text = open(nazev_souboru)
#     znak = text.read(1)
#     while znak != "":
#         print(znak, end = "")
#         znak = text.read(1)
#     text.close()
    
# cteni_souboru3("text.csv")
