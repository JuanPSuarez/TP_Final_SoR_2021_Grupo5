import Funciones
 
VecPass= ["admin", "pwdeluser1"]
VecNom= ["Susana Horia", "Esteban Quito"]
VecNIF= ["23647832", "34526478"]
VecNac= ["05/09/1974", "23/03/1990"]
VecLoc= ["Miramar", "Unquillo"]
VecDir= ["Gob. Loza 345", "Güemes 34"]
VecTarj= ["23443543533", "42354643"]
VecNomTarj= ["Susana Horia", "Esteban Quito"]
VecCodSeg= ["767", "986"]
VecVenc= ["09/25", "12/23"]
 
Opc=int(input("¿Qué desea realizar? Seleccione una opción\n1- Ingresar a su cuenta\n2- ¿No tiene una cuenta? Regístrese\n"))
 
while Opc == 1 or 2:
 
    if Opc==2:
        print("Complete el siguiente formulario")
        Nom=str(input("Nombre completo: "))
        VecNom.append(Nom)
        NIF=str(input("DNI: "))
        VecNIF.append(NIF)
        Pass=str(input("Contraseña: "))
        VecPass.append(Pass)
        Nac=str(input("Fecha de nacimiento (DD/MM/AAAA): "))
        VecNac.append(Nac)
        Loc=str(input("Localidad: "))
        VecLoc.append(Loc)
        Dir=str(input("Dirección: "))
        VecDir.append(Dir)
        Tarj=str(input("Número de tarjeta de crédito/débito: "))
        VecTarj.append(Tarj)
        NomTarj=str(input("Nombre como figura en la tarjeta: "))
        VecNomTarj.append(NomTarj)
        CodSeg=str(input("Código de seguridad: "))
        VecCodSeg.append(CodSeg)
        Venc=str(input("Fecha de vencimiento: "))
        VecVenc.append(Venc)
        print("¡Su usuario ha sido dado de alta! Ingrese su DNI y contraseña para ingresar al sistema.")
        Opc=1
 
    if Opc==1:
        Tipo= int(input("Ingrese el tipo de cuenta: \n1- Usuario\n2- Administrador\n"))
 
        while Tipo != (1 or 2):
            print("Ingrese una opción válida.")
            Tipo= int(input("Ingrese el tipo de cuenta: \n1- Usuario\n2- Administrador\n"))
 
 
        NIF= str(input("Ingrese su DNI: "))
        Pass= str(input("Ingrese su contraseña: "))
        Msj=""
 
       
 
        if Funciones.ValidarUsuario(VecNIF, VecPass, NIF, Pass, len(VecNIF)) == True:
            if Tipo==2:
                Msj= "Ingrese una opción para continuar: "
                print(Msj)
            if Tipo==1:
                Msj= "Bienvenido/a, has ingresado al sistema."
                print(Msj)
                OpcMenuUser = 0
                while OpcMenuUser != 4:
                    print (f"""
                    ¿Que desea hacer?
                    1. Alta de una linea. (Prueba)
                    2. Cargar saldo. (Placeholder)
                    3. Dar de baja su usuario.
                    4. Salir. \n""")
                   
                    OpcMenuUser = int(input("Ingrese una opción: "))
 
                    if OpcMenuUser == 3:                        
                        print(f"""
                        ¿Está seguro de que quiere dar de baja su usuario?
                        1 - Sí, confirmo la baja de mi usuario.
                        2 - Cancelar.
                        """)
                        ConfBaja = int(input("Ingrese una opción: "))
                        if ConfBaja == 1:
                            Pass = str(input("Ingrese su contraseña para confirmar: "))
                            h = VecPass.index(Pass)
                            print(h)
                            VecPass.pop(h) #Se remueve todo lo relacionado con dicho usuario.
                            VecNom.pop(h)
                            VecNIF.pop(h)
                            VecNac.pop(h)
                            VecLoc.pop(h)
                            VecDir.pop(h)
                            VecTarj.pop(h)
                            VecNomTarj.pop(h)
                            VecCodSeg.pop(h)
                            VecVenc.pop(h)
                            print("Usuario eliminado correctamente.")
                            break
                        if ConfBaja == 2:
                            OpcMenuUser = 0
                        else:
                            OpcMenuUser = 0
                            print ("Ingrese una opción válida.")
                    if OpcMenuUser == 1 or OpcMenuUser == 2:
                        print("Menú en construcción...")
                        OpcMenuUser = int(input("Ingrese otra opción: "))
                    if OpcMenuUser == 4:
                        break
        else:
            print("Usuario o contraseña incorrectos.")
 
    break
 
print("Programa finalizado.")
