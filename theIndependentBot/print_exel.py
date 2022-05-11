import win32com.client
from PIL import ImageGrab
import os



o = win32com.client.gencache.EnsureDispatch("Excel.Application")
wb = o.Workbooks.Open("<PATH TO WORKBOOK>")
ws = wb.Worksheets("Sheet1")
ws.Range(ws.Cells(2,1),ws.Cells(32,8)).CopyPicture(Format= win32com.client.constants.xlBitmap)  
img = ImageGrab.grabclipboard()
imgFile = os.path.join(os.getcwd(),'test.jpg')
img.save(imgFile)
