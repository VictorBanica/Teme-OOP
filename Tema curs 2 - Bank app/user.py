import account # Modul ce contine clasa Account

# Clasa ce reprezinta un utilizator al bancii
class User:

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.accList = []  # lista de conturi a fiecarui  utilizator, initial
                           # goala

    # Metoda pentru cautarea unui cont in lista de conturi a utilizatorului
    def search_account(self, accname):
        for accobj in self.accList:
        # Pentru fiecare obiect de tip Account din lista cautam numele introdus
            if accobj.name == accname:
                return accobj # Daca utilizatorul are un cont cu numele cautat
                             # atunci returnam obiectul Account corespunzator
        return None # Daca nu exista un cont cu numele introdus returnam None

    # Metoda pentru crearea unui cont nou
    def create_account(self, accname):
        aux = 1
        # Verificam daca exista deja un cont cu numele introdus
        for accobj in self.accList:
            if accobj.name == accname:
                aux = 0 # Exista deja un cont cu numele introdus
                break
    
        if aux == 1:
            # Cream un nou obiect de tip Account si il adaugam in lista
            # de conturi a utilizatorului
            self.accList.append(account.Account(accname))
            print("\n\nAti creat un nou cont cu numele '{}'! Pentru a adauga "
                  "fonduri in acest cont, selectati optiunea corespunzatoare "
                  "din meniul principal!".format(accname))
        else:
            print("\nExista deja un cont cu acest nume. Reincercati "
                  "deschiderea unui cont folosind un nume diferit")

    # Metoda pentru stergerea unui cont al utilizatorului
    def delete_account(self, accname):        
        aux = -1
        # Cautam obiectul Account cu numele introdus in lista de conturi
        for accobj in self.accList:
            if accobj.name == accname:
                if accobj.balance > 0:
                    aux = 0 # Daca contul are deja bani acesta nu poate fi sters
                    break
                else:
                    aux = 1
                    # S-a gasit contul cautat si acesta nu are bani in el, deci
                    # poate fi sters din lista
                    self.accList.pop(self.accList.index(accobj))
                    break

        # Afisarea unor mesaje de eroare sau confirmare
        if aux == -1:
            print("\nNu aveti deschis un cont cu acest nume!")
        elif aux == 0:
            print("\nContul specificat nu poate fi sters deoarece exista bani "
                  "in el. Transferati banii apoi reincercati!")
        else:
            print("\nContul a fost sters cu succes")

    # Metoda ce afiseaza raportul contului
    def display_accounts(self):
        if self.accList == []: # Daca nu exista conturi se afiseaza eroare
            print("\nNu aveti conturi deschise!")
        else:
            print("\n\nYOUR ACCOUNT STATUS\n")
            # Pentru fiecare obiect de tip Account din lista, se afiseaza id-ul
            # numele contului si suma de bani
            for accobj in self.accList:
                print("ACCOUNT ID {} ----- Account name: {} --- " 
                    "Balance: {} lei\n\n"
                    .format(accobj.accid, accobj.name, accobj.balance))