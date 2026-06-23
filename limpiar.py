import nbformat
import glob

# 1. Define aquí tus reemplazos exactos
reemplazos = {
    "práctica": "pipeline",
    "Práctica": "Pipeline",
    "ejercicio": "análisis",
    "Ejercicio": "Análisis",
    "enunciado": "requisitos del sistema",
    "Enunciado": "Requisitos del sistema",
    "profesor": "validación",
    "Parte I": "Fase 1",
    "Parte 1": "Fase 1",
    "Parte II": "Fase 2",
    "Parte 2": "Fase 2"
}

# 2. Encuentra todos los cuadernos del repositorio
cuadernos = glob.glob("**/*.ipynb", recursive=True)

for ruta in cuadernos:
    # Leer el cuaderno de forma segura usando la API oficial
    notebook = nbformat.read(ruta, as_version=4)
    modificado = False

    for celda in notebook.cells:
        # Solo aplicamos los cambios a celdas de texto
        if celda.cell_type == 'markdown':
            for palabra_vieja, palabra_nueva in reemplazos.items():
                if palabra_vieja in celda.source:
                    celda.source = celda.source.replace(palabra_vieja, palabra_nueva)
                    modificado = True

    # Si hubo cambios, se sobrescribe el archivo con el JSON perfecto
    if modificado:
        nbformat.write(notebook, ruta)
        print(f"[OK] Limpiado: {ruta}")

print("Limpieza masiva completada.")