def pozdrav(ime):
    print(f"Pozdrav {ime}!")

dobrodosao = lambda ime: print(f"Dobrodošao {ime}!")

def ispisi_dobrodoslicu(funkcija):
    funkcija("Filip")

ispisi_dobrodoslicu(pozdrav)
ispisi_dobrodoslicu(dobrodosao)
