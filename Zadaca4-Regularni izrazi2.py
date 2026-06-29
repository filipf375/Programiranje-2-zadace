import re

mail = input("Unesi FPMOZ mail: ")
eduid = input("Unesi eduID: ")

uzorak_mail = r"^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$"
uzorak_eduid = r"^[a-zA-Z]+\.[a-zA-Z]+\d*@sum\.ba$"

if re.match(uzorak_mail, mail):
    print("FPMOZ mail je ispravan")
else:
    print("FPMOZ mail NIJE ispravan")

if re.match(uzorak_eduid, eduid):
    print("eduID je ispravan")
else:
    print("eduID NIJE ispravan")
