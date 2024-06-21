import json
import svgwrite




miny='-v[2]'
minx='-v[0]-v[1]'
maxy='.5*v[0]'
maxx='v[0]+v[1]'






caixa={
    "nom":"electronica-",
    "client":"fotodekora",
    "any": 2022,
    "mes:": 12,
    "versió": 1,
    "ca":"Caixa indicada per a productes fràgils o material d'elctrónica amb al menys doble cartro a totes les cares, només obrir tenim una safata superior per a instruccions, cables i/o transformadors",
    "es":"Caja insicada para productos fràgiles o de electrónica, con al menos dos capas de cartón en cualquiera de las caras, al abrir tenemos una bandeja superior situar para cables, folletos o un transformador",
    "en": "Box indicated for fragile products or electronic material with at least double cardboard on all sides, just open it we have an upper tray for instructions, cables and/or transformers",
    "variables":{
        "v[0]":{"eti":"ample","val":140},
        "v[1]":{"eti":"llarg","val":140},    
        "v[2]":{"eti":"alt","val":200},
        "v[3]":{"eti":"safata", "val":10},
        "v[4]":{"eti":"nose","val":10},
        "v[5]":{"eti":"gruix cartro","val":1.5},
        },
    "minx":minx,
    "miny":miny,
    "maxx":maxx,
    "maxy":maxy,
    "grupsSVG":{
        "hendit1":
                {
                "color":"red",
                "path" : ['M -v[0]-v[1] 0',
                        'h v[1]',
                        'v -v[2]',
                        'M  0 -v[2]',
                        'v v[2]',
                        'h v[1]',
                        'v -v[2]']
                },
            "tall1" :
                {
                "color": "blue",
                "path" : [
                        'M v[1]+v[0]-v[5] -v[2]',
                        'V 0',
                        'H v[1]+v[5]',
                        'c -0.552284866666667*v[5] 0 -0.9996106*v[5] 0.447325753333333*v[5] -0.9996106*v[5] 0.9996106*v[5] 0 0.436080133333333*v[5] 0.277391933333333*v[5] 0.808435133333333*v[5] 0.667240066666667*v[5] 0.943382533333333*v[5] ',
                        'c 0.193764213333333*v[5] 0.0672158666666667*v[5] 0.332370533333333*v[5] 0.267395866666667*v[5] 0.332370533333333*v[5] 0.472316*v[5] ',
                        'V .5*(v[0]+v[5])',
                        'H -v[5]',
                        'V 2.41466666666666*v[5]',
                        'c 0.000202466666666667*v[5] -0.2049356*v[5] 0.137976*v[5] -0.404611733333333*v[5] 0.332370533333333*v[5] -0.472316*v[5] ',
                        'c 0.1440566*v[5] -0.0498286666666667*v[5] 0.2759172*v[5] -0.133912933333333*v[5] 0.3823996*v[5] -0.242926466666667*v[5] 0.2857312*v[5] -0.284193266666667*v[5] 0.3659352*v[5] -0.747100133333333*v[5] 0.196571533333333*v[5] -1.1119248*v[5] -0.154517133333333*v[5] -0.351912446666667*v[5] -0.5266296*v[5] -0.593284313333333*v[5] -0.911341666666667*v[5] -0.58814182*v[5] ',
                        'H -v[0]+v[5]',
                        'c -0.552284866666667*v[5] 0 -0.9996106*v[5] 0.447325753333333*v[5] -0.9996106*v[5] 0.9996106*v[5] 0 0.436080133333333*v[5] 0.277391933333333*v[5] 0.808435133333333*v[5] 0.667240066666667*v[5] 0.943382533333333*v[5] ',
                        'c 0.193764213333333*v[5] 0.0672158666666667*v[5] 0.332370533333333*v[5] 0.267395866666667*v[5] 0.332370533333333*v[5] 0.472316*v[5] ',
                        'V .5*(v[0]+v[5])',
                        'H -v[0]-v[1]-v[5]',
                        'V 2.41466666666666*v[5]',
                        'c 0.000202466666666667*v[5] -0.2049356*v[5] 0.137976*v[5] -0.404611733333333*v[5] 0.332370533333333*v[5] -0.472316*v[5] ',
                        'c 0.1440566*v[5] -0.0498286666666667*v[5] 0.2759172*v[5] -0.133912933333333*v[5] 0.3823996*v[5] -0.242926466666667*v[5] 0.1851952*v[5] -0.1841984*v[5] 0.284050133333333*v[5] -0.443473*v[5] 0.2845734*v[5] -0.7024576*v[5] ',
                        'L -v[0]-v[1] 0',
                        'V -v[2]',
                        'Z '
                        ]
                }
            }
}



with open('c:\caixes\electronica.json', 'w') as f:
    json.dump(caixa, f, indent=4, sort_keys=True)


print ('JSON')

rate  = 3.77953232067064    #proporcio d'unitats svg / mm  CorelDraw
pth ="c:\caixes\\" #ruta de eixida fitxer




def demana_valors(obje): #funcio que demana a l'usuari els valor per a les variables 
    v =[]
    fname=pth+"prova.svg"
    for i in obje["variables"]:        
        v.append(caixa["variables"][i]["val"])
    
    return v,fname

def genera_path(grup,obje): #genera el path d'un grup evaluant les formules 
    cadena=""
    for j in obje["grupsSVG"][grup]["path"]: # j es una llista de ordres de un path svg parametritzades amb variables
        cadena+=j[:2] #els dos primers caracter son: ordre svg + espai en blanc
        #print(j)
        for k in j[2:].split():
            if k[0] == "l":
                cadena += k[1:] +" "
            else:
                #print(k)
                cadena+=str(eval(k)*rate)+" " #evalua cada fórmula aplicant els valors v[]
    return cadena

with open('c:\caixes\electronica.json', "r") as file: #importa una caixa paramentrizada en json
    caixa = json.load(file)


v, filename =demana_valors(caixa)


dwg = svgwrite.Drawing(filename, profile='tiny') # Crea un SVG Nom fitxer i ruta

for i in caixa["grupsSVG"].keys():    
    group = dwg.add(dwg.g(id=i)) #afegeix grup al SVG 
    group.add(dwg.path(genera_path(i,caixa)).stroke(color=caixa["grupsSVG"][i]["color"]).fill(color="none")) #afegeix path al grup

dwg.save() #tanca el fitxer SVG

print("\nel fitxer resultat es en" , filename)
