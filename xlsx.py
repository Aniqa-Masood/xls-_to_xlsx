import win32com.client as win32

'''xls  to xlsx'''

filename = "D:\\Documents\\GitHub\\xls _to_xlsx\\Test 3.xls"
excel = win32.gencache.EnsureDispatch('Excel.Application')     #It attaches Python session to a running Excel process or starts Excel if it is not running.
wb = excel.Workbooks.Open(filename)

wb.SaveAs(filename+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
wb.Close()                                  #FileFormat = 56 is for .xls extension
excel.Application.Quit()
print("Successfully Converted!")