def lista_divisores(n):
    divisores = [divisores for divisores in range(1, n+1) if n%divisores == 0]
    
    return divisores

if __name__ == '__main__':
    n = 25
    print(lista_divisores(n))