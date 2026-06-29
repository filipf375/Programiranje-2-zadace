import random

matrica = []

for i in range(7):
    red = []
    for j in range(7):
        red.append(random.randint(1, 9))
    matrica.append(red)

print("Matrica:")
for red in matrica:
    print(red)

zbroj = 0
velicina = 7

for i in range(velicina):
    for j in range(velicina):
        if i == 0 or i == velicina - 1 or j == 0 or j == velicina - 1:
            zbroj += matrica[i][j]

print("Zbroj rubnih elemenata:", zbroj)
