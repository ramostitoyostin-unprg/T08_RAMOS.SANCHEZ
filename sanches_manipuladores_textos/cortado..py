# CORTADO DE CADENAS 1:
#     0         1         2         3         4         5         6
#     0123456789012345678901234567890123456789012345678901234567890123456
msg1="LA UNIVERSIDAD NACIONAL PEDRO RUIZ GALLO SE ENCUENTRA EN LAMBAYEQUE"

# mostrar UNIVERSIDAD
print(msg1[3:14])

# mostrar OLLA
print(msg1[39:35:-1])

# mostrar PEDRO
print(msg1[24:29])

# CORTADO DE CADENAS 2:
#     0         1         2         3         4
#     012345678901234567890123456789012345678901234567
msg2="SI NO QUIERES SER DERROTADO, SOLO SIGUE ADELANTE"

# Mostrar la cadena: DERROTADO No
subcadena=msg2[18:27] + " " + msg2[3:5]
print(subcadena)

# CORTADO DE CADENAS 3:
#     0         1
#     012345678901
msg3="¿DONDE VIVES?"

# Mostrar la cadena: EN DONDE VOI
subcadena=msg3[5] + msg3[3] + " " + msg3[1:6] + " " + msg3[7] + msg3[2] + msg3[8]
print(subcadena)

# CORTADO DE CADENAS 4:
#     0         1         2         3         4         5         6
#     012345678901234567890123456789012345678901234567890123456789012
msg4="El peor fracaso es rendirse cuando ya estás a un paso del éxito"

# mostrar la cadena: fracaso ay oti
subcadena=msg4[8:15] + " " + msg4[36:34:-1] + " " + msg4[62:59:-1]
print(subcadena)

# CORTADO DE CADENAS 5:
#     0         1
#     01234567890
msg5="BUENOS DIAS"

# Mostrar la cadena: SAID BUENO
subcadena=msg5[10:6:-1] + " " + msg5[0:5]
print(subcadena)

# CORTADO DE CADENAS 6:
#     0         1
#     0123456789012
msg6="BUENAS TARDES"

#  Mostrar la cadena: TARDAN
subcadena=msg6[7:11] + msg6[4:2:-1]
print(subcadena)

# CORTADO DE CADENAS 7:
#     0         1
#     0123456789012
msg7="BUENAS NOCHES"

# Mostrar la cadena: CHE BUENO
subcadena=msg7[9:12] + " " + msg7[0:4] + msg7[8]
print(subcadena)

# CORTADO DE CADENA 8:
#     0         1         2
#     0123456789012345678901
msg8="INGENIERIA ELECTRONICA"

# Mostrar la cadena: INGENIO ELECTRO
subcadena=msg8[0:6]+ msg8[17] + " " + msg8[11:18]
print(subcadena)

# CORTADO DE CADENA 9:
#     0         1
#     012345678901234
msg9="MEDICINA HUMANA"

# Mostrar la cadena: HUMAN ICNA
subcadena=msg9[9:14] + " " + msg9[5:3:-1] + msg9[13:15]
print(subcadena)

# OORTADO DE CADENA 10:
#      0         1         2
#      01234567890123456789012
msg10="LOS NIÑOS SON EL FUTURO"

# Mostrar la cadena: EL FUTURO ES OI
subcadena=msg10[14:] + " " + msg10[14] + msg10[2] + " " + msg10[7] + msg10[5]
print(subcadena)

# CORTADO DE CADENA 11:
#      0         1         2
#      0123456789012345678901
msg11="INGENIERIA DE SISTEMAS"

# Mostrar la cadena: SISTEM DE AIRE
subcadena=msg11[14:20] + " " + msg11[11:13] + " " + msg11[9:5:-1]
print(subcadena)

# CORTADO DE CADENA 12:
#      0         1         2         3         4
#      01234567890123456789012345678901234567890123456789
msg12="LAS MATEMATICAS ES LA CIENCIA MAS BONITA DEL MUNDO"

# Mostrar la cadena: EL MUNDO AL MAS ALLA
subcadena=msg12[42:] + " " + msg12[20:18:-1] + " " + msg12[30:33] + " " + msg12[1::-1] + msg12[19:21]
print(subcadena)

# CORTADO DE CADENA 13:
#      0         1
#      012345678901234567890
msg13="PROGRAMACION ES BACAN"

# Mostrar la cadena: PROGRAMACION
subcadena=msg13[0:12]
print(subcadena)

# CORTADO DE CADENA 14:
#      0         1         2
#      01234567890123456789012345678
msg14="NIKOLA TEZLA UN GRAN INVENTOR"

# Mostrar la cadena: TEZLA INVENTOR
subcadena=msg14[7:12] + " " + msg14[21:]
print(subcadena)

# CORTADO DE CADENA 15:
#      0         1         2         3         4
#      01234567890123456789012345678901234567890123
msg15="EL GUEPARDO ES EL ANIMAL MAS VELOZ DEL MUNDO"

# Mostrar la cadena: GUAPO ZOI LLO
subcadena=msg15[3:5] + msg15[18] + msg15[6] + msg15[10] + " " + msg15[33:31:-1] + msg15[20] + " " + msg15[16] + msg15[23] + msg15[43]
print(subcadena)
