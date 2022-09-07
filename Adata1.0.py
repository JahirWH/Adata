import csv
import os
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from time import sleep
import getpass
#import tk
#import tkinter
#from tkinter import ttk



def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

items = list(range(0, 50))
l = len(items)

loadbar(0, l, prefix='Progress:', suffix='Complete', length=l)
for i, item in enumerate(items):
        sleep(0.1)
        loadbar(i + 1, l, prefix='Progress:', suffix='Complete', length=l)

def clearConsole():
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)




def show():
    print("███╗░░░███╗██╗░░░██╗  ██████╗░░█████╗░████████╗░█████╗░██████╗░░█████╗░░██████╗███████╗")
    print("████╗░████║╚██╗░██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝")
    print("██╔████╔██║░╚████╔╝░  ██║░░██║███████║░░░██║░░░███████║██████╦╝███████║╚█████╗░█████╗░░")
    print("██║╚██╔╝██║░░╚██╔╝░░  ██║░░██║██╔══██║░░░██║░░░██╔══██║██╔══██╗██╔══██║░╚═══██╗██╔══╝░░")
    print("██║░╚═╝░██║░░░██║░░░  ██████╔╝██║░░██║░░░██║░░░██║░░██║██████╦╝██║░░██║██████╔╝███████╗")
    print("╚═╝░░░░░╚═╝░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝")

def img():
    print("               _________")
    print("              |MMMMMMMMM|                _")
    print("  ________    |MMMMMMMMM|              _|l|_")
    print(" |!!!!!!!_|___|MMMMMMMMM|             |lllll|")
    print(" |!!!!!!|=========|MMMMM|             |lllll|_______")
    print(" |!!!!!!|=========|MMMMM|            _|lllll|HHHHHHH|")
    print(" |!!!!!!|=========|MMMMM|   ________|lllllllll|HHHHH|")
    print(" |!!!!!!|=========|MMMMM|  |unununun|lllllllll|HHHHH|______")
    print(" |!!!!!!|=========|MMMMM|  |nunununu|lllllllll|HH|:::::::::|")
    print(" |!!!!!!|=========|MMM__|..|un__unun|lllllllll|HH|:::::::::|")
    print(" |!!!!!!|=======_=|M_( ')' );' .)unu|lllllllll|HH|:::::::::|")
    print(" |!!!_!!|======( )|(. ` ,) (_ ', )un|lllllllll|HH|:::::::::| ~~~")
    print(" |!!(.)!|===__(`.')_(_ ')_,)(. _)unu|lllllllll|HH|:__::::::|~~  ~~")
    print(" |!(.`')|==( .)' .)MMM|M|| |un|nunun|lllllllll|``|( ,)_::::| ~~~~ ~")
    print("  -(: _)|=(`. ')_)|---|- '  ``|`````|lll____ll|  (_; `'):::|~~~  ~~~")
    print("     |  |==(_'_)|=|    ______        ''/\   \'   |(_'_)::::|\~~~~__|)__")
    print("     |   ''''|''o/`.-``~~~~~ ``-.     /--\___\    ``|`````` /____\____/")
    print(" ....        |  h ( `; ~~~ ~~  ~ )    |M_|#_#|      ' --   __________|~")
    print("       --   *      '-.._~~__~..-'   --           -* -     /  ~~~~ ~~~~~~")
    print(" *   -   -      --           ----         ---         _.-'~~~~~     ~ ~~")
    print("__--_________............-------------'''''''''''''''` ~~~~~    ~~~ ~~~~")
    print("~~    ~~~~~~~~     ~~~~~~~   ~~~~~~~~~   ~~~~~~~~~~      ~~~~~~~     ~~~")
    print("~~~~~~~~~  ~~~~  ~~~~~ ~~~~~~~~~ ~ ~      ~~~~~~ ~~~~~~     ~~~~    ~~~~")
    print("~~~~~~~~     ~~~~~~~~~~~~~~~        ~~~~~~~~~~~~ ~~~~~~  ~~~ ~~~~~~  ~~~")

def lenguaje():
    print(" Java")
    print("Oracle")
    print("Maven")
    print("HTML5")
    print("Java Script")
    print("Desarrollo de Software")
    print("Consumo de web services")
    print("Base de datos")
    print("Framework")
    print("Lenguajes de desarrollo")
    print("4+ years of experience as a key .NET C# developer on enterprise projects (WPF + WinForms)")
    print("General knowledge of Web Services (SOAP, REST)")
    print("Some experience with automated testing with frameworks like nUnit, though not required")
    print("Experience as a full stack developer with knowledge of OOP design patterns and their implementation (MVVM, MVP)")
    print("Experience writing SQL and stored procedures (MSSQL)")
    print("Strong analytical, organizational, written and verbal communication skills")
    print("‘Get it done' mentality with a love for creative problem solving")
    print("Experienced with Team Foundation Server/Azure DevOps code management and planning tools")
    print("Web:")
    print("4+ years of experience as a key .NET C# developer on enterprise projects (MVC + webforms)")
    print("2+ years of experience with HTML, CSS, and JavaScript")
    print("Azure App Services and Azure SQL for hosted products")
    print("SQL Server Integration Services")
    print("Some experience with automated testing with frameworks like nUnit, though not required.")
    print("Experience as a full stack developer with knowledge of OOP design patterns and their implementation")
    print("Experience writing SQL and stored procedures (MSSQL)")
    print("Strong analytical, organizational, written and verbal communication skills")
    print("‘Get it done' mentality with a love for creative problem solving")
    print("Experienced with Team Foundation Server/Azure DevOps code management and planning tools")
    
    
def mexico():
    print("                .")
    print("         \'~~~-,")
    print("          \    '-,_ ")
    print("           \ /\    `~'~''\          M E X I C O")
    print("           _\ \\          \/~\ ")
    print("           \__ \\             \   ")
    print("              \ \\.             \  ")
    print("               \ \ \             `~~")
    print("                '\\ \.             /")
    print("                 L \  \            |")
    print("                  \_\  \      o    |             _.----,")
    print("                        |       San \           !     /")
    print("                       '._      Luis \_      __/    _/")
    print("                          \_    Potosi ''--''    __/")
    print("                            \.__                |")
    print("                                ''.__  __.._   __\"")
    print("                                     ''     './  ` ")




def validate():
    while True:
        password = getpass.getpass("Introduce tu contraseña: ")
        if password =="1656":
              break
        if password=="1":
            VerInventario()
        elif password !="1656!":
                clearConsole()
                print("┌─┐┌─┐┌─┐┌─┐┬ ┬┌─┐┬─┐┌┬┐   ┬┌┐┌┌─┐┌─┐┬─┐┬─┐┌─┐┌─┐┌┬┐")  
                print("├─┘├─┤└─┐└─┐││││ │├┬┘ ││   │││││  │ │├┬┘├┬┘├┤ │   │ ")  
                print("┴  ┴ ┴└─┘└─┘└┴┘└─┘┴└──┴┘   ┴┘└┘└─┘└─┘┴└─┴└─└─┘└─┘ ┴ ")
                

def menu():

    print("******MENU INVENTARIO******")
    print("1.Ver invetario")
    print("2.Agregar contraseña")
    print("3.Modificar Contraseña")
    print("6.buscar por nombre ")
    print("Buscar Compañia")
    print("the word ,exit, show, mexico, lenguaje")
    option=input("Introduzca el número de la opción deseada: ")
    return option

def ExisteCodigo(codigo):
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        for row in reader:
            if(codigo==row['codigo']):
                return row
        return "No existe"

def VerInventario():
      #with open('Inventario.csv')as File:
        #reader=csv.DictReader(File)
        #contador=0
        #for row in reader:
            #print('' + str(row['codigo'])+'\t' + str(row['restrictiva'])+'\t' + str(row['ubicacion'])+'\t' 
            #+ str(row['descripcion'])+'\t' + str(row['unidad'])+'\t'+ str(row['tipo'])
            #+'\t' + str(row['familia'])+'\t' + str(row['stock_minimo'])+'\t' + str(row['cantidad_inicial'])
            #+'\t' + str(row['ingresos'])+'\t' + str(row['egresos'])+'\t' + str(row['perdidas'])
            #+'\t' + str(row['total'])+'\t' + str(row['observaciones'])+'\t' + str(row['observacion_perdida']))
            #contador=contador+1
        #print('****Total Filas('+str()+')')
    df=pd.read_csv(r'Inventario.csv',engine='python')
    print(df)
    print( "Aqueronte_1887")
    print("francisco hayes the Bacio_1859")
    print("las meninas de diego velasquez Barroco1656 ")
    print("la balsa de la meduse1819")
    print("El inocente pedro infante1956" )
    print("el hombre llega a la lunaªm Apolo1969")
    print("miroslava Stern1955")
    print("escuela de vagabundos 1955")
    print("Tabla 2")
    print("Nip bitso 251656")
    #df2=pd.read_csv(r'Inventario2.csv',engine='python')
    #print(df2)
    return




def ProductoNuevo():
    codigo = input('Ingrese nuevo numero: ')
    if ExisteCodigo(codigo)=="No existe":
        ubicacion=input('IName Service: ')
        descripcion=input('Email ')
        unidad=input('Password ')
        tipo=input(' Username ?: ')
        familia=input('Web: ')
        #stock_minimo=0
        #cantidad_inicial=0
        #ingresos="0"
        #egresos="0"
        #perdidas="0"
        #total="0"
        #observaciones="N"
        #observaciones_perdida="O"
        restrictiva="N"
        with open ('Inventario.csv','a')as File:
            File.write('\n'+codigo+','+restrictiva+','+ubicacion+','+descripcion+','
            +unidad+','+tipo+','+familia)
    else:
        print("****Error el codigo ya existe****")

def ModificarProducto():
    codigo=input('Ingrese codigo modificar: ')
    if ExisteCodigo(codigo)=="No existe":
        print('----Error el codigo que desea modificar no existe----')
    else:
        ubicacion=input(' name service: ')
        descripcion=input('Email: ')
        unidad=input('New password :')
        tipo=input('username: ')
        familia=input('Pagina Web: ')
        modificarBDD(codigo,ubicacion,descripcion,unidad,tipo,familia)

def modificarBDD(codigo,ubicacion,descripcion,unidad,tipo,familia):
    result=[]
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        for row in reader:
            #Compara el codigo hasta encontrar lugar vacio
            if row['codigo']==codigo:
                row['codigo']=codigo
                row['restrictiva']=row['restrictiva']
                row['service']=ubicacion
                row['email']=descripcion
                row['password']=unidad
                row['username']=tipo
                row['web']=familia
                #row['stock_minimo']=row['stock_minimo']
               # row['cantidad_inicial']=row['cantidad_inicial']
                #row['ingresos']=row['ingresos']
                #row['egresos']=row['egresos']
                #row['perdidas']=row['perdidas']
                #a=int(str(row['cantidad_inicial']))
                #b=int(str(row['ingresos']))
                #c=int(str(row['egresos']))
                #d=int(str(row['perdidas']))
                #operacion=(a+b)-(c+d)
                #total=int(str(operacion))
                #stock=int(str(row['stock_minimo']))
                #if total <= stock:
                #temp=str(total)
                   # observaciones="Solicitar Material"
                #row['total']=temp
                #row['observaciones']=observaciones
               # else:
                 #   observaciones="Stok a favor"
               # row['total']=total
                #row['observaciones']=observaciones
                #row['observacion_perdida']=row['observacion_perdida']
            result.append(row)
        
    with open('Inventario.csv','w')as File:
        fieldnames=['codigo','restrictiva','service','email','password','username','web']
        writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
        writer.writeheader()
        writer.writerows(result)
        #writer = csv.DictWriter(csvfile, fieldnames=["Bio_Id","Last_Name","First_Name","late","undertime","total_minutes", "total_ot", "total_nsd", "total_absences"], 
         #               extrasaction='ignore', delimiter = ';')

def EliminarProducto():
    codigo=input('Ingrese codigo a eliminar: ')
    if ExisteCodigo(codigo)=="No existe":
        print('----Error el codigo que desea eliminar no existe----')
    else:
        eleccion=input('Si esta seguro si=S no=N? ')
        if eleccion=='S':
            EstadoElimandoBDD(codigo) 

def EstadoElimandoBDD(codigo):
    result=[]
    contraseña=str(input('Ingrese contraseña: '))
    if contraseña =="1324":
        with open('Inventario.csv')as File:
            reader=csv.DictReader(File)
            estado="S"
            for row in reader:
                if row['codigo']==codigo:
                    row['codigo']=row['codigo']
                    row['restrictiva']=estado
                    row['ubicacion']=row['ubicacion']
                    row['descripcion']=row['descripcion']
                    row['unidad']=row['unidad']
                    row['tipo']=row['tipo']
                    row['familia']=row['familia']
                    row['stock_minimo']=row['stock_minimo']
                    row['cantidad_inicial']=row['cantidad_inicial']
                    row['ingresos']=row['ingresos']
                    row['egresos']=row['egresos']
                    row['perdidas']=row['perdidas']
                    row['total']=row['total']
                    row['observaciones']=row['observaciones']
                    row['observacion_perdida']=row['observacion_perdida']
                result.append(row)
        with open('Inventario.csv','w')as File:
            fieldnames=['codigo','restrictiva','ubicacion','descripcion','unidad','tipo','familia','stock_minimo','cantidad_inicial'
            ,'ingresos','egresos','perdidas','total','observaciones','observacion_perdida']
            writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
            writer.writeheader()
            writer.writerows(result)
    else:
        print('Contraseña incorrecta')

def BuscarProducto():
    codigo=input('Ingrese codigo de producto a buscar: ')
    if ExisteCodigo(codigo)=="No existe":
        print('----Error el codigo que desea buscar no existe----')
    else:
        BuscarBDD(codigo) 

def BuscarBDD(codigo):
    result=[]
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        for row in reader:
            if row['codigo']==codigo:
                df=pd.read_csv(r'Inventario.csv',engine='python')

def BuscarPorNombre():
    df=pd.read_csv(r'Inventario.csv',engine='python')
    #df2=pd.read_csv(r'Inventario2.csv',engine='python')
    palabra=str(input('Ingrese el nombre a filtrar: '))
    print(df[df['service'].str.contains(palabra)])
    #print(df2[df2['service'].str.contains(palabra)])

def IngresarProducto():
    codigo=input('Ingrese codigo de producto a ingresar: ')
    if ExisteCodigo(codigo)=="No existe":
        print('----Error el codigo que desea eliminar no existe----')
    else:
        IngresarProductoBDD(codigo) 

def IngresarProductoBDD(codigo):
    result=[]
    print('Datos del producto') 
    BuscarBDD(codigo)
    ingresos=input('Cantidad a ingresar a bodega: ')
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        for row in reader:
            #Compara el codigo hasta encontrar lugar vacio
            if row['codigo']==codigo:
                row['codigo']=row['codigo']
                row['restrictiva']=row['restrictiva']
                row['ubicacion']=row['ubicacion']
                row['descripcion']=row['descripcion']
                row['unidad']=row['unidad']
                row['tipo']=row['tipo']
                row['familia']=row['familia']
                row['stock_minimo']=row['stock_minimo']
                row['cantidad_inicial']=row['cantidad_inicial']
                verificar=int(str(row['ingresos']))
                temp=int(str(ingresos))
                total_ingreso=0
                if verificar>0:
                    total_ingreso=verificar+temp
                    temp1=str(total_ingreso)
                    row['ingresos']=temp1
                else:
                    row['ingresos']=ingresos         
                row['egresos']=row['egresos']
                row['perdidas']=row['perdidas']
                a=int(str(row['cantidad_inicial']))
                b=int(str(row['ingresos']))
                c=int(str(row['egresos']))
                d=int(str(row['perdidas']))
                operacion=(a+b)-(c+d)
                total=int(str(operacion))
                stock=int(str(row['stock_minimo']))
                if total <= stock:
                    temp=str(total)
                    observaciones="Solicitar Material"
                    row['total']=temp
                    row['observaciones']=observaciones
                else:
                    observaciones="Stok a favor"
                    row['total']=total
                    row['observaciones']=observaciones
                row['observacion_perdida']=row['observacion_perdida']
            result.append(row)    
    with open('Inventario.csv','w')as File:
        fieldnames=['codigo','restrictiva','ubicacion','descripcion','unidad','tipo','familia','stock_minimo','cantidad_inicial'
        ,'ingresos','egresos','perdidas','total','observaciones','observacion_perdida']
        writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
        writer.writeheader()
        writer.writerows(result)
    
def SalidaDeProducto():
    codigo=input('Ingrese codigo de producto para darle salida: ')
    if ExisteCodigo(codigo)=="No existe":
        print('----Error el codigo que desea eliminar no existe----')
    else:
        SalidaProductoBDD(codigo) 

def SalidaProductoBDD(codigo):
    result=[]
    print('Datos del producto') 
    BuscarBDD(codigo)
    egresos=input('Cantidad de salida de bodega: ')
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        for row in reader:
            #Compara el codigo hasta encontrar lugar vacio
            if row['codigo']==codigo:
                row['codigo']=row['codigo']
                row['restrictiva']=row['restrictiva']
                row['ubicacion']=row['ubicacion']
                row['descripcion']=row['descripcion']
                row['unidad']=row['unidad']
                row['tipo']=row['tipo']
                row['familia']=row['familia']
                row['stock_minimo']=row['stock_minimo']
                row['cantidad_inicial']=row['cantidad_inicial']
                row['ingresos']=row['ingresos']
                verificar=int(str(row['egresos']))
                temp=int(str(egresos))
                total_egresos=0
                if verificar>0:
                    total_egresos=verificar+temp
                    temp1=str(total_egresos)
                    row['egresos']=temp1
                else:
                    row['egresos']=egresos
                row['perdidas']=row['perdidas']
                a=int(str(row['cantidad_inicial']))
                b=int(str(row['ingresos']))
                c=int(str(row['egresos']))
                d=int(str(row['perdidas']))
                operacion=(a+b)-(c+d)
                total=int(str(operacion))
                stock=int(str(row['stock_minimo']))
                if total <= stock:
                    temp=str(total)
                    observaciones="Solicitar Material"
                    row['total']=temp
                    row['observaciones']=observaciones
                else:
                    observaciones="Stok a favor"
                    row['total']=total
                    row['observaciones']=observaciones
                row['observacion_perdida']=row['observacion_perdida']
            result.append(row)    
    with open('Inventario.csv','w')as File:
        fieldnames=['codigo','restrictiva','ubicacion','descripcion','unidad','tipo','familia','stock_minimo','cantidad_inicial'
        ,'ingresos','egresos','perdidas','total','observaciones','observacion_perdida']
        writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
        writer.writeheader()
        writer.writerows(result)

def AjustePerdida():
    codigo=input('Ingrese codigo de producto perdido: ')
    if ExisteCodigo(codigo)=="No existe":
        print('----Error el codigo que desea eliminar no existe----')
    else:
        AjustePerdidaBDD(codigo) 

def AjustePerdidaBDD(codigo):
    result=[]
    contraseña=str(input('Ingrese contraseña: '))
    if contraseña == "1324":    
        print('Datos del producto')
        BuscarBDD(codigo)
        perdidas=input('Cantidad de producto perdido: ')
        observacion_perdida=input('Escriba observación de perdida: ')
        with open('Inventario.csv')as File:
            reader=csv.DictReader(File)
            for row in reader:
                #Compara el codigo hasta encontrar lugar vacio
                if row['codigo']==codigo:
                    row['codigo']=row['codigo']
                    row['restrictiva']=row['restrictiva']
                    row['ubicacion']=row['ubicacion']
                    row['descripcion']=row['descripcion']
                    row['unidad']=row['unidad']
                    row['tipo']=row['tipo']
                    row['familia']=row['familia']
                    row['stock_minimo']=row['stock_minimo']
                    row['cantidad_inicial']=row['cantidad_inicial']
                    row['ingresos']=row['ingresos']
                    row['egresos']=row['egresos']
                    verificar=int(str(row['perdidas']))
                    temp=int(str(perdidas))
                    total_perdidas=0
                    if verificar>0:
                        total_perdidas=verificar+temp
                        temp1=str(total_perdidas)
                        row['perdidas']=temp1
                    else:
                        row['perdidas']=perdidas
                    a=int(str(row['cantidad_inicial']))
                    b=int(str(row['ingresos']))
                    c=int(str(row['egresos']))
                    d=int(str(row['perdidas']))
                    operacion=(a+b)-(c+d)
                    total=int(str(operacion))
                    stock=int(str(row['stock_minimo']))
                    if total <= stock:
                        temp=str(total)
                        observaciones="Solicitar Material"
                        row['total']=temp
                        row['observaciones']=observaciones
                    else:
                        observaciones="Stok a favor"
                        row['total']=total
                        row['observaciones']=observaciones
                    if row['observacion_perdida']=="Vacio":
                        row['observacion_perdida']=observacion_perdida
                    else:
                        row['observacion_perdida']=row['observacion_perdida']+","+observacion_perdida
                result.append(row)    
        with open('Inventario.csv','w')as File:
            fieldnames=['codigo','restrictiva','ubicacion','descripcion','unidad','tipo','familia','stock_minimo','cantidad_inicial'
            ,'ingresos','egresos','perdidas','total','observaciones','observacion_perdida']
            writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
            writer.writeheader()
            writer.writerows(result)
    else:
        print('Contraseña incorrecta')

def ReporteStockMinimo():
    df=pd.read_csv(r'Inventario.csv',engine='python')
    print(df[df['observaciones'].str.contains("Solicitar Material")])

def ReporteInventarioTotal():
    df=pd.read_csv(r'Inventario.csv',engine='python')
    ord=df.sort_values(by=['ubicacion'])[['ubicacion','tipo','familia']]
    print(ord)

def ReporteParcialStock():
    df=pd.read_csv(r'Inventario.csv',engine='python')
    print(df[df['observaciones'].str.contains("Stok a favor")])

def RellenarEspacios():
    codigo=input('Ingrese codigo de producto a rellenar: ')
    if ExisteCodigo(codigo)=="No existe":
        print('----Error el codigo que desea eliminar no existe----')
    else:
        RellenarEspaciosBDD(codigo) 

def RellenarEspaciosBDD(codigo):
    result=[]
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        restrictiva="N"
        ubicacion="Vacio"
        descripcion="Vacio"
        unidad="Vacio"
        tipo="Vacio"
        familia="Vacio"
        stock_minimo="0"
        cantidad_inicial="0"
        ingresos="0"
        egresos="0"
        perdidas="0"
        total="0"
        observaciones="Vacio"
        observaciones_perdida="Vacio"
        for row in reader:
            #Compara el codigo hasta encontrar lugar vacio
            if row['codigo']==codigo:
                row['codigo']=row['codigo']
                if row['restrictiva'] =="":
                    row['restrictiva']=restrictiva
                else:
                    row['restrictiva']=row['restrictiva']
                
                if row['ubicacion'] =="":
                    row['ubicacion']=ubicacion
                else:
                    row['ubicacion']=row['ubicacion']
                
                if row['descripcion']=="":
                    row['descripcion']=descripcion
                else:
                    row['descripcion']=row['descripcion']
                
                if row['unidad']=="":
                    row['unidad']=unidad
                else:
                    row['unidad']=row['unidad']
                
                if row['tipo']=="":
                    row['tipo']=tipo
                else: 
                    row['tipo']=row['tipo']
                
                if row['familia']=="":
                    row['familia']=familia
                else: 
                    row['familia']=row['familia']
                
                if row['stock_minimo']=="":
                    row['stock_minimo']=stock_minimo
                else:
                    row['stock_minimo']=row['stock_minimo']
                
                if row['cantidad_inicial']=="":
                    row['cantidad_inicial']=cantidad_inicial
                else:
                    row['cantidad_inicial']=row['cantidad_inicial']
                
                if row['ingresos']=="":
                    row['ingresos']=ingresos
                else: 
                    row['ingresos']
                
                if row['egresos']=="":
                    row['egresos']=egresos
                else:
                    row['egresos']=row['egresos']
                
                if row['perdidas']=="":
                    row['perdidas']=perdidas
                else: 
                    row['perdidas']=row['perdidas']
                
                if row['total']=="":
                    row['total']=total
                else:
                    row['total']=row['total']
                
                if row['observaciones']=="":
                    row['observaciones']=observaciones
                else:
                    row['observaciones']=row['observaciones']
                
                if row['observacion_perdida']=="":
                    row['observacion_perdida']=observaciones_perdida
                else: 
                    row['observacion_perdida']=row['observacion_perdida']
            result.append(row)
        
    with open('Inventario.csv','w')as File:
        fieldnames=['codigo','restrictiva','ubicacion','descripcion','unidad','tipo','familia','stock_minimo','cantidad_inicial'
        ,'ingresos','egresos','perdidas','total','observaciones','observacion_perdida']
        writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
        writer.writeheader()
        writer.writerows(result)
        
        


def main():
    while True:
        validate()
        show()
        option=menu()
        if option == '1':
            VerInventario()
        elif option == '2':
            ProductoNuevo()
        elif option == '3':
            ModificarProducto()
        elif option == '4':
            EliminarProducto()
        elif option == '5':
            BuscarProducto()
        elif option == '6':
            BuscarPorNombre()
        elif option == '7':
            IngresarProducto()
        elif option == '8':
            SalidaDeProducto()
        elif option == '9':
            AjustePerdida()
        elif option == '10':
            ReporteStockMinimo()
        elif option == '11':
            ReporteInventarioTotal()
        elif option == '12':
            ReporteParcialStock()
        elif option == '13':
            RellenarEspacios()
        elif option == 'show':
            img()
        elif option == 'mexico':
            mexico()
        elif option == 'lenguaje':
            lenguaje()
        elif option == 'exit':
            break
    return

main()


