import serial
import openpyxl
from datetime import datetime
import SQL
import  PrinterConnect
import logging

# Setting up info logger.
LoggerInfo=logging.getLogger('DATA INFO LOGGER')
handler=logging.FileHandler('InfoFile.log')
format=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setLevel(logging.INFO)
handler.setFormatter(format)
LoggerInfo.addHandler(handler)

#Setting up error logger
LoggerError=logging.getLogger('ERROR LOGGER')
handler1=logging.FileHandler('ErrorFile.log')
format1=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler1.setLevel(logging.ERROR)
handler1.setFormatter(format1)
LoggerInfo.addHandler(handler1)

#Setting scale port function parameters
def Auto(ScalePort,PrinterPort,id):
    Department_list={
    0:"Transport Material and Handling",
    1:"Logistics"
}

    Material_list={
        0:"PetCoke",
        1:"Alumina",
        2:"Waste",
        3:"Scraps",
        4:"LPG",
        5:"RFO",
        6:"Diesel",
        7:"Burnoffs",
        8:"Exporting other materials"
    }

    ConnectScale= serial.Serial(port=ScalePort,baudrate=9600,timeout=2)
    if id==1 and ConnectScale.is_open:
        
        print("Connection established")
        #Check to see if the COM6 port is open, if true then code the while loop will run
        while ConnectScale.is_open:

            SerialData=ConnectScale.read(120)
            if len(SerialData)>5:
                InputD=SerialData.decode().splitlines()
                print(InputD)
                dataSize=len(SerialData)
                LoggerInfo.info("Streaming Data Size:%s",SerialData)
                
                #error handling for list indexes should be hear, print something
                if len(InputD)<6:
                    Mode='No mode'
                    LoggerError.error("%s: Data length not reach, missing data",InputD)
                    Message='Error with Passed data, please try again'
                    Format=Message.encode()
                    SetPrinterIn=PrinterConnect.Printer(PrinterPort,True,Format)
                    return Mode
            
                #WeighIn Mode
                if dataSize >1 and dataSize <90:
                    #set weigh in mode 
                    printerDataIn=SerialData
                    Gross=""
                    Mode="WEIGH IN"
                    print("Weigh In")
            
                    for item in range(len(InputD)+1):
                        match item:
                            case 1:
                                TruckId=InputD[item][11:]# ID inputted into scale
                                E_ID=TruckId[0:5]#Employee ID
                                B_ID=TruckId[5:11]#Badge number
                                D_ID=TruckId[11:12]#ID of department
                                M_ID=TruckId[12:13]#ID of material being weighed
                                department=Department_list[int(D_ID)]
                                material=Material_list[int(M_ID)]

                            case 3:
                                start=InputD[item]

                                for letter in range(len(start)):
                                    word=str(start[letter])
                                    search=word.isnumeric()

                                    if search:
                                        Gross+=word

                            case 5:
                                Date=datetime.strptime(InputD[item][0:7],"%m/%d/%Y").date()
                                Time=datetime.strptime(InputD[item][8:],"%I:%M%p").time()

                    ExData=[E_ID,B_ID,department,material,Gross,Date,Time]
                    LoggerInfo.info("Mode:%s",Mode)
                    LoggerInfo.info("SQL DATA:%s",ExData)
                    
                    SetSQL=SQL.SQL_IN(ExData)
                    SetPrinterIn=PrinterConnect.Printer(PrinterPort,True,printerDataIn)
                    print(TruckId)
                    print(Gross)
                    print(Date)
                    print(Time)
                    return Mode
                
                #WeigghOut Mode
                elif dataSize>100:
                    #set weighout mode
                    printerDataOut=SerialData
                    print("Weigh Out")
                    Gross=""
                    Net=""
                    Tare=""
                    Mode="WEIGH OUT"
                    for item in range(len(InputD)+1):
        
                        match item:
                            case 0:
                                TruckId=InputD[item][10:]
                                E_ID=TruckId[0:5]#Employee ID
                                B_ID=TruckId[5:11]#Badge number
                                D_ID=TruckId[11:12]#ID of department
                                M_ID=TruckId[12:13]#ID of material being weighed
                                department=Department_list[int(D_ID)]
                                material=Material_list[int(M_ID)]    
                            
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
                                Date=datetime.strptime(InputD[item][0:7],"%m/%d/%Y").date()
                                Time=datetime.strptime(InputD[item][8:],"%I:%M%p").time()
                    
                    ExData=[E_ID,B_ID,department,material,Gross,Tare,Net,Date,Time]
                    LoggerInfo.info("Mode:%s",Mode)
                    LoggerInfo.info("SQL DATA:%s",ExData)
                    SetSQL=SQL.SQL_OUT(ExData)
                    SetPrinterOut=PrinterConnect.Printer(PrinterPort,True,printerDataOut)

                    print(TruckId)
                    print(Gross)
                    print(Tare)
                    print(Net)
                    print(Date)
                    print(Time)

                    return Mode

            
        
            # Remove all data in the read buffer
            ConnectScale.reset_input_buffer() 

    #Close Scale and Excel file
    ConnectScale.close










