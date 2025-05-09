
def convert(tipo, numero):
    if tipo == "segundos":
       ms = numero * 1000
       return ms
    elif tipo == "minutos":
        ms = numero * 60000
        return ms
    
    elif tipo == "horas":
        ms = numero * 3600000
        return ms
    
    elif tipo == "dias":
        ms = numero * 86400000
        return ms
    else:
        return "tipo o numero no valido"
    
tipo = "horas"
numero = 1

print(convert(tipo, numero))
    
    