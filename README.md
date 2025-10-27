# SortMaster 🚀

**Organización Inteligente de Archivos para Productividad Profesional**

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com/Willyperic0/SortMaster)

## 📋 Tabla de Contenidos
- [Visión General](#visión-general)
- [Características Principales](#características-principales)
- [Requisitos del Sistema](#requisitos-del-sistema)
- [Instalación Rápida](#instalación-rápida)
- [Guía de Uso](#guía-de-uso)
- [Tecnologías](#tecnologías)
- [FAQ](#faq)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Reconocimientos](#reconocimientos)

## 🎯 Visión General

**SortMaster** es una herramienta de línea de comandos profesional diseñada para automatizar la organización de archivos mediante clasificación inteligente por extensiones. Elimina la tediosa tarea manual de organizar documentos, imágenes, código y otros tipos de archivos en carpetas estructuradas.

### ⚡ Propuesta de Valor
- **Ahorro de Tiempo**: Reduce minutos/horas de organización manual a segundos
- **Precisión**: Clasificación 100% precisa sin errores humanos
- **Flexibilidad**: Control granular sobre qué extensiones organizar
- **Seguridad**: Auto-protección y prevención de sobrescrituras

## ✨ Características Principales

| Feature | Descripción | Beneficio |
|---------|-------------|-----------|
| 🎨 **Interfaz Profesional** | CLI con colores, arte ASCII y barras de progreso | Experiencia de usuario premium |
| 🔧 **Análisis Inteligente** | Detección automática de TODAS las extensiones | Cobertura completa sin archivos olvidados |
| 🛡️ **Auto-Protección** | Exclusión automática del script y carpetas sistema | Operación segura sin riesgos |
| 📊 **Resumen Detallado** | Estadísticas con tamaños y distribución visual | Toma de decisiones informada |
| 🎯 **Selección Selectiva** | Elección granular de extensiones a organizar | Control total del proceso |
| 🔄 **Manejo de Conflictos** | Renombrado automático para evitar sobrescrituras | Protección de datos |

## 🖥️ Requisitos del Sistema

- **Python**: Versión 3.6 o superior
- **Sistema Operativo**: Windows, Linux, o macOS
- **Permisos**: Lectura/escritura en directorios objetivo
- **Espacio**: Suficiente para operaciones de movimiento

### Verificación de Python
```bash
python --version
# o
python3 --version
```

## ⚡ Instalación Rápida

### Método 1: Clonación del Repositorio
```bash
git clone https://github.com/Willyperic0/SortMaster.git
cd SortMaster
```

### Método 2: Descarga Directa
```bash
# Descargar el archivo directamente
wget https://github.com/Willyperic0/SortMaster/raw/main/SortMaster.py
# o
curl -O https://github.com/Willyperic0/SortMaster/raw/main/SortMaster.py
```

## 🚀 Guía de Uso

### Ejecución Directa Desde Cualquier Ubicación
```bash
# Ejecutar directamente desde la ruta completa
python /ruta/completa/hacia/SortMaster.py

# Ejemplo en Windows
python C:\Users\Usuario\SortMaster\SortMaster.py

# Ejemplo en Linux/macOS
python /home/usuario/SortMaster/SortMaster.py
```

### Ejecución Desde Directorio Local
```bash
# Navegar al directorio y ejecutar
cd /ruta/del/script
python SortMaster.py
```

### Flujo de Trabajo Típico

1. **Inicio**: Interfaz visual con arte ASCII profesional
2. **Selección de Ruta**: Especificar directorio o usar actual (Enter)
3. **Configuración Destino**: Organizar en raíz o carpeta nueva
4. **Exclusión de Carpetas**: Seleccionar carpetas a excluir del análisis
5. **Análisis Automático**: Escaneo completo con estadísticas detalladas
6. **Selección de Extensiones**: Elegir tipos específicos de archivo
7. **Confirmación Final**: Verificación antes de ejecución
8. **Ejecución**: Proceso automático con barras de progreso

### Ejemplos Prácticos de Uso

#### Organizar Directorio de Descargas
```bash
python SortMaster.py
# Ruta: C:\Users\Usuario\Downloads (Windows) o ~/Downloads (Linux/macOS)
```

#### Limpiar Proyecto de Desarrollo
```bash
cd /ruta/del/proyecto
python /ruta/SortMaster.py
# Excluir: node_modules, .git, venv, etc.
```

#### Organizar Escritorio
```bash
python SortMaster.py
# Ruta: C:\Users\Usuario\Desktop (Windows) o ~/Desktop (Linux/macOS)
```

## 🛠️ Tecnologías

- **Lenguaje Principal**: Python 3.6+
- **Bibliotecas Nativas**: 
  - `os` - Operaciones del sistema de archivos
  - `shutil` - Operaciones de movimiento y copia
  - `sys` - Funcionalidades del sistema
  - `subprocess` - Gestión automática de dependencias
  - `collections` - Estructuras de datos eficientes
- **Dependencia Opcional**: 
  - `colorama` - Soporte de colores en Windows (instalación automática)

## ❓ FAQ

### ¿SortMaster modifica mis archivos?
Solo **mueve** archivos a nuevas carpetas organizadas. No modifica contenido, nombres (excepto por conflictos) ni metadatos.

### ¿Es seguro para proyectos de programación?
**Totalmente seguro**. Excluye automáticamente el script mismo y permite exclusión manual de cualquier carpeta crítica.

### ¿Qué pasa si se interrumpe el proceso?
El sistema es **resistente a fallos**. Los archivos se mueven individualmente, manteniendo la integridad en caso de interrupción.

### ¿Maneja archivos con nombres complejos?
Sí, maneja todos los casos: espacios, caracteres especiales, múltiples extensiones, y archivos ocultos.

### ¿Requiere conocimientos técnicos avanzados?
**No**. Diseñado específicamente para usuarios con conocimientos básicos de línea de comandos.

### ¿Puedo usarlo en redes corporativas?
Sí, funciona completamente offline una vez descargado. No requiere conexión a internet.

## 🤝 Contribuciones

¡Tu contribución es valiosa! Si usas SortMaster como inspiración o base:

1. **Reconocimiento**: Menciona al autor original [Willyperic0](https://github.com/Willyperic0)
2. **Mejoras**: Comparte mejoras mediante pull requests
3. **Reportes**: Informa bugs o sugerencias via issues

### Guía Rápida para Contribuir
```bash
# 1. Fork del proyecto en GitHub
# 2. Clonar tu fork localmente
git clone https://github.com/TU_USUARIO/SortMaster.git
# 3. Crear rama para feature
git checkout -b feature/mejora-nueva
# 4. Desarrollar y probar cambios
# 5. Commit y push
git commit -m "Agregar mejora nueva"
git push origin feature/mejora-nueva
# 6. Abrir Pull Request en GitHub
```

## 📄 Licencia

Distribuido bajo licencia **MIT** - eres libre de usar, modificar y distribuir este software.

```text
MIT License

Copyright (c) 2025 Willyperic0

Se concede permiso, libre de cargos, a cualquier persona que obtenga una copia 
de este software y de los archivos de documentación asociados (el "Software")...
```

**Puedes:**
- ✅ Usar comercialmente
- ✅ Modificar y adaptar
- ✅ Distribuir libremente
- ✅ Usar privadamente

**Debes:**
- 📝 Incluir aviso de copyright y licencia original
- 🎯 Dar crédito al autor original

**No puedes:**
- ❌ Responsabilizar al autor por problemas

## 👏 Reconocimientos

- **Autor Original**: [Willyperic0](https://github.com/Willyperic0)
- **Inspiración**: Necesidad práctica de automatizar organización de archivos
- **Contribuidores**: Lista de personas que han ayudado a mejorar SortMaster

---

**¿SortMaster te resultó útil?** ⭐ Dale una estrella en [GitHub](https://github.com/Willyperic0/SortMaster) para apoyar el proyecto.

**¿Encontraste un error?** 🐛 [Reporta un issue](https://github.com/Willyperic0/SortMaster/issues) para ayudar a mejorar.

**¿Tienes preguntas?** 💬 Abre un discussion en el repositorio.

