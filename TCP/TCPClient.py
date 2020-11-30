import sys
import socket              
 
# Obtener los parámetros de ejecución
arglen = len(sys.argv)

# Comprobar número de parametros
if arglen < 3:
    print('please run as python TCPClient.py <ip_address> <numbers>')
    exit()

# Obtener los números indicados por parámetros
data = str()
data = data+str(sys.argv[2])

for i in range(3,arglen):
    data = data+':'+str(sys.argv[i])

# Creamos un socket
s = socket.socket()        
 
# Definimos el puerto de conexión
port = 11111          
 
# Conexión al servidor
s.connect((sys.argv[1], port))

# Enviar la información
s.send(data.encode())

# Mostrar la información devuelta por el servidor
print(s.recv(1024).decode())

# Cerrar la conexión
s.close()