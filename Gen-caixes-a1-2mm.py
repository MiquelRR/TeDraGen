"""
Generador del dibuix de troquel de caixes
a partir de les dades de l'usuari de les mides d'una caixa, genera l'arxiu del dibuix del troqulel necesari en SVG, diferenciant hendit i tall en dos colors de linea
"""
import os
import svgwrite
import json

#rate  = 2.834643883688892  #proporcio d'unitats svg / mm    RDworks v8.01.60
#rate  = 3.77953232067064    #proporcio d'unitats svg / mm  CorelDraw
#rate=1.408450704225352
rate="mm"

def demana_valors(obje): #funcio que demana a l'usuari els valor per a les variables 
    v =[]
    fname=eixida+obje["nom"]
    for i in obje["variables"]:        
        ent=input(obje["variables"][i]["eti"]+" ("+str(obje["variables"][i]["val"])+"mm) :")
        v.append(float(ent) if ent else caixa["variables"][i]["val"])
        fname+= str(v[-1])+"x"
    fname=fname[:-1]+".svg"
    return v,fname

def genera_path(grup,obje): #genera el path d'un grup evaluant les formules 
    cadena=""
    for j in obje["grupsSVG"][grup]["path"]: # j es una llista de ordres de un path svg parametritzades amb variables
        cadena+=j[:2] #els dos primers caracter son: ordre svg + espai en blanc
        for k in j[2:].split():
            if k[0] == "l":         # la lletra l evita evaluar el que li seguisca
                cadena += k[1:] +" "
            else:
                cadena+=str(eval(k))+rate+" " #evalua cada fórmula aplicant els valors v[]
    return cadena



pth = os.path.dirname(os.path.abspath(__file__)) #ruta de eixida fitxer
models_pth = pth + "\models\\"
eixida = pth + "\caixes\\"

print(f"\n\nMiquel Real Dec 2022\nGenerador SVG caixes  Alfa 1.2\nDirectori d'eixida {eixida}\n\n")

with os.scandir(models_pth) as models:
    models = [model.name for model in models if model.is_file() and model.name.endswith('.json')]

print("tria el teu model de caixa :")
c=0
for i in models:
    print(f"[{c+1}] {i[:-4]}  ", end= "")
    c+=1
print("\n)")
m=int(input("-------->"))-1
selected_model_pth = models_pth+models[m]

with open(selected_model_pth, "r") as file: #importa una caixa paramentrizada en json
    caixa = json.load(file)

print("Model de caixa : "+caixa["nom"])
print("escriu les mesures interiors o enter per deixar les mateixes\n")
v, filename =demana_valors(caixa)

dwg = svgwrite.Drawing(filename, profile='tiny' ) # Crea un SVG Nom fitxer i ruta viewBox=('-5000 -5000 10000 10000'

for i in caixa["grupsSVG"].keys():    
    group = dwg.add(dwg.g(id=i)) #afegeix grup al SVG 
    group.add(dwg.path(genera_path(i,caixa)).stroke(color=caixa["grupsSVG"][i]["color"]).fill(color="none")) #afegeix path al grup
dwg.viewbox(-2*v[0],-5*v[2],3.5*v[0],2*v[1])
dwg.save() #tanca el fitxer SVG

print("\nel fitxer resultat es en" , filename)

input()