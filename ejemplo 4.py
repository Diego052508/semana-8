carreras = ["Sistemas", "Marketing", "Derecho"]
anios = ["Primer Año", "Segundo Año", "Tercer Año"]
secciones = ["Sección A", "Sección B"]


totales_por_carrera = [0, 0, 0] 


for i in range(len(carreras)):
    print("Carrera:", carreras[i])
    

    for j in range(len(anios)):
        print("  ", anios[j])
        

        for k in range(len(secciones)):
            print("    ", secciones[k])
            
            print("--------------------------------------------------------------------")
            print("")
        
            participantes = int(input("      Ingrese el número de estudiantes que participaron: "))
   
         
            totales_por_carrera[i] = totales_por_carrera[i] + participantes


print("\n-------------Resumen de Participaciones----------------")
total_general = 0

for i in range(len(carreras)):
    print("Total de participantes en", carreras[i] + ":", totales_por_carrera[i])
    total_general = total_general + totales_por_carrera[i]


print("Total general de participantes:", total_general)