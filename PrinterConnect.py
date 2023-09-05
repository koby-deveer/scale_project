import serial
from datetime import date, time, datetime

#Setting up com port settings
ScaleConnecT= serial.Serial(port="COM5",baudrate=9600,timeout=100)

Check=ScaleConnecT.is_open

#Check coneection

def Printer(PrintInfo, Data):
    if Check:
        ScaleFormat=Data
        BytesInfo=ScaleFormat.encode()
        if PrintInfo==True:
            ScaleConnecT.write(BytesInfo)

ScaleConnecT.close    








    

