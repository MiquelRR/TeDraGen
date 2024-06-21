"""
Generador del dibuix de troquel de caixes
a partir de les dades de l'usuari de les mides d'una caixa, genera l'arxiu del dibuix del troqulel necesari en SVG, diferenciant hendit i tall en dos colors de linea
"""
import os #per a manejar fitxers
import svgwrite # per escrire SVG
import json

#rate  = 2.834643883688892  #proporcio d'unitats svg / mm    RDworks v8.01.60
rate  = 3.77953232067064    #proporcio d'unitats svg / mm  CorelDraw
#rate=1.408450704225352
mx,mn=0,0
tamany_miniatura_px=496 #miniatura

def demana_valors(obje): #funcio que demana a l'usuari els valor per a les variables 
    v =[]
    fname=eixida+obje["nom"]
    for i in obje["variables"]:        
        ent=input(obje["variables"][i]["eti"]+" ("+str(obje["variables"][i]["val"])+"mm) :")
        v.append(float(ent) if ent else caixa["variables"][i]["val"])
        fname+= str(v[-1])+"x"
    fname=fname[:-1]+".svg"
    return v,fname

def genera_path(grup,obje,escala): #genera el path d'un grup evaluant les formules 
    global mx,mn
    cadena=""
    for j in obje["grupsSVG"][grup]["path"]: # j es una llista de ordres de un path svg parametritzades amb variables
        cadena+=j[:2] #els dos primers caracter son: ordre svg + espai en blanc
        for k in j[2:].split():
            if k[0] == "l":         # la lletra l evita evaluar el que li seguisca
                cadena += k[1:] +" "
            else:
                vl=eval(k)
                mx = mx if vl < mx else vl
                mn = mn if vl > mn else vl
                cadena+=str(vl*escala)+" " #evalua cada fórmula aplicant els valors v[]
    return cadena

def escriu_svg(fitxer,model, escala):
    dwg = svgwrite.Drawing(fitxer, profile='tiny' , size=(0,0)) # Crea un SVG Nom fitxer i ruta 
    for i in model["grupsSVG"].keys():    
        group = dwg.add(dwg.g(id=i)) #afegeix grup al SVG 
        group.add(dwg.path(genera_path(i,model,escala)).stroke(color=model["grupsSVG"][i]["color"]).fill(color="none")) #afegeix path al grup

    dwg.save() #tanca el fitxer SVG

pth = os.path.dirname(os.path.abspath(__file__)) #ruta de eixida fitxer
models_pth = pth + "\models\\"
eixida = pth + "\caixes\\"


print(f"\n\nMiquel Real Dec 2022\nGenerador SVG caixes  Alfa 1.2\nDirectori d'eixida {eixida}\n\n")

with os.scandir(models_pth) as models:
    models = [model.name for model in models if model.is_file() and model.name.endswith('.json')]

print("tria el teu model de caixa :")
c=0
for i in models:
    print(f"[{c+1}] {i[:-5]}  ", end= "")
    c+=1
print("\n")
m=int(input("-------->"))-1
selected_model_pth = models_pth+models[m]

with open(selected_model_pth, "r") as file: #importa una caixa paramentrizada en 
    caixa = json.load(file)

print("Model de caixa : "+caixa["nom"])
print("escriu les mesures interiors o enter per deixar les mateixes\n")
v, filename =demana_valors(caixa)

escriu_svg(filename,caixa, rate)

horizontal=eval(caixa["maxx"])-(eval(caixa["minx"]))
vertical=eval(caixa["maxy"])-(eval(caixa["miny"]))
gran= horizontal if horizontal> vertical else vertical
rate_min=tamany_miniatura_px/gran

print("hor =",horizontal,"ver =",vertical,"guanya =",gran, "prop =", rate_min )

escriu_svg(eixida+"preview.svg",caixa,rate_min)


print("\nel fitxer resultat es en" , filename)

input()