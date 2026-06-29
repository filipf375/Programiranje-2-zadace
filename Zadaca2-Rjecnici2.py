import random

imena = ["Miro", "Stjepan", "Josip", "Toni", "Robert", "Marko", "Ljubo", "Josipa", "Magdalena", "Ivana", "Stipe", "Emanuel", "Petar", "Ivan", "Luka", "Filip", "Lara", "Laura", "Mario", "Ana", "Marija", "Nikolina", "Andrija", "Slaven", "Sebastian", "Marko", "Frano", "Stipan", "Eugen", "Toni", "Dražan", "Matej", "Nives", "Nemanja", "Sara", "Ružica", "Gabrijel", "Darian", "Ivana", "Ivan Stjepan", "Kristian", "Josip", "Tomislav", "Jovan", "Gabrijel", "Mia", "Ante", "Josip", "Ante", "Josip", "Danijel", "Goran", "Zoran Ivan", "Franjo Francisko", "Sergej", "Matej", "Marin", "Sara", "Josip", "Stjepan", "Iva", "Marko", "Sara", "Krešimir", "Magdalena", "Marko", "Mirko", "David", "Ema", "Paul", "Sven", "Natalija", "Petar", "Emanuel", "Helena", "Antonio", "Petar"]

ocjene = {}

broj_ocjena = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}

for ime in imena:
    ocjena = random.randint(1, 5)
    ocjene[ime] = ocjena
    broj_ocjena[ocjena] += 1

print("Broj ocjena:")
print(broj_ocjena)

ukupno = len(imena)
prosli = ukupno - broj_ocjena[1]

postotak = (prosli / ukupno) * 100

print("Postotak prolaznosti:", postotak, "%")
