def interes_compuesto_for (monto_monto,tiempo,opcionProducto): 
  for i in range(tiempo):
     ValorPorIntereses = monto_monto * (interes/100)
     monto_monto = monto_monto + ValorPorIntereses
  return monto_monto

def interes_compuesto_formula (monto_monto,tiempo,opcionProducto): 
  monto_montoTotalaPagar = monto_monto*((1+(interes/100))**tiempo)
  print("---EL INTERES COMPUESTO CON FORMULA ES: {0:.2f}".format(monto_montoTotalaPagar - monto_monto)," y el valor total a pagar es: ""{0:.2f}".format(monto_montoTotalaPagar))

interes = 0
monto_monto = float(input("Ingrese el monto_monto a prestar: "))
tiempo = int(input("Digite el tiempo del crédito: "))
opcionProducto = int(input("""Seleccionar el producto financiero a validar:
1. Crédito Hipotecario
2. Tarjeta Crédito
3. Crédito Libre Inversión
4. Compra de Cartera"""))

if opcionProducto == 1:
    interes = 0.4
elif opcionProducto == 2:
    interes = 2.16
elif opcionProducto == 3:
     interes = 1.5  
elif opcionProducto == 4:
    interes = 0.8
else:
    print("---Opción Invalida...")

monto_monto_inicial = monto_monto

monto_montototal1=interes_compuesto_for (monto_monto,tiempo,opcionProducto)
print("---El Interes compuesto con For es: {0:.2f}".format(monto_montototal1 - monto_monto_inicial), "y el el valor total a pagar es: {0:.2f}".format(monto_montototal1))

interes_compuesto_formula (monto_monto,tiempo,opcionProducto)