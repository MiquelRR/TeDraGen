import svgpathtools

def obtener_posiciones_tamanos(svg_file):
    doc = svgpathtools.svg2paths(svg_file)  # Lee el archivo SVG y obtiene los objetos Path
    
    resultados = []
    
    for path in doc:
        if isinstance(path, svgpathtools.path.Path):
            print(type(path.id))

        if isinstance(path, svgpathtools.path.Path) and path.id.startswith("rf"):
            start = path.start  # Punto de inicio del segmento
            end = path.end  # Punto final del segmento
            longitud = abs(path.length())  # Longitud del segmento
            
            # Agrega los datos a la lista de resultados
            resultados.append({"start": start, "end": end, "longitud": longitud})
    
    return resultados

# Ejemplo de uso
archivo_svg = "C:\\Users\\miquel\\Downloads\\plov.svg"
resultados = obtener_posiciones_tamanos(archivo_svg)

# Imprime los resultados
for resultado in resultados:
    print("Start:", resultado["start"])
    print("End:", resultado["end"])
    print("Longitud:", resultado["longitud"])
    print()
