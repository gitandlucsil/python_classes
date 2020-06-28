import types

def showtype(data):
    _type = type(data)
    print(_type)
    #print(types.BuiltinFunctionType)

showtype(5)
showtype(5.6)
showtype('5')
showtype("5")
showtype(True)
_list = []
showtype(_list)
showtype(list)
showtype([3, 4])
showtype({"a":1, "b":2})
showtype(None)
showtype(print)