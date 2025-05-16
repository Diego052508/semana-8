secciones = {"A": 0, "B": 0, "C": 0}
dias = 5
estudiantes_por_dia = 6

for seccion in secciones:
    print(f"\nRegistrando asistencia para la sección {seccion}")
    for dia in range(1, dias + 1):
        print(f"Día {dia}:")
        for estudiante in range(1, estudiantes_por_dia + 1):
            asistio = input(f"¿Asistió el estudiante {estudiante}? (s/n): ").lower()
            if asistio == "s":
                secciones[seccion] += 1
            elif asistio != "n":
                print("Entrada inválida, por favor escriba 's' o 'n'.")
            

total_general = sum(secciones.values())

print("\nResumen de asistencia por sección:")
for seccion, total in secciones.items():
    print(f"Sección {seccion}: {total} asistencias")

print(f"Total general de asistencias: {total_general}")