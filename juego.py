import random
Numero=random.randint(1,4)
i=0
while i<=3 :
    NumeroUsuario=int(input("Ingrese Numero que estoy pensando: "))
    if NumeroUsuario==Numero :
       print("Adivinastes !!")
       break
    else:
        print("Intenta Nuevamente")
    i+=1
print("Perdistes!!")