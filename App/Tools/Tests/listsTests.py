a = [1,2,3]
b = [1,2,3,4,5,6,7,8,9,10]

c = a + b[:2]
a += b
b = b[2:]
print("A =", a)
print("B =", b)
print("C=",c)

