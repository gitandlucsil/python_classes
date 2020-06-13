dicCurses = {
            "python":[130, "basic"],
            "java":[110, "advanced"],
            "c":[90, "medium"]
            }

print("Dictionary: ", dicCurses)
print("Keys: ", dicCurses.keys())
print("Values: ", dicCurses.values())
print("Itens: ", dicCurses.items())

for key, infos in dicCurses.items():
    print("Curse: ", key)
    print("Price: %5.2f" % infos[0])
    print("Level: ", infos[1])

print("Java infos: ",dicCurses.get("java")) #If not exists, return None
print("Java infos2: ",dicCurses.setdefault("java2")) #If not exists, add in the dictionary

dicCursescopy1 = dicCurses
dicCursescopy2 = dicCurses.copy()
print(dicCursescopy1)
print(dicCursescopy2)
if dicCurses is dicCursescopy1:
    print("Copy 1 is the same!")
if dicCurses is dicCursescopy2:
    print("Copy 2 is the same!")
if dicCursescopy1 is dicCursescopy2:
    print("Copy 1 and Copy 2 are the same!")

dicCurses.clear()
print("After clear: ", dicCurses)

d = dict.fromkeys(["java", "python", "android"])
print(d)

d.update(java=[130,"advanced"])
d.update(python=[120,"medium"])
d.update(android=[100,"basic"])
print(d)

d.pop("python")
print(d)