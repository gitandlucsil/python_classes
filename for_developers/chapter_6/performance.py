import cProfile

#Função usando range()
def rgb1():
    rgbs = []
    for r in range(256):
        for g in range(256):
            for b in range(256):
                rgbs.append('#%02x%02x%02x' % (r, g, b))
    return rgbs

#Função usando uma lista várias vezes
def rgb2():
    rgbs = []
    ints = range(256)
    for r in ints:
        for g in ints:
            for b in ints:
                rgbs.append('#%02x%02x%02x' % (r, g, b))
    return rgbs

#Gerador usando apenas uma lista
def rgb3():
    for i in range(256 ** 3):
        yield("#%06x"%i)

#Benchmarks
print("rgb1:")
cProfile.run("rgb1()")
print("rgb2:")
cProfile.run("rgb2()")
print("rgb3:")
cProfile.run("list(rgb3())")