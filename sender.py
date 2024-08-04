import socket
from packet import Packet
import pickle

client=socket.socket()

SERVER_PORT = 4321
client.connect(('localhost',SERVER_PORT))

serverMsg = client.recv(1024).decode('utf-8')
print(f"Message from receiver: {serverMsg}")


server_address = client.getpeername()
client_address = client.getsockname()

#STOP & WAIT to send packets
data = ['0010101','0101010101','1111111111','001','1010110010101','-1']

seq = 0
for packet in data:
    seq = seq+1
    curPacket = Packet(client_address,server_address,seq,packet)
    #curPacket.displayPacket()
    pickledCurPacket = pickle.dumps(curPacket)
    while True:
        #client.send(packet.encode('utf-8'))
        client.send(pickledCurPacket)
        acknowledgement = client.recv(8192).decode('utf-8')
        print(f"Response from Receiver {server_address}: {acknowledgement}")
        if acknowledgement == 'ACK':
            break



client.close()