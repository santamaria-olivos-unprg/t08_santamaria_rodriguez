#EJERCICIO 1
#Funcion   : Validar si es día de la semana
#Parametros: strDia => Entero que corresponde a día
#Retorna   : bool
def validar_dia_semana(strDia):
    #1.strDia puede ser Lunes,Martea,Miercoles,Jueves,Viernes,Sabado,Domingo
    #2. Si strDia es diferente , devolver Falso
    if(strDia=="Lunes" or strDia=="Martes" or strDia=="Miercoles" or strDia=="Jueves" or strDia=="Viernes" or strDia=="Sabado" or strDia=="Domingo"):
        return True
    else:
        return False
    #fin_if
#fin_validar_dia_semana

#EJERCICIO 2
# Funcion   : Validar si es un nombre
# Parametros: strNombre => Cadena que corresponde a Nombre
# Retorna   : bool
def validar_nombre(strNombre):
    #1. Covertir srtNombre en Mayuscula
    #2. La longitud de la cadena es al menos de 5
    #3.si strNombre es diferente al valor anterior, devolver Falso
    strNombre=strNombre.upper()
    if ( len(strNombre) >= 5):
        return True
    else:
        return False
    #fin_if
#fin_validar_nombre

#EJERCICIO 3
# Funcion   : Validar promedio
# Parametros: intProm => promedio entero
# Retorna   : str
def promedio_final(intProm):
    if ( intProm >= 11 and intProm <= 20):
        return "Aprobado"
    if ( intProm >= 0 and intProm <= 10):
        return "Desaprobado"
    else:
        return " "
#fin_promedio_final

#EJERCICIO 4
# Funcion   : Verifica si floatDeuda es un real
# Parametros: floatPago => Pagó float
# Retorna   : bool
def validar_deuda(floatDeuda):
    if ( isinstance(floatDeuda, float)):
        return True
    else:
        return False
#fin_validar_deuda

#EJERCICIO 5
# Funcion   : Validar tipo de DNI (amarillo o azul)
# Parametros: intEdad => Edad es entero
# Retornar  : bool
def validar_DNI(intEdad):
    if ( intEdad >= 0 and intEdad <= 17):
        return "DNI AMARILLO"
    if ( intEdad >= 18):
        return "DNI AZUL"
    else:
        return " "

# EJERCICIO 6
# Funcion   : Devuelve el mensaje de error de los idiomas
# Parametros: strIdioma =>
# Retorna   : str
def mensaje_error(strIdioma):
    #1.strIdioma puede se ESPAÑOL,INGLES,FRANCES
    #2.SI strIdioma es diferente, devolver "no es un idioma "
    if ( strIdioma == "ESPAÑOL" or strIdioma=="INGLES" or strIdioma=="Frances"):
        return "Es un idioma"

    else:
        return "no es un idioma"
#fin_mensaje_error

#EJERCICIO 7
# Funcion   : Validar letra de abecedario
# Parametros: strLetra => Letra es cadena
# Retorna   : bool
def validar_letra(strLetra):
    if(strLetra=="A" or strLetra=="B" or strLetra=="C" or strLetra=="D" or strLetra=="E" or strLetra=="F" or strLetra=="G" or
    strLetra=="H" or strLetra=="I" or strLetra=="J" or strLetra=="K" or strLetra=="L" or strLetra=="M" or strLetra=="N" or strLetra=="Ñ"
    or strLetra=="O" or strLetra=="P" or strLetra=="Q" or strLetra=="R" or strLetra=="S" or strLetra=="T" or strLetra=="U" or strLetra=="V"
    or strLetra=="W" or strLetra=="X" or strLetra=="Y" or strLetra=="Z" ):
        return True
    else:
        return False
#validar_letra

#EJERCICIO 8
# Función   : Validar si es menor de edad
# Parametros: strEdad => Edad es entero
# Retornar  : str
def validar_edad(strEdad):
    if (strEdad <= 17):
        return "menor de edad"
    else:
        return "mayor de edad"
#fin_validar_edad

#EJERCICIO 9
# Función    : Validar tiempo de pagó
# Paramatros : strTiempo
# Retornar   : bool
def validar_tiempo(strTiempo):
    #1: El tiempo de pagó es de 1mes o 2 meses
    #2: Si es diferente, devolver Falso
    if(strTiempo=="1 MES" or strTiempo=="2 MESES"):
        return True
    else:
        return False
#fin_validar_tiempo

#EJERCICIO 10
# Función    : Cantidad de digitos de una tarjeta de credito, correcta
# Paramatros : strTarjeta
# Retornar: bool
def digitos_correcto(strTarjeta):
    if ( strTarjeta ==14 or strTarjeta==15 or strTarjeta==16):
        return True
    else:
        return False
#fin_digitos_correcto

#EJERCICIO 11

# Funcion   : Retorna JUAN Y MARIA SON FELICES
# Parametros: strNombre => Nombre de la persona
# Retornar  : str

def son_felices(strNomb):
    if (strNomb=="JUAN" or strNomb=="MARIA"):
        return  "SON FELICES"
    else:
        return " "
#fin_son_felices

#EJERCICIO 12
# Funcion   : Verifica si strCurso es un cadena
# Parametros: strCurso => CUrso es cadena
# Retorna   : bool
def validar_curso(strCurso):
    if ( isinstance(strCurso,str)):
        return True
    else:
        return False
#fin_validar_curso

#EJERCICIO 13
# Funcion   : Tipo de calificación para sorteo
# Parametros: strCalif => Calificacion
# Retorna   : float
def tipo_sorteo(strCalif):
    if ( strCalif == "A" or strCalif=="B"):
        return 100.0
    if ( strCalif == "C"):
        return 50.0
    else:
        return 0.0
#fin_tipo_sorteo

#EJERCICIO 14
# Funcion   : Validar año del 2000 al 2020
# Parametros: strAño => Año es una cadena
# Retorna   : bool
def validar_año(strAño):
    if( strAño >=2000 and strAño<=2020):
        return True
    else:
        return False
#fin_validar_año

#EJERCICIO 15
# Funcion   : Validar premios
# Parametros: strPremio => Premio es una cadena
# Retorna   : bool
def validar_premio(strPrem):
    if( strPrem =="TV" or strPrem=="COCINA" ):
        return True
    else:
        return False
#fin:validar_premio
