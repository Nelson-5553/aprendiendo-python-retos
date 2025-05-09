
# def palindromo(palabra):

palabra = "Ana lleva al oso la avellana"

def polindromo(palabra):
    texto = palabra.replace(" ", "").lower()
    textoinvert = palabra.replace(" ", "").lower()[::-1]
    if texto == textoinvert:
       return True
    else:
       return False
    
print(polindromo(palabra))
