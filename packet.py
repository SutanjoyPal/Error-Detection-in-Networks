
class Packet:
    def __init__(self, srcAddress, dstAddress,seqNumber,data,crcRemainder):
        self.srcAddress = srcAddress
        self.dstAddress = dstAddress
        self.seqNumber = seqNumber
        self.data = data
        self.crcRemainder = crcRemainder
    
    def displayPacket(self):
        print(f"    Source Address: {self.srcAddress}")
        print(f"    Destination Address: {self.dstAddress}")
        print(f"    Sequence Number: {self.seqNumber}")
        print(f"    Data: {self.data}")