#CORTADO DE CADENAS

#manipulacion de texto numero nro1
#    01234567890123456789
msg="EL MUNDO ES UN LIBRO"
#realizar el cortado de cadenas y luego concatenizarlas ,MOSTRAR:EL MUNDO
msg2=(msg[0:2])  #mostrara la subcadena "EL"
msg1=(msg[3:8])  #mostrara la subcadena "MUNDO"
print(msg2+" "+msg1)

#manipulacion de texto numero nro2
#    012345678901234567890123456789012345
msg="ser TALENTOSO te abre muchas puertas"
#realizar el cortado de cadenas y  mostrar el mensaje:
#TALENTOSO
#abre
#puertas
print(msg[4:13])
print(msg[17:21])
print(msg[29:36])


#manipulacion de texto numero nro3
#     012345678901234567890123456789012345
msg="ser TALENTOSO te abre muchas puertas"
#realizar el cortado de cadenas y  mostrar el mensaje:
#OSOTNELAT
#erba
#satreup
print(msg[12:3:-1])
print(msg[20:16:-1])
print(msg[35:28:-1])

#manipulacion de texto numero nro4
#    0123456789012345678901234567890123456789012345
msg="VOY A SALIR ADELANTE POR QUE DIOS ESTA CONMIGO"
#realizar el cortado de cadenas y concatenizarlas para mostrar el siguiente mensaje:
#DIOS VOY A SALIR ADELANTE
print(msg[29:33]+" "+msg[0:20])

#manipulacion de texto numero nro5
msg="EL LOGRO DE UN AMIGO SE FESTEJA COMO SI FUERA EL TUYO"
#invertir la cadena
print(msg[::-1])
#                10        20        30        40        50
#      01234567890123456789012345678901234567890123456789012
msg_i="OYUT LE AREUF IS OMOC AJETSEF ES OGIMA NU ED ORGOL LE"
#realizar cortados de cadenas y concatenizarlas y mostrar el sgte mensaje de la cadena invertida:
#AMIGO EL LOGRO ES TUYO
print(msg_i[37:32:-1]+" "+msg_i[49:44:-1]+" "+msg_i[30:32:]+" "+msg_i[3:0:-1])


#manipulacion de texto numero nro6
msg="EL LOGRO DE UN AMIGO SE FESTEJA COMO SI FUERA EL TUYO"
#invertir la cadena
print(msg[::-1])
#                10        20        30        40        50
#      012345678901234567890123456789012345678901234567890123
msg_i="OYUT LE AREUF IS OMOC AJETSEF ES OGIMA NU ED ORGOL LE"
#realizar cortados de cadenas y concatenizarlas y mostrar el sgte mensaje de la cadena invertida:
#AMIGO
# EL
# LOGRO
# ES
# TUYO
print(msg_i[37:32:-1]+"\n"+msg_i[49:44:-1]+"\n"+msg_i[30:32:]+"\n"+msg_i[3:0:-1])


#manipulacion de texto numero nro7
msg="EL LOGRO DE UN AMIGO SE FESTEJA COMO SI FUERA EL TUYO"
#invertir la cadena
print(msg[::-1])

#manipulacion de texto numero nro8
#              10        20        30        40
#    012345678901234567890123456789012345678901234567890
msg5="UN BRINDIS POR TI.POR MI Y POR TODO LO MARAVILLOSO"
#realizar el cortado de cadenas y luego concatenizarlas
print(msg5[39:51])  #mostrara la subcadena "MARAVILLOSO"
print(msg5[3:11])  #mostrara la subcadena "BRINDIS"
print(msg5[11:18]) #mostrara la subcadena "POR TI"

#manipulacion de texto numero nro9
#              10        20        30        40
#     01234567890123456789012345678901234567890123456789
msg5="UN BRINDIS POR TI.POR MI Y POR TODO LO MARAVILLOSO"
#realizar el cortado de cadenas y luego concatenizarlas
print(msg5[49:38:-1])  #mostrara la subcadena "OSOLLIVARAM"
print(msg5[9:2:-1])  #mostrara la subcadena "SIDNIRB"
print(msg5[16:10:-1]) #mostrara la subcadena "IT ROP"

#manipulacion de texto numero nro10

#    012345678901234567890123456789012345
msg="ser TALENTOSO te abre muchas puertas"
#realizar el cortado de cadenas y  mostrar el mensaje:
#TALENTOSO abre puertas
print(msg[4:13]+" "+msg[17:21]+" "+msg[29:36])

#manipulacion de texto numero nro11

msg9="CURSO DE PROGRAMACIÓN -> INGENIERÍA ELECTRÓNICA"
#MOSTRAR CADENA entera
print(msg9[:])

#manipulacion de texto numero nro12
#      012345678901234567890123456789012345
texto="CUIDAR EL MUNDO ES NUETRA OBLIGACION"
#realizar el cortado de cadenas y concatenizar
msg5=texto[0:6] +" " +texto[7:9] +" " +texto[10:15]
print(msg5)

#manipulacion de texto numero nro13
#    0123456789012345678901
msg="ERES FELIZ,TÚ REALMENTE?"

# Mostrar la cadena: ERES REALMENTE?
subcadena=msg[0:4] + " " + msg[14:]
print(subcadena)

#manipulacion de texto numero nro14
#    01234567890123456789012345678901234567
msg="UNIVERSIDAD NACIONAL PEDRO RUIZ GALLO"
#cortar:
#Universidad
#pedro
#ruiz
#nacional
print(msg[0:11])
print(msg[21:27])
print(msg[27:32])
print(msg[12:20])

#manipulacion de texto numero nro15
#    012345678901234567890
msg="hola como has estado?"

print(msg[0:4])   #subcadena -> hola
print(msg[14:21])  #subcadena-> estado?




