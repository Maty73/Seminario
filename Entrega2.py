nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
           85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

listaNombres = nombres.replace('\n', '').replace(' ', '').replace('\'', '').split(',')

def relacionarDatos (nombres, notas_1, notas_2):
    estudiantes = {}
    for i in range(len(listaNombres)):
        estudiantes[listaNombres[i]] = (notas_1[i], notas_2[i])
    return estudiantes

def calcularPromedios(estudiantes):
    promedios = {}
    for clave, valor in estudiantes.items():
        promedios[clave] = (valor[0] + valor[1])/2
    return promedios

def promedioGeneral(promedios):
    return sum(promedios.values()) / len(promedios)

def promedioMasAlto(promedios):
    return max(promedios, key=promedios.get)

def notaMasBaja(estudiantes):
    return min(estudiantes, key=lambda clave: min(estudiantes[clave]))


estudiantes = relacionarDatos(listaNombres, notas_1, notas_2)
promedios = calcularPromedios(estudiantes)

print("ESTUDIANTES Y NOTAS: ")
for clave, valor in estudiantes.items():
    print(f" {clave}: {valor[0]}, {valor[1]} ")

print("\n"*5)
print("ESTUDIANTES Y PROMEDIOS")
for clave, valor in promedios.items():
    print(f" {clave}: {valor}")

print("\n"*5)
print('Promedio general: ', promedioGeneral(promedios))
print('Estudiante con el promedio más alto: ', promedioMasAlto(promedios))
print('Estudiante con la nota más baja: ', notaMasBaja(estudiantes))