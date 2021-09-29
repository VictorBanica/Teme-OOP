import menus
import bank

# Functia de test
def testfc():
   
    print("\n\nTEST START!!!")

    testBank = bank.Bank("BCR") # Creeam o noua instanta a clasei Bank

    # Adaugam 4 utilizatori, primul parametru al functiei reprezentant numele,
    # iar al doilea parola
    testBank.add_user("Mircea", "1234")
    testBank.add_user("Ion", "5678")
    testBank.add_user("George", "1234")
    testBank.add_user("Petre", "0000")

    # Incercam sa adaugam al 5-lea utilizator
    testBank.add_user("Mircea", "1234") # Eroare: Exista deja un utilizator cu
                                        # acest nume

    # Incercam sa ne autentificam cu un utilizator inexistent. Programul va
    # afisa acest lucru iar aux va avea valoarea 'None'
    aux = testBank.user_auth("Mihai", "0000")

    # Incercam sa ne autentificam cu un utilizator existent dar cu parola
    # introdusa gresit. Programul va afisa acest lucru iar aux va fi 'None'
    aux = testBank.user_auth("Mircea", "0000")

    # Incercam o autentificare corecta
    user = testBank.user_auth("Mircea", "1234") # Succes
    
    # Incercam sa cream trei conturi
    user.create_account("Cont curent") # Succes
    user.create_account("Cont economii") # Succes
    user.create_account("Cont curent") # Eroare: Exista deja un cont cu acest 
                                       # nume

    # Incercam sa alimentam conturile cu bani                                    
    account = user.search_account("Cont curent")
    account.deposit(50) # Succes
    account = user.search_account("Cont economii")
    account.deposit(50) # Succes
    account = user.search_account("Cont curent")
    account.deposit(25) # Succes
    
    # Un test pentru functia de search. Va afisa faptul ca utilizatorul nu are
    # un cont cu acest nume
    account = user.search_account("Test")

    # Incercam sa extragem bani din conturi

    account = user.search_account("Cont curent")
    account.withdraw(50) # Succes
    account = user.search_account("Cont economii")
    account.withdraw(100) # Va afisa eroare deoarece suma introdusa depaseste
                          # suma de bani existenta in cont

    # Incercam sa facem transfer de bani intre conturi
    account1 = user.search_account("Cont curent")
    account2 = user.search_account("Cont economii")
    
    account1.transfer(account2, 100) # Va afisa eroare deoarece nu suma de bani
                                     # introdusa > suma de bani din cont
    account1.transfer(account2, 5) # Succes    
    
    # Afisam raportul conturilor
    user.display_accounts()

    # Incercam sa stergem conturi
    user.delete_account("Cont curent") # Programul va afisa o eroare deoarece
                                       # exista inca bani in cont
    user.delete_account("Test") # Eroare: Nu exista acest cont

    user.create_account("Test")
    user.delete_account("Test") # Succes

    print("\n\nTEST END!!!")