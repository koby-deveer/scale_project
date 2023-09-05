import serial
import openpyxl
from datetime import date,datetime
import SQL
import  PrinterConnect

#Setting scale port parameters
ConnectScale= serial.Serial(port='COM6',baudrate=9600,timeout=100)

#Opening Excel workbook
Scale_Data=openpyxl.load_workbook(r"C:\Users\Kody\Desktop\VALCO\Valco\Scale\Scale project\Scale_Data.xlsx")

#Getting the active sheet
DataSheet=Scale_Data.active

# Iterate over rows in order to most recently filled row
for row in DataSheet.iter_rows():
    # Get the current row index
    row_index = row[0].row

    # Do something with the row index
    print(f"Current row index: {row_index}")

# Since the code above provides the number of the last formatted row, we add one in order to add data to a new row
count=row_index+1

#Check to see if the COM6 port is open, if true then code the while loop will run
while ConnectScale.is_open:

    #Retrieve data coming from Scale on port COM6
    RealData=ConnectScale.read(60).decode()
    #RealData=ScaleConnecT.readline().decode()
    #printerData=ConnectScale.read(60).decode()
    printerData=RealData
    #If the size of real data is above 60, take from the extract the ID, Weight and Date
    if len(RealData)>=50:
        RealData=RealData.splitlines()
        Ids=RealData[1][11:]
        print(Ids)
        Weight=RealData[3][12:]
        print(Weight)
        Time=RealData[5][0:8]
        print(Time)
        Dates=date.today()
        ExDate=Dates.strftime("%d/%m/%Y")
        print(Dates)

        ExData=[Ids,Weight,Time,ExDate]

        #For loop to add to the new row and columns
        for column in range(1,5,1):
            rows=count
            DataSheet.cell(rows,column).value=ExData[column-1]
        count+=1

        # Save the data added
        Scale_Data.save(r"C:\Users\Kody\Desktop\VALCO\Valco\Scale\Scale project\Scale_Data.xlsx")

        SetSQL=SQL.SQL(ExData)
        SetPrinter=PrinterConnect.Printer(True,printerData)
    
        # Remove all data in the read buffer
        ConnectScale.reset_input_buffer()

#Close Scale and Excel file
ConnectScale.close
Scale_Data.close()









