import socket
import sys

# Obtener los parámetros de ejecución
arglen = len(sys.argv)

# Comprobar número de parametros
if arglen < 3:
    print('please run as python UDPClient.py <ip_address> <numbers>')
    exit()

# Obtener los números indicados por parámetros
data = str()
data = data+sys.argv[2]

for i in range(3,len(sys.argv)):
    data = data+':'+sys.argv[i]

# Creamos el socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Definimos el puerto del servidor
port = 22222

# Obtener la dirección indicada por parámetros
addr = sys.argv[1]

# Enviar la información por el socket
s.sendto(data.encode(),(addr,port))

# Obtener la información del servidor
data, addr = s.recvfrom(1024)

# Mostrar la información
print('Address:',addr,'Data:',data.decode())