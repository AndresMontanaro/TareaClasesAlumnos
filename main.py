alumnos = []
profesores = []
cursos = []

class Curso:

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.profesores = []
        self.alumnos = []

    def asignar_profesor_curso(self, objeto_profesor):
        self.profesores.append(objeto_profesor)

    def asignar_alumno_curso(self, objeto_alumno):
        self.alumnos.append(objeto_alumno)

    def consultar_curso(self):
        print(f"{self.codigo}:\t{self.nombre}\t",
              f"Llevado por: {", ".join([profesor.nombre for profesor in self.profesores])}")

    def reporte_alumnos_curso(self):
        
        print(f"\n{str(self.nombre).upper()}\n")

        if self.alumnos:
            
            print(f"Alumnos encontrados en este curso: {len(self.alumnos)}")

            promedio = sum(int(alumno.nota) for alumno in self.alumnos) / len(self.alumnos)

            print(f"Promedio de las notas: {promedio:.2f}")
                            
            print(f"Aprobados: {len(list(filter(lambda nota: nota >= 70, 
                                                (int(alumno.nota) for alumno in self.alumnos))))}")
                            
            print(f"Aplazados: {len(list(filter(lambda nota: 60 <= nota < 70, 
                                                (int(alumno.nota) for alumno in self.alumnos))))}")
                            
            print(f"Reprobados: {len(list(filter(lambda nota: nota < 60, 
                                                (int(alumno.nota) for alumno in self.alumnos))))}")
                            
            print(f"Notas superiores al promedio: {len(list(filter(lambda nota: nota > promedio, 
                                                                (int(alumno.nota) for alumno in self.alumnos))))}\n")

            alumnos_ordenados = sorted(self.alumnos, key=lambda alum: alum.nota, reverse=True)

            for alumno in alumnos_ordenados:
                alumno.consultar_alumno(promedio)  

        else:
            print("No hay alumnos en este curso")


class Alumno:

    def __init__(self, nombre, cedula, curso : Curso, nota):
        self.nombre = nombre
        self.cedula = cedula
        self.curso = curso
        self.nota = nota
        
    def consultar_alumno(self, promedio):
        print(f"{str(self.cedula).ljust(8)}: {str(self.nombre).ljust(20)}  "
              f"{str(self.curso.nombre).ljust(14)}  {str(self.nota).ljust(11)}  "
              f"{str("APROBADO" if int(self.nota) >= 70 else "APLAZADO" if 60 <= int(self.nota) < 70 else "REPROBADO").ljust(13)}  "
              f"{str("SUPERIOR AL PROMEDIO" if int(self.nota) > promedio else "INFERIOR AL PROMEDIO").ljust(16)}")               
            
class Profesor:

    def __init__(self, cedula, nombre, curso : Curso):
        self.cedula = cedula
        self.nombre = nombre
        self.curso = curso

    def consultar_profesor(self):
        print(f"{str(self.cedula).ljust(8)}:  {str(self.nombre).ljust(12)}  "
              f"{str(self.curso.nombre).ljust(16)}")
        
def menu():
 
    while True:
        print("\n SISTEMA ESCOLAR DE CALIFICACIONES \n")

        print("1. Agregar\consultar alumnos")
        print("2. Agregar\consultar profesores")
        print("3. Agregar\consultar cursos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                subopcion = input("\na) Agregar alumno\nb) Consultar alumnos\nc) Salir\nSeleccione una opción: ").lower()

                if subopcion == 'a':
                    
                    if agregar_alumno():
                        break

                elif subopcion == 'b':
                    
                    if len(alumnos) > 0:

                        reporte_alumnos()

                        input("\nPresione Enter para seguir")

                    else:
                        print("\nNo hay alumnos para consultar")

                    break
                
                elif subopcion == 'c':

                    break

                else:

                    print("\nOPCIÓN INVÁLIDA")
        
        elif opcion == "2":
            while True:
                subopcion = input("\na) Agregar profesor\nb) Consultar profesores\nc) Salir\nSeleccione una opción: ").lower()

                if subopcion == 'a':
                    
                    if agregar_profesor():
                        break

                elif subopcion == 'b':

                    if len(profesores) > 0:
                        
                        reporte_profesores()
                    
                        input("\nPresione Enter para seguir")

                    else:
                        print("\nNo hay profesores para consultar")

                    break
                
                elif subopcion == 'c':

                    break

                else:

                    print("\nOPCIÓN INVÁLIDA")

        elif opcion == "3":
            while True:
                subopcion = input("\na) Agregar curso\nb) Consultar cursos\nc) Salir\nSeleccione una opción: ").lower()

                if subopcion == 'a':
                    
                    if agregar_curso():
                        break

                elif subopcion == 'b':
                    
                    if len(cursos) > 0:
                        
                        reporte_cursos()
                            
                        input("\nPresione Enter para seguir")

                    else:
                        print("\nNo hay cursos para consultar")

                    break
                
                elif subopcion == 'c':

                    break

                else:

                    print("\nOPCIÓN INVÁLIDA")

        elif opcion == "4":

            print("\nSISTEMA FINALIZADO")
            break
        
        else:

            print("\nOPCIÓN INVÁLIDA")

def agregar_alumno():

    nombre = input("\nNombre del alumno: ")

    if list(filter(lambda alum: alum.nombre==nombre, alumnos)):
        print("\nEse nombre de alumno ya existe.")
        return False

    cedula = input("Cédula del alumno (9 dígitos): ")

    if len(cedula) != 9 or not cedula.isdigit():
        print("\nLa cédula debe ser numérica con solo 9 dígitos.")
        return False
     
    if list(filter(lambda alum: alum.cedula==cedula, alumnos)) \
                        or list(filter(lambda prof: prof.cedula==cedula, profesores)):
        print("\nEsa cédula ya existe.")
        return False
     
    if len(cursos) == 0:
        print("\nNo hay cursos. Tendrás que agregar cursos desde la opción de cursos.")
        return False
                    
    print("\nCURSOS\n")

    for objeto_curso in cursos:
        objeto_curso.consultar_curso()
                        
    codigo_curso = input("\nCurso del alumno (Código): ")

    if not list(filter(lambda curs: curs.codigo==codigo_curso, cursos)):
        print(f"\nNo existe el curso con código: {codigo_curso}. Tendrás que agregarlo en la opción de cursos.")
        return False

    objeto_curso = list(filter(lambda curs: curs.codigo==codigo_curso, cursos))[0]

    nota = input("\nNota del alumno: ")
                    
    if not nota.isdigit() or int(nota) > 100:
        print("\nLa nota debe ser totalmente en número entero y entre 0 y 100.")
        return False  
    
    objeto_alumno = Alumno(nombre, cedula, objeto_curso, nota) 
    
    objeto_curso.asignar_alumno_curso(objeto_alumno)

    alumnos.append(objeto_alumno)

    print("\nALUMNO AGREGADO")  
    return True

def reporte_alumnos():

    print("\nREPORTE DE ALUMNOS\n")
    print(f"Alumnos encontrados en total: {len(alumnos)}")

    promedio = sum(int(alumno.nota) for alumno in alumnos) / len(alumnos)

    print(f"Promedio total de las notas: {promedio:.2f}")
                        
    print(f"Aprobados totales: {len(list(filter(lambda nota: nota >= 70, 
                                            (int(alumno.nota) for alumno in alumnos))))}")
                        
    print(f"Aplazados totales: {len(list(filter(lambda nota: 60 <= nota < 70, 
                                            (int(alumno.nota) for alumno in alumnos))))}")
                        
    print(f"Reprobados totales: {len(list(filter(lambda nota: nota < 60, 
                                            (int(alumno.nota) for alumno in alumnos))))}")
                        
    print(f"Notas totales superiores al promedio: {len(list(filter(lambda nota: nota > promedio, 
                                                              (int(alumno.nota) for alumno in alumnos))))}\n")

    for objeto_curso in cursos:
        objeto_curso.reporte_alumnos_curso()

def agregar_profesor():
    cedula = input("\nCédula del profesor (9 dígitos): ")

    if len(cedula) != 9 or not cedula.isdigit():
        print("\nLa cédula debe ser numérica con solo 9 dígitos.")
        return False
                    
    if list(filter(lambda alum: alum.cedula==cedula, alumnos)) \
        or list(filter(lambda prof: prof.cedula==cedula, profesores)):
        print("\nEsa cédula ya existe.")
        return False

    nombre = input("Nombre del profesor: ")

    if list(filter(lambda prof: prof.nombre==nombre, profesores)):
        print("\nEse nombre de profesor ya existe.")
        return False
            
    if len(cursos) == 0:
        print("\nNo hay cursos. Tendrás que agregar cursos desde la opción de cursos.")
        return False
            
    print("\nCURSOS\n")

    for objeto_curso in cursos:
        objeto_curso.consultar_curso()
                        
    codigo_curso = input("\nCurso del profesor (Código): ")

    if not list(filter(lambda curs: curs.codigo==codigo_curso, cursos)):
        print(f"\nNo existe el curso con código: {codigo_curso}. Tendrás que agregarlo en la opción de cursos.")
        return False

    objeto_curso = list(filter(lambda curs: curs.codigo==codigo_curso, cursos))[0]

    objeto_profesor = Profesor(cedula, nombre, objeto_curso)

    objeto_curso.asignar_profesor_curso(objeto_profesor)

    profesores.append(objeto_profesor)

    print("\nPROFESOR AGREGADO")
    return True

def reporte_profesores():

    print("\nPROFESORES\n")
    print(f"Profesores encontrados: {len(profesores)}\n")

    for objeto_profesor in profesores:
        objeto_profesor.consultar_profesor()

def agregar_curso():
    codigo_curso = input("\nCódigo del curso: ")
    
    if not codigo_curso.isdigit():
        print("\nEl código debe ser totalmente numérico")
        return False
                        
    if list(filter(lambda curs: curs.codigo==codigo_curso, cursos)):
        print(f"\nEl código del curso ya existe.")
        return False

    nombre = input("Nombre del curso: ")

    if list(filter(lambda curs: curs.nombre==nombre, cursos)):
        print("\nEse nombre de curso ya existe.")
        return False

    objeto_curso = Curso(codigo_curso, nombre)

    cursos.append(objeto_curso)

    print("\nCURSO AGREGADO")
    return True

def reporte_cursos():

    print("\nCURSOS\n")
    print(f"Cursos encontrados: {len(cursos)}\n")

    for objeto_curso in cursos:
        objeto_curso.consultar_curso()

if __name__=='__main__':
    menu()    