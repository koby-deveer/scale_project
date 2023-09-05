import serial
from datetime import date, time, datetime

#Setting up com port settings
ScaleConnecT= serial.Serial(port="COM6",baudrate=9600,timeout=100)

Check=ScaleConnecT.is_open

#Check coneection

while Check:

    #Read Data
    #RealData=ScaleConnecT.readline().decode().splitlines()
    #SerialData=ScaleConnecT.read(60)
    RealData=ScaleConnecT.read(60).decode().splitlines()
    #print(RealData)
    #print(len(RealData))
    #Ids=RealData[1][11:]
    #print(Ids)
    Weight=RealData[3][12:14]
    print(Weight)
    Time=RealData[5][0:8]
    print(Time)
    Dates=date.today()
    print(Dates)
ScaleConnecT.close    








    

