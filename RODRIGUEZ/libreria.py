#Ejercicio 1

def valida_Dni(strDNI):
    #1.strDNI es una cadena de 8 caracteres
    #2.la longitud debe ser de 8
    if(len(strDNI))!= 8:
        return False
    else:
        return True
#fin_valida_Dni

#Ejercicio 2

def valida_Vocal(strVocal):
    #1.strVocal es un caracter
    #2.Se validara si es vocal
    if(strVocal=='a' or strVocal== 'e' or strVocal=='i' or strVocal=='o' or strVocal=='u' ):
        return True
    else:
        return False
#fin_valida_Vocal

#Ejercicio 3

def valida_NroPar(Par):
    #1.strPar es un numero
    #2.Se validara solo si es un numero par

    if(Par%2==0):
        return True
    else:
        return False
#fin_valida_NroPar

#Ejercicio 4

def es_Moneda_valido(strMoneda):
    #1. Convertir strMoneda es Mayuscula
    #2. Convertir si moneda es igual a EUROS SOLES DOLARES
       #retornar True
       #caso contrario False

    strMoneda= strMoneda.upper()
    if (strMoneda == "EUROS" or strMoneda=="SOLES" or strMoneda=="DOLARES"):
        return True
    else:
        return False
#fin_es_Moneda_valido

#Ejercicio 5

def es_EstadoCivil_valido(strEstado):
    #1. Convertir strEstado es Mayuscula
    #2. Convertir si Estado es igual a SOLTERO CASADO VIUDO DIVORCIADO
       #retornar True
       #caso contrario False

    strEstado= strEstado.upper()
    if (strEstado == "DIVORCIADO" or strEstado=="VIUDO" or strEstado=="CASADO" or strEstado=="SOLTERO"):
        return True
    else:
        return False
#fin_es_EstadoCivil_valido


#Ejercicio 6

def validamayorEdad(strEdad):
    #1. Verificar strEdad
    #2. retornar Verdadero si es mayo de edad, falso si es lo contrario

    if(strEdad >= 18):
        return True
    else:
        return False
#fin_validamayorEdad

#Ejercicio 7

def validaNroTelefono(strTelefono):
    #1. Verificar strTelefono
    #2. retornar Verdadero si la longitud de la cadena es de 9 caracteres, falso si es lo contrario

    if(len(strTelefono)==9 ):
        return True
    else:
        return False
#fin_validaNroTelefono

#Ejercicio 8

def validarAñoNacimiento(Anio):
    #1. validar Año nacimiento
    #2. retornar Verdadero si el año conrresponde al limite de la funcion, falso si es lo contrario

    if(Anio>=1940 and Anio<=2020):
        return True
    else:
        return False
#fin_validarAñoNacimiento

#Ejercicio 9

def ValidarNumeroImpar(Impar):
    #1. validar si numero es impar
    #2. retornar verdadero si el numero es impar, falso si es lo contrario

    if(Impar%2!=0):
        return True
    else:
        return False
#fin_ValidarNumeroImpar

#Ejercicio 10

def validarNroCuenta(strCuenta):
    #1.Validar numero de cuenta
    #2.Retornar verdadero si el numero de cuenta tiene la misma longitud, falso si es lo contrario

    if(len(strCuenta)==18):
        return True
    else:
        return False
#fin_validarNroCuenta

#Ejercicio 11

def validarRUC(strRUC):
    #1.Validar RUC
    #2.Retornar verdadero si el RUC tiene la misma longitud, falso si es lo contrario

    if(len(strRUC)==11):
        return True
    else:
        return False
#fin_validarRUC

#Ejercicio 12

def validarID(strID):
    #1.Validar ID
    #2.Retornar verdadero si el ID tiene la misma longitud, falso si es lo contrario

    if(len(strID)==7):
        return True
    else:
        return False
#fin_validarID

#Ejercicio 13

def validarMenorEdad(Edad):
    #1.validar Edad
    #2.retornar verdadero si la edad es menor a 18 , falso si es lo contrario

    if(Edad<18):
        return True
    else:
        return False
#fin_validarMenorEdad

#Ejercicio 14

def validarMes(strMes):
    #1.validar Mes
    #2. retornar verdadero si el mes coincide , falso si es lo contrario

    if(strMes=="ENERO" or strMes=="FEBRERO" or strMes=="MARZO" or strMes=="ABRIL" or strMes=="MAYO" or strMes=="JUNIO"
        or strMes=="JULIO" or strMes=="AGOSTO" or strMes=="SETIEMBRE" or strMes=="OCTUBRE"
        or strMes=="NOVIEMBRE" or strMes=="DICIEMBRE"):
        return True
    else:
        return False
#fin_validarMes

#Ejercicio 15

def valida_Letra(strLetra):
    #1.strLetra es un caracter
    #2.Se validara si es letra
    if(strLetra=='R' or strLetra== 'F' or strLetra=='G' or strLetra=='A'):
        return True
    else:
        return False
#fin_valida_Letra
