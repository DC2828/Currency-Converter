from tkinter import *
from tkinter import messagebox
import FileOperation
import time

# return type and events given by gpt

def Save(Amount ,Base ,ConversionResult ,Target ,Rate ,SaveTime):
    YN = messagebox.askyesno(title="Save Record", message="Do you want to save this record?")

    if YN:
        FileOperation.Write(Amount ,Base ,ConversionResult ,Target ,Rate ,SaveTime)
        ResultWindow.destroy()
    elif not YN:
        ResultWindow.destroy()

# window for result
def result(ResultString,main_window,Amount):
    global ResultWindow
    ResultWindow = Toplevel(main_window)
    ResultWindow.title("Result")
    ResultWindow.maxsize(300,100)

    Result = StringVar()
    Time = StringVar()

    Base = ResultString["base_code"]
    ConversionResult = ResultString["conversion_result"]
    Target = ResultString["target_code"]

    Result.set(str(Amount) + " of " + Base + " is equal to " + str(ConversionResult)+ " of " + Target)

    Time.set("Last Update: " + ResultString["time_last_update_utc"])
    ResultFrame = Frame(ResultWindow,
                        padx=10,
                        pady=10,
                        width=300,
                        height=60,
                        bg="linen")
    
    ResultLabel = Label(ResultFrame,
                        textvariable=Result,
                        bg="linen",
                        font=("Arial",10))
    ResultLabel.pack()

    ResultFrame.pack()

    TimeLabel = Label(ResultFrame,
                      textvariable=Time,
                      bg="linen",
                      font=("Arial",10))
    TimeLabel.pack()

    ResultFrame.propagate(0)

    ResultWindow.protocol("WM_DELETE_WINDOW",lambda: Save(Amount ,Base ,ConversionResult ,Target ,Rate=ResultString["conversion_rate"] ,SaveTime=time.ctime()))
    ResultWindow.mainloop()



