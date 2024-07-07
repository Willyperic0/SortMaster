import os
import shutil

# Obtiene la ruta del archivo .py actual
ruta_actual = os.path.dirname(os.path.abspath(__file__))

# Obtiene el nombre del archivo ejecutable
archivo_ejecutable = os.path.basename(__file__)

# Define la ruta de origen y destino como la ruta actual
ruta_origen = ruta_actual
ruta_destino = ruta_actual

# Obtiene los archivos existentes en la ruta de destino
archivos_destino = set(os.listdir(ruta_destino))

# Extrae los archivos de las subcarpetas a la ruta actual, omitiendo el archivo ejecutable y los que ya están en el destino
for carpeta_actual, _, archivos in os.walk(ruta_origen):
    for archivo in archivos:
        if archivo == archivo_ejecutable:
            continue
        ruta_completa = os.path.join(carpeta_actual, archivo)
        if (not archivo.startswith(".") and not os.path.islink(ruta_completa) 
            and os.path.isfile(ruta_completa) and not archivo.endswith(".ini") 
            and archivo not in archivos_destino):
            shutil.move(ruta_completa, ruta_destino)

# Organiza los archivos por extensión
if not os.path.exists(ruta_destino):
    os.makedirs(ruta_destino)

archivos = [archivo for archivo in os.listdir(ruta_destino) 
            if os.path.isfile(os.path.join(ruta_destino, archivo)) 
            and archivo != archivo_ejecutable]

for archivo in archivos:
    # Obtén la ruta completa del archivo
    ruta_completa = os.path.join(ruta_destino, archivo)

    # Si es un archivo y tiene una extensión
    if '.' in archivo:
        # Obtiene la extensión del archivo
        extension = archivo.split('.')[-1]

        # Si la extensión es 'log', 'config', 'ini' o no tiene extensión, omitir el archivo
        if extension in ['log', 'config', 'ini'] or not extension:
            continue

        # Crea una carpeta con el nombre de la extensión, si no existe
        ruta_extension = os.path.join(ruta_actual, extension)
        if not os.path.exists(ruta_extension):
            os.makedirs(ruta_extension)

        # Intenta mover el archivo a la carpeta correspondiente
        # Si el archivo ya existe en la carpeta destino, renombrar con un sufijo numérico
        contador = 1
        nuevo_nombre = archivo
        while os.path.exists(os.path.join(ruta_extension, nuevo_nombre)):
            nombre_sin_extension = archivo.rsplit('.', 1)[0]
            nuevo_nombre = f"{nombre_sin_extension}_{contador}.{extension}"
            contador += 1

        shutil.move(ruta_completa, os.path.join(ruta_extension, nuevo_nombre))

# Elimina las carpetas vacías
for carpeta_actual, subcarpetas, _ in os.walk(ruta_actual, topdown=False):
    for subcarpeta in subcarpetas:
        carpeta_completa = os.path.join(carpeta_actual, subcarpeta)
        try:
            os.rmdir(carpeta_completa)
        except OSError:
            continue

print("Muchas gracias por usar este programa.")
