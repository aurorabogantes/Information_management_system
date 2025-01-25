import pandas as pd   #DataFrame
import pickle   #Archivo

login = "¡Bienvenid@ al sistema GIRASOL!"
print(login)
    
class User:
    def __init__(self, nombre, email, passw, id, direc, edad, rol, admin):
        self.nombre = nombre
        self.email = email
        self.passw = passw
        self.id = id
        self.direc = direc
        self.edad = edad
        self.rol = rol
        self.admin = admin
        
class Curso:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos
        
class CursoMatriculado:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos
        
class Calificacion:
    def __init__(self, nota, evaluacion):
        self.nota = nota
        self.evaluacion = evaluacion
        
class Tarea:
    def __init__(self, nombre, estado, desc):
        self.nombre = nombre
        self.estado = estado
        self.desc = desc
        
    def entregar(self):
        if self.estado == "No entregado":
            self.estado = "Entregado"
            print("¡Tarea entregada correctamente!")
        else:
            print("La tarea ya fue entregada anteriormente.")
            return
        
class MenuPrincipal:
    def __init__(self):
        self.users = []
        self.cursos = []
        self.cursos_matr = []
        self.calificaciones = []
        self.comentarios = []
        self.tareas = []
        
    def registro(self):
        
        nombre = input("Ingrese su nombre completo: ")
        email = input("Ingrese su correo electrónico: ")
        passw = input("Digite su contraseña: ")
        id = input("Ingrese su número de cédula: ")
        direc = input("Ingrese su dirección exacta: ")
        edad = input("Ingrese su edad: ")
        rol = input("Ingrese su rol (estudiante/profesor): ")
        admin = input("¿Desea inciar como administrador? S/N: ")
        
        user = User(nombre, email, passw, id, direc, edad, rol, admin)
        self.users.append(user)
        
        print("¡Se ha completado su registro!")
        
        txt = f"""
        Nombre completo: {nombre}
        Correo electrónico: {email}
        Contraseña: {passw}
        Número de cédula: {id}
        Dirección: {direc}
        Edad: {edad}
        Rol: {rol}
        ¿Admin?: {admin}
        """
        
        print(txt)  
    
    def inicio_sesion(self):
        while True:
            email = input("Ingrese su correo electrónico: ")
            passw = input("Digite su contraseña: ")
                
            for user in self.users:
                if user.email == email and user.passw == passw:
                    print("¡Se ha iniciado la sesión correctamente!")
                    print(f"Sus credenciales son: {email} y {passw}")
                    if user.rol.lower() == "profesor":
                        print("¡Se ha iniciado sesión como profesor!")
                    elif user.rol.lower() == "estudiante":
                        print("¡Se ha iniciado sesión como estudiante!")
                    else:
                        raise ValueError("Rol incorrecto. Cerrando el programa...")
                    if user.admin.upper() == "S":
                        print("Tiene permisos como administrador.")
                    elif user.admin.upper() == "N":
                        print("No tiene permisos como administrador.")
                    else:
                        raise ValueError("Opción de administrador incorrecta. Cerrando el programa...")
                    return
                print("Sus credenciales son incorrectas. Por favor ingréselas de nuevo. ")
    
    def agregar(self):
        resp = "S"
        while resp.upper() == "S":
            nombre = input("Ingrese el nombre del curso a agregar: ")
            creditos = input("Ingrese la cantidad de créditos del nuevo curso: ")
        
            curso = Curso(nombre, creditos)
            self.cursos.append(curso)
        
            print("¡Curso añadido correctamente!")
        
            txt = f"""
            Nombre del curso: {nombre}
            Créditos del curso: {creditos}
            """
        
            print(txt)
            resp = input("¿Desea añadir otro curso? S/N ")

    
    def leer(self):
        if len(self.cursos) == 0:
            print("No hay cursos registrados.")
            return
        datos = {"Nombre del curso": [curso.nombre for curso in self.cursos],
                    "Créditos del curso": [curso.creditos for curso in self.cursos]}
        
        df = pd.DataFrame(datos)
        print(df)
    
    def editar(self):
        resp = "S"
        while resp.upper() == "S":
            if len(self.cursos) == 0:
                print("No hay cursos registrados.")
                return
                
            print("Cursos disponibles para editar: ")
                
            for i, curso in enumerate(self.cursos):
                print(f"{i + 1}. {curso.nombre} - Créditos: {curso.creditos}")
                
            op = int(input("Ingrese el número de curso a editar: "))
            try:
                if op < 1 or op > len(self.cursos):
                    print("El curso no existe. Pof favor ingrese un número válido. ")
                    return
            except ValueError:
                print("El curso no existe. Por favor ingrese un número válido. ")
                return
                
            select = self.cursos[op - 1]
                
            new_nombre = input("Ingrese el nuevo nombre del curso (no escriba nada para mantener el nombre actual): ")
            if new_nombre:
                select.nombre = new_nombre
                    
            new_creditos = input("Ingrese la nueva cantidad de créditos del curso (no escriba nada para mantener los créditos actuales): ")
            if new_creditos:
                select.creditos = new_creditos
                    
            print(f""""Los nuevos datos del curso son: 
                    Nombre: {select.nombre}
                    Créditos: {select.creditos}""")
                    
            resp = input("¿Desea editar otro curso? S/N ")
                
    def eliminar(self):
        resp = "S"
        while resp.upper() == "S":
            if len(self.cursos) == 0:
                print("No hay cursos registrados. ")
                return
                
            print("Cursos disponibles para eliminar: ")
                
            for i, curso in enumerate(self.cursos):
                print(f"{i + 1}. {curso.nombre} - Créditos: {curso.creditos}")
                    
            op = int(input("Ingrese el número de curso a eliminar: "))
            try:
                if op < 1 or op > len(self.cursos):
                    print("El curso no existe. Por favor ingrese un número válido. ")
                else:
                    curso_eliminar = self.cursos.pop(op - 1)
                    print(f"Se eliminó el curso: {curso_eliminar.nombre}")
                    for i, curso in enumerate(self.cursos):
                        print(f"{i + 1}. {curso.nombre} - Créditos: {curso.creditos}")
            except ValueError or IndexError:
                print("El curso no existe. Por favor ingrese un número válido. ")
                return
                
            resp = input("¿Desea eliminar otro curso? S/N ")
                
    def inscribir(self):
        resp = "S"
        while resp.upper() == "S":
            print("Los cursos disponibles son: ")
        
            for i, curso in enumerate(self.cursos):
                print(f"{i + 1}. {curso.nombre} - Créditos: {curso.creditos}")
            
            op = int(input("Ingrese el número de curso al que desea inscribirse: "))
            try:
                if op < 1 or op > len(self.cursos):
                    print("El curso no existe. Pof favor ingrese un número válido. ")
                    return
            except ValueError:
                print("El curso no existe. Por favor ingrese un número válido. ")
                return
                    
            select = self.cursos[op - 1]
        
            for curso_matr in self.cursos_matr:
                if curso_matr.nombre == select.nombre:
                    print(f"Ya está inscrito en el curso: {select.nombre}")
                    return
        
            self.cursos_matr.append(select)
            print(f"Se inscribió al curso: {select.nombre}")   
            resp = input("¿Desea inscribirse a otro curso? S/N ")
        
    def calificar(self):
        resp = "S"
        while resp.upper() == "S":
            evaluacion = input("Ingrese el nombre de la evaluación a calificar: ")
            nota = input("Ingrese la nota de la evaluación a calificar: ")
            
            calific = Calificacion(nota, evaluacion) 
            self.calificaciones.append(calific)
        
            self.guardar_nota("calificaciones.pkl")
          
            print("¡Nota añadida correctamente!")
            print(f"""
                Nombre de la evaluación: {evaluacion}
                Nota: {nota}
                """)
            resp = input("¿Desea ingresar otra calificación? S/N ")   
            
    def ver_nota(self):
        self.cargar_nota("calificaciones.pkl")
        
        if len(self.calificaciones) == 0:
            print("No hay calificaciones registradas.")
            return
        datos = {"Nombre de la evaluación": [calific.evaluacion for calific in self.calificaciones],
                 "Nota": [calific.nota for calific in self.calificaciones]}   
        df = pd.DataFrame(datos)
        print(df)     
        
    def comentar(self):
        resp = "S"
        while resp.upper() == "S":
            self.cargar_nota("calificaciones.pkl")
        
            if len(self.calificaciones) == 0:
                print("No hay calificaciones registradas.")
                return
        
            print("Calificaciones disponibles para agregar un comentario: ")
        
            for i, calificacion in enumerate(self.calificaciones):
                print(f"{i + 1}. {calificacion.evaluacion} - Nota: {calificacion.nota}")
            
            op = int(input("Ingrese el número de calificación a la que quiere agregar el comentario: "))
            try:
                if op < 1 or op > len(self.calificaciones):
                    print("El curso no existe. Por favor ingrese un número válido. ")
                    return
            except ValueError or IndexError:
                print("El curso no existe. Por favor ingrese un número válido. ")
        
            select = self.calificaciones[op - 1]
            coment = input("Ingrese el comentario que desea agregar: ")
            select.coment = coment
        
            self.guardar_nota("calificaciones.pkl")
        
            print("¡Comentario añadido correctamente!")
            print(f"""
                  Nombre de la evaluación: {select.evaluacion}
                  Nota: {select.nota}
                  Comentario: {select.coment}
                  """)
            resp = input("¿Desea comentar otra evaluación? S/N ")
        
    def guardar_nota(self, Calificaciones):
        with open(Calificaciones, 'wb') as file:
            pickle.dump(self.calificaciones, file)
        print("Calificaciones guardadas correctamente")
        
    def cargar_nota(self, Calificaciones):
        try:
            with open(Calificaciones, 'rb') as file:
                self.calificaciones = pickle.load(file)
            print("Calificaciones cargadas correctamente")
        except FileNotFoundError:
            print("El archivo especificado no existe")
        except Exception as e:
            print("Ocurrió un error al cargar las calificaciones: ", e)
            
    def crear_asignar(self):
        resp = "S"
        while resp.upper() == "S":
            nombre = input("Ingrese el título de la tarea a asignar: ")
            desc = input("Ingrese la descripción de la tarea: ")
            estado = "No entregado"
        
            tarea = Tarea(nombre, estado, desc)
            self.tareas.append(tarea)
        
            self.guardar_tarea("tareas.plk")
        
            print("¡Tarea añadida correctamente!")
            print(f"""
                  Título de la tarea: {nombre}
                  Descripción: {desc}
                  Estado: {estado}
                  """)
            resp = input("¿Desea asignar otra tarea? S/N ")
        
    def ver_tareas(self):
        self.cargar_tarea("tareas.pkl")
        
        if len(self.tareas) == 0:
            print("No hay tareas asignadas.")
            return
        datos = {"Título de la tarea": [tarea.nombre for tarea in self.tareas],
                 "Descripción": [tarea.desc for tarea in self.tareas],
                 "Estado": [tarea.estado for tarea in self.tareas]}
        df = pd.DataFrame(datos)
        print(df)
        
    def enviar(self):
        resp = "S"
        while resp.upper() == "S":
            self.cargar_tarea("tareas.plk")
        
            if len(self.tareas) == 0:
                print("No hay tareas asignadas aún.")
                return
        
            print("Tareas disponibles para entregar: ")
        
            for i, tarea in enumerate(self.tareas):
                print(f"{i + 1}. {tarea.nombre} - Descripción: {tarea.desc}")
            
            op = int(input("Ingrese el número de tarea que desea entregar: "))
            try:
                if op < 1 or op > len(self.tareas):
                    print("La tarea no existe. Por favor ingrese un número válido.")
                    return
            except ValueError or IndexError:
                print("La tarea no existe. Por favor ingrese un número válido.")
            
            entregada = self.tareas[op - 1]
            entregada.entregar()
            self.guardar_tarea("tareas.pkl")
            
            resp = input("¿Desea enviar otra tarea? S/N ")
        
    def guardar_tarea(self, Tareas):
        with open(Tareas, 'wb') as file:
            pickle.dump(self.tareas, file)
        print("Tarea/s guardadas correctamente")
        
    def cargar_tarea(self, Tareas):
        try:
            with open(Tareas, 'rb') as file:
                self.tareas = pickle.load(file)
            print("Tareas cargadas correctamente")
        except FileNotFoundError:
            print("El archivo especificado no existe")
        except Exception as e:
            print("Ocurrió un error al cargar las calificaciones: ", e)
    
    def opciones_admin(self):
        print("¡Bienvenid@ a la pantalla administrador!")
        bool = True
        while bool == True:
            op = int(input("¿Desea registrarse o iniciar sesión? Digite '1' para registrarse, '2' para iniciar sesión o '3' para salir: "))
            if op == 1:
                menu.registro()
            elif op == 2:
                menu.inicio_sesion()
                bool = False
            elif op == 3:
                print("Cerrando el programa...")
                exit()
            else:
                print("Opción inválida. Por favor digite el número nuevamente. ")
                
    def opciones_mant_cursos(self):
        print("¡Bienvenid@ a la pantalla de mantenimiento de cursos!")
        while True:
            op = int(input("Digite '1' para crear un nuevo curso, '2' para leer los cursos ya creados, '3' para editar los cursos, '4' para eliminar algún curso o '5' para volver al menú principal: "))
            if op == 1:
                menu.agregar()
            elif op == 2:
                menu.leer()
            elif op == 3:
                menu.editar()
            elif op == 4:
                menu.eliminar()
            elif op == 5:
                print("Volviendo...")
                break
            else:
                print("Opción inválida. Por favor digite el número nuevamente. ")
                
    def gestion_cursos(self):
        print("¡Bienvenid@ a la pantalla de gestión de cursos!")
        while True:
            for user in self.users:
                if user.rol.lower() == "profesor":
                    op = int(input("Digite '1' para editar algún curso, '2' para eliminarlo o '3' para volver al menú principal: "))
                    if op == 1:
                        menu.editar()
                    elif op == 2:
                        menu.eliminar()
                    elif op == 3:
                        print("Volviendo...")
                        return
                    else:
                        print("Opción inválida. Por favor digite el número nuevamente. ")
                elif user.rol.lower() == "estudiante":
                    op = int(input("Digite '1' para inscribirse a algún curso o '2' para volver al menú principal: "))
                    if op == 1:
                        menu.inscribir()
                    elif op == 2:
                        print("Volviendo...")
                        return
                    else:
                        print("Opción inválida. Por favor digite el número nuevamente. ")
         
    def calif_eval(self):
        print("¡Bienvenid@ a la pantalla de calificaciones y evaluaciones!")
        while True:
            for user in self.users:
                if user.rol.lower() == "profesor":
                    op = int(input("Digite '1' para asignar calificaciones o '2' para volver al menú principal: "))
                    if op == 1:
                        menu.calificar()
                    elif op == 2:
                        print("Volviendo...")
                        return   
                    else:
                        print("Opción inválida. Por favor digite el número nuevamente. ")
                elif user.rol.lower() == "estudiante":
                    op = int(input("Digite '1' para ver sus calificaciones, '2' para hacer un comentario a una nota o '3' para volver al menú principal: "))
                    if op == 1:
                        menu.ver_nota()
                    elif op == 2:
                        menu.comentar()
                    elif op == 3:
                        print("Volviendo...")
                        return
                    else:
                        print("Opción inválida. Por favor digite el número nuevamente. ")
                        
    def asignaciones_tareas(self):
        print("¡Bienvenid@ a la pantalla de asignaciones y tareas!")
        while True:
            for user in self.users:
                if user.rol.lower() == "profesor":
                    op = int(input("Digite '1' para asignar una tarea, '2' para ver las tareas asignadas o '3' para volver al menú principal: "))
                    if op == 1:
                        menu.crear_asignar()
                    elif op == 2:
                        menu.ver_tareas()
                    elif op == 3:
                        print("Volviendo...")
                        return
                    else:
                        print("Opción inválida. Por favor digite el número nuevamente. ")
                elif user.rol.lower() == "estudiante":
                    op = int(input("Digite '1' para entregar una tarea o '2' para volver al menú principal: "))
                    if op == 1:
                        menu.enviar()
                    elif op == 2:
                        print("Volviendo...")
                        return
                    else:
                        print("Opción inválida. Por favor digite el número nuevamente. ")
    
    def historial_academico(self):
        print("¡Bienvenid@ a la pantalla de historial académico!")
        while True:
            for user in self.users:
                if user.rol.lower() == "estudiante":
                    op = int(input("Digite '1' para ver los cursos, '2' para ver el desglose de notas o '3' para volver al menú principal: "))
                    if op == 1:
                        menu.leer()
                    elif op == 2:
                        menu.ver_nota()
                    elif op == 3:
                        print("Volviendo...")
                        return
                    else:
                        print("Opción inválida. Por favor digite el número nuevamente. ")
                        
    def menu_principal(self):
        while True:
            for user in self.users:
                if user.rol.lower() == "estudiante":
                    print("""
                          Opción '1' para ingresar a la pantalla de mantenimiento de cursos (solo para admins).
                          Opción '2' para ingresar a la pantalla de gestión de cursos.
                          Opción '3' para ingresar a la pantalla de calificaciones y evaluaciones.
                          Opción '4' para ingresar a la pantalla de asignaciones y tareas.
                          Opción '5' para ingresar a la pantalla de historial académico.
                          Opción '6' para salir del programa.
                          """)
                    op = int(input("Digite la opción que desea ejecutar: "))
                    
                    if op == 1:
                        if user.admin.upper() == "S":
                            self.opciones_mant_cursos()
                    elif op == 2:
                        self.gestion_cursos()
                    elif op == 3:
                        self.calif_eval()
                    elif op == 4:
                        self.asignaciones_tareas()
                    elif op == 5:
                        self.historial_academico()
                    elif op == 6:
                        print("Cerrando el programa...")
                        return
                    else:
                        print("Opción inválida. Por favor inténtelo de nuevo. ")
                elif user.rol.lower() == "profesor":
                    print("""
                          Opción '1' para ingresar a la pantalla de mantenimiento de cursos (solo para admins).
                          Opción '2' para ingresar a la pantalla de gestión de cursos.
                          Opción '3' para ingresar a la pantalla de calificaciones y evaluaciones.
                          Opción '4' para ingresar a la pantalla de asignaciones y tareas.
                          Opción '5' para salir del programa.
                          """)
                    op = int(input("Digite la opción que desea ejecutar: "))
                    
                    if op == 1:
                        if user.admin.upper() == "S":
                            self.opciones_mant_cursos()
                    elif op == 2:
                        self.gestion_cursos()
                    elif op == 3:
                        self.calif_eval()
                    elif op == 4:
                        self.asignaciones_tareas()
                    elif op == 5:
                        print("Cerrando el programa...")
                        return
                    else:
                        print("Opción inválida. Por favor inténtelo de nuevo.")
             
menu = MenuPrincipal()
menu.opciones_admin()
menu.menu_principal()