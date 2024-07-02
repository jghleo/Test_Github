import os
import time
#Especificar variables
cpi = 0
cot = 0
cpv = 0
can = 0
ccn = 0
pt = 0
tps = 0
tpd = 0
pi = 4500
ot = 5000
pv = 5200
an = 4800
wh = 1
ds = 0
total = 0
l = "*"
l *= 30
while wh == 1:
    try:
        os.system("cls")
        print("Bienvenido usario ")
        print("Selecione el pedido \n1. Pikachu Roll $4500 \n2. Otaku Roll $5000 \n3. Pulpo Venenoso Roll $5200\n4. Anguila Eléctrica Roll $4800 \n5. Salir")
        op =int(input("Ingrese el pedido: "))
        if op >=1 and op <=5:  
            if op == 1:
                os.system("cls")
                print("Selecionaste el Pikachu Roll")
                cn = int(input("Ingrese la cantidad: "))
                total = (pi * cn)
                os.system("cls")
                cpi += cn
                ccn += cn
                tps += total
                wh = int(input("Deseas relizar otro pedido (1) si no presione (2): "))
            elif op == 2:
                os.system("cls")
                print("Selecionaste el Otaku Roll")
                cn = int(input("Ingrese la cantidad: "))
                total = (ot * cn)
                os.system("cls")
                cot += cn
                ccn += cn
                tps += total
                wh = int(input("Deseas relizar otro pedido (1), si no presione (2): "))
            elif op == 3:
                os.system("cls")
                print("Selecionaste el Pulpo Venenoso Roll")
                cn = int(input("Ingrese la cantidad: "))
                total = (pv * cn)
                os.system("cls")
                cpv += cn
                ccn += cn
                tps += total
                wh = int(input("Deseas relizar otro pedido (1), si no presione (2): "))
            elif op == 4:
                print("Selecionaste el Anguila Eléctrica Roll")
                cn = int(input("Ingrese la cantidad: "))
                total = (an * cn)
                os.system("cls")
                can += cn
                ccn += cn
                tps += total
                wh = int(input("Deseas relizar otro pedido (1), si no presione (2): "))
            elif op == 5:
                wh = 0
        else:
            print("Codigo erroneo, ingrese nuevamente")
            wh = int(input("Deseas relizar otro pedido (1), si no presione (2): "))
    except ValueError:
        print("Error, ingrese nuevamente los digitos")
os.system("cls")
ds = (input("Ingrese el descuento: "))
if ds == "soyotaku":
    print("Aplicando el descuento de 10%")
    ds = (tps * 0.10)
    tpd = (tps - ds)
else:
    print("No se aplica ningun descuento")
    tpd = tps
    ds = 0
os.system("cls")
time.sleep(1)
print(f"{l} \nTOTAL PRODUCTOS:{ccn} \n{l} \nPikachu Roll :{cpi} \nOtaku Roll:{cot} \nPulpo Venenoso Roll:{cpv}\nAnguila Eléctrica Roll:{can} \n{l}  \nSubtotal por pagar: ${tps} \nDescuento por código: ${ds} \nTotal:{tpd}")            
print("Gracias por utlizar el programa")