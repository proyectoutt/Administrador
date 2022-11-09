
import getpass
import telnetlib

HOST = input ("Teclea el valor de la direccion del dispositivo: ")
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
eleccion=input("""Teclea la accion a realizar
                  1.-Cambiar el nombre del archivo
                  2.-Asignar una ip a una interfaz
                  3.-Mostrar la configuracion actual del dispositivo 
                  4.-Crear una Vlan y Asignar una ip
                  5.-Guardar los cambios  
                  """)
if eleccion =="1":
    tn.write(b"config terminal\n")
    nombre=input("Teclea el valor del nombre: ")
    tn.write(b"host " + nombre.encode('utf-8') + b" \n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
elif eleccion == "2":
    print(tn)
    tn.write(b"show ip interface brief \n")
    tn.write(b"\n")
    tn.write(b"\n")
    tn.write(b"exit \n") 
    print(tn.read_all().decode('ascii'))
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    interfaz=input("Escribe la interfaz a utilizar: ")
    direccion=input("Escribe la direccion ip a implementar junto con su mascara de red separados por un espacio: ")
    tn.write(b"configure terminal\n ")
    tn.write(b"interfa "+ interfaz.encode('utf-8') + b"\n ")
    tn.write(b"ip address "+ direccion.encode('utf-8') + b"\n ")
    tn.write(b"no shutdown \n") 
    tn.write(b"end\n")  
    tn.write(b"exit \n") 
    print(tn.read_all().decode('ascii'))
elif eleccion == "3":
    print(tn)
    tn.write(b"show running-config view full \n")
    tn.write(b"\n")
    tn.write(b"\n")
    tn.write(b"exit \n") 
    print(tn.read_all().decode('ascii'))
elif eleccion == "4":
    print(tn)
    tn.write(b"show vlan \n")
    tn.write(b"\n")
    tn.write(b"\n")
    tn.write(b"exit \n") 
    print(tn.read_all().decode('ascii'))
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    numero=input("Escribe el numero de la Vlan: ")
    nombre=input("Escribe el  nombre de la vlan: ")
    direccion=input("Escribe la direccion ip a implementar junto con su mascara de red separados por un espacio")
    tn.write(b"configure terminal\n ")
    tn.write(b"vlan "+ numero('utf-8') + b"\n ")
    tn.write(b"vlan "+ nombre('utf-8') + b"\n ")
    tn.write(b"interface vlan "+ numero('utf-8') + b"\n ")
    tn.write(b"ip address "+ direccion.encode('utf-8') + b"\n ")
    tn.write(b"no shutdown \n") 
    tn.write(b"end\n")  
    tn.write(b"exit \n") 
    tn.write(b"show vlan \n")
    tn.write(b"\n")
    tn.write(b"\n")
    tn.write(b"exit \n") 
    print(tn.read_all().decode('ascii'))
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    modo=input("Escribe la interfaz a utilizar la Vlan : ")
    interfaz=input("Teclea el modo a utilizar en la interfaz: ")
    tn.write(b"configure terminal\n ")
    tn.write(b"interfa "+ interfaz.encode('utf-8') + b"\n ")
    tn.write(b"switchport mode "+ modo.encode('utf-8') + b"\n ")
    

    print(tn.read_all().decode('ascii'))



#print(tn.read_all().decode('ascii'))

