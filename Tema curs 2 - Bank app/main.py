import menus # Modul ce contine functiile de meniu
import bank # Modul ce contine clasa bank
import testfunction as test # Modul ce contine functia de test


print("Do you want to run the test function? '1' = YES, '0' = NO\n")
option = input("Your choice: ")

if option == '0':
    menus.cls() # Stergere consola
    myBank = bank.Bank("ING") # Crearea unui obiect de tip Bank
    menus.main_menu(myBank) # Apelarea meniului pentru banca respectiva
if option == '1':
    menus.cls() # Stergere consola
    test.testfc() # Apelam functia de test