studenti = []

with open("rezultati.csv", "r", encoding="utf-8") as datoteka:
    for red in datoteka:
        ime, prezime, bodovi = red.strip().split(",")
        studenti.append((ime, prezime, int(bodovi)))

for student in studenti:
    ime, prezime, bodovi = student
    
    if bodovi > 49:
        print(ime, prezime, bodovi)
