import serial
from datetime import date, time, datetime

#Setting up com port settings
PrintConnecT= serial.Serial(port="COM5",baudrate=9600,timeout=1)

Check=PrintConnecT.is_open

#Check coneection

def Printer(PrintInfo, Data):
    if Check:
        ScaleFormat=Data
        if PrintInfo==True:
            PrintConnecT.write(ScaleFormat)

PrintConnecT.close    








    

