

# Definirea operatiei binare op
def op(x, y):
    return ( x*y + x + y ) % 3


# Alte exemple de rulaj
# op = ( x * y + x + y - 5 ) % 7  si  A = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]  - doar comutativa
# op = x * y   si  A = [-1, 1]  - grup comutativ


# Urmatoarele functii verifica anumite proprietati matematice ale operatiei op in raport cu multimea A
# Toate aceste functii primesc ca parametru de intrare multimea finita si nevida A, notata cu S in cadrul acestora

# Functia ce testeaza daca operatia este comutativa              
def testComutative(S):
    for x in S:
        for y in S:
            if op(x, y) != op(x, y):     # In cazul in care este descoperit un singur element ce nu respecta proprietatea de comutativitate, functia va returna False
                return False
    return True


# Functia ce testeaza daca operatia este asociativa
def testAssociative(S):
    for x in S:
        for y in S:
            for z in S:
                if op( op(x, y), z) != op( x, op(y, z)) :    # In cazul in care este descoperit un singur element ce nu respecta proprietatea de asociativitate, functia va returna False
                    return False
    return True


# Aceasta functie cauta un element neutru, conform formulei matematice. In cazul in care acesta exista, el trebuie sa fie unic si va fi returnat de catre functie, altfel functia returneaza False
# Elementul gasit de aceasta functie trebuie testat in raport cu toate elementele multimii pentru a verifica intr-adevar proprietatea de neutralitate. Acest lucru este facut de functia isNeutralForAll(S, e)
def getNeutralElem(S):
    for x in S:
        for e in S:
            if op(x, e) == x and op(x, e) == op(e, x):
                return e
    return -1234.567   # Un echivalent pentru infinit, semnificand inexistenta unui element neutru


# Paramentrul de intrare 'e' reprezinta elementul neutru, returnat de functia getNeutralElem(S)
# Daca a fost gasit un element neutru, proprietatea de neutralitate a acestuia este testata pentru toate elementele multimii. Daca se verifica, functia va returna True
# Daca nu exista element neutru, functia va returna din start False
def isNeutralForAll(S, e):
    if e != -1234.567:  # Daca nu are element neutru
        for x in S:
            if op(x, e) != x or op(x, e) != op(e, x):
                return False
        return True
    return False
    

# Aceasta functie testeaza existenta unui element invers in multimea A pentru un element dat
# Paramentrul 'e' reprezinta elementul neutru al multimii, iar parametrul 'x' elementul pentru care se cauta inversul
def hasInverse(S, x, e):
    for inv in S:
        if op(x, inv) == op(inv, x) and op(x, inv) == e:
            return True
    return False

# Aceasta functie verifica existenta unui element invers pentru fiecare element din multimea A
def hasAllElementsInverse(S, e):
    for x in S:
        if hasInverse(S, x, e) == False:
            return False
    return True

# Afisarea perechilor (x,y) si a valorii operatiei op(x,y) pentru acestea
def printAll(S):
    for x in S:
        for y in S:
            print("{%s, %s, %s}" % (x, y, op(x, y)))

# Functie ce verifica proprietatea de grup
# Parametrul 'e' reprezinta elementul neutru al multimii
def isGroup(S, e):
    if testAssociative(S) == False:
        return False
    if isNeutralForAll(S, e) == False:
        return False
    if hasAllElementsInverse(S, e) == False:
        return False
    return True
