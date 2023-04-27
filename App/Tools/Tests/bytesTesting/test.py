






# message = "blablabla"
# print("Message = ", message, "; Message Length = ", len(message))
# byteMessage = bytes(message, "utf-8")
# messageLength = len(byteMessage)
# header = bytes([messageLength])

# header = header + bytes(8-len(header))
# print("Header = ",header, "; Header Lenght = ", len(header))

# print("Header/Message Size = ",int.from_bytes(header, "little"))

import socket 
import pickle

print("===== [CLIENT] =====")
msg = "Hello éôÄþ aka Alien Name"
byteMsg = pickle.dumps(msg)
print("String Msg = ", msg, "; Len of String = ", len(msg))
print("Byte Msg = ", byteMsg, "; Len of Byte", len(byteMsg))

header = bytes([len(byteMsg)])
print("Byte Header = ", header)
header = header + bytes(8-len(header))
print("Byte Header = ", header, "; Byte Header Length = ", len(header))

data = header + byteMsg
print("Byte Data = ", data, "; Byte Data Length =", len(data))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 60000))
s.sendall(data)

