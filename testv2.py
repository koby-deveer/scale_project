import SQL


TruckID=""
listing=['', 'Truck ID   1111111111', '', 'Gross       10 kg', '', '08:54AM 09/13/2023']
listing1=['Truck ID  1111111111', '', 'Gross       40 kg ', 'Tare        10 kg RECALLED', 'Net         30 kg', '', '08:54AM 09/13/2023']
stop1=""
stop2=""
stop3=""
for item in range(len(listing1)+1):
 
    match item:
        case 0:
            TruckID=listing1[item][10:]    
        
        case 2:
            start=listing1[item]

            for letter in range(len(start)):
                middle=str(start[letter])
                #print(middle)
                Test=middle.isnumeric()
                if Test:
                    stop1+=middle

        case 3:
            start1=listing1[item]

            for letter in range(len(start1)):
                middle1=str(start1[letter])
                #print(middle)
                Test1=middle1.isnumeric()
                if Test1:
                    stop2+=middle1
        
        case 4:
            start2=listing1[item]

            for letter in range(len(start2)):
                middle2=str(start2[letter])
                #print(middle)
                Test2=middle2.isnumeric()
                if Test2:
                    stop3+=middle2
        
        case 5:
            Date=listing[item][0:7]
            Time=listing[item][8:]       

print(TruckID)
print(stop1)
print(stop2)
print(stop3)
print(Date)
print(Time)

Data=[TruckID,stop1,stop2,stop3,Date,Time]
SetSQL=SQL.SQL_OUT(Data)