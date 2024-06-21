import json
import svgwrite
import pyperclip
from math import pi, sin, asin, sqrt, pow, cos







cy='(4/7*v[2])'
ro=f'({cy}-2*v[5])'
#ro=f'(18/35*v[2])'
hh=f'(v[0]-(2*({cy}+{ro}-1.75*v[5])))'
ve='((v[2]-v[3])/2)'
gr='(v[2]/2+.5*v[4])'
r='(v[3]/2)'

H0='-v[2]'
H1='4/7*v[2]+3*v[5]'
H2='8/7*v[2]+3*v[5]'
H4='v[1]+3*v[5]-'+cy
H3= H4+'-'+cy
H5=H4+'+'+H1
H6=H5+'+v[2]'
H7=f'({H5})-v[2]'
H8=f'-{ve}+1.5*v[5]'
H9=f'{H5}-1.5*v[5]+{ve}'

x=f"sqrt({r}**2-(.5*v[4])**2)"
y=f'({r}-{x})'


V1='(v[0]+6*v[5])'
V2='(-v[2]-1.5*v[5])'
#V3=f'{V2}-3*v[5]-({cy})-({ro})'
#V4=f'{V3}+3*v[5]'
V5=f'({V2}-3*v[5])'
V4=f'({V5}-v[2])'
V3=f'({V4}-3*v[5])'
V6=f'{V1}+v[2]+1.5*v[5]'
V7=f'{V6}+3*v[5]'
V8=f'{V7}+v[2]'
V9=f'{V8}+3*v[5]'
V10=f'{V7}-v[5]+1.5*v[3]'
V11=f'{V1}-v[3]-1.25*v[5]'
V12=F'({V5}+v[5]-1.5*v[3])'

VV1=f'{V11}-{y}'
VV2=f'1.25*v[5]+v[3]+{y}'

miny=f'{H0}-1.5*v[5]'
minx=V3
maxy=f'{H6}+1.5*v[5]'
maxx=V9


caixa={
    "nom":"esquadrada-",
    "client":"fotodekora",
    "any": 2023,
    "mes:": 5,
    "versió": 1,
    "ca":"Caixa mostrador, amb una cara oberta, apilable, de fàcil muntatgr sense colar ni precintar, cantons reforçats, ideal per transport, emmagatzematge i exposició",
    "es":"Caja mostrador, con una cara abierta, apilable, de fácil montaje sin adhesivos ni precintos, esquinas reforzadas, ideal para transporte, almacenamiento y exposición",
    "en": "Counter display box, with one open side, stackable, easy to assemble without nails or seals, reinforced corners, ideal for transportation, storage, and exhibition.",
    "variables":{
        "v[0]":{"eti":"llarg","es":"longitud","en":"leght","rang":[100,1500,2],"val":284},
        "v[1]":{"eti":"ample","es":"anchura","en":"width","rang":[100,1500,2],"val":248},    
        "v[2]":{"eti":"alt","es":"altura","en":"high","rang":[30,300,2],"val":70},
        "v[3]":{"eti":"diam","es":"diam","en":"diam","rang":[11,30,2], "val":20},
        "v[4]":{"eti":"frontisa","es":"bisagra","en":"hinge","rang":[3,10,2], "val":8},        
        "v[5]":{"eti":"gruix cartro","es":"grosor cartón","en":"carboard width","rang":[.1,12,2],"val":2},
        },
    "minx":minx,
    "miny":miny,
    "maxx":maxx,
    "maxy":maxy,
    "grupsSVG":{
        "hendit":
                {
                "color":"red",
                "path" : ['M 1.25*v[5] -v[2]',
                        'V 0',
                        'h '+cy,
                        'm '+ro+' 0',
                        'h '+hh,
                        'm '+ro+' 0',
                        'h '+cy,
                        'v -v[2]',
                        'M '+V1+' 0',
                        'V '+H1,
                        'M '+V1+' '+H2,
                        'V '+H3,
                        'M '+V1+' '+H4,
                        'V '+H5,
                        'M '+V1+'-1.25*v[5] '+H6,
                        'V '+H5,
                        'h -'+cy,
                        'm -('+ro+') 0',
                        'h -('+hh+')',
                        'm -('+ro+') 0',
                        'h -'+cy,
                        'V '+H6,
                        'M 0 '+H5,
                        'V '+H4,
                        'M 0 '+H3,
                        'V '+H2,
                        'M 0 '+H1,
                        'V 0',
                        'M -v[2]-1.5*v[5] 0',
                        'V '+H5,
                        'm -3*v[5] -1.5*v[5]',
                        'h -v[2]',
                        'm v[2] -v[2]+1.5*v[5]', # diagonal
                        'V v[2]',
                        'M -4.5*v[5]-v[2] 1.5*v[5]',
                        'h -v[2]',
                        'M '+V1+'+4.5*v[5]+2*v[2] 1.5*v[5]',
                        'h -v[2]',
                        'm -3*v[5] -1.5*v[5]', #tik
                        'V '+H5,
                        'm 3*v[5] -1.5*v[5]', #tok
                        'h v[2]',
                        'm -v[2] -v[2]+1.5*v[5]',# diagonal
                        'V v[2]'
                        ]
                },
            "tall" :
                {
                "color": "blue",
                "path" : [
                        'M 1.25*v[5] 0',
                        'H '+V2,
                        'l -3*v[5] 1.5*v[5]', #tok
                        'V '+H0,
                        f'h -({cy})',
                        'l -v[5] -1.5*v[5]', #tuk
                        f'H {V3}',
                        'V 1.5*v[5]',
                        f'H {V4}',
                        'l v[2] v[2]-1.5*v[5]', # diagonal baixant dreta
                        f'M {V5} {H7}',
                        'l -v[2] v[2]-1.5*v[5]', # diagonal baixant esquerra
                        f'H {V3}',
                        f'V {H6}+1.5*v[5]',
                        f'h ({ro})-v[5]',
                        'l v[5] -1.5*v[5]', #tukk
                        f'h {cy}',
                        f'V {H5}-1.5*v[5]',
                        'l 3*v[5] 1.5*v[5]', #tikk
                        f'H 1.25*v[5]',
                        f'M {V1}-1.25*v[5] {H5}',
                        f'H {V6}',
                        'l 3*v[5] -1.5*v[5]', #tikkk
                        f'V {H6}',
                        f'h {cy}',
                        'l v[5] 1.5*v[5]', #tukkk
                        f'H {V9}',
                        f'V {H5}-1.5*v[5]',
                        f'H {V8}',
                        'l -v[2] -v[2]+1.5*v[5]', # diagonal pujant esquerra
                        f'M {V7} v[2]',
                        'l v[2] -v[2]+1.5*v[5]', # diagonal pujant dreta
                        f'H {V9}',
                        f'V {H0}-1.5*v[5]',
                        f'h v[5]-({ro})',
                        'l -v[5] 1.5*v[5]', #tukkkk
                        f'H {V7}',
                        f'V 0+1.5*v[5]',
                        'l -3*v[5] -1.5*v[5]', #tik
                        f'H {V1}-1.25*v[5]',
                        f'M {V7} {H0}',
                        f'H {V5}',
                        f'M {V4} 1.5*v[5]',
                        f'V {H1}',
                        'l -2*v[5] 1.25*v[5]', #pim
                        f'V {H2}-1.25*v[5]',
                        'l 2*v[5] 1.25*v[5]', #-pim
                        f'V {H3}',
                        'l -2*v[5] 1.25*v[5]', #pim
                        f'V {H4}-1.25*v[5]',
                        'l 2*v[5] 1.25*v[5]', #-pim
                        f'V {H5}-1.5*v[5]',
                        f'M {V5} {H6}',
                        f'H {V7}',
                        f'M {V8} {H5}-1.5*v[5]',
                        f'V {H4}',
                        'l 2*v[5] -1.25*v[5]', #pim-
                        f'V {H3}+1.25*v[5]',
                        'l -2*v[5] -1.25*v[5]', #-pim-
                        f'V {H2}',
                        'l 2*v[5] -1.25*v[5]', #pim-
                        f'V {H1}+1.25*v[5]',
                        'l -2*v[5] -1.25*v[5]', #-pim-
                        'V 1.5*v[5]'
                        ]
                },
            "punxonat" :
                {
                "color": "purple",
                "path" : [
                    f'M {V10} {H8}',
                    f'a {r} {r} l0 l1 l1 l.005 l0', # Disc sencer
                    f'M {VV1} -{gr}',
                    f'a {r} {r} l0 l1 l0 l0 v[4]',   # Disc obert per la dreta
                    f'M {V1}-1.25*v[5]-{cy} 0',
                    f'h -{ro} lv 3*v[5] lh {ro} lz', #punxonat roig
                    f'M 1.25*v[5]+{cy}+{ro} 0',
                    f'h -{ro} lv 3*v[5] lh {ro} lz', #punxonat roig
                    f'M {VV2} -{gr}',
                    f'a {r} {r} l0 l1 l1 l0 v[4]',   # Disc obert per l'esquerra
                    f'M {V12} {H8}',
                    f'a {r} {r} l0 l1 l1 l.005 l0', # Disc sencer
                    f'M 0 {H1}',
                    f'v {cy} lh 3*v[5] lv -{cy} lz', #punxonat cyan
                    f'M 0 {H3}',
                    f'v {cy} lh 3*v[5] lv -{cy} lz', #punxonat cyan
                    f'M {V12} {H9}',
                    f'a {r} {r} l0 l1 l0 l.005 l0', # Disc sencer
                    f'M {VV2} {H5}+{gr}',
                    f'a {r} {r} l0 l1 l0 l0 -v[4]',   # Disc obert per l'esquerra
                    f'M 1.25*v[5]+{cy} {H5}',
                    f'h {ro} lv -3*v[5] lh -{ro} lz', #punxonat roig
                    f'M {V1}-1.25*v[5]-{cy}-{ro} {H5}',
                    f'h {ro} lv -3*v[5] lh -{ro} lz', #punxonat roig
                    f'M {VV1} {H5}+{gr}',
                    f'a {r} {r} l0 l1 l1 l0 -v[4]',   # Disc obert per la dreta
                    f'M {V10} {H9}',
                    f'a {r} {r} l0 l1 l0 l.005 l0', # Disc sencer
                    f'M {V1} {H4}',
                    f'v -{cy} lh -3*v[5] lv {cy} lz', #punxonat cyan
                    f'M {V1} {H2}',
                    f'v -{cy} lh -3*v[5] lv {cy} lz', #punxonat cyan
                ]

                }
                
            }
}

file='C:\python_code\\tedragen_dev\models\\frutera.json'

with open(file, 'w') as f:
    json.dump(caixa, f, indent=4, sort_keys=True)


print ('JSON')

rate  = 3.77953232067064    #proporcio d'unitats svg / mm  CorelDraw
pth ="c:\caixes\\" #ruta de eixida fitxer




def demana_valors(obje): #funcio que demana a l'usuari els valor per a les variables modificada per a pasar els valors per defecte
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

with open(file, "r") as file: #importa una caixa paramentrizada en json
    caixa = json.load(file)


v, filename =demana_valors(caixa)


dwg = svgwrite.Drawing(filename, profile='tiny') # Crea un SVG Nom fitxer i ruta

for i in caixa["grupsSVG"].keys():    
    group = dwg.add(dwg.g(id=i)) #afegeix grup al SVG 
    group.add(dwg.path(genera_path(i,caixa)).stroke(color=caixa["grupsSVG"][i]["color"]).fill(color="none")) #afegeix path al grup

dwg.save() #tanca el fitxer SVG

print("\nel fitxer resultat es en" , filename)
pyperclip.copy(filename)
