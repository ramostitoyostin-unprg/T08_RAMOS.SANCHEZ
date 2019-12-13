# CONCATENACIÓN

#MANIPULACION DE TEXTOS
#manipulacion de texto nro 1
nombre="jose"
escuela="ingeniería electrónica"
curso="programacion"
facultad="ciencias fisicas y matematicas"
#agrupacion de  cadenas
print(nombre+" estudia " + curso + " en la " + escuela + " en la facultad "+facultad)

#manipulacion de texto nro 2
nombre="juan jose"
apellidos="lozano Gomez"
nacimiento=25
nombre_completo=(nombre+" se apellidad "+apellidos+" nacion el "+str(nacimiento)+" de mayo")

print(nombre_completo)

#manipulacion de texto nro 3
suma=5+16
resultado=("el resultado de 5+11 es :" +str(suma))
print(resultado)

#manipulacion de texto nro 4
nombre="elmer miguel"
estudia="ingenieria electronica"
nota1,nota2,nota3=14,12,13
promedio=(nota1+nota2+nota3)/3

mensaje=nombre+" estudia "+estudia+"y tiene un promedio de "+str(promedio)
print(mensaje)
#si el promedio es mayor que diez mostrar esta aprobado
if (promedio>10):
    mensaje=nombre + " ha aprobado el curso  "
print(mensaje)


#manipulacion de texto nro 5
cadena="jose"
cadena_nueva="."
while (cadena_nueva!=cadena):
    cadena_nueva=input("por favor ingrese una apellido")
    cadena_p=cadena +" " + cadena_nueva
    print(cadena_p)


#manipulacion de texto nro 6
suma="suma"
resta="resta"
division="division"
multiplicacion="multiplicacion"
resultado=("son operaciones arimeticas "+suma+","+resta+","+division+","+multiplicacion)
print(resultado)

#manipulacion de texto nro 7
nombre="miguel"
escuela="estadistica"
curso="poblacion y muestra"
facultad="ciencias fisicas y matematicas"
#agrupacion de  cadenas
print(nombre+" estudia " + curso + " en la " + escuela + " en la facultad "+facultad)

#manipulacion de texto numero nro8
nombre="elmer miguel"
estudia="ingenieria electronica"
nota1,nota2=14,12
promedio=(nota1+nota2)/2
mensaje=nombre+" estudia "+estudia+"y tiene un promedio de "+str(promedio)
print(mensaje)
#si el promedio es menor que diez mostrar esta desaprobado
if (promedio<10):
    mensaje=nombre + " ha desaprobado el curso  "
print(mensaje)

#manipulacion de texto numero nro9

palabras_1="hola como estas?"
palabras_2="sabes te extrañado mucho."
palabras_3="espero que te encuentres bien, muy bien. "

print(palabras_1+" "+palabras_2+" "+palabras_3)


#manipulacion de texto numero nro10
promedio=(5+16+17+10)/4
print("el promedio final de un alumno es de "+str(promedio))

#manipulacion de texto numero nro11
alumno="\"Juan Carlos\""
curso='\'Base de datos\''
nota=18
condicion= "\"Aprobado\""


print("El alumno" + alumno + " llevo el curso de " + curso + "\n" + "y su nota es" + str(nota) +" , su condicion es " + condicion)

#manipulacion de texto numero nro12
#CUIDAR EL MUNDO ES NUETRA OBLIGACION
#concatenar la siguiente frase
#CUIDAR EL MUNDO

#      012345678901234567890123456789012345
texto="CUIDAR EL MUNDO ES NUETRA OBLIGACION"
msg=texto[0:6] +" " +texto[7:9] +" " +texto[10:15]
print(msg)

#manipulacion de texto numero nro13
#CUIDAR EL MUNDO ES NUETRA OBLIGACION
#concatenar la siguiente frase:
#RADIUC LE ODNUM
#      012345678901234567890123456789012345
texto="CUIDAR EL MUNDO ES NUETRA OBLIGACION"
msg=texto[0:6:-1] +" " +texto[7:9:-1] +" " +texto[10:15:-1]
print(msg)

#manipulacion de texto numero nro14
#QUIEN QUIERE VIAJAR CONMIGO
#concatenar la siguiente frase
#QUIEN
#QUIERE
#VIAJAR
#      012345678901234567890123456
texto="QUIEN QUIERE VIAJAR CONMIGO"
msg=texto[0:5] +"\n" +texto[6:12] +"\n" +texto[13:19]
print(msg)

#manipulacion de texto numero nro15
cad1="hola"
cad2="mundo"
print(cad1+" "+cad2)










