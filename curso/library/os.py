import os


# Obteniendo directorio actual
cwd = os.getcwd()
print(f"actualmente te encuentras en {cwd}")

# Listar archivos

txt_file = [f for f in os.listdir('./document') if f.endswith(".json")]
print("los txt son", txt_file)

#Renombrar archivos

os.rename('./document/cuento3.txt', './document/cuento2.txt')

print("Renombrado")