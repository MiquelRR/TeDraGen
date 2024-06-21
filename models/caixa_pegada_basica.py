import json
import svgwrite
from math import pi, sin, asin, sqrt, pow, cos



f=cos(pi/4)


p1='0 v[1]-.5*v[5]'
p2='-v[2] v[1]'
p3= '-v[0]-v[2] v[1]-.5*v[5]'
p4= '-v[0]-2*v[2] v[1]-.5*v[5]'
p5= '-v[0]-2*v[2] .5*v[5]'
p6= '-v[0]-v[2]-1.5*v[5] .5*v[5]'
p7= '-v[2] .5*v[5]'
p75='-v[2]+1.5*v[5] .5*v[5]'
p8= '0 .5*v[5]'
esp='(1/2)*v[4]'

p9= esp+' -v[2]'
p10= 'v[0]-'+esp+' -v[2]'


h= '-(3/4)*v[0]-v[2]'



r='(3*v[5])'

v1='v[1]+(1/2)*v[2]'
v2='v[1]+(3/4)*v[2]'
v3='(-(10/33)*v[0])'
v4='v[1]+(1/4)*v[0]+2*'+r



miny='-v[2]-v[4]'
minx='-2*v[2]-v[0]'
maxy='v[1]+(3/4)*v[2]'
maxx='v[0]+v[4]'

caixa={
    "nom":"caixa_basica_pegada-",
    "client":"Fotodekora",
    "any": 2023,
    "mes:": 3,
    "versió": 1,
    "ca":"Caixa depegada amb solapa base montables",
    "es":"Caja con solapa pegada y fondo montable",
    "en":"Box with glued flap and mountable bottom",
    "variables":{
        "v[0]":{"eti":"horitzontal","es":"ahorizontal","en":"height","rang":[20,1500,2],"val":86.5},
        "v[1]":{"eti":"vertical","es":"vertical","en":"vertical","rang":[20,1500,2],"val":79},    
        "v[2]":{"eti":"profunditat","es":"profundidad","en":"depth","rang":[20,1500,2],"val":37 },
        "v[3]":{"eti":"solapa pegada","es":"solapa pegada","en":"glued flap","rang":[3,100,2], "val":19},
        "v[4]":{"eti":"tancament","es":"cierre","en":"lock tab","rang":[5,100,2],"val":20},
        "v[5]":{"eti":"gruix","es":"grosor","en":"thickness","rang":[.1,12,2],"val":1.5},
        },
    "minx":minx, 
    "miny":miny,
    "maxx":maxx,
    "maxy":maxy,
    "grupsSVG":{
        "hendit" :
                {
                "color": "red",
                "path" : [
                    'M 0 0',
                    'H v[0]',
                    'V v[1]',
                    'H 0',
                    'Z',
                    'M '+p1,
                    'H -v[2]',
                    'M '+p2,
                    'h -v[0]',
                    'v -v[1]+.5*v[5]',
                    'M '+ p7,
                    'L '+p2,
                    'M '+p3,
                    'L '+p4,
                    'M '+p5,
                    'L '+p6,
                    'M '+p75,
                    'L '+p8,
                    'M '+p9,
                    'L '+p10,]
                },
             "tall" :
                {
                "color": "blue",
                "path" : [
                    'M -.5*v[5]-(.5*v[5])*cos(pi/4) cos(pi/4)*(.5*v[5])',
                    'A .5*v[5] .5*v[5] l0 l0 l0 0 0',
                    'V -v[2]',
                    'L '+p9,
                    'v -v[5]',
                    'h v[5]-'+esp,
                    'v -.5*v[4]',
                    'a .5*v[4] .5*v[4] l0 l0 l1 .5*v[4] -.5*v[4]',
                    'H v[0]-v[5]-.5*v[4]',
                    'a .5*v[4] .5*v[4] l0 l0 l1 .5*v[4] .5*v[4]',
                    'v .5*v[4]',
                    'h v[5]-'+esp,
                    'L '+p10,
                    'H v[0]',
                    'V 0',
                    'l v[3] 3*v[5]',
                    'v v[1]-6*v[5]',
                    'l -v[3] 3*v[5]',
                    'v (3/4)*v[2]',
                    'h -(1/4)*v[0]+'+r,
                    'a '+r+' '+r+' l0 l0 l1 -'+r+' -'+r,
                    'V '+v1,
                    'H (1/4)*v[0]',
                    'v (1/4)*v[2]-'+r,
                    'a '+r+' '+r+' l0 l0 l1 -'+r+' '+r,
                    'H 0',
                    'L '+p1,
                    'l -(1/2)*v[2] (1/4)*v[0]',
                    'V -'+r+'+'+v4,
                    'a '+r+' '+r+' l0 l0 l1 -'+r+' '+r,
                    'H '+p2.split()[0],
                    'L '+p2,
                    'l -(1/4)*v[0] (1/2)*v[2]',
                    'V '+v2+'-'+r,
                    'a '+r+' '+r+' l0 l0 l1 -'+r+' '+r,
                    'H '+h+'+'+r,
                    'a '+r+' '+r+' l0 l0 l1 -'+r+' -'+r,
                    'V '+v1,
                    'L '+p3+'+(1/2)*v[5]',
                    'V '+v4,
                    'h -(1/2)*v[2]+'+r,
                    'a '+r+' '+r+' l0 l0 l1 -'+r+' -'+r,
                    'V v[1]+(1/4)*v[0]-(1/2)*v[5]',
                    'L '+p4,
                    'L '+p5,
                    'l 2*v[5] -1.5*v[5]',
                    'V '+v3,
                    'H -6*v[5]+'+p6.split()[0],
                    's 1.4*v[5] 0 1.8*v[5] 1.45*v[5]',
                    'l 1.2*v[5] .11*v[0]',
                    'L '+p6.split()[0]+' .35*'+v3,
                    'L '+p6,
                    'L '+p75,
                    'V .35*'+v3,
                    'L '+p75.split()[0]+'+3*v[5] 1.45*v[5]+.11*v[0]+'+v3,
                    'l 1.2*v[5] -.11*v[0]',
                    's .4*v[5] -1.45*v[5] 1.8*v[5] -1.45*v[5]',
                    'H -2*v[5]',
                    'V -v[5]',
                    'Z'
                     
                    



                ]
                }
         }
}

with open('C:\python_code\\tedragen_dev\models\\'+caixa["nom"]+'.json', 'w') as f:
    print ('JSON')
    json.dump(caixa, f, indent=4, sort_keys=True)



rate  = 3.77953232067064    #proporcio d'unitats svg / mm  CorelDraw
pth ="C:\python_code\\tedragen_dev\caixes\\" #ruta de eixida fitxer




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
                
                k=str(k).replace('_',' ')
                print(k,"= ",end="")
                cadena+=str(eval(k)*rate)+" " #evalua cada fórmula aplicant els valors v[]
                print(eval(k))
    return cadena

with open('C:\python_code\\tedragen_dev\models\\'+caixa["nom"]+".json", "r") as file: #importa una caixa paramentrizada en json
    caixa = json.load(file)


v, filename =demana_valors(caixa)


dwg = svgwrite.Drawing(filename, profile='tiny') # Crea un SVG Nom fitxer i ruta

for i in caixa["grupsSVG"].keys():    
    group = dwg.add(dwg.g(id=i)) #afegeix grup al SVG 
    print(i)
    group.add(dwg.path(genera_path(i,caixa)).stroke(color=caixa["grupsSVG"][i]["color"]).fill(color="none")) #afegeix path al grup

dwg.save() #tanca el fitxer SVG
