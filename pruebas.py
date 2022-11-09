
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

eleccion=input("Teclea las acciones realizar en el quipo \n 1.-Cambiar el nombre del dispositivo \n 2.-Asignar una ip ")
if eleccion =="1":
    tn.write(b"config terminal\n")
    nombre=input("Teclea el valor del nombre: ")
    tn.write(b"host " + nombre.encode('utf-8') + b" \n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
elif eleccion == "2":
    print(tn)
    tn.write(b"show ip route \n")
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
    tn.write(b"show running-config view full \n ")
    tn.write(b"\n")  
    tn.write(b"exit \n") 
    print(tn.read_all().decode('ascii'))


print(tn.read_all().decode('ascii'))

