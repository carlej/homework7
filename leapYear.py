def LY(a):
    year = int(a)
    if year%4 == 0:
        if year%100 == 0:
            return False
        else:
            return True
    else:
        return False