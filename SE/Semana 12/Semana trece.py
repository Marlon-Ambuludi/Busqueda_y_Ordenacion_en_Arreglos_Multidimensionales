# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
from operator import truediv

temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 72},
            {"day": "Martes", "temp": 57},
            {"day": "Miércoles", "temp": 62},
            {"day": "Jueves", "temp": 69},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 80},
            {"day": "Domingo", "temp": 92}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 73},
            {"day": "Miércoles", "temp": 93},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 79},
            {"day": "Domingo", "temp": 63}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 87},
            {"day": "Martes", "temp": 81},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 78},
            {"day": "Sábado", "temp": 91},
            {"day": "Domingo", "temp": 95}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 88},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 69},
            {"day": "Viernes", "temp": 84},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 81}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 62},
            {"day": "Martes", "temp": 74},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 63},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 79}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 63},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 60},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 75},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 80},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 66},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 69},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 90}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 80},
            {"day": "Martes", "temp": 92},
            {"day": "Miércoles", "temp": 84},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 82}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 89},
            {"day": "Martes", "temp": 71},
            {"day": "Miércoles", "temp": 93},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 91}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 91},
            {"day": "Martes", "temp": 83},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 88},
            {"day": "Martes", "temp": 70},
            {"day": "Miércoles", "temp": 92},
            {"day": "Jueves", "temp": 89},
            {"day": "Viernes", "temp": 96},
            {"day": "Sábado", "temp": 83},
            {"day": "Domingo", "temp": 80}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print(suma)

while True:
    print("Selecciona una ciudad:")
    print("1. Ciudad 1")
    print("2. Ciudad 2")
    print("3. Ciudad 3")
    print("4. Salir")

    opción=input("Ingrese la apción deseada:")
    if opción == "1":
        ciudad=temperaturas[0]
        print(ciudad)

    elif opción == "2":
        ciudad=temperaturas[1]
        print(ciudad)
    elif opción == "3":
        ciudad=temperaturas[2]
        print(ciudad)
    elif opción == "4":
        print("Fin")
    else:
        print("No se encuentra su opción:")
    continue

    opción=input("Ingrese la opción:")
    if opción == "1":
        calcular_promedio(temperaturas[0])
        print
