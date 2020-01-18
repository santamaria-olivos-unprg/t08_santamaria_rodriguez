import libreria

assert (libreria.validar_dia_semana("Lunes")==True)
assert (libreria.validar_dia_semana("Martes")==True)
assert (libreria.validar_dia_semana("Hola")==False)
assert (libreria.validar_dia_semana("Adios")==False)
assert (libreria.validar_dia_semana("Viernes")==True)
print("validar_dia_semana OK")

assert (libreria.validar_nombre("Max") == False)
assert (libreria.validar_nombre("Edwar") == True)
assert (libreria.validar_nombre("Mirella") == True)
assert (libreria.validar_nombre("Maria") == True)
assert (libreria.validar_nombre("Smic")==False)
print("validar_nombre OK")


assert (libreria.promedio_final(20)=="Aprobado")
assert (libreria.promedio_final(15)=="Aprobado")
assert (libreria.promedio_final(10)=="Desaprobado")
assert (libreria.promedio_final(11)=="Aprobado")
print("promedio_final OK ")

assert (libreria.validar_deuda(5)==False)
assert (libreria.validar_deuda(10.6)==True)
assert (libreria.validar_deuda(50.5)==True)
assert (libreria.validar_deuda(100.9)==True)
assert (libreria.validar_deuda(8)==False)
print("validar_pago OK")

assert (libreria.validar_DNI(24)=="DNI AZUL")
assert (libreria.validar_DNI(12)=="DNI AMARILLO")
assert (libreria.validar_DNI(25)=="DNI AZUL")
assert (libreria.validar_DNI(14)=="DNI AMARILLO")
assert (libreria.validar_DNI(76)=="DNI AZUL")
print("validar_DNI OK")

assert (libreria.mensaje_error("INGLES")=="Es un idioma")
assert (libreria.mensaje_error("ESPAÑOL")=="Es un idioma")
assert (libreria.mensaje_error("Frances")=="Es un idioma")
assert (libreria.mensaje_error("HOLA")=="no es un idioma")
assert (libreria.mensaje_error("I")=="no es un idioma")
print("mensaje_error")

assert (libreria.validar_letra("A")==True)
assert (libreria.validar_letra("B")==True)
assert (libreria.validar_letra("5")==False)
assert (libreria.validar_letra("7")==False)
assert (libreria.validar_letra("Z")==True)
print("validar_letra OK")

assert (libreria.validar_edad(16)=="menor de edad")
assert (libreria.validar_edad(64)=="mayor de edad")
assert (libreria.validar_edad(12)=="menor de edad")
assert (libreria.validar_edad(23)=="mayor de edad")
assert (libreria.validar_edad(10)=="menor de edad")
print("validar_edad OK")

assert (libreria.validar_tiempo("1 MES")==True)
assert (libreria.validar_tiempo("2 MESES")==True)
assert (libreria.validar_tiempo("5 MES")==False)
assert (libreria.validar_tiempo("6 MES")==False)
assert (libreria.validar_tiempo("7 MES")==False)
print("validar_tiempo OK")

assert (libreria.digitos_correcto(15)==True)
assert (libreria.digitos_correcto(16)==True)
assert (libreria.digitos_correcto(13)==False)
assert (libreria.digitos_correcto(12)==False)
assert (libreria.digitos_correcto(14)==True)
print("Digitos correcto OK")

assert (libreria.son_felices("MARIA")=="SON FELICES")
assert (libreria.son_felices("JUAN")=="SON FELICES")
assert (libreria.son_felices("ANA")==" ")
assert (libreria.son_felices("MIGUEL")==" ")
assert (libreria.son_felices("ELSA")==" ")
print("son_felices OK")

assert (libreria.validar_curso("MATEMATICA")==True)
assert (libreria.validar_curso("LOGICA")==True)
assert (libreria.validar_curso(123)==False)
assert (libreria.validar_curso("LEP2")==True)
assert (libreria.validar_curso(123456)==False)
print("validar_curso OK")

assert (libreria.tipo_sorteo("A")==100.0)
assert (libreria.tipo_sorteo("B")==100.0)
assert (libreria.tipo_sorteo("C")==50.0)
assert (libreria.tipo_sorteo("X")==0.0)
assert (libreria.tipo_sorteo("Z")==0.0)
print("tipo_sorteo OK")

assert (libreria.validar_año(2019)==True)
assert (libreria.validar_año(2018)==True)
assert (libreria.validar_año(2017)==True)
assert (libreria.validar_año(1998)==False)
assert (libreria.validar_año(1987)==False)
print("validar_año OK")

assert (libreria.validar_premio("TV")==True)
assert (libreria.validar_premio("COCINA")==True)
assert (libreria.validar_premio("LAVADORA")==False)
assert (libreria.validar_premio("LICUADORA")==False)
assert (libreria.validar_premio("PLANCHA")==False)
print("validar_premio OK")



