import socket
import pickle

class Socket:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def encodeInt(self, integer):
        """Max Integer Size = 65535 | Encoded on two bytes - little"""
        return integer.to_bytes(2, 'little')

    def decodeInt(self, integer):
        return int.from_bytes(integer, "little")

    def encodeObj(self, obj):
        return pickle.dumps(obj)

    def decodeObj(self, obj):
        return pickle.loads(obj)

    def generateHeader(self, data):
        """
        Generate a 5 bytes header containing size of data in bytes 
        Parameters:
        data is awaited to be encoded in bytes already
        type has to be an integer (max 65535)
        """
        dataLength = self.encodeInt(len(data))

        # Generates 5 - length of header empty bytes to keep header size constant to 5
        header = dataLength + bytes(2-len(dataLength))
        return header

    def send(self, socket, data):
        encodedData = self.encodeObj(data)
        encodedHeader = self.generateHeader(encodedData)
        finalPacket = encodedHeader + encodedData
        socket.sendall(finalPacket)

    def recv(self, socket):
        data = None
        encodedHeader = socket.recv(2)
    
        header = self.decodeInt(encodedHeader)
        encodedData = socket.recv(header)
        data = self.decodeObj(encodedData)
        
        return data