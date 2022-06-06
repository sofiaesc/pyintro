from posixpath import split

def es_valido(dni):
    
    for i in dni:
        if (not(i.isnumeric() or i == '.')):
            return False

    ls = dni.split(".")

    if(len(ls) > 3):
        return False
    
    if(int(ls[0]) < 0 or int(ls[0]) > 99):
        return False

    if(int(ls[1]) < 0 or int(ls[1]) > 999):
        return False

    if(int(ls[2]) < 0 or int(ls[2]) > 999):
        return False

    return True

if __name__ == '__main__':
    dni = '0.345.478'
    print(es_valido(dni))
    
