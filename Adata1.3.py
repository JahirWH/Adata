import csv
import os
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from time import sleep
import getpass
import random 
from datetime import date
from datetime import datetime
from cryptography.fernet import Fernet

#import tk
#import tkinter
#from tkinter import ttk

today = date.today()

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

    

#Problema de logica al hacer un bucle de desincryptacion

def validate():
    while True:
        password = getpass.getpass("Introduce tu contraseña: ")
        if password =="1656":
            break

        elif password !="1656!":
                clearConsole()
                print("┌─┐┌─┐┌─┐┌─┐┬ ┬┌─┐┬─┐┌┬┐   ┬┌┐┌┌─┐┌─┐┬─┐┬─┐┌─┐┌─┐┌┬┐")  
                print("├─┘├─┤└─┐└─┐││││ │├┬┘ ││   │││││  │ │├┬┘├┬┘├┤ │   │ ")  
                print("┴  ┴ ┴└─┘└─┘└┴┘└─┘┴└──┴┘   ┴┘└┘└─┘└─┘┴└─┴└─└─┘└─┘ ┴ ")

    
#encryptacion automatica al cerrar el programa


def encrypted():
    key = Fernet.generate_key()
      
    with open('key.key', 'wb') as filekey:
       filekey.write(key)
       
      
    fernet = Fernet(key) 
      
    with open('inventario.csv', 'rb') as file: 
        original = file.read() 
          
    encrypted = fernet.encrypt(original) 
    with open('inventario.csv', 'rb') as file: 
        original = file.read()

      
    with open('inventario.csv', 'wb') as encrypted_file: 
        encrypted_file.write(encrypted) 

#desencrptacion automatica al introducior la contraseña correcta
def decrypted():
    key = Fernet.generate_key()
      
    with open('key.key', 'rb') as filekey: 
        key = filekey.read() 
      
    fernet = Fernet(key) 
      
    with open('inventario.csv', 'rb') as enc_file: 
        encrypted = enc_file.read() 
      
    decrypted = fernet.decrypt(encrypted)
    
      
    with open('inventario.csv', 'wb') as dec_file:
        dec_file.write(decrypted) 
      

def menu():

    print("******MENU INVENTARIO******")
    print("1.Ver invetario")
    print("2.Agregar contraseña")
    print("3.Modificar Contraseña")
    print("4.Buscar por nombre ")
    print("5.Encryptar base de datos")
    print("6.Desencryptar")


    option=input("Introduzca el número de la opción deseada: ")
    return option

def ExisteCodigo(codigo):
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        for row in reader:
            if(codigo==row['codigo']):
                return row
        return "No existe"







def acert():

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

def VerInventario():
    
    df=pd.read_csv(r'Inventario.csv',engine='python')
    print(df)
    #df2=pd.read_csv(r'Inventario2.csv',engine='python')
    #print(df2)
    return




def ProductoNuevo():
    
    from random import randint
    lista = []
    for x in range(2):
        lista.append(str(randint(0,9)))
        #lista.append(str(a)) #Estas 2 líneas se pueden juntar en: lista.append(str(randint(0,9)))

    codigo = ''
    for x in range(2):
        codigo = codigo + lista[x]
        codigo_int = int(codigo)

        today = str(date.today())

        
    if ExisteCodigo(codigo)=="No existe":
        ubicacion=input('Name Service: ')
        descripcion=input('Email ')
        unidad=input('Password ')
        tipo=input(' Username ?: ')
        familia=input('Web: ')
        fecha=today


        with open ('Inventario.csv','a')as File:
            File.write('\n'+codigo+','+ubicacion+','+descripcion+','
            +unidad+','+tipo+','+familia+','+fecha)


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
        fecha=today
        modificarBDD(codigo,ubicacion,descripcion,unidad,tipo,familia,fecha)

def modificarBDD(codigo,ubicacion,descripcion,unidad,tipo,familia,fecha):
    result=[]
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        for row in reader:
            #Compara el codigo hasta encontrar lugar vacio
            if row['codigo']==codigo:
                row['codigo']=codigo
                row['service']=ubicacion
                row['email']=descripcion
                row['password']=unidad
                row['username']=tipo
                row['web']=familia
                row['fecha']=fecha
            
            result.append(row)
        
    with open('Inventario.csv','w')as File:
        fieldnames=['codigo','service','email','password','username','web','fecha']
        writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
        writer.writeheader()
        writer.writerows(result)
    

def BuscarPorNombre():
    df=pd.read_csv(r'Inventario.csv',engine='python')
    #df2=pd.read_csv(r'Inventario2.csv',engine='python')
    palabra=str(input('Ingrese el nombre a filtrar: '))
    #print("Codigos con la palabra  "+ (palabra))
    #print(df[df['codigo'].str.contains(palabra)])
    print("Servicios con la palabra  "+ (palabra))
    print(df[df['service'].str.contains(palabra)])
    print("Emails con la palabra  "+ (palabra))
    print(df[df['email'].str.contains(palabra)])
    print("Contraseñas con la palabra  "+ (palabra))
    print(df[df['password'].str.contains(palabra)])
    print("Usuarios con la palabra  "+ (palabra))
    print(df[df['username'].str.contains(palabra)])
    print("Webs con la palabra  "+ (palabra))
    print(df[df['web'].str.contains(palabra)])
    #print(df2[df2['service'].str.contains(palabra)])


#soluconar logica para encryptarb sin que se vuelva un bucle

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
            BuscarPorNombre()
        elif option == 'show':
            img()
        elif option == 'lenguaje':
            lenguaje()
        elif option == 'acertijos':
            acert()
        elif option == '5':
            encrypted()
            print("El archivo se encrypto con exito")
        elif option == '6':
            decrypted()
            print("El archivo se desencrypto correctamente")
        elif option == 'exit':
            print("No olvides encryptar tu base de datos antes de salir")
            confor=input("Si ya lo hiciste preciona enter si no preciona 1: ")
            if confor=='1':
                encrypted()
            elif confor!='1':
                print("Saliendo...")
                break
            break
    return

main()


