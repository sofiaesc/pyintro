def es_primo(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def lista_numeros_primos(n):
    primos = [i for i in range(2,n+1) if es_primo(i)]

    return primos

if __name__ == '__main__':
    n = 20
    print(lista_numeros_primos(n))