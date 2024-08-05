import socket
import pickle
from packet import Packet
from checksum import verify_checksum

server = socket.socket()

PORT = 4321
server.bind(('localhost',PORT))

noOfClients = 5
server.listen(noOfClients)
print(f"Server listening on {PORT} to at max {noOfClients} Clients")

while True:
    clientsocket, addr = server.accept()
    print(f"Connection from {addr} has been established.")
    
    clientsocket.send(bytes("You are connected to receiver! Please send the packets", 'utf-8'))
        
    codewords = []
    while True:
        #clientData = clientsocket #.recv(8192) #.decode('utf-8')
        #packetData = pickle.loads(clientData)



        # Buffer to accumulate incoming data
        buffer = b""
        while True:
            chunk = clientsocket.recv(4096)
            if not chunk:
                break
            buffer += chunk
            # Check if the buffer contains a complete packet
            try:
                packetData = pickle.loads(buffer)
                break
            except (pickle.UnpicklingError, EOFError):
                continue

        # If no data is received, break the loop
        if not buffer:
            break



        clientsocket.send(bytes('ACK', "utf-8"))
        
        if packetData.data == "-1":
            break
        codewords.append(packetData.data)
        #print(f"Received from Sender{addr}: {clientData}")
        print(f"Received from Sender {addr}")
        packetData.displayPacket()
        
    codewords_string = ''.join(codewords)    
    if verify_checksum(codewords_string):
        print("Received data is correct as per checksum.")
    else:
        print("Received data has some error as per checksum.")    
    clientsocket.close()
