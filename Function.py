def functionTwo(z):
    return z*5


def functionOne(a,b):
    x = a
    y = b
    z = x + y
    return  functionTwo(z)

a = functionOne(2,3)
print (a)