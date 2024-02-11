import customtkinter
import threading
import keyboard

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Kiosk Login")
        #self.geometry("{}x{}".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.geometry("500x350")

        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.pack(side="left", fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Enter Your Barcode:")
        self.label.pack(pady=20)

        self.barcodeEntry = customtkinter.CTkEntry(master=self.frame)
        self.barcodeEntry.pack(pady=20)

        self.button = customtkinter.CTkButton(master=self.frame, text="Submit", command=self.parseBarcode)
        self.button.pack(pady=10)

        self.idNum = customtkinter.CTkLabel(master=self.frame, text="**********")
        self.idNum.pack(pady=20)

        

    def checkInput(self):
        if(len(self.barcodeEntry.get()) >= 18):
            self.parseBarcode()
            self.barcodeEntry.delete(0, "end")

    def parseBarcode(self):
            base32Barcode = self.barcodeEntry.get()
            parsedBarcode = int(base32Barcode[8:15], 32)
            self.idNum.configure(text=str(parsedBarcode))
        


app = App()


while True:
    app.checkInput()
    app.update_idletasks()
    app.update()





