import random

def generar_laboratorio(nombre):
    lab = []
    for fila in range(5):
        fila_computadoras = [random.choice(["ocupada", "libre"]) for _ in range(4)]
        lab.append(fila_computadoras)
    return lab

def contar_estado(lab):
    ocupadas = sum(comp == "ocupada" for fila in lab for comp in fila)
    libres = sum(comp == "libre" for fila in lab for comp in fila)
    return ocupadas, libres

laboratorio1 = generar_laboratorio("Lab 1")
laboratorio2 = generar_laboratorio("Lab 2")

for i, lab in enumerate([laboratorio1, laboratorio2], 1):
    ocupadas, libres = contar_estado(lab)
    print(f"\nResumen del Laboratorio {i}:")
    print(f"Computadoras ocupadas: {ocupadas}")
    print(f"Computadoras libres: {libres}")