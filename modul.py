def dodaj(*args):
    wynik = sum(args)
    return wynik

def utworz_slownik(**kwargs):
    my_dict = dict(kwargs)
    return my_dict




def zmien(b):
    global a
    a = b
    return a

a = 80
zmien(7)
print(a)

