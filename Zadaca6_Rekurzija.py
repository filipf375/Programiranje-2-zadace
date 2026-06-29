def ispisi_unazad(s):
    if len(s) == 0:
        return
    else:
        print(s[-1], end="")
        ispisi_unazad(s[:-1])


tekst = input("Unesi string: ")

ispisi_unazad(tekst)
print()
