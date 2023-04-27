a = 5
b = 255
c = 1024
d = 65535
e = 65536
print("a = ", a, "; a in bytes = ",a.to_bytes(3, 'little'))
print("b = ", b,"; b in bytes = ",b.to_bytes(3, 'little'))
print("c = ", c,"; c in bytes = ",c.to_bytes(3, 'little'))
print("d = ", d,"; d in bytes = ",d.to_bytes(3, 'little'))
print("e = ", e,"; e in bytes = ",e.to_bytes(4, 'little'))