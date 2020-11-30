import socket              
 

# Creamos un socket
s = socket.socket()

# Definimos el puerto del servidor
port = 11111  
             
# Conexión del socket al puerto
s.bind(('', port))        
 
# Se definen el número máximo de peticiones no aceptadas
s.listen(5)  
               
while True:
    # Aceptar la información del socket
    c, addr = s.accept()
    # Obtener la información
    data = c.recv(1024).decode()   
    # Mostrar la información
    print('Address:',addr,'Data:',data)
    
    # Crear una lista 
    mylist = list(data.split(':'))
    intlist = list()

    # Insertar la información en una lista
    for i in range(0, len(mylist)):
        intlist.append(int(mylist[i]))
    
    # Ordenar la lista
    intlist.sort()

    # Enviar la información al cliente
    c.send(str(intlist).encode())

    # Cerrar la conexión
    c.close()