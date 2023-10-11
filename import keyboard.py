from win32 import win32print
import tempfile
import os


ScaleTemp=tempfile.mktemp(".txt")
open(ScaleTemp,"w").write("\r\nTruck ID   5556\r\n\r\nGross       10 kg\r\n\r\n06:24AM 08/02/2023")

files=open(ScaleTemp,"r").read()
fileBytes=files.encode()
printer_name="Brother DCP-L8410CDW series Printer"
printer=win32print.OpenPrinter(printer_name)

win32print.StartDocPrinter(printer,1,(files,None,None))
win32print.StartPagePrinter(printer)
win32print.WritePrinter(printer,fileBytes)
win32print.EndPagePrinter(printer)
win32print.EndDocPrinter(printer)
win32print.ClosePrinter(printer)

