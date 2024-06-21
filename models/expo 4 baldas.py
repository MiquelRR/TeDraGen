import json
import svgwrite
from math import pi, sin, asin, sqrt, pow, cos






baldes=4

f='(v[1]+4*v[5]+2*v[6])'
s='('+str(1/baldes)+'*v[2]-'+str(10/baldes)+'*v[5])' #espai entre baldes


vt='.1'


h0='.5*v[0]+.5*v[5]'
h0n='-('+h0+')'
h1=h0+'+0.231972049689441*'+f
h1n='-('+h1+')'
h2=h0+'+0.301127329192547*'+f
h2n='-('+h2+')'
h3='0.30833333333333333*(v[0]-2*v[6]-2*v[7])'

h3n='-v[6]-v[7]-'+h3

r1='(.5*v[0]-v[6]-v[7]-'+h3+')'
r2='(v[6]+2*'+h3+')'

b1='6*v[5]+'+s
b2='6*v[5]+2*'+s
b3='6*v[5]+3*'+s
b4='6*v[5]+4*'+s

ref='('+b1+'-1.5*v[3]-1.5*v[6])' #altura superior lliure
sup = '0.244372990353698*'+ref #superposició corona amb cos principal



p1= h0+'+0.347391304347826*'+f+ ' 0.0556130081300813*'+ref
p1n='-('+h0+'+0.347391304347826*'+f+ ')  0.0556130081300813*'+ref
p3= h0+'+0.920164596273292*'+f+' 0.722035772357724*'+ref
p3n='-('+h0+'+0.920164596273292*'+f+') 0.722035772357724*'+ref
p4=h0+'+'+f+' 0.813008130081301*'+ref
p4n='-('+h0+'+'+f+') 0.813008130081301*'+ref
p5=h0+'+'+f+' +0.939586991869919*'+ref



dv='+2*v[3]+v[1]+3*v[5]'

v1='v[3]+v[2]'
v2=v1+dv
v3=v2+dv
v4=v3+dv

inc='h v[7]+v[6] '+'lv -v[5]-v[6] '+'lh 2*v[5] '+'lv -v[5]-3*v[6] '+'lh -'+vt+' '+'lv v[5]+3*v[6]-'+vt+' '+'lh -v[7]-v[6]-4*v[5]+2*'+vt+' '+'lv -v[5]-3*v[6]+'+vt+' lh -'+vt+' lv v[5]+3*v[6] '+'lh 2*v[5] lz'
incv ='h -v[5]-v[6] lv v[3]+v[6] lh +v[5]+v[6] lv -.5*v[3]-.5*v[6] lh -v[5]-v[6]+'+vt+' lv -.5*v[3]-.5*v[6]+'+vt+' lh +v[5]+v[6]-'+vt+' lz'
incvn='h +v[5]+v[6] lv v[3]+v[6] lh -v[5]-v[6] lv -.5*v[3]-.5*v[6] lh +v[5]+v[6]-'+vt+' lv -.5*v[3]-.5*v[6]+'+vt+' lh -v[5]-v[6]+'+vt+' lz'

t=  'v v[5]+v[6] lh 2*v[5] lv v[5] ll -(v[5]-v[6]) (v[5]-v[6]) lh -(v[7]+4*v[5]-2*(v[5]-v[6])) ll -(v[5]-v[6]) -(v[5]-v[6]) lv -v[5] lh 2*v[5] lv -v[5]-v[6]'


sth='h 4*v[5]+v[7]+v[6]' #semitall horitzontal
stv='v .5*v[3]+.5*v[6]'




miny='0'
minx=h0n+'-'+f
maxy=v4+dv
maxx=h0+'+'+f

caixa={
    "nom":"display-4-baldas-",
    "client":"polcart",
    "any": 2023,
    "mes:": 2,
    "versió": 1,
    "ca":"Display estanteria expositor de 4 baldes",
    "es":"Display estantería expositor de 4 baldas",
    "en":"Display shelf exhibitor of 4 buckets",
    "variables":{
        "v[0]":{"eti":"ample util balda","es":"ancho util balda","en":"bucket width","rang":[20,1500,2],"val":500},
        "v[1]":{"eti":"fondo balda","es":"profundidad balda","en":"bucket depth","rang":[20,1500,2],"val":300},    
        "v[2]":{"eti":"altura cos principal","es":"altura cuerpo principal","en":"principal body height","rang":[300,3000,2],"val":1450 },
        "v[3]":{"eti":"frontals baldes","es":"frontales de balda","en":"bucket front","rang":[10,200,2], "val":45},
        "v[4]":{"eti":"altura corona","es":"altura corona","en":"crown height","rang":[30,1200,2],"val":287},
        "v[5]":{"eti":"gruix","es":"grosor","en":"thickness","rang":[.1,25,2],"val":5},
        "v[6]":{"eti":"marge en gruix","es":"holgura grosor","en":"clearance in thickness","rang":[.05,5,2],"val":1},
        "v[7]":{"eti":"enganxes baldes","es":"enganches baldas","en":"shelf hooks","rang":[5,150,2],"val":39},
        },
    "minx":minx, 
    "miny":miny,
    "maxx":maxx,
    "maxy":maxy,
    "grupsSVG":{
        "tall_corona" :
                {
                "color": "blue",
                "path" : [
                    'M  .5*v[0]-.5*v[6]-0.05*v[0] -v[3]-v[4]-'+sup,
                    'a 0.05*v[0] 0.05*v[0] l0 l0 l1 0.05*v[0] 0.05*v[0]',
                    'v v[4]-0.05*v[0]+'+sup,
                    'h -.5*v[0]+v[7]+v[5]+'+h3,
                    'q -v[5] 0 -v[5] -v[5]',
                    'v 2*v[5]-'+sup,
                    'q 0 -v[5] -v[5] -v[5]',
                    'h -.5*v[7]+v[5]',
                    'q -.87*v[5] 0 -.95*v[5] .5*v[5]',
                    'L .2*v[5]+'+h3+' -.6*v[5]-v[3]',
                    'Q '+h3+' -v[3] '+h3+'-.6*v[5] -v[3]',
                    'H .6*v[5]-'+h3,
                    'Q -'+h3+' -v[3] -'+h3+'-.2*v[5] -.6*v[5]-v[3]',
                    'l 1.25*v[5]-0.5*v[7] 1.1*v[5]-'+sup,
                    'q -.05*v[5] -.5*v[5] -.95*v[5] -.5*v[5]',#
                    'h -.5*v[7]+v[5]',
                    'q -v[5] 0 -v[5] v[5]',
                    'v -2*v[5]+'+sup,
                    'q 0 v[5] -v[5] v[5]',
                    'h -.5*v[0]+v[7]+v[5]+'+h3,
                    'v -v[4]+0.05*v[0]-'+sup,
                    'a 0.05*v[0] 0.05*v[0] l0 l0 l1 0.05*v[0] -0.05*v[0]',
                    'Z'
                    ]
                },


        "tall_silueta_ppal" :
                {
                "color": "blue",
                "path" : [
                    'M '+h1+' 0',
                    'Q '+h2+' 0 '+p1,
                    'L '+p3,
                    'Q '+p4+' '+p5,
                    'V v[2]',
                    'H '+h0n+'-'+f,
                    'V '+p5.split(' ')[1],
                    'Q '+p4n+' ' +p3n,
                    'L '+p1n,
                    'Q '+h2n+' 0 '+h1n+' 0',
                    'Z '
                    ]
                },
                "incisions" :
                {
                "color": "blue",
                "path" : [
                    #hor
                    'M '+h3n+' '+b1,
                    inc,
                    'M '+h3+' '+b1,
                    inc,
                    'M '+h3+' '+b2,
                    inc,
                    'M '+h3n+' '+b2,
                    inc,
                     'M '+h3+' '+b3,
                    inc,
                    'M '+h3n+' '+b3,
                    inc,
                     'M '+h3+' '+b4,
                    inc,
                    'M '+h3n+' '+b4,
                    inc,
                    #ver
                    'M '+h0+'+v[1] '+b1+'-1.5*v[3]-1.5*v[6]',
                    incvn,
                    'M '+h0+'+v[1] '+b2+'-1.5*v[3]-1.5*v[6]',
                    incvn,
                    'M '+h0+'+v[1] '+b3+'-1.5*v[3]-1.5*v[6]',
                    incvn,
                    'M '+h0+'+v[1] '+b4+'-1.5*v[3]-1.5*v[6]',
                    incvn,
                    'M '+h0n+'-v[1] '+b4+'-1.5*v[3]-1.5*v[6]',
                    incv,
                    'M '+h0n+'-v[1] '+b3+'-1.5*v[3]-1.5*v[6]',
                    incv,
                    'M '+h0n+'-v[1] '+b2+'-1.5*v[3]-1.5*v[6]',
                    incv,
                    'M '+h0n+'-v[1] '+b1+'-1.5*v[3]-1.5*v[6]',
                    incv,
                          
                ]   
                },
                "semitall" :
                {
                "color": "green",
                "path" : [
                    #hor
                    'M '+h3n+'-2*v[5] '+b1+'-2*v[5]-4*v[6]',
                    sth,
                    'M '+h3+'-2*v[5] '+b1+'-2*v[5]-4*v[6]',
                    sth,
                    'M '+h3+'-2*v[5] '+b2+'-2*v[5]-4*v[6]',
                    sth,
                    'M '+h3n+'-2*v[5] '+b2+'-2*v[5]-4*v[6]',
                    sth,
                     'M '+h3+'-2*v[5] '+b3+'-2*v[5]-4*v[6]',
                    sth,
                    'M '+h3n+'-2*v[5] '+b3+'-2*v[5]-4*v[6]',
                    sth,
                     'M '+h3+'-2*v[5] '+b4+'-2*v[5]-4*v[6]',
                    sth,
                    'M '+h3n+'-2*v[5] '+b4+'-2*v[5]-4*v[6]',
                    sth,
                    #ver
                    'M '+h0+'+v[1] '+b1+'-1.5*v[3]-1.5*v[6]',
                    stv,
                    'M '+h0+'+v[1] '+b2+'-1.5*v[3]-1.5*v[6]',
                    stv,
                    'M '+h0+'+v[1] '+b3+'-1.5*v[3]-1.5*v[6]',
                    stv,
                    'M '+h0+'+v[1] '+b4+'-1.5*v[3]-1.5*v[6]',
                    stv,
                    'M '+h0n+'-v[1] '+b4+'-1.5*v[3]-1.5*v[6]',
                    stv,
                    'M '+h0n+'-v[1] '+b3+'-1.5*v[3]-1.5*v[6]',
                    stv,
                    'M '+h0n+'-v[1] '+b2+'-1.5*v[3]-1.5*v[6]',
                    stv,
                    'M '+h0n+'-v[1] '+b1+'-1.5*v[3]-1.5*v[6]',
                    stv,                 
                ]   
                },
                "hendit_ppal" :
                {
                "color": "red",
                "path" : [
                    'M '+h0+' 0',
                    'V v[2]',
                    'M '+h0n+' v[2]',
                    'V 0'
                ]
                },
                "tall_balda1" :
                {
                "color": "blue",
                "path" : [
                    'M .5*v[0]+v[5]+.5*v[6] '+v1,
                    'a .5*v[3] .5*v[3] l0 l0 l1 0 v[3]',
                    'v -.5*v[3]-.5*v[6]',
                    'h -v[5]-v[6]',
                    'v .5*v[3]+.5*v[6]+v[1]',
                    'h -'+r1,
                    t,
                    'h -'+r2,
                    t,
                    'h -'+r1,
                    'v -.5*v[3]-.5*v[6]-v[1]',
                    'h -v[5]-v[6]',
                    'v .5*v[3]+.5*v[6]',
                    'a .5*v[3] .5*v[3] l0 l0 l1 0 -v[3]',
                    'z'
                ]
                },
                "hendit_balda1" :
                {
                "color": "red",
                "path" : [
                    'M .5*v[0]-.5*v[6] '+v1+'+v[3]',
                    'h -v[0]+v[6]'
                ]
                },
                 "tall_balda2" :
                {
                "color": "blue",
                "path" : [
                    'M .5*v[0]+v[5]+.5*v[6] '+v2,
                    'a .5*v[3] .5*v[3] l0 l0 l1 0 v[3]',
                    'v -.5*v[3]-.5*v[6]',
                    'h -v[5]-v[6]',
                    'v .5*v[3]+.5*v[6]+v[1]',
                    'h -'+r1,
                    t,
                    'h -'+r2,
                    t,
                    'h -'+r1,
                    'v -.5*v[3]-.5*v[6]-v[1]',
                    'h -v[5]-v[6]',
                    'v .5*v[3]+.5*v[6]',
                    'a .5*v[3] .5*v[3] l0 l0 l1 0 -v[3]',
                    'z'
                ]
                },
                "hendit_balda2" :
                {
                "color": "red",
                "path" : [
                    'M .5*v[0]-.5*v[6] '+v2+'+v[3]',
                    'h -v[0]+v[6]'
                ]
                },
                 "tall_balda3" :
                {
                "color": "blue",
                "path" : [
                    'M .5*v[0]+v[5]+.5*v[6] '+v3,
                    'a .5*v[3] .5*v[3] l0 l0 l1 0 v[3]',
                    'v -.5*v[3]-.5*v[6]',
                    'h -v[5]-v[6]',
                    'v .5*v[3]+.5*v[6]+v[1]',
                    'h -'+r1,
                    t,
                    'h -'+r2,
                    t,
                    'h -'+r1,
                    'v -.5*v[3]-.5*v[6]-v[1]',
                    'h -v[5]-v[6]',
                    'v .5*v[3]+.5*v[6]',
                    'a .5*v[3] .5*v[3] l0 l0 l1 0 -v[3]',
                    'z'
                ]
                },
                "hendit_balda3" :
                {
                "color": "red",
                "path" : [
                    'M .5*v[0]-.5*v[6] '+v3+'+v[3]',
                    'h -v[0]+v[6]'
                ]
                },
                 "tall_balda4" :
                {
                "color": "blue",
                "path" : [
                    'M .5*v[0]+v[5]+.5*v[6] '+v4,
                    'a .5*v[3] .5*v[3] l0 l0 l1 0 v[3]',
                    'v -.5*v[3]-.5*v[6]',
                    'h -v[5]-v[6]',
                    'v .5*v[3]+.5*v[6]+v[1]',
                    'h -'+r1,
                    t,
                    'h -'+r2,
                    t,
                    'h -'+r1,
                    'v -.5*v[3]-.5*v[6]-v[1]',
                    'h -v[5]-v[6]',
                    'v .5*v[3]+.5*v[6]',
                    'a .5*v[3] .5*v[3] l0 l0 l1 0 -v[3]',
                    'z'
                ]
                },
                "hendit_balda4" :
                {
                "color": "red",
                "path" : [
                    'M .5*v[0]-.5*v[6] '+v4+'+v[3]',
                    'h -v[0]+v[6]'
                ]
                },
                "corona" :
                {
                "color": "blue",
                "path" : [
                    'M .5*v[0]-.5*v[6] '+v4+'+v[3]',
                    'h -v[0]+v[6]'
                ]
                },




         
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
