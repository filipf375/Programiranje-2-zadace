import re

uzorak = r"^F(?=.*[0-5])(?=.*\s).*C$"

tekst = input("Unesi string: ")

if re.match(uzorak, tekst):
    print("Podudara se")
else:
    print("Ne podudara se")
