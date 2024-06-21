import json
import svgwrite
caixa={

    "nom":"postal-1",
    "client":"fotodekora",
    "any": 2022,
    "mes:": 12,
    "versió": 1,
    "variables":{
        "v[0]":{"eti":"ample","val":256},
        "v[1]":{"eti":"llarg","val":300},    
        "v[2]":{"eti":"alt","val":50},
        "v[3]":{"eti":"cantonera", "val":70},
        "v[4]":{"eti":"enclaves","val":50},
        "v[5]":{"eti":"gruix cartro","val":2},
        "v[6]":{"eti":"diam ungla","val":30}
    },
    "grupsSVG":{
        "hendit":
                {
                "color":"red",
                "path" : ['M 0 0 ',
                        'h -v[0]',
                        'v +v[1]',
                        'h +v[0]',
                        'v -v[1]',
                        'm 0 -3*v[5]',
                        'h +v[2]',
                        'm 0 6*v[5]+v[1]',
                        'h -v[2]',
                        'm -v[0]-1.5*v[5] -2*v[5]',
                        'h -v[2]+3*v[5]',
                        'm -1.5*v[5] 3*v[5]',
                        'h -v[0]',
                        'm 0 +v[2]',
                        'h +v[0] ',
                        'm 0 4*v[5]',
                        'h -v[0]',
                        'm -1.5*v[5] -v[2]-7*v[5]',
                        'h -v[2]+3*v[5]',
                        'm v[2]-1.5*v[5] 3*v[5]',
                        'v -v[1]-8*v[5]',
                        'm -v[2]+1.5*v[5] 3*v[5]',
                        'h +v[2]-3*v[5]',
                        'm 1.5*v[5] -3*v[5]',
                        'h +v[0]',
                        'm 0 -v[2]',
                        'h -v[0]',
                        'm 0 -4*v[5]',
                        'h +v[0]',
                        'm v[2]-1.5*v[5] v[2]+7*v[5]',
                        'h -v[2]+3*v[5]',
                        'm -1.5*v[5] -3*v[5]',
                        'v v[1]+8*v[5]'
                        ]
                },
            "tall" :
                {"color": "blue",
                "path" : ['M 0 0',
                        'l -.25*v[2] -.7*v[2]',
                        'q -.1*v[2] -.3*v[2]+v[5] -.4*v[2] -.3*v[2]+v[5]',
                        'h -v[0]+1.3*v[2]',
                        'q -.3*v[2] 0 -.4*v[2] .3*v[2]-v[5]',
                        'L -v[0] 0',
                        'v -v[5]',#
                        'h -1.5*v[5]',#
                        'v -v[3]',#
                        'h -v[2]+3*v[5]',#
                        'v v[3]',#
                        'h -1.5*v[5]',#
                        'v -2*v[2]-7*v[5]',#
                        'h -0.5*v[0]+.5*v[4]',#
                        'v -v[5]',#
                        'h -v[4]',#
                        'v v[5]',#
                        'h -0.5*v[0]+.5*v[4]',#
                        'v 2*v[2]+7*v[5]',#
                        'h -1.5*v[5]',
                        'v -v[3]',
                        'h -v[2]+3*v[5]',
                        'v v[3]',
                        'h -1.5*v[5]',
                        'v v[1]+2*v[5]',
                        'h 1.5*v[5]',
                        'v v[3]',
                        'h v[2]-3*v[5]',
                        'v -v[3]',
                        'h 1.5*v[5]',
                        'v 2*v[2]+7*v[5]',
                        'h 0.5*v[0]-.5*v[4]',
                        'v v[5]',
                        'h v[4]',
                        'v -v[5]',
                        'h 0.5*v[0]-.5*v[4]',
                        'v -2*v[2]-7*v[5]',
                        'h 1.5*v[5]',
                        'v v[3]',
                        'h v[2]-3*v[5]',
                        'v -v[3]',
                        'h 1.5*v[5]',
                        'v -v[5]',
                        'l .25*v[2] .7*v[2]',
                        'q .1*v[2] .3*v[2]+v[5] .4*v[2] .3*v[2]+v[5]',
                        'h v[0]-1.3*v[2]',
                        'q .3*v[2] 0 .4*v[2] -.3*v[2]+v[5]',
                        'L 0 v[1]',
                        'v 3*v[5]',
                        'c 0.01*v[2] 0.01*v[2] 0.12493362*v[2] 0.171766362*v[2] 0.17430742*v[2] 0.4210019*v[2] 0.0159914*v[2] 0.08027588*v[2] 0.026386*v[2] 0.1683591*v[2] 0.0461754*v[2] 0.24683326*v[2] 0.0197894*v[2] 0.07887456*v[2] 0.0491738*v[2] 0.1479398*v[2] 0.1029452*v[2] 0.19037992*v[2] 0.035981*v[2] 0.0284269*v[2] 0.0827562*v[2] 0.04504256*v[2] 0.145123*v[2] 0.04504256*v[2] 0.186101*v[2] 0*v[2] 0.3132334*v[2] -0.12191518*v[2] 0.3971888*v[2] -0.29587962*v[2] 0.0837554*v[2] -0.1737642*v[2] 0.1363276*v[2] -0.3923708*v[2] 0.1363276*v[2] -0.6059726578*v[2]',
                        'v -0.5*v[1]-3*v[5]+0.5*v[6]',
                        'a 0.5*v[6] 0.5*v[6] l0 l0 l1 0 -v[6]',
                        'L v[2] -3*v[5]',
                        'c 0 -0.213601560062*v[2] -0.0525722187672*v[2] -0.432208501318*v[2] -0.1363276078318*v[2] -0.605972328236*v[2] -0.0839554138126*v[2] -0.173964380832*v[2] -0.2110878098956*v[2] -0.295879993904*v[2] -0.3971887716874*v[2] -0.295879993904*v[2] -0.0623668168442*v[2] 0*v[2] -0.1091420220814*v[2] 0.0166158124*v[2] -0.1451230346676*v[2] 0.04504260992*v[2] -0.0537713618398*v[2] 0.042440171532*v[2] -0.08315579107*v[2] 0.111505330354*v[2] -0.1029451707218*v[2] 0.190380168484*v[2] -0.0197894325684*v[2] 0.078474259468*v[2] -0.0301839990562*v[2] 0.166557115164*v[2] -0.0461753955762*v[2] 0.246833184862*v[2] -0.04937383363*v[2] 0.249235598502*v[2] -0.1643074188316*v[2] 0.411001644702*v[2] -0.1743074391498*v[2] 0.42100182377*v[2]',
                        'z'
                        'M -v[2]-1.5*v[0]+.5*v[4]+.5*v[5] -.75*v[5]',
                        'h -v[4]-v[5]',
                        'v 1.5*v[5]',
                        'h v[4]+v[5]',
                        'z',
                        'm 0 v[1]',
                        'h -v[4]-v[5]',
                        'v 1.5*v[5]',
                        'h v[4]+v[5]',
                        'z',
                    ]
                }
    }
}

with open('c:\caixes\postal-1.json', 'w') as f:
    json.dump(caixa, f, indent=4, sort_keys=True)


rate  = 3.77953232067064    #proporcio d'unitats svg / mm  CorelDraw
pth ="c:\caixes\\" #ruta de eixida fitxer

import svgwrite
import json

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
        for k in j[2:].split():
            if k[0] == "l":
                cadena += k[1:] +" "
            else:
                cadena+=str(eval(k)*rate)+" " #evalua cada fórmula aplicant els valors v[]
    return cadena

with open('c:\caixes\postal-1.json', "r") as file: #importa una caixa paramentrizada en json
    caixa = json.load(file)


v, filename =demana_valors(caixa)


dwg = svgwrite.Drawing(filename, profile='tiny') # Crea un SVG Nom fitxer i ruta

for i in caixa["grupsSVG"].keys():    
    group = dwg.add(dwg.g(id=i)) #afegeix grup al SVG 
    group.add(dwg.path(genera_path(i,caixa)).stroke(color=caixa["grupsSVG"][i]["color"]).fill(color="none")) #afegeix path al grup

dwg.save() #tanca el fitxer SVG

print("\nel fitxer resultat es en" , filename)
