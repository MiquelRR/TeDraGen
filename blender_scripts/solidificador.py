"""
solidifica tots els ojectes on la ID escomença per 'rect'
"""

grosor=0.0015
mascara:str='rect'
import bpy


# Recorre todos los objetos en la escena
for obj in bpy.data.objects:
    # Verifica si el nombre del objeto comienza por mascara
    if obj.name.startswith(mascara):
        # Selecciona el objeto
        obj.select_set(True)
        
        # Convierte el objeto en una malla
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.convert(target='MESH')
        
        # Agrega el modificador Solidify con un grosor 
        solidify_modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
        solidify_modifier.thickness = grosor
        
        # Aplica el modificador
        bpy.ops.object.modifier_apply(modifier=solidify_modifier.name)
        
        # Deselecciona el objeto
        obj.select_set(False)