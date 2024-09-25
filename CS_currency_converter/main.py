from tkinter import *
from tkinter import ttk
import CurrencyList
import Result_window
import Auto
import Converter
import FileOperation
import Calender
# propergate() & protocal() for frame & window method
# file potential error
# function(Record Saving) idea
# function concepts(Autocomplete & placeholder)
# syntax(how to pass event to a function with other argument)
# event listeners events 
# module function(json/csv) detail
# API Documents and usage from API website(https://app.exchangerate-api.com)

def main():
    global main_window
    main_window = Tk()
    main_window.geometry("480x500")
    main_window.maxsize(480,500)
    main_window.title("Currency Converter")

    TitleLable = Label(main_window,
                       bg="white",
                       text="Currency Converter",
                       font=("Arial",25))
    TitleLable.grid(row=0,column=0)

    global Currencies
    Currencies = CurrencyList.CurrencyListGenerate()
    options = list(Currencies.keys())

#Main Frame
    MainFrame = Frame(main_window,
                      bg="grey",
                      padx=30,
                      pady=30,
                      width=480,
                      height=400,
                      relief=SUNKEN)

# Select Frame1 elements
    SelectFrame1 = Frame(MainFrame,
                         bg="grey",
                         padx=10,
                         pady=10,
                         relief=SUNKEN)
    
    SelectFromLabel1 = Label(SelectFrame1,
                            text="Select the currency you want to convert:",
                            font=("Arial",15),
                            padx=10,
                            pady=10,
                            bg="grey")
    SelectFromLabel1.pack()

    #Set SelectFrom as a global variable so that it can be accessed by other functions
    global SelectFrom
    SelectFrom = ttk.Combobox(SelectFrame1,
                              values=options,
                              width=40)
    SelectFrom.pack()

    SelectFrom.bind("<KeyRelease>",lambda event, args=Currencies: Auto.AutoComplete(Currencies,event))
    SelectFrom.bind("<Button-1>",Auto.Placeholder)

    SelectFrom.set("Select a Currency")
    
    AmountLabel = Label(SelectFrame1,
                        bg="grey",
                        padx=10,
                        pady=10,
                        text="Type in the amount to convert:",
                        font=("Arial",15))
    AmountLabel.pack()

    #Set AmountEntry as a global variable so that it can be accessed by other functions
    global AmountEntry
    AmountEntry = Entry(SelectFrame1)
    AmountEntry.pack()
    SelectFrame1.pack() 
# Select Frame1 end-------------------------------------------
# Select Frame2 elements
    SelectFrame2 = Frame(MainFrame,
                         bg="grey",
                         padx=10,
                         pady=10,
                         relief=SUNKEN)
    
    SelectFromLabel2 = Label(SelectFrame2,
                            text="Select the currency you want to convert to:",
                            font=("Arial",15),
                            padx=10,
                            pady=10,
                            bg="grey")
    SelectFromLabel2.pack()
    #Set SelectTo as a global variable so that it can be accessed by other functions
    global SelectTo
    SelectTo = ttk.Combobox(SelectFrame2,values=options,width=40)
    SelectTo.pack()

    SelectTo.bind("<KeyRelease>",lambda event, arg=Currencies: Auto.AutoComplete(Currencies,event))
    SelectTo.bind("<Button-1>",Auto.Placeholder)

    SelectTo.set("Select a Currency")

    SelectFrame2.pack()
#Select Frame2 end --------------------------------------------

    ButtonFrame = Frame(MainFrame,
                        bg="grey",
                        padx=10,
                        pady=10,
                        relief=SUNKEN)


    ConvertButton = Button(ButtonFrame,
                           text="Start Conversion",
                           font=("Arial",15),
                           activebackground="grey",
                           command=lambda:GetValue(1))
    ConvertButton.grid(row=0,column=0)

    DummyLable = Label(ButtonFrame,
                       bg="grey",
                       width=10)
    DummyLable.grid(row=0,column=1)
    HistoricalRecordButton = Button(ButtonFrame,
                                    text="Historical Rate",
                                    font=("Arial",15),
                                    activebackground="grey",
                                    command=lambda:GetValue(2))
    HistoricalRecordButton.grid(row=0,column=2)

    ButtonFrame.pack()
    global Error
    Error = StringVar()

    ErrorLable = Label(MainFrame,
                        bg="grey",
                        fg="dark red",
                        font=("Arial",10),
                        textvariable=Error)
    ErrorLable.pack()

    MainFrame.grid(row=1,column=0)
    MainFrame.propagate(0)

    RecordFrame = Frame(main_window,
                        width=480,
                        height=50,
                        padx=10,
                        pady=10)
    
    RecordButton = Button(RecordFrame,
                          text="Conversion History",
                          bg="grey",
                          fg="white",
                          font=("Arial",15),
                          command=lambda: FileOperation.Read(main_window))
    RecordButton.pack()
    RecordFrame.grid(row=2,column=0)
    RecordFrame.propagate(0)
#Main Frame end------------------------
    main_window = mainloop()

# ----------------------------------------------------------------------------------------

def GetValue(FunctionId):

# First Input Check--------------------------------------
    # get the value from SelectForm and SelectTO
    SF = SelectFrom.get()

    # check if the input exists in the Currencies dictionary key, if yes the value of SF will be changed from the key to the value of the Dictionary(Hong Kong Dollar -> HKD)
    if SF in Currencies.keys():
        SF = Currencies[SF]

    # if the value is invalid the original value will not be changed so SF will still equals to the value of SelectFrom.get()/SelectTO.get()
    if SF == SelectFrom.get():
        Error.set("Invalid input: Currency to convert from not found")
        return 
        
#Amount Input Check--------------------------------------
    if FunctionId == 1:
        Amount = AmountEntry.get()
        try:
            Amount = float(Amount)
            if Amount <= 0:
                Error.set("Invalid input: Amount must be a positive or non zero number")
                return
        except ValueError:
            Error.set("Invalid input: Numbers only")
            return
            
        except Exception as e:
            Error.set(e)
            return
        
#Target Input Check----------------------------------------
    ST = SelectTo.get()
    
    if ST in Currencies.keys():
        ST = Currencies[ST]
    

    if ST == SelectTo.get():
        Error.set("Invalid input: Currency to convert to not found")
        return
        
    if FunctionId == 1:
        ResultString =  Converter.convert_currency(SF,ST,Amount,Error)

        Result_window.result(ResultString,main_window,Amount)
    else:
        Calender.SelectDate(main_window,SF,ST)



if __name__ == "__main__":
    main()