import os
import msvcrt
# Modulele 'os' si 'msvcrt' sunt folosite petru a putea curata consola,
# respectiv pentru a putea citi un caracter de la tastatura

# Functie utilizata pentru a curata consola in functie de
# sistemul de operare folosit (Windows sau Linux)
def cls():
    os.system('cls' if os.name=='nt' else 'clear') 

# Functia meniu principal ce are ca paramentru de intrare un obiect de tip Bank
def main_menu(bankobj):
    
    option = True

    while option != '0':
        
        print_main_menu_options() # Afisarea optiunilor
        option = input("Alegeti optiunea: ")
        cls()  # Curatarea consolei

        main_menu_exec_option(option, bankobj) # Exectuarea optiunii alese

        if option != '0': # In cazul in care optiunea este 0 nu mai este nevoie
                       # de afisearea mesajului deoarece programul se va inchide
            print("\n\n\n»»» APASATI ORICARE TASTA PENTRU "
                  "A REVENI LA MENIUL PRINCIPAL! «««")

            ch = msvcrt.getch() # Introducerea oricarui caracter de la tastatura
                                # va declansa curatarea consolei si continuarea
                                # ciclului 'while'          
            cls() # Curatarea consolei


# Functie ce primeste ca parametrii de intrare un obiect din clasa Bank si 
# optiunea ce indica metoda acestuia care trebuie executata
def main_menu_exec_option(option, bankobj):

    if option == '1':

        username = input("Introduceti numele dorit: ")
        password = input("Introduceti parola dorita: ")

        bankobj.add_user(username, password) # Adaugam un utilizator
    elif option == '2':

        username = input("Introduceti numele dorit: ")
        password = input("Introduceti parola dorita: ")

        aux = bankobj.user_auth(username, password) # Autentificare utilizator
        if aux != None:
            user_menu(aux, bankobj) # Daca autentificarea reuseste se apeleaza
                                    # functia de meniu a utilizatorului

    elif option == '0':
        print("Incheiere executie program")

    else:
        print("\nOptiune incorecta! Reintroduceti o optiune valida\n\n")

# Functie ce printeaza optiunile meniului principal
def print_main_menu_options():
    print("Introduceti de la tastatura cifra corespunzatoare "
          "optiunii dorite")
    print("\n")
    print("1. Crearea unui nou profil de client in cadrul bancii")
    print("2. Autentificarea unui client existent")
    print("0. Iesire din program")
    print("\n\n")

# Functia meniului de utilizator ce primeste ca parametrii de intrare un obiect
# de tip User (utilizatorul asupra caruia se executa modificari) si un obiect
# de tip Bank (banca caruia apartine utilizatorul)
def user_menu(userobj, bankobj):
    
    option = True

    while option != '0':

        print_user_menu_options() # Functie ce afiseaza optiunile meniului
        option = input("Alegeti optiunea: ")
        cls()  # Curatarea consolei

        user_menu_exec_option(option, userobj, bankobj) # Functie ce executa
                                                        # optiunea aleasa
        if option != '0': # In cazul in care optiunea este 0, mesajul urmator nu 
                        # mai are sens sa fie afisat
            print("\n\n\n»»» APASATI ORICARE TASTA PENTRU "
                  "A REVENI LA MENIUL PRINCIPAL! «««")

            ch = msvcrt.getch() # Introducerea oricarui caracter de la tastatura
                                # va declansa curatarea consolei si continuarea
                                # ciclului 'while'
            cls() # Curatarea consolei

# Functie ce primeste ca parametrii de intrare un obiect de tip Bank, un obiect
# de tip User (utilizatorul autentificat) si optiunea corespunzatoare metodei
# ce trebuie apelata
def user_menu_exec_option(option, userobj, bankobj):
    if option == '1':
        accname = input("Introduceti un nume pentru noul cont (ex. Cont curent,"
                        " Cont economii, Credit): ")
        userobj.create_account(accname) # Crearea unui nou cont bancar

    elif option == '2':
        accname = input("Introduceti numele contului pe care "
                        "doriti sa il inchideti: ")
        userobj.delete_account(accname) # Stergerea unui cont

    elif option == '3':
        accname = input("Introduceti numele contului pe care "
                        "doriti sa-l accesati: ")
        aux = userobj.search_account(accname) # Cautarea unui cont

        # In cazul in care contul cautat exista, se alimenteaza cu bani
        if aux != None:
            sum = int(input("Introduceti suma pe care "
                            "doriti sa o depozitati: "))
            aux.deposit(sum) # Alimentarea contului
        else:
            print("\n\nNume de cont introdus inexistent!")
    
    elif option == '4':
        accname = input("Introduceti numele contului pe care "
                        "doriti sa-l accesati: ")

        aux = userobj.search_account(accname) # Cautarea unui cont

        # In cazul incare contul cautat exista, se extrag banii din acesta
        if aux != None:
            sum = int(input("Introduceti suma pe care doriti sa o retrageti: "))
            aux.withdraw(sum) # Extragerea banilor
        else: 
            print("\n\nNume de cont introdus inexistent!")

    elif option == '5':
        srcacc = input("\nIntroduceti numele contului din care doriti "
                       "sa transferatii banii (contul sursa): ")
        destacc = input("\nIntroduceti numele contului in care doriti "
                        "sa transferati banii (contul destinatie): ")

        aux1 = userobj.search_account(srcacc) # Cautarea contului sursa
        aux2 = userobj.search_account(destacc) # Cautarea contului destinatie

        # Daca ambele conturi sunt valide, se executa transferul
        if aux1 != None and aux2 != None:
            sum = int(input("\n\nIntroduceti suma pe care "
                            "doriti sa o transferati: "))
            aux1.transfer(aux2, sum) # Executare transfer
        # Afisare mesaje de eroare corespunzatoare ( daca este cazul )
        elif aux1 == None:
            print("\n\nContul din care doriti sa transferati banii nu exista!")
        else:
            print("\n\nContul in care doriti sa transferati banii nu exista!")

    elif option == '6':
        srcid = int(input("\nIntroduceti id-ul contului din care doriti "
                       "sa transferatii banii (contul sursa): "))
        # Se cauta contul cu id-ul introdus in lista de conturi a utilizatorului
        for accobj in userobj.accList:
            if srcid == accobj.accid:
                # Daca utilizatorul este propietarul contului sursa cu id-ul
                # introdus se va cere introducerea id-ului codului sursa
                destid = int(input("\nIntroduceti id-ul contului in care doriti"
                        " sa transferati banii (contul destinatie): "))
                # Cautam conturile in banca
                aux1 = bankobj.search_account_id(srcid)
                aux2 = bankobj.search_account_id(destid)
                aux3 = 1
                break
            else:
                aux3 = None
                break
        # Daca ambele conturi sunt valide executam transferul
        if aux1 != None and aux2 != None:
            sum = int(input("\n\nIntroduceti suma pe care "
                            "doriti sa o transferati: "))
            aux1.transfer(aux2, sum) # Executarea transferului
        # Afisare mesaje eroare corespunzatoare
        elif aux3 == None:
            print("\n Nu sunteti proprietarul contului cu acest id")
        elif aux1 == None:
            print("\n\nContul din care doriti sa transferati banii nu exista!")
        else:
            print("\n\nContul in care doriti sa transferati banii nu exista!")

    elif option == '7':
        userobj.display_accounts() # Afisarea raportului conturilor
    
    elif option == '0':
        print("\nLa revedere!\n")
    
    else:
        print("\nOptiune incorecta! Reintroduceti o optiune valida\n\n")

# Functie ce afiseaza optiunile meniului de utilizator   
def print_user_menu_options():        
        print("Introduceti de la tastatura cifra corespunzatoare "
              "optiunii dorite")
        print("\n")
        print("1. Deschiderea unui cont")
        print("2. Inchiderea unui cont")
        print("3. Depunere numerar in lei")
        print("4. Retragere numerar in lei")
        print("5. Transfer intre conturile proprii")
        print("6. Transfer intre doua conturi")
        print("7. Afisare raport conturi")
        print("0. Logout")
        print("\n\n")