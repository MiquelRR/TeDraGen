import json
caixa={
    "nom":"caixa-plana-tapa",
    "variables":{
        "v[0]":{"eti":"ample","val":500},
        "v[1]":{"eti":"llarg","val":500},    
        "v[2]":{"eti":"alt","val":20},
        "v[3]":{"eti":"solapa", "val":70},
        "v[4]":{"eti":"cantonera","val":70},
        "v[5]":{"eti":"gruix cartro","val":2}
    },

    "grupsSVG":{
        "hendit":
                {
                "color":"red",
                "path" :   ['m v[0]-v[5] -3*v[5]',
                            'v -v[2]+3*v[5]',
                            'm 0 -2*v[5]',
                            'h -v[0]+v[5]',
                            'm -2*v[5] v[2]+2*v[5]',
                            'h -v[2]+4*v[5]',
                            'm -2*v[5] 0',
                            'v v[1]-2*v[5]',
                            'm 2*v[5] 0',
                            'h v[2]-4*v[5]',
                            'm 2*v[5] v[2]+2*v[5]',
                            'h v[0]-v[5]',
                            'm 0 -2*v[5]',
                            'v -v[2]+3*v[5]',#
                            'm v[2]+3*v[5] -2*v[5]',
                            'v -v[1]',
                            'm -v[2]-2*v[5] 0',
                            'h -v[0]',
                            'v v[1]',
                            'h v[0]',
                            'z'
                            #'v -v[1]'
                        ]
        },
        "tall":{
               "color":"blue",
               "path": ['m v[0]-v[5] -v[5]',
                        'v -v[5]',
                        'h v[4]',
                        'v -v[2]+v[5]',
                        'h -v[4]',
                        'v -v[3]-v[5]',
                        'h -v[0]+v[5]',
                        'v v[3]+2*v[5]+v[2]',
                        'h -v[5]',
                        'v -v[4]',
                        'h -v[2]+2*v[5]',
                        'v v[4]',
                        'h -v[3]-v[5]',
                        'v v[1]-2*v[5]', #
                        'h v[3]+v[5]',
                        'v v[4]',
                        'h v[2]-2*v[5]',
                        'v -v[4]',#
                        'h v[5]',
                        'v v[2]+2*v[5]+v[3]',
                        'h v[0]-v[5]',
                        'v -v[3]-v[5]',
                        'h v[4]',
                        'v -v[2]+v[5]',
                        'h -v[4]',
                        'v -v[5]',
                        'h 3*v[5]+v[2]+v[0]',
                        'v -v[1]',
                        'z'
                        #'h -3*v[5]-v[2]-v[0]'
                        ]


        }
        }
}
with open('c:\caixes\caixa_plana.json', 'w') as f:
    json.dump(caixa, f, indent=4, sort_keys=True)