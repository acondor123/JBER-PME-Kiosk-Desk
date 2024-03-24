import customtkinter
import pandas as pd

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Kiosk Login")
        #self.geometry("{}x{}".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.geometry("1000x700")

        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.pack(fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Enter Your Barcode:", font=("Arial", 25))
        self.label.place(relx=0.5, rely=0.1, anchor="center")
        

        self.barcodeEntry = customtkinter.CTkEntry(master=self.frame, width=500)
        self.barcodeEntry.place(relx=0.5, rely=.3, anchor="center")


        self.button = customtkinter.CTkButton(master=self.frame, text="Submit", command=self.parseBarcode, width=500)
        self.button.place(relx=0.5, rely=.5, anchor="center")

        self.idNum = customtkinter.CTkLabel(master=self.frame, text="**********", font=('arial', 20))
        self.idNum.place(relx=0.5, rely=.8, anchor="center")


        

    def checkInput(self):
        if(len(self.barcodeEntry.get()) >= 18):
            self.parseBarcode()
            self.barcodeEntry.delete(0, "end")

    def parseBarcode(self):
            base32Barcode = self.barcodeEntry.get()
            parsedBarcode = int(base32Barcode[8:15], 32)
            self.findStudent(parsedBarcode)

    def findStudent(self, dod_id):
        #data = pd.read_excel(io='E:\\Repos\\JBER-PME-Kiosk-Desk\\Code\\mockSpreadsheet.xlsx', usecols=['DOD ID', 'First Name', 'Last Name', 'Flight', 'Room Number', 'Instructor Name'])

        data = pd.read_excel(io='mockSpreadsheet.xlsx', usecols=['DOD ID', 'First Name', 'Last Name', 'Flight', 'Room Number', 'Instructor Name'])

        students = data.groupby("DOD ID").agg(list).to_dict('index')

        try:
            self.idNum.configure(text=students[dod_id]["Last Name"])
        except KeyError:
             self.idNum.configure(text="Student not found!\nScan again")
        


app = App()


while True:
    app.checkInput()
    app.update_idletasks()
    app.update()





