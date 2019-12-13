#OPERACION COMPARACION DE CADENAS

#manipulador de texto nro 1#
cad1="hola"
cad2="5"
print(cad1==cad2)

#manipulador de texto nro 2#
cad3="mundo"
cad4="planeta"
print(cad3!=cad4)

#manipulador de texto nro 3#
cad5="15"
cad6="12"
print(cad5>cad6)

#manipulador de texto nro 4#
msg="1000"
msg1="1000"
print(msg>=msg1)

#manipulador de texto nro5#

pais= input("ingrese su pais de origen:")
descuento=0.0
mensaje=""
msg2= "Procedera el descuento"
#Si el pais de origen no es PERU, no hay descuento
#Caso contrario, aplicar el 10 %  de descuento

if(pais != "PERU"):
    mensaje= "No" + msg2 + "por no ser del PERU"

#fin_if
#en caso contrario proceder el descuento
else:
    mensaje = "Si " + msg2 + " por ser del PERU"
print(mensaje)

#manipulador de texto nro6#
numero="5"
numero1="8"

if (numero==numero1):
    print("las cadenas no son iguales")

else :
    print("las cadenas son diferentes")

#manipulador de texto nro7#

cadena="planeta tierra"
cadena1="planeta tierra"
mesje="mi hogar, tu hogar ; nuestro hogar"

if (cadena==cadena1):
    print(mesje)

#manipulador de texto nro8#

print("juan"=="julio")  #  -> False

#manipulador de texto nro9#
nota1="15"
nota2="17"
if (nota1!=nota2):
    print("puede que este desaprobado o aprobado")

#manipulador de texto nro10#
universidad= input("ingrese su universidad de:")
descuento=0.0
mensaje1=""
msje= "Procedera el descuento"
#Si la universidad no es UNMSM, no hay descuento
#Caso contrario, aplicar el 10 %  de descuento

if(universidad != "UNMSM","UNPRG"):
    mensaje1= "No" + msje + "por no ser de la UNMSM"

#fin_if
#en caso contrario proceder el descuento
else:
    mensaje1 = "Si " + msje + " por ser de la UNMSM"
print(mensaje1)

#manipulador de texto nro11#
nota_1=18
nota_2=20
promedio_desaprobatorio=10
promedio=(nota_1+nota_2)/2

if (promedio_desaprobatorio!=promedio):
    print("el alumno esta aprobado")

#fin_if

#manipulador de texto nro12#
apellido1="SANDOVAL"
apellido2="FLORES"

print(apellido1>apellido2)

#manipulador de texto nro13#
cad5="15"
cad6="12"
print(cad5!=cad6)

#manipulador de texto nro14#
cad3="mundo"
cad4="planeta"
print(cad3>=cad4)

#manipulador de texto nro15#
frase="hola linda"
frase1="eres hermosa"

if (frase!=frase1):
    print("seguro eres de peru")
