def tree_search_1(root, x):
    if root == []:
        return False
    if x == root[VALUE]:
        return True
    if x < root[VALUE]:
        return tree_search_1(root[LEFT_CHILD], x)
    else:
        return tree_search_1(root[RIGHT_CHILD], x)

VALUE = 0
LEFT_CHILD = 1
RIGHT_CHILD = 2

root = [8, [4, [], []], [16, [15, [], []], [42, [23, [], []], []]]]
# print(tree_search_1(root, 23))
# print(tree_search_1(root, 8))
# print(tree_search_1(root, 17))


def pridej_do_binarniho_stromu(seznam, x, rodic = []):
    if seznam == []:
        seznam.extend([rodic, x, [], []])
    elif x < seznam[HODNOTA]:
        seznam[LEFT_CHILD] = pridej_do_binarniho_stromu(seznam[LEFT_CHILD], x, seznam)
    else:
        seznam[RIGHT_CHILD] = pridej_do_binarniho_stromu(seznam[RIGHT_CHILD], x, seznam)
    return seznam

RODIC = 0
HODNOTA = 1
LEFT_CHILD = 2
RIGHT_CHILD = 3

binarni_strom = []
# pridej_do_binarniho_stromu(binarni_strom, 8)
# pridej_do_binarniho_stromu(binarni_strom, 4)
# pridej_do_binarniho_stromu(binarni_strom, 16)
# pridej_do_binarniho_stromu(binarni_strom, 15)
# print(binarni_strom)

    
def add_uzel(graph, label):
    value = 0
    graph.append([label, value,[]])
    
def add_hrana(graph, od, do, value):
    for uzel in graph:
        if uzel[LABEL] == od:
            uzel[1] = value
            v = uzel # v = a
            
        elif uzel[LABEL] == do:
            uzel[1] = value
            w = uzel # w = b
            
    v[HRANY].append(w)
    w[HRANY].append(v)
    
LABEL = 0
HRANY = 2

graph = []
# add_uzel(graph, "a")
# add_uzel(graph, "b")
# add_uzel(graph, "c")
# print(graph)

# add_hrana(graph, "a", "b", 5)
# add_hrana(graph, "a", "c", 1)
# add_hrana(graph, "c", "b", 3)
# print(graph)