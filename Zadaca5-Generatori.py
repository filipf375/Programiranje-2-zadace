def parni(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def neparni(n):
    for i in range(n):
        if i % 2 != 0:
            yield i


n = int(input("Unesi broj: "))

print("Parni brojevi:")
for broj in parni(n):
    print(broj)

print("Neparni brojevi:")
for broj in neparni(n):
    print(broj)
