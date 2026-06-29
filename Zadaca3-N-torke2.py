studenti = []

with open("rezultati.csv", "r", encoding="utf-8") as datoteka:
    for red in datoteka:
        ime, prezime, bodovi = red.strip().split(",")
        studenti.append((ime, prezime, int(bodovi)))

studenti.sort(key=lambda student: student[1])

rangovi = {
    "Nedovoljan": 0,
    "Dovoljan": 0,
    "Dobar": 0,
    "Vrlo dobar": 0,
    "Izvrstan": 0
}

for student in studenti:
    bodovi = student[2]

    if bodovi < 50:
        rangovi["Nedovoljan"] += 1
    elif bodovi <= 65:
        rangovi["Dovoljan"] += 1
    elif bodovi <= 80:
        rangovi["Dobar"] += 1
    elif bodovi <= 90:
        rangovi["Vrlo dobar"] += 1
    else:
        rangovi["Izvrstan"] += 1

print(studenti)
print(rangovi)
