
def anstrong(valor):
    caracter = len(str(valor))
    cifras = []
    potencias = []
    
    for i in str(valor):
        cifras.append(i)
    for j in cifras:
        potencia = int(j) ** int(caracter)
        potencias.append(potencia)
    total = sum(potencias)
    if total == valor:
        return True
    else:
        return False

valor = 93081  

print(anstrong(valor))