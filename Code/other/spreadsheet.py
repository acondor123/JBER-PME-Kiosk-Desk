import pandas as pd

#data = pd.read_excel(io='E:\\Repos\\JBER-PME-Kiosk-Desk\\Code\\mockSpreadsheet.xlsx', dtype={"DoD_ID":int, 'First_Name': str, 'Last_Name':str, 'Flight':str, 'Room_Nunber': int, 'Instructor_Name':str})
data = pd.read_excel(io='E:\\Repos\\JBER-PME-Kiosk-Desk\\Code\\mockSpreadsheet.xlsx', usecols=['DOD ID', 'First Name', 'Last Name', 'Flight', 'Room Number', 'Instructor Name'])
#data = pandas.ExcelFile('E:\\Repos\\JBER-PME-Kiosk-Desk\\Code\\mockSpreadsheet.xlsx')

#print(data.to_dict())

out = data.groupby("DOD ID").agg(list).to_dict('index')

print(out)