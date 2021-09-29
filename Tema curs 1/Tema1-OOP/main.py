import functions as fc    # Modulul ce contine functiile
import os
import msvcrt
# Modulele 'os' si 'msvcrt' sunt folosite petru a putea curata consola, respectiv pentru a putea citi un caracter de la tastatura

#Functie utilizata pentru a curata consola in functie de sistemul de operare folosit (Windows sau Linux)
def cls():
    os.system('cls' if os.name=='nt' else 'clear') 
   
# Multimea finita si nevida A
A = [-4, -2, -1, 0, 1, 2, 3, 5]

# Variabila folosita pentru a determina optiunile din meniu, initializata cu True pentru a permite intrarea in ciclul 'while'
option = True

# Structura folosita pentru implementarea unui meniu
while option != False:
    print("Introduceti de la tastatura cifra corespunzatoare optiunii dorite")
    print("\n")
    print("1. Verificarea comutativitatii")
    print("2. Verificarea asociativitatii")
    print("3. Verificarea elementului neutru si a elementelor simetrizabile (inverse)")
    print("4. Verificarea proprietatii de grup comutativ")
    print("5. Analiza completa a operatiei")  # Verificarea simultana a optiunilor de mai sus
    print("6. Afisarea valorilor operatiei")
    print("0. Iesire din program")
    print("\n\n")

    option = input("Alegeti optiunea: ")
    # Implementarea cazurilor este analoaga, difera doar functiile folosite si mesajele afisate
    # Structurile if...elif sunt folosite in locul instructiunii switch din C
    if option == '1':

        cls()  # Curatarea consolei
        if fc.testComutative(A) == True:
            print("Operatia binara este comutativa")
        else:
            print("Operatia binara nu este comutativa")

        print("\nApasati oricare tasta pentru a reveni la meniul principal")
        ch = msvcrt.getch() # Introducerea oricarui caracter de la tastatura va declansa curatarea consolei, urmatata de revenirea in meniul princpal
        cls()

    elif option == '2':

        cls()
        if fc.testAssociative(A) == True:
            print("Operatia binara este asociativa")
        else:
            print("Operatia binara nu este asociativa")

        print("\nApasati oricare tasta pentru a reveni la meniul principal")
        ch = msvcrt.getch()
        cls()

    elif option == '3':

        cls()
        aux = fc.getNeutralElem(A)  # Variabila auxiliara ce retine elementul neutru, pentru a evita apeluri multiple ale functiei

        # Daca exista un element neutru acesta va fi afisat, apoi se va testa existenta elementelor inverse
        if fc.isNeutralForAll(A, aux) == True: 

            print("Operatia binara are elementul neutru : %i" %aux)

            if fc.hasAllElementsInverse(A, aux) == True:
                print("Toate elementele din multimea A sunt simetrizabile in raport cu operatia binara op")
            else:
                print("Nu toate elementele din multimea A sunt simetrizabile in raport cu operatia binara op")
        
        # Daca nu exista element neutru, atunci nu vor exista nici elemente inverse
        else:
            print("Operatia binara nu are element neutru in raport cu multimea A, si deci nu are nici elemente simetrizabile")

        print("\nApasati oricare tasta pentru a reveni la meniul principal")
        ch = msvcrt.getch()
        cls()

    elif option == '4':
        cls()

        aux = fc.getNeutralElem(A) # Variabila auxiliara ce retine elementul neutru, pentru a evita apeluri multiple ale functiei

        # Se testeaza daca operatia verifica proprietatiile unui grup (si daca acesta este comutativ)
        if fc.isGroup(A, aux) == True and fc.testComutative(A) == False:
            print("Operatia verifica proprietatiile unui grup, dar acesta nu este si comutativ")
        elif fc.isGroup(A, aux) == True and fc.testComutative(A) == True:
            print("Operatia verifica proprietatiile unui grup comutativ")
        else:
            print("Operatia nu verifica proprietatea de grup")


        print("\nApasati oricare tasta pentru a reveni la meniul principal")
        ch = msvcrt.getch()
        cls()

    elif option == '5': # Aceasta optiune reprezinta executarea succesiva a tuturor testelor proprietatiilor operatiei

        cls()
        if fc.testComutative(A) == True:
            print("Operatia binara este comutativa")
        else:
            print("Operatia binara nu este comutativa")

        if fc.testAssociative(A) == True:
            print("Operatia binara este asociativa")
        else:
            print("Operatia binara nu este asociativa")

        aux = fc.getNeutralElem(A)
        if fc.isNeutralForAll(A, aux) == True:

            print("Operatia binara are elementul neutru %s" % (aux))
            
            if fc.hasAllElementsInverse(A, aux) == True:
                print("Toate elementele din multimea A sunt simetrizabile in raport cu operatia binara op")
            else:
                print("Nu toate elementele din multimea A sunt simetrizabile in raport cu operatia binara op")
        else:
            print("Operatia binara nu are element neutru in raport cu multimea A, si deci nu are nici toate elementele simetrizabile")


        if fc.isGroup(A, aux) == True and fc.testComutative(A) == True:
            print("Operatia verifica proprietatiile unui grup comutativ")
        elif fc.isGroup(A, aux) == True and fc.testComutative(A) == False:
            print("Operatia verifica proprietatiile unui grup, dar acesta nu este si comutativ")
        else:
            print("Operatia nu verifica proprietatea de grup")

        
        print("\nApasati oricare tasta pentru a reveni la meniul principal")
        ch = msvcrt.getch()
        cls()

    elif option == '6':
        cls()
        print("Valorile operatiei sunt reprezentate prin urmatoarele triplete")
        print("Prima cifra reprezinta x, a doua y, iar a 3-a rezultatul operatiei op(x,y)")
        fc.printAll(A)

        print("\nApasati oricare tasta pentru a reveni la meniul principal")
        ch = msvcrt.getch()
        cls()

    elif option == '0': # Daca se introduce optiunea '0' atunci se va afisa un mesaj de confirmare, iar ciclul 'while' va fi intrerupt, urmand incheierea executiei programului
        cls()
        option = False
        print("Incheiere executie program")
    else:    # Daca optiunea are orice valoare inafara de cele prezente in meniul afisat, atunci utilizatorul va fi atentionat si va trebui sa introduca o noua optiune valida
        print("\nOptiune incorecta! Reintroduceti o optiune valida")
        


