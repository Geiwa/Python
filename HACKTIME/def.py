
def searchstr(stroka):
    unique = set(stroka)
    if len(unique) == len(stroka):
        return True
    else:
        return False
print(searchstr('Good morning'))
