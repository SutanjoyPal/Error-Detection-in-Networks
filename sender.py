import socket
from packet import Packet
import pickle
from fileIO import read_input_file,prepare_datawords
from checksum import calculate_checksum
from crc import mod2div,CRC_10_POLY,CRC_16_POLY,CRC_32_POLY,CRC_8_POLY
from error import inject_single_error,inject_double_error,inject_burst_error

client=socket.socket()

SERVER_PORT = 4321
client.connect(('localhost',SERVER_PORT))

serverMsg = client.recv(1024).decode('utf-8')
print(f"Message from receiver: {serverMsg}")


server_address = client.getpeername()
client_address = client.getsockname()

#STOP & WAIT to send packets
filename = input("Enter input filename: ")
data = read_input_file(filename)

datawords = prepare_datawords(data,16)

#print(calculate_checksum(data))
datawords.append(calculate_checksum(data))
datawords.append("-1") 
#data = ['0010101','0101010101','1111111111','001','1010110010101','-1']
appended_data = data + '0'*(len(CRC_10_POLY)-1)
crc = mod2div(appended_data, CRC_10_POLY)

datawordsList = []
datawordsList.append(datawords)
#datawords = prepare_datawords(inject_single_error(data),16)
# datawordsList.append(datawords)
#datawords = prepare_datawords(inject_double_error(data),16)
# datawordsList.append(datawords)
#datawords = prepare_datawords(inject_burst_error(data,20),16)
# datawordsList.append(datawords)

seq = 0
for packet in datawords:
    seq = seq+1
    curPacket = Packet(client_address,server_address,seq,packet,crc)
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


