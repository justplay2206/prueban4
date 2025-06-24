datos_estudiantes={
    [
        "Estudiantes",
        {
        "Nombre":"Juan",
        "Sexo":"M",
        "Contraseña":"a12345"
        }
    ]
}



def validar_texto (mensajeinput:str,texto:str):
    while True:
        try:
            texto=input(mensajeinput)
            if len(texto) == 0:
                print("Debe colocar un caracter valido")
                continue 
        except:
            print("Debe colocar un caracter valido")
            continue
        break


def validar_bool(sexo:str,mensajeinput:str,texto:str):
    while True:
        sexo=validar_texto(mensajeinput)
        texto.upper(sexo)
        if not sexo == ("F") and not sexo ==("M"):    
            print("Caracter no valido")
            continue



def registrar_estudiantes(estudiantes:dict,nombre:str,sexo:str,contraseña:int):
    while True:
        try:
            nombre=validar_texto("Ingrese el nombre del estudiante: ")
            sexo=validar_bool("Ingrese el sexo del estudiante")
            contraseña
        except:
            print("Debe colocar un caracter valido")
            continue
        estudiantes={
            "Nombre":nombre,
            "Sexo":sexo,
            "Contraseña":contraseña
        }
        if estudiantes == None:
            datos_estudiantes["Estudiantes"].append[estudiantes]
            print("Registro hecho exitosamente!!!")
        else:
            print("Este estudiante ya se encuentra registrado")




def buscar_usuario(nombre:str,contraseña:str,sexo:str):
    nombre=validar_texto("Ingrese el nombre del estudiante que desea ingresar:" )
    for i in datos_estudiantes["Estudiantes"]:
        if i[nombre] in datos_estudiantes["Estudiantes"]:
            print(f"Nombre: {i(nombre)}- Sexo: {"Sexo"}, Contraseña: {"Contraseña"}")
            
        return i   


def eliminar_usuario(nombre:str,mensajeinput):
    while True:
        nombre=input(mensajeinput)
        for i in datos_estudiantes["Estudiantes"]:
            if i[nombre] in datos_estudiantes ["Estudiantes"]:
                datos_estudiantes["Estudiantes"].remove[nombre]
                break
            elif not i [nombre] in datos_estudiantes ["Estudiantes"]:
                print("Error, debe hacerlo de nuevo")
                continue