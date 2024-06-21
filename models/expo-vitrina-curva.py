import json
import svgwrite
from math import pi, sin, asin, sqrt, pow, cos



a='abs(v[0]-v[5]-v[7])'
b='abs(-v[1]+v[5]+v[6])'
h='sqrt(pow('+a+',2)+pow('+b+',2))'
alpha='asin('+b+'/'+h+')'
beta='(pi-2*'+alpha+')'
radio='('+b+'/sin('+beta+'))'
arc=radio+'*'+beta

radi2='('+radio+'-2*v[4]-.5*v[3])'
ix=radi2+"-"+radi2+"*cos(abs("+beta+")*.4)"
iy=radi2+"*-sin(abs("+beta+")*.4)"


d='2.5*v[4]'
dx='v[7]-2.75*v[5]-'+d

h1='v[1]+3*v[4]'
h2=h1+'+3*v[4]'
h3=h2+'+5.75*v[5]+'+d
h4=h3+'+'+dx
h6=h3+'+v[0]-1.5*v[5]'
h5=h6+'-('+dx+')-'+d+'-v[5]'
h7=h6+'+4.75*v[5]'
h9=h6+'+v[6]-.75*v[5]'
h8=h9+'-2*v[5]-'+d
h10=arc+'+'+h9
h11=h10+'+v[5]'
h12=h11+'+'+d+'+v[5]+'+dx
h13=h12+'+4.75*v[5]'
h14=h13+'+v[5]+3*v[4]+'+d

sp='(v[2]-3*v[4])/3'
v1='.95*v[4]'
v2=v1+'+'+sp
v4='v[2]-2.05*v[4]'
v3=v4+'-'+sp


espai='(v[0]+2*v[4]+3*v[5])'

miny='0'
minx='0'
maxy=v4
maxx=espai+'*5_if_'+espai+'*5>v[2]_else_v[2]'
mos='a .5*v[5] .5*v[5] l0 l0 l1 0 v[5]'
mox='a .5*v[5] .5*v[5] l0 l0 l1 0 -v[5]'
bx='v '+d+'+v[5] lh 1.1*v[4] lv -'+d+'-v[5] lz'
tl='a .5*v[3] .5*v[3] l0 l0 l1 0 v[3] la .5*v[3] .5*v[3] l0 l0 l1 0 -v[3] lz'







caixa={
    "nom":"expo-vitrina-curva-",
    "client":"fotodekora",
    "any": 2023,
    "mes:": 1,
    "versió": 1,
    "ca":"Vitrina de frontal corb amb tres baldes amb accés al producte per un lateral",
    "es":"Vitrina de frente curvo con tres estantes abierta con acceso al producto por lateral",
    "en":"Showcase with curved front with three buckets with access to the product on one side",
    "variables":{
        "v[0]":{"eti":"ample","es":"ancho","en":"width","rang":[100,1000,2],"val":174},
        "v[1]":{"eti":"llarg","es":"largo","en":"length","rang":[150,1500,2],"val":300},    
        "v[2]":{"eti":"alt","es":"altura","en":"height","rang":[300,3000,2],"val":1035 },
        "v[3]":{"eti":"taladres","es":"taladros","en":"drill","rang":[1,25,2], "val":3},
        "v[4]":{"eti":"gruix baldes","es":"grosor baldas","en":"shelves thickness","rang":[1,40,2],"val":4},
        "v[5]":{"eti":"gruix lamina","es":"grosor lamina","en":"cover thickness","rang":[.1,10,2],"val":2},
        "v[6]":{"eti":"planol frontal","es":"plano frontal","en":"straight front","rang":[50,1200,2],"val":100},
        "v[7]":{"eti":"planol lateral","es":"plano lateral","en":"straight side","rang":[50,1200,2],"val":40},

        },
    "minx":minx,
    "miny":miny,
    "maxx":maxx,
    "maxy":maxy,
    "grupsSVG":{

        "tall_baldes" :
                {
                "color": "blue",
                "path" : [
                    #primera
                    'M 0 0',
                    'm v[0]-v[7]+1.5*v[5] v[5]',
                    'v -v[5]',
                    'h '+d,
                    'v v[5]',
                    'h v[7]-2.5*v[4]-5*v[5]',
                    'a 2.5*v[5] 2.5*v[5] l0 l0 l1 2.5*v[5] 2.5*v[5]',
                    'v 2.5*v[5]',
                    'h v[5]', 
                    'l v[5] '+d,
                    'a .5*v[5] .5*v[5] l0 l0 l1 -v[5] 0',
                    'h -v[5]',
                    'v v[1]-12*v[5]-2*'+d,
                    'h v[5]',
                    'a .5*v[5] .5*v[5] l0 l0 l1 v[5] 0',
                    'l -v[5] '+d,
                    'h -v[5]',
                    'v 2.5*v[5]',
                    'a 2.5*v[5] 2.5*v[5] l0 l0 l1 -2.5*v[5] 2.5*v[5]',
                    'h 5*v[5]-v[7]+'+d,
                    'v v[5]',
                    'h -'+d,
                    'v -v[5]',
                    'h -v[0]+2*v[7]-3*v[5]',
                    'v v[5]',
                    'h -'+d,
                    'v -v[5]',
                    'h 5*v[5]-v[7]+'+d,
                    'a 2.5*v[5] 2.5*v[5] l0 l0 l1 -2.5*v[5] -2.5*v[5]',
                    'v -2.5*v[5]',
                    'h -v[5]',
                    'v -'+d,
                    'h v[5]',
                    'v -v[6]+7.5*v[5]+2*'+d,
                    'h -v[5]',
                    'v -'+d,
                    'h v[5]',
                    'v -1.5*v[5]',
                    'a '+radio+' '+radio+' l0 l0 l1 '+a+' -'+b,
                    'z',
                    #segunda
                    'M '+espai+' 0',
                    'm v[0]-v[7]+1.5*v[5] v[5]',
                    'v -v[5]',
                    'h '+d,
                    'v v[5]',
                    'h v[7]-2.5*v[4]-5*v[5]',
                    'a 2.5*v[5] 2.5*v[5] l0 l0 l1 2.5*v[5] 2.5*v[5]',
                    'v 2.5*v[5]',
                    'h v[5]', 
                    'l v[5] '+d,
                    'a .5*v[5] .5*v[5] l0 l0 l1 -v[5] 0',
                    'h -v[5]',
                    'v v[1]-12*v[5]-2*'+d,
                    'h v[5]',
                    'a .5*v[5] .5*v[5] l0 l0 l1 v[5] 0',
                    'l -v[5] '+d,
                    'h -v[5]',
                    'v 2.5*v[5]',
                    'a 2.5*v[5] 2.5*v[5] l0 l0 l1 -2.5*v[5] 2.5*v[5]',
                    'h 5*v[5]-v[7]+'+d,
                    'v v[5]',
                    'h -'+d,
                    'v -v[5]',
                    'h -v[0]+2*v[7]-3*v[5]',
                    'v v[5]',
                    'h -'+d,
                    'v -v[5]',
                    'h 5*v[5]-v[7]+'+d,
                    'a 2.5*v[5] 2.5*v[5] l0 l0 l1 -2.5*v[5] -2.5*v[5]',
                    'v -2.5*v[5]',
                    'h -v[5]',
                    'v -'+d,
                    'h v[5]',
                    'v -v[6]+7.5*v[5]+2*'+d,
                    'h -v[5]',
                    'v -'+d,
                    'h v[5]',
                    'v -1.5*v[5]',
                    'a '+radio+' '+radio+' l0 l0 l1 '+a+' -'+b,
                    'z',
                    #tercera
                    'M 2*'+espai+' 0',
                    'm v[0]-v[7]+1.5*v[5] v[5]',
                    'v -v[5]',
                    'h '+d,
                    'v v[5]',
                    'h v[7]-2.5*v[4]-5*v[5]',
                    'a 2.5*v[5] 2.5*v[5] l0 l0 l1 2.5*v[5] 2.5*v[5]',
                    'v 2.5*v[5]',
                    'h v[5]', 
                    'l v[5] '+d,
                    'a .5*v[5] .5*v[5] l0 l0 l1 -v[5] 0',
                    'h -v[5]',
                    'v v[1]-12*v[5]-2*'+d,
                    'h v[5]',
                    'a .5*v[5] .5*v[5] l0 l0 l1 v[5] 0',
                    'l -v[5] '+d,
                    'h -v[5]',
                    'v 2.5*v[5]',
                    'a 2.5*v[5] 2.5*v[5] l0 l0 l1 -2.5*v[5] 2.5*v[5]',
                    'h 5*v[5]-v[7]+'+d,
                    'v v[5]',
                    'h -'+d,
                    'v -v[5]',
                    'h -v[0]+2*v[7]-3*v[5]',
                    'v v[5]',
                    'h -'+d,
                    'v -v[5]',
                    'h 5*v[5]-v[7]+'+d,
                    'a 2.5*v[5] 2.5*v[5] l0 l0 l1 -2.5*v[5] -2.5*v[5]',
                    'v -2.5*v[5]',
                    'h -v[5]',
                    'v -'+d,
                    'h v[5]',
                    'v -v[6]+7.5*v[5]+2*'+d,
                    'h -v[5]',
                    'v -'+d,
                    'h v[5]',
                    'v -1.5*v[5]',
                    'a '+radio+' '+radio+' l0 l0 l1 '+a+' -'+b,
                    'z',
                    #cuarta
                    'M 3*'+espai+' 0',
                    'm v[0]-v[7]+1.5*v[5] v[5]',
                    'v -v[5]',
                    'h '+d,
                    'v v[5]',
                    'h v[7]-2.5*v[4]-5*v[5]',
                    'a 2.5*v[5] 2.5*v[5] l0 l0 l1 2.5*v[5] 2.5*v[5]',
                    'v 2.5*v[5]',
                    'h v[5]', 
                    'l v[5] '+d,
                    'a .5*v[5] .5*v[5] l0 l0 l1 -v[5] 0',
                    'h -v[5]',
                    'v v[1]-12*v[5]-2*'+d,
                    'h v[5]',
                    'a .5*v[5] .5*v[5] l0 l0 l1 v[5] 0',
                    'l -v[5] '+d,
                    'h -v[5]',
                    'v 2.5*v[5]',
                    'a 2.5*v[5] 2.5*v[5] l0 l0 l1 -2.5*v[5] 2.5*v[5]',
                    'h 5*v[5]-v[7]+'+d,
                    'v v[5]',
                    'h -'+d,
                    'v -v[5]',
                    'h -v[0]+2*v[7]-3*v[5]',
                    'v v[5]',
                    'h -'+d,
                    'v -v[5]',
                    'h 5*v[5]-v[7]+'+d,
                    'a 2.5*v[5] 2.5*v[5] l0 l0 l1 -2.5*v[5] -2.5*v[5]',
                    'v -2.5*v[5]',
                    'h -v[5]',
                    'v -'+d,
                    'h v[5]',
                    'v -v[6]+7.5*v[5]+2*'+d,
                    'h -v[5]',
                    'v -'+d,
                    'h v[5]',
                    'v -1.5*v[5]',
                    'a '+radio+' '+radio+' l0 l0 l1 '+a+' -'+b,
                    'z',
                     
                    #quinta
                    'M 4*'+espai+' 0',
                    'm v[0]-3.5*v[5] v[5]',
                    'a 2.5*v[5] 2.5*v[5] l0 l0 l1 2.5*v[5] 2.5*v[5]',
                    'v v[1]-7*v[5]',
                    'a 2.5*v[5] 2.5*v[5] l0 l0 l1 -2.5*v[5] 2.5*v[5]',
                    'h -v[0]+7*v[5]',                     
                    'a 2.5*v[5] 2.5*v[5] l0 l0 l1 -2.5*v[5] -2.5*v[5]',
                    'v -v[6]+3.5*v[5]',
                    'a '+radio+' '+radio+' l0 l0 l1 '+a+' -'+b,
                    'z'
                    
                    ]
                },

         "taladres_baldes":
                {
                 "color": "green",
                 "path" : [
                     #cuarta
                     'M 3*'+espai+' 0',
                     'm v[0]-v[5]-2*v[4]-.5*v[3] v[5]+2*v[4]',tl,
                     'm 0 v[1]-2*v[5]-4*v[4]-v[3]',tl,
                     'm -v[0]+2*v[5]+4*v[4]+v[3] 0',tl,

                     'm '+ix+' -v[6]+v[5]+2*v[4]+v[3]+'+iy,tl,

                     #quinta
                     'M 4*'+espai+' 0',
                     'm v[0]-v[5]-2*v[4]-.5*v[3] v[5]+2*v[4]',tl,
                     'm 0 v[1]-2*v[5]-4*v[4]-v[3]',tl,
                     'm -v[0]+2*v[5]+4*v[4]+v[3] 0',tl,
                     'm '+ix+' -v[6]+v[5]+2*v[4]+v[3]+'+iy,tl
                     ]
                },
            "tall_lamina":{
                "color": "blue",
                "path": [
                    'M 0 '+h1,
                    'V -.5*v[5]+'+h3,mos,
                    'V -.5*v[5]+'+h6,mos,
                    'V -.5*v[5]+'+h10,mos,
                    'V -.5*v[5]+'+h12,mos,
                    'V '+h14,
                    'H v[2]',
                    'V +.5*v[5]+'+h12,mox,
                    'V +.5*v[5]+'+h10,mox,
                    'V +.5*v[5]+'+h6,mox,
                    'V +.5*v[5]+'+h3,mox,
                    'V '+h1,
                    'Z'
                    ]
                },
            "taladres_lamina":{
                "color":"green",
                "path":[
                    'M 5*v[4]+'+v1+' '+h4,tl,
                    'M 5*v[4]+'+v1+' '+h5+'+'+d+'+v[5]-v[3]',tl,
                    'M -4*v[4]+'+v4+' '+h5+'+'+d+'+v[5]-v[3]',tl,
                    'M -4*v[4]+'+v4+' '+h4,tl,

                ]

            },
            "punxons":{
                "color": "green",
                "path":[
                    'M '+v1+' '+h2,bx,'M '+v2+' '+h2,bx,'M '+v3+' '+h2,bx,'M '+v4+' '+h2,bx,
                    'M '+v1+' '+h4,bx,'M '+v2+' '+h4,bx,'M '+v3+' '+h4,bx,'M '+v4+' '+h4,bx,
                    'M '+v1+' '+h5,bx,'M '+v2+' '+h5,bx,'M '+v3+' '+h5,bx,'M '+v4+' '+h5,bx,
                    'M '+v1+' '+h7,bx,'M '+v2+' '+h7,bx,'M '+v3+' '+h7,bx,'M '+v4+' '+h7,bx,
                    'M '+v1+' '+h8,bx,'M '+v2+' '+h8,bx,'M '+v3+' '+h8,bx,'M '+v4+' '+h8,bx,
                    'M '+v1+' '+h11,bx,'M '+v2+' '+h11,bx,'M '+v3+' '+h11,bx,'M '+v4+' '+h11,bx,
                    'M '+v1+' '+h13,bx,'M '+v2+' '+h13,bx,'M '+v3+' '+h13,bx,'M '+v4+' '+h13,bx,
                  ]
                },
            "hendit90":{
                "color":"red",
                "path":[
                    'M -0 '+h3,'H v[2]',
                    'M -0 '+h6,'H v[2]',
                    'M -0 '+h12,'H v[2]'
                ]
             },
             "hendit_menor":{
                "color":"yellow",
                "path":[
                    'M -0 '+h10,'H v[2]'
                ]
             },
    }
}



with open('C:\python_code\\tedragen_dev\models\expo-vitrina-curva-.json', 'w') as f:
    json.dump(caixa, f, indent=4, sort_keys=True)


print ('JSON')

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

with open('C:\python_code\\tedragen_dev\models\expo-vitrina-curva-.json', "r") as file: #importa una caixa paramentrizada en json
    caixa = json.load(file)


v, filename =demana_valors(caixa)


dwg = svgwrite.Drawing(filename, profile='tiny') # Crea un SVG Nom fitxer i ruta

for i in caixa["grupsSVG"].keys():    
    group = dwg.add(dwg.g(id=i)) #afegeix grup al SVG 
    print(i)
    group.add(dwg.path(genera_path(i,caixa)).stroke(color=caixa["grupsSVG"][i]["color"]).fill(color="none")) #afegeix path al grup

dwg.save() #tanca el fitxer SVG
print("radio", eval(radio)*eval(beta))
print(eval(ix),eval(iy))
print("alfa", eval(alpha))
print('beta',  eval(beta))
print("coseno beta/2",eval("cos("+beta+"/2)"))
print("espai",eval(espai))
print("longitud",eval(radio+"*"+beta))
print("\nel fitxer resultat es en" , filename)
