import serial
from datetime import date, time, datetime

#Setting up com port settings
ScaleConnecT= serial.Serial(port="COM6",baudrate=9600,timeout=1)

Check=ScaleConnecT.is_open
InputD=[]
while Check:
    #Check coneection
    #Read Data1
    #RealData=ScaleConnecT.readline()
    
    SerialData=ScaleConnecT.read(110)
    if len(SerialData)>5:
        InputD=SerialData.decode().splitlines()
        print(InputD)
        dataSize=len(SerialData)
        
        #WeighIn Mode
        if dataSize >1 and dataSize <90:
            #set weigh in mode function
            Gross=""

            for item in range(len(InputD)+1):
                match item:
                    case 1:
                        TruckId=InputD[item][11:]

                    case 3:
                        start=InputD[item]

                        for letter in range(len(start)):
                            word=str(start[letter])
                            search=word.isnumeric()

                            if search:
                                Gross+=word

                    case 5:
                        Date=InputD[item][0:7]
                        Time=InputD[item][8:]
            
            print(TruckId)
            print(Gross)
            print(Date)
            print(Time)

        #WeigghOut Mode
        elif dataSize>100:
            #set weighout mode
            Gross=""
            Net=""
            Tare=""
            for item in range(len(InputD)+1):
 
                match item:
                    case 0:
                        TruckId=InputD[item][10:]    
                    
                    case 2:
                        start=InputD[item]

                        for letter in range(len(start)):
                            word=str(start[letter])
                            #print(middle)
                            search=word.isnumeric()
                            if search:
                                Gross+=word

                    case 3:
                        start=InputD[item]

                        for letter in range(len(start)):
                            word=str(start[letter])
                            #print(middle)
                            search=word.isnumeric()
                            if search:
                                Tare+=word
                    
                    case 4:
                        start=InputD[item]

                        for letter in range(len(start)):
                            word=str(start[letter])
                            #print(middle)
                            search=word.isnumeric()
                            if search:
                                Net+=word
                    
                    case 6:
                        Date=InputD[item][0:7]
                        Time=InputD[item][8:]
            print(TruckId)
            print(Gross)
            print(Tare)
            print(Net)
            print(Date)
            print(Time)

    
    

ScaleConnecT.close        


#Input=InputData.join(SerialData)
    #InputData.append(SerialData)
    #Input=SerialData.splitlines()
    #print(len(InputData))
    #print(type(InputData))
    #RealData=ScaleConnecT.read().decode()
   
    #print(len(RealData))
    #Ids=RealData[1][11:]
    #print(Ids)
    #Weight=RealData[3][12:14]
    #print(Weight)
    #Time=RealData[5][0:8]
    #print(Time)
    #Dates=date.today()
    
    #print(Dates)