def search(list, code):
    for index, codes in enumerate(list):
        if codes == code:
            return index
    return None

def searchDic(dictionary, course):
    if course in dictionary:
        return True
    else:
        return False

list_data = [4, 8, 7, 10, 15, 22]
print(search(list_data, 8))
print(search(list_data, 11))

dicCurses = {
            "python":[130, "basic"],
            "java":[110, "advanced"],
            "c":[90, "medium"]
            }

print("Is Python in the Dictionary?, ", searchDic(dicCurses, "python"))
print("Is PHP in the Dictionary?, ", searchDic(dicCurses, "php"))


