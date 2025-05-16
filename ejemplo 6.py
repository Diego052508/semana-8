total_mensual = 0

for domingo in range(1, 5):
    print("\nDomingo", domingo)
    
    clientes = int(input("Ingrese la cantidad de clientes para este domingo: "))
    
    total_domingo = 0
    
    for cliente in range(1, clientes + 1):
        print("  Cliente", cliente)
        cantidad = int(input("    ¿Cuántos nacatamales compró?: "))
        
   
        total_domingo = total_domingo + cantidad
    
    print("Total de nacatamales vendidos el Domingo", domingo, ":", total_domingo)
    

    total_mensual = total_mensual + total_domingo

print("\nResumen del mes:")
print("Total de nacatamales vendidos en los 4 domingos:", total_mensual)