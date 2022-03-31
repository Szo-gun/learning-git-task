print("Lista_zakupow")
zakupy = {"piekarnia": ["chleb, " "bułki, " "pączek, "],
"warzywniak": ["marchew, " "seler, " "rukola"]}

for i in zakupy:
    print(f" Idę do sklepu {i.capitalize()} i kupuję {str(zakupy[i]).title()}")

list = str(zakupy.values())
string = list.split()
print(f" W sumie kupuję {len(string)} produktów")

