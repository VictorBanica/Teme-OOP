from itertools import count

# Clasa ce reprezinta contul unui utilizator
class Account:
    
    _accids = count(1) # Variabila ce retine numarul de instante ale clasei
                       # folosita pentru a determina un id unic pt fiecare cont 
    def __init__(self, name):
        self.name = name
        self.balance = 0 # Numarul de bani din cont, initializat cu 0
        self.accid = next(self._accids) # Id-ul unic al contului

    # Metoda pentru extragerea baniilor din cont
    def withdraw(self, amount):
        # Daca suma de bani care trebuie extrasa este mai mare decat suma de 
        # bani prezenta in cont, se va afisa eroare
        if self.balance - amount < 0:
            print("\nNu se poate efectua operatiunea de retragere deoarece suma"
                  " de bani prezenta in cont este de doar {} lei"
                  .format(self.balance))
        # Altfel se va efectua retragerea
        else:
            self.balance = self.balance - amount # Se scade suma de bani ce
                                               # trebuie extrasa din suma totala 
                                               # a instantei curente  
            print("\nAti retras cu succes suma de {} lei.".format(amount))
            print("\nSuma de bani ramasa in cont "
                  "dupa retragere: {}".format(self.balance))

    # Metoda pentru depunerea banilor in cont
    def deposit(self, amount):
        self.balance = self.balance + amount # Se adauga suma de bani introdusa
                                            # la suma totala a instantei curente            
        print("\nAti depositat cu succes suma de {} lei.".format(amount))
        print("\nSuma de bani prezenta in cont dupa depozitare: {}"
              .format(self.balance))

    # Metoda pentru transferarea banilor
    def transfer(self, destination, amount):
        # Daca suma ce trebuie transferata depaseste suma totala din cont se va
        # afisa un mesaj de eroare
        if self.balance - amount < 0:
            print("\nNu se poate efectua transferul deoarece suma de bani "
                  "prezenta in contul sursa este de doar {} lei"
                  .format(self.balance))
        # Se executa transferul
        else:
            self.balance = self.balance - amount # Se scade suma transferata
                        # din suma totala de bani a instantei curente
            destination.balance = destination.balance + amount # Se adauga suma
                        # transferata la suma totala de bani a instantei 
                        # destintatie   
            print("\nSuma de {} lei a fost transferata cu succes!" 
                  .format(amount, self.name, destination.name))

