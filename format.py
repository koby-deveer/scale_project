
ScaleFormat=" \r\nTruck ID  7412580963\r\n\r\nGross       10 kg\r\n\r\n03:24AM 08/03/2023\r\n"
Bytes= b'Truck ID  1111\r\n\r\nGross       20 kg \r\nTare        10 kg RECALLED\r\nNet         10 kg\r\n\r\n09:30AM 09/08/2023\r\n'
D=Bytes.decode()
Info=D.splitlines()
#print(Info[0][10:])
#print(len(Info[0][10:]))

print(len(ScaleFormat))
print(len(Bytes))
IDs=ScaleFormat[3:22]
Weight=ScaleFormat[27:41]
Date=ScaleFormat[48:66]

#print(IDs)
#print(Weight)
#print(Date)

I=IDs[10:19]
W=Weight[12:]
D=Date[8:]
T=Date[0:8]
#print(I)
#print(W)
#print(D)
#print(T)