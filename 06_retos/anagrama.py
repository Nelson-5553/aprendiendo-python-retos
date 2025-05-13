palabra1 = "Amor"
palabra2 = "Roma"

def anagrama(palabra1, palabra2):
    if sorted(palabra1.lower()) == sorted(palabra2.lower()):
        return True
    else:
        return False
print(anagrama(palabra1, palabra2))