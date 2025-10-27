import os
import shutil
import sys
import subprocess
from collections import defaultdict

# Configuración de colores
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'

def clear_console():
    """Limpia la consola según el sistema operativo."""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

def install_dependencies():
    """Instala las dependencias necesarias automáticamente."""
    required_packages = []
    
    # Verificar si estamos en Windows y activar soporte de colores
    if os.name == 'nt':
        try:
            import colorama
        except ImportError:
            required_packages.append('colorama')
    
    # Instalar paquetes faltantes
    if required_packages:
        print(f"{Colors.YELLOW}[INFO] Instalando dependencias necesarias...{Colors.RESET}")
        for package in required_packages:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package], 
                                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"{Colors.GREEN}[SUCCESS] {package} instalado correctamente{Colors.RESET}")
            except subprocess.CalledProcessError:
                print(f"{Colors.RED}[ERROR] No se pudo instalar {package}{Colors.RESET}")
                return False
    
    # Inicializar colorama en Windows
    if os.name == 'nt':
        try:
            import colorama
            colorama.init()
        except ImportError:
            pass
    
    return True

def print_banner():
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
  /$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$$ /$$      /$$  /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$$$$$$ 
 /$$__  $$ /$$__  $$| $$__  $$|__  $$__/| $$$    /$$$ /$$__  $$ /$$__  $$|__  $$__/| $$_____/| $$__  $$
| $$  \__/| $$  \ $$| $$  \ $$   | $$   | $$$$  /$$$$| $$  \ $$| $$  \__/   | $$   | $$      | $$  \ $$
|  $$$$$$ | $$  | $$| $$$$$$$/   | $$   | $$ $$/$$ $$| $$$$$$$$|  $$$$$$    | $$   | $$$$$   | $$$$$$$/
 \____  $$| $$  | $$| $$__  $$   | $$   | $$  $$$| $$| $$__  $$ \____  $$   | $$   | $$__/   | $$__  $$
 /$$  \ $$| $$  | $$| $$  \ $$   | $$   | $$\  $ | $$| $$  | $$ /$$  \ $$   | $$   | $$      | $$  \ $$
|  $$$$$$/|  $$$$$$/| $$  | $$   | $$   | $$ \/  | $$| $$  | $$|  $$$$$$/   | $$   | $$$$$$$$| $$  | $$
 \______/  \______/ |__/  |__/   |__/   |__/     |__/|__/  |__/ \______/    |__/   |________/|__/  |__/
{Colors.RESET}
{Colors.GRAY}{'=' * 80}{Colors.RESET}
{Colors.WHITE}{Colors.BOLD}                    P R O F E S S I O N A L   F I L E   O R G A N I Z E R{Colors.RESET}
{Colors.GRAY}{'=' * 80}{Colors.RESET}
{Colors.YELLOW}                    Created by: willyperic0 | Version: 2.0 | License: MIT{Colors.RESET}
{Colors.GRAY}{'=' * 80}{Colors.RESET}
"""
    print(banner)

def print_header(text):
    print(f"\n{Colors.BLUE}{Colors.BOLD}╔{'═' * (len(text) + 2)}╗{Colors.RESET}")
    print(f"{Colors.BLUE}{Colors.BOLD}║ {text} ║{Colors.RESET}")
    print(f"{Colors.BLUE}{Colors.BOLD}╚{'═' * (len(text) + 2)}╝{Colors.RESET}")

def print_success(text):
    print(f"{Colors.GREEN}{Colors.BOLD}[SUCCESS] {text}{Colors.RESET}")

def print_warning(text):
    print(f"{Colors.YELLOW}{Colors.BOLD}[WARNING] {text}{Colors.RESET}")

def print_error(text):
    print(f"{Colors.RED}{Colors.BOLD}[ERROR] {text}{Colors.RESET}")

def print_info(text):
    print(f"{Colors.CYAN}{Colors.BOLD}[INFO] {text}{Colors.RESET}")

def print_step(text):
    print(f"{Colors.MAGENTA}{Colors.BOLD}[>>] {text}{Colors.RESET}")

def print_progress_bar(iteration, total, prefix='', suffix='', length=50, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '░' * (length - filled_length)
    print(f'\r{Colors.CYAN}{prefix} |{bar}| {percent}% {suffix}{Colors.RESET}', end='\r')
    if iteration == total:
        print()

def check_system_compatibility():
    """Verifica la compatibilidad del sistema."""
    print(f"{Colors.CYAN}[INFO] Verificando compatibilidad del sistema...{Colors.RESET}")
    
    # Verificar versión de Python
    if sys.version_info < (3, 6):
        print_error("Se requiere Python 3.6 o superior")
        return False
    
    print_success(f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} - Compatible")
    return True

def obtener_carpeta_destino(ruta_base):
    """Pregunta al usuario si quiere crear una carpeta para la organización."""
    print_header("CONFIGURACIÓN DE DESTINO")
    
    print(f"\n{Colors.WHITE}Directorio base: {Colors.CYAN}{ruta_base}{Colors.RESET}")
    print(f"\n{Colors.YELLOW}¿Dónde desea guardar los archivos organizados?{Colors.RESET}")
    print(f"  {Colors.CYAN}1.{Colors.RESET} En la raíz del directorio (se crearán carpetas directamente en {os.path.basename(ruta_base)})")
    print(f"  {Colors.CYAN}2.{Colors.RESET} En una carpeta nueva (recomendado para mantener el orden)")
    
    opcion = input(f"\n{Colors.WHITE}Seleccione una opción (1 o 2): {Colors.RESET}").strip()
    
    if opcion == "2":
        nombre_carpeta = input(f"\n{Colors.WHITE}Nombre de la carpeta para los archivos organizados: {Colors.RESET}").strip()
        if not nombre_carpeta:
            nombre_carpeta = "Archivos_Organizados"
        
        carpeta_destino = os.path.join(ruta_base, nombre_carpeta)
        
        # Crear la carpeta si no existe
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
            print_success(f"Carpeta creada: {carpeta_destino}")
        else:
            print_info(f"Carpeta ya existe: {carpeta_destino}")
        
        return carpeta_destino
    else:
        print_info("Los archivos se organizarán en la raíz del directorio")
        return ruta_base

def contar_archivos_en_carpeta(ruta):
    """Cuenta exactamente todos los archivos en una carpeta (incluyendo subcarpetas)."""
    total = 0
    try:
        for carpeta_actual, subcarpetas, archivos in os.walk(ruta):
            total += len(archivos)
    except (PermissionError, OSError):
        return -1  # Indicador de error
    return total

def obtener_script_actual():
    """Obtiene la ruta absoluta del script actual para excluirlo."""
    return os.path.abspath(__file__)

def obtener_extension_archivo(nombre_archivo):
    """Obtiene la extensión de un archivo de forma robusta, manejando todos los casos."""
    # Usar os.path.splitext que es más confiable
    nombre, extension = os.path.splitext(nombre_archivo)
    
    # Si no hay extensión
    if not extension:
        return 'sin_extension'
    
    # Remover el punto inicial de la extensión y convertir a minúsculas
    extension = extension.lstrip('.').lower()
    
    return extension

def analizar_carpeta(ruta, carpetas_excluidas, carpeta_destino=None):
    """Analiza la carpeta y devuelve un diccionario de extensiones y archivos encontrados."""
    extensiones = defaultdict(list)
    archivos_procesados = 0
    
    # Obtener el script actual para excluirlo
    script_actual = obtener_script_actual()
    
    print_step("Iniciando análisis del directorio...")
    
    try:
        for carpeta_actual, subcarpetas, archivos in os.walk(ruta):
            # Saltar carpetas excluidas - CORREGIDO
            ruta_absoluta = os.path.abspath(carpeta_actual)
            
            # Verificar si esta carpeta debe ser excluida
            excluir = False
            for exc in carpetas_excluidas:
                exc_absoluta = os.path.abspath(exc)
                # CORRECCIÓN: Solo excluir si es exactamente la misma carpeta o una subcarpeta
                if ruta_absoluta == exc_absoluta or ruta_absoluta.startswith(exc_absoluta + os.sep):
                    excluir = True
                    break
                    
            if excluir:
                continue
                
            # Excluir la carpeta destino si se especificó y NO es la raíz del análisis
            if carpeta_destino:
                destino_absoluta = os.path.abspath(carpeta_destino)
                ruta_base_absoluta = os.path.abspath(ruta)
                # Solo excluir si la carpeta destino no es la raíz de análisis
                if destino_absoluta != ruta_base_absoluta:
                    if ruta_absoluta == destino_absoluta or ruta_absoluta.startswith(destino_absoluta + os.sep):
                        continue

            for archivo in archivos:
                ruta_completa = os.path.join(carpeta_actual, archivo)
                if not os.path.isfile(ruta_completa):
                    continue

                # Excluir el script actual para que no se mueva a sí mismo
                if os.path.abspath(ruta_completa) == script_actual:
                    continue

                # Obtener extensión del archivo de forma robusta
                extension = obtener_extension_archivo(archivo)
                extensiones[extension].append(ruta_completa)
                archivos_procesados += 1
                
        print_success(f"Análisis completado. Procesados {archivos_procesados} archivos")
        
        # DEBUG: Mostrar extensiones encontradas
        if archivos_procesados > 0:
            print(f"{Colors.GRAY}[DEBUG] Extensiones encontradas: {list(extensiones.keys())}{Colors.RESET}")
            
        return extensiones
    
    except PermissionError as e:
        print_error(f"Error de permisos: {e}")
        return {}
    except Exception as e:
        print_error(f"Error durante el análisis: {e}")
        import traceback
        print(f"{Colors.RED}[DEBUG] Error detallado: {traceback.format_exc()}{Colors.RESET}")
        return {}

def mostrar_resumen(extensiones):
    if not extensiones:
        print_warning("No hay datos para mostrar en el resumen")
        return
        
    print_header("RESUMEN DE ANÁLISIS")
    
    print(f"\n{Colors.WHITE}{Colors.BOLD}EXTENSIÓN{' ' * 12}CANTIDAD{' ' * 6}TAMAÑO APROX.{Colors.RESET}")
    print(f"{Colors.GRAY}{'─' * 50}{Colors.RESET}")
    
    total_archivos = 0
    extensiones_ordenadas = sorted(extensiones.items(), key=lambda x: len(x[1]), reverse=True)
    
    for ext, archivos in extensiones_ordenadas:
        cantidad = len(archivos)
        total_archivos += cantidad
        
        # Calcular tamaño total con manejo de errores
        tamaño_total = 0
        for archivo in archivos:
            try:
                tamaño_total += os.path.getsize(archivo)
            except (OSError, PermissionError):
                pass
        
        tamaño_mb = tamaño_total / (1024 * 1024)
        
        # Barra de proporción
        if total_archivos > 0:
            proporción = (cantidad / total_archivos) * 20
        else:
            proporción = 0
        barra = '█' * int(proporción)
        
        print(f"  {Colors.CYAN}{ext:<15}{Colors.RESET} {Colors.GREEN}{cantidad:>7}{Colors.RESET} "
              f"{Colors.YELLOW}{tamaño_mb:>10.1f} MB{Colors.RESET} {Colors.MAGENTA}{barra}{Colors.RESET}")
    
    print(f"{Colors.GRAY}{'─' * 50}{Colors.RESET}")
    print(f"{Colors.WHITE}{Colors.BOLD}Total archivos: {total_archivos}{Colors.RESET}\n")

def elegir_carpetas_excluir(ruta, carpeta_destino=None):
    """Permite al usuario elegir qué subcarpetas excluir del análisis."""
    try:
        # Obtener todas las carpetas en la ruta
        todas_carpetas = [os.path.join(ruta, c) for c in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, c))]
        
        # Excluir la carpeta destino si existe y NO es la raíz
        carpetas = []
        for carpeta in todas_carpetas:
            if carpeta_destino and os.path.abspath(carpeta) == os.path.abspath(carpeta_destino) and os.path.abspath(carpeta_destino) != os.path.abspath(ruta):
                continue
            carpetas.append(carpeta)
            
    except PermissionError:
        print_error("No se tienen permisos para leer el directorio")
        return []
    
    carpetas_excluidas = []
    
    if not carpetas:
        print_info("No se encontraron subcarpetas para excluir")
        return carpetas_excluidas

    print_header("CARPETAS DETECTADAS")
    
    print(f"\n{Colors.WHITE}{Colors.BOLD}#  {'NOMBRE CARPETA':<30} CONTENIDO EXACTO{Colors.RESET}")
    print(f"{Colors.GRAY}{'─' * 60}{Colors.RESET}")
    
    for i, c in enumerate(carpetas, 1):
        nombre = os.path.basename(c)
        try:
            # Contar archivos exactamente (incluyendo subcarpetas)
            total_archivos = contar_archivos_en_carpeta(c)
            if total_archivos == -1:
                print(f"{Colors.CYAN}{i:2d}.{Colors.RESET} {nombre:<30} {Colors.RED}Error al contar{Colors.RESET}")
            else:
                print(f"{Colors.CYAN}{i:2d}.{Colors.RESET} {nombre:<30} {Colors.YELLOW}{total_archivos:>4} archivos{Colors.RESET}")
        except PermissionError:
            print(f"{Colors.CYAN}{i:2d}.{Colors.RESET} {nombre:<30} {Colors.RED}Acceso denegado{Colors.RESET}")

    print_info("Seleccione carpetas del sistema o temporales para excluir")
    seleccion = input(f"\n{Colors.WHITE}Selección (números separados por comas, Enter para ninguna): {Colors.RESET}")
    
    if seleccion.strip():
        try:
            indices = [int(i.strip()) for i in seleccion.split(",")]
            carpetas_excluidas = [carpetas[i - 1] for i in indices if 0 < i <= len(carpetas)]
            if carpetas_excluidas:
                excluidas_nombres = [os.path.basename(c) for c in carpetas_excluidas]
                print_success(f"Carpetas excluidas: {', '.join(excluidas_nombres)}")
        except ValueError:
            print_warning("Formato inválido. No se excluirán carpetas.")

    return carpetas_excluidas

def elegir_extensiones_organizar(extensiones):
    """Permite seleccionar qué extensiones organizar."""
    print_header("SELECCIÓN DE EXTENSIONES")
    
    lista_extensiones = list(extensiones.keys())
    
    if not lista_extensiones:
        print_error("No se encontraron archivos para organizar.")
        return []

    print(f"\n{Colors.WHITE}{Colors.BOLD}#  {'EXTENSIÓN':<12} CANTIDAD{' ' * 6}TIPO{Colors.RESET}")
    print(f"{Colors.GRAY}{'─' * 50}{Colors.RESET}")
    
    # Clasificación básica de tipos de archivo
    tipos_archivo = {
        'imagen': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'svg', 'webp', 'tiff', 'ico', 'raw'],
        'documento': ['pdf', 'doc', 'docx', 'txt', 'rtf', 'odt', 'xls', 'xlsx', 'ppt', 'pptx', 'csv'],
        'video': ['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm', 'm4v', '3gp'],
        'audio': ['mp3', 'wav', 'flac', 'aac', 'ogg', 'm4a', 'wma', 'mid', 'midi'],
        'código': ['py', 'js', 'html', 'css', 'java', 'cpp', 'c', 'php', 'rb', 'go', 'rs', 'ts', 'jsx', 'tsx', 'xml', 'json'],
        'comprimido': ['zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'xz'],
        'ejecutable': ['exe', 'msi', 'dmg', 'pkg', 'deb', 'rpm', 'apk'],
        'fuente': ['ttf', 'otf', 'woff', 'woff2', 'eot']
    }
    
    for i, ext in enumerate(lista_extensiones, 1):
        cantidad = len(extensiones[ext])
        # Determinar tipo
        tipo = "otros"
        for tipo_nombre, extensiones_tipo in tipos_archivo.items():
            if ext in extensiones_tipo:
                tipo = tipo_nombre
                break
        
        color_tipo = {
            'imagen': Colors.MAGENTA,
            'documento': Colors.BLUE,
            'video': Colors.RED,
            'audio': Colors.GREEN,
            'código': Colors.YELLOW,
            'comprimido': Colors.CYAN,
            'ejecutable': Colors.RED,
            'fuente': Colors.MAGENTA,
            'otros': Colors.GRAY
        }[tipo]
        
        print(f"{Colors.CYAN}{i:2d}.{Colors.RESET} {ext:<12} {Colors.GREEN}{cantidad:>7}{Colors.RESET}   "
              f"{color_tipo}{tipo:<10}{Colors.RESET}")

    print_info("Seleccione extensiones para organizar en carpetas separadas")
    seleccion = input(f"\n{Colors.WHITE}Selección (números separados por comas): {Colors.RESET}")
    
    elegidas = []
    try:
        indices = [int(i.strip()) for i in seleccion.split(",")]
        elegidas = [lista_extensiones[i - 1] for i in indices if 0 < i <= len(lista_extensiones)]
        
        if elegidas:
            print_success(f"Extensiones seleccionadas: {', '.join(elegidas)}")
            
    except ValueError:
        print_error("Formato de entrada no válido.")

    return elegidas

def organizar_archivos(ruta_base, extensiones, extensiones_elegidas):
    """Organiza los archivos seleccionados por extensión en subcarpetas."""
    print_header("PROCESANDO ORGANIZACIÓN")
    
    total_archivos = 0
    for ext in extensiones_elegidas:
        if ext in extensiones:
            total_archivos += len(extensiones[ext])
    
    print(f"\n{Colors.WHITE}Archivos a organizar: {Colors.GREEN}{total_archivos}{Colors.RESET}")
    print(f"{Colors.WHITE}Directorio destino: {Colors.CYAN}{ruta_base}{Colors.RESET}")
    print(f"{Colors.GRAY}{'─' * 60}{Colors.RESET}")

    archivos_procesados = 0
    errores = 0
    
    # Obtener el script actual para no moverlo
    script_actual = obtener_script_actual()
    
    for ext in extensiones_elegidas:
        if ext not in extensiones:
            continue
            
        destino = os.path.join(ruta_base, ext.upper())
        os.makedirs(destino, exist_ok=True)
        archivos_ext = len(extensiones[ext])
        
        print(f"\n{Colors.CYAN}Organizando {archivos_ext} archivos {Colors.WHITE}.{ext}{Colors.RESET}")
        
        for i, archivo in enumerate(extensiones[ext], 1):
            try:
                # Verificar que no sea el script actual
                if os.path.abspath(archivo) == script_actual:
                    print(f"{Colors.YELLOW}[INFO] Ignorando auto-movimiento del script SortMaster{Colors.RESET}")
                    continue
                    
                nombre = os.path.basename(archivo)
                nuevo_destino = os.path.join(destino, nombre)

                # Evitar sobrescrituras
                contador = 1
                nombre_sin_ext, extension_archivo = os.path.splitext(nombre)
                while os.path.exists(nuevo_destino):
                    nuevo_nombre = f"{nombre_sin_ext}_{contador}{extension_archivo}"
                    nuevo_destino = os.path.join(destino, nuevo_nombre)
                    contador += 1

                shutil.move(archivo, nuevo_destino)
                archivos_procesados += 1
                
                # Mostrar progreso
                if i % 10 == 0 or i == archivos_ext:
                    print_progress_bar(i, archivos_ext, 
                                     prefix=f'  .{ext}', 
                                     suffix=f'{i}/{archivos_ext}')
            
            except (PermissionError, OSError) as e:
                print(f"\n{Colors.RED}[ERROR] No se pudo mover {archivo}: {e}{Colors.RESET}")
                errores += 1
                continue
            
        print_success(f"  {archivos_ext} archivos .{ext} movidos a: {os.path.basename(destino)}")

    print_header("ORGANIZACIÓN COMPLETADA")
    print(f"\n{Colors.GREEN}{Colors.BOLD}RESULTADOS:{Colors.RESET}")
    print(f"  {Colors.WHITE}• Total archivos organizados: {Colors.GREEN}{archivos_procesados}{Colors.RESET}")
    print(f"  {Colors.WHITE}• Extensiones procesadas: {Colors.CYAN}{len(extensiones_elegidas)}{Colors.RESET}")
    print(f"  {Colors.WHITE}• Errores encontrados: {Colors.RED if errores > 0 else Colors.GREEN}{errores}{Colors.RESET}")
    print(f"  {Colors.WHITE}• Directorio organizado: {Colors.YELLOW}{ruta_base}{Colors.RESET}")
    
    if errores == 0:
        print(f"\n{Colors.GREEN}Todos los archivos han sido clasificados exitosamente.{Colors.RESET}")
    else:
        print(f"\n{Colors.YELLOW}La organización se completó con {errores} error(es). Verifique los mensajes anteriores.{Colors.RESET}")

def main():
    """Función principal del programa."""
    try:
        # Inicialización del sistema
        print(f"{Colors.CYAN}[INFO] Inicializando SortMaster...{Colors.RESET}")
        
        # Verificar compatibilidad
        if not check_system_compatibility():
            print_error("El sistema no es compatible con SortMaster")
            input("Presione Enter para salir...")
            return
        
        # Instalar dependencias
        if not install_dependencies():
            print_warning("Algunas dependencias no se pudieron instalar, continuando...")
        
        # Limpiar consola y mostrar banner
        clear_console()
        print_banner()
        
        print(f"{Colors.GRAY}SortMaster - Professional File Organization System{Colors.RESET}")
        print(f"{Colors.GRAY}{'=' * 80}{Colors.RESET}")
        
        # Obtener ruta a analizar
        ruta = input(f"\n{Colors.WHITE}Ruta a analizar (Enter para directorio actual): {Colors.RESET}").strip()
        if not ruta:
            ruta = os.getcwd()

        if not os.path.isdir(ruta):
            print_error("La ruta especificada no existe o no es una carpeta válida.")
            input("Presione Enter para salir...")
            return

        print_info(f"Directorio de trabajo: {ruta}")

        # Preguntar por carpeta destino
        carpeta_destino = obtener_carpeta_destino(ruta)

        # Proceso de organización - EXCLUIR carpeta destino automáticamente
        carpetas_excluidas = elegir_carpetas_excluir(ruta, carpeta_destino)
        
        print_step("Analizando contenido del directorio...")
        # Pasar carpeta_destino para excluirla del análisis
        extensiones = analizar_carpeta(ruta, carpetas_excluidas, carpeta_destino)
        
        if not extensiones:
            print_error("No se encontraron archivos para organizar en la ruta especificada.")
            input("Presione Enter para salir...")
            return
            
        mostrar_resumen(extensiones)

        extensiones_elegidas = elegir_extensiones_organizar(extensiones)

        if not extensiones_elegidas:
            print_warning("No se seleccionaron extensiones. Operación cancelada.")
            input("Presione Enter para salir...")
            return

        print_header("CONFIRMACIÓN FINAL")
        print(f"\n{Colors.YELLOW}{Colors.BOLD}ACCIÓN CRÍTICA: Reorganización de archivos{Colors.RESET}")
        print(f"{Colors.YELLOW}Esta acción moverá permanentemente los archivos a nuevas carpetas.{Colors.RESET}")
        print(f"{Colors.YELLOW}Directorio destino: {carpeta_destino}{Colors.RESET}")
        print(f"{Colors.CYAN}[INFO] El script SortMaster se excluirá automáticamente de la organización{Colors.RESET}")
        
        confirmar = input(f"\n{Colors.WHITE}¿Continuar con la organización? (s/N): {Colors.RESET}").lower()
        
        if confirmar == 's':
            print()
            organizar_archivos(carpeta_destino, extensiones, extensiones_elegidas)
        else:
            print_warning("Operación cancelada por el usuario.")
            print("No se realizaron cambios en el sistema de archivos.")

        input(f"\n{Colors.WHITE}Presione Enter para salir...{Colors.RESET}")

    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}[INTERRUPT] Operación cancelada por el usuario.{Colors.RESET}")
        input(f"\n{Colors.WHITE}Presione Enter para salir...{Colors.RESET}")
    except Exception as e:
        print(f"\n\n{Colors.RED}[FATAL ERROR] Error inesperado: {e}{Colors.RESET}")
        print(f"{Colors.YELLOW}Por favor, reporte este error al desarrollador.{Colors.RESET}")
        input(f"\n{Colors.WHITE}Presione Enter para salir...{Colors.RESET}")

if __name__ == "__main__":
    main()
