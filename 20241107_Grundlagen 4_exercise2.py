
def teilbar(x,y):
    if y == 0: 
        print("es ist unmöglich durch 0 zu teilen")
    elif x == y:
        print("x ist gleich y")
    else: 
        if x % y == 0 : 
            print("x ist durch y teilbar")
        else: 
            print("x is nicht durch y teilbar")

teilbar(18,22)

