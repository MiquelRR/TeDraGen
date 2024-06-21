
"""
modul que importa un arxiy SVG i localitza els paths(segments) que tenen com a nom rfxxxx
amb ells crea "osos" dins dun arxiu de blender amb la direcció i la llargaria del segments
els selecciona tots i fa un "join" per que es queden a la mateixa armadura
FALTA ASIGNAR LES RELACIONS ENTRE OSOS : ELS OSOS QUE ACABEN UN UN ALTRE ESCMENÇA SON PARE I FILL


NOMENCLATURA DEL OSOS
rf-A9-99-90-N
A:indica el conjunt de osos A, B,C... junt la xifra despres del conjunt es l'eidentrificador unic
99 : indica l'odre de plegat de l'animació la s'animarán per decenes,fins que no acaben els de
la primera decena no sescomenza la següent
90 - indica els graus sexagesimals de rotació máxims
N/R: indica el sentir normal de l'animació o el revers


Nomenclatura dels objectes
ob-A9-999-MAT
A9 -es coincident amb l'os que li genera influència
999 es l'espesor en décimes de mm si es 000 no es
realment un objecte per a solidificar, indicaria un àrea d'influencia d'un os
MAT  es el codi-acònim del material

"""
import bpy
from math import pi

archivo_svg = "C:\\Users\\miquel\\Downloads\\proves-caixa-plana.svg"

import svgpathtools

def orienta(inici,final):
    """
    retorna l'eIx x o y sobre el que tombar l'os i la direcció
    a partir dels punts d'inici i final
    """
    if inici[1]==final[1]:
        eix= "Y"
        dir = -1 if final[0] < inici[0] else 1
    else:
        eix= "X"
        dir = -1 if final[1] > inici[1] else 1
    return eix,dir


def listar_paths(svg_file):
    resultados = []
    
    #OJO  esa es la escala que he tret per "ingenyeria inversa" vamos que no tinc la minima idea de perque
    sc=3542.1

    paths, attributes = svgpathtools.svg2paths(svg_file)
    
    for i, path in enumerate(paths):
        if attributes[i].get('id').startswith('rf'):
            stroke_color = attributes[i].get('stroke:')
            longitud = abs(path.length())
            start = path.point(0)
            end = path.point(1)
            
            resultados.append({
                'id': attributes[i].get('id'),
                'color': stroke_color,
                'longitud': longitud/sc,
                'punto_inicial': (start.real/sc, -start.imag/sc),
                'punto_final': (end.real/sc, -end.imag/sc)
            })
    
    return resultados


refs = listar_paths(archivo_svg)
refs.sort(key=lambda r : r['id'])

for ref in refs:
    #importa un os en la poscició del segment amb nom "rfxxxx" 
    bpy.ops.object.armature_add(enter_editmode=False, align='WORLD', location=ref['punto_inicial']+(0,), scale=(1,1,1))
    armature=False
    #canvia el nom de l'os pel del segment "osxxxxx"
    bpy.data.armatures[-1].bones[-1].name= 'os'+ref['id'][2:]
    #escala l'os a la mida del segment ref['longitud']
    bpy.ops.transform.resize(value=(ref['longitud'], ref['longitud'], ref['longitud']),
                             orient_type='GLOBAL',
                             orient_matrix=((1, 0, 0), (0, 1, 0),(0, 0, 1)),
                             orient_matrix_type='GLOBAL',
                             mirror=False,
                             use_proportional_edit=False,
                             proportional_edit_falloff='SMOOTH',
                             proportional_size=1, use_proportional_connected=False,
                             use_proportional_projected=False, snap=False,
                             snap_elements={'INCREMENT'}, use_snap_project=False,
                             snap_target='CLOSEST', use_snap_self=True,
                             use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
    #tomba l'os en la direcció i orientació del segment referència
            
    eix,dir=orienta(ref['punto_inicial'],ref['punto_final'])
    print('os'+ref['id'][2:],eix,ref['punto_inicial'][1],ref['punto_final'][1])
    bpy.ops.transform.rotate(value=dir*pi/2,
                             orient_axis=eix,
                             orient_type='GLOBAL',
                             orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
                             orient_matrix_type='GLOBAL',
                             constraint_axis=(False, True, False) if eix == "Y" else (True, False, False),
                             mirror=False, use_proportional_edit=False,
                             proportional_edit_falloff='SMOOTH',
                             proportional_size=1, use_proportional_connected=False,
                             use_proportional_projected=False, snap=False,
                             snap_elements={'INCREMENT'}, use_snap_project=False,
                             snap_target='CLOSEST',
                             use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True,
                             use_snap_selectable=False)

    
#fusiona tots el osos dins  d'una armadura          
for obj in bpy.data.objects:
    # Verifica si el nombre del objeto comienza por mascara
    if obj.name.startswith("Arma"):
        # Selecciona el objeto
        obj.select_set(True)
        bpy.ops.object.join()

                             