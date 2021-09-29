import user # Modul ce contine clasa User

# Clasa ce reprezinta banca
class Bank:

    def __init__(self, name):
        self.name = name
        self.userList = [] # Lista de utilizatori ai bancii, initial goala

    # Metoda pentru adaugarea unui nou utilizator
    def add_user(self, username, password):
        aux = 1
        # Cautam utilizatorul in lista de utilizatori
        for userobj in self.userList:
            if username == userobj.name: # Daca exista deja se afiseaza eroare
                print("\nExista deja un utilizator cu acest nume. Reincercati "
                      "inregistrarea!")
                aux = 0
                break
        # Daca nu exista utilizatorul, atunci se creaza
        if aux == 1:
            # Adaugam in lista de utilizatori un nou obiect de tip User
            self.userList.append(user.User(username, password))
    
    # Metoda pentru autentificarea unui utilizator
    def user_auth(self, username, password):
        aux = -1
        # Se cauta utilizator in lista de utilizatori
        for userobj in self.userList:
            if userobj.name == username and userobj.password == password:
                aux = 1 # Autentificare reusita
                break
            elif userobj.name == username and userobj.password != password:
                aux = 0 # Parola incorecta
                break

        if aux == -1:
            print("\nUtilizator inexistent!")
            return None
        elif aux == 0:
            print("\nParola incorecta! Reincercati autentificarea!")
            return None
        elif aux == 1:
            print("\nAUTENTIFICARE REUSITA! BUN VENIT!")
            return userobj # Metoda returneaza instanta clasei User ce are
                           # numele si parola introduse

    # Metoda ce cauta un cont al unui utilizator in cadrul bancii
    def search_account_id(self, id):
        #Pentru fiecare obiect de tip User din lista de utilizatori ai bancii...
        for userobj in self.userList:
            # Pentru fiecare obiect de tip Account din lista de conturi
            # corespunzatoare fiecarui user...
            for accobj in userobj.accList:
                # cautam id-ul contului introdus
                if accobj.accid == id:
                    return accobj # Daca am gasit un id corespunzator, returnam
                                  # obiectul de tip Account corespunzator
        return None # Daca nu am gasit id-ul corespunzator, returnam None