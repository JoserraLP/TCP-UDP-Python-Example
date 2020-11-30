import socket

# Creamos un socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Definimos el puerto del servidor
port = 22222  

# Conexión del socket al puerto
s.bind(('',port))


while True:

    # Obtener la información
    data, addr = s.recvfrom(1024)
    data = data.decode()
    # Mostrar la información
    print('Address:', addr,'Data:', data)

    # Crear una lista 
    mylist = list(data.split(':'))
    intlist = list()

    # Insertar la información en una lista
    for i in range(0, len(mylist)):
        intlist.append(int(mylist[i]))
    
    # Ordenar la lista al revés
    intlist.sort(reverse=True)

    # Enviar la información al cliente
    s.sendto(str(intlist).encode(), addr)