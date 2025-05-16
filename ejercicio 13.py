dias = 3
stands_por_dia = 4
productos_por_stand = 3
total_general = 0

for dia in range(1, dias + 1):
    print(f"\nDía {dia}")
    total_dia = 0
    for stand in range(1, stands_por_dia + 1):
        print(f" Stand {stand}")
        total_stand = 0
        for producto in range(1, productos_por_stand + 1):
            venta = float(input(f"  Ingrese monto de venta del producto {producto}: "))
            total_stand += venta
        print(f"  Total vendido por el stand {stand}: C${total_stand:.2f}")
        total_dia += total_stand
    print(f"Total vendido en el día {dia}: C${total_dia:.2f}")
    total_general += total_dia

print(f"\nTotal general de la feria: C${total_general:.2f}")