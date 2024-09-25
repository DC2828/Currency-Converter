from tkinter import *
import datetime
from tkcalendar import Calendar
import Graph
# clear selected dates in DateList
def Clear(DateList,SelectedPeriod):
    DateList.clear()
    SelectedPeriod.set("Histoical rate Between  and .")

# test if the date is within the range by changing it's format
def ParseTime(DateList):
    FirstDate = datetime.datetime.strptime(DateList[0],"%m/%d/%y")
    SecondDate = datetime.datetime.strptime(DateList[1],"%m/%d/%y")
    # use the absolute value of days so that we don't have to find the start and end
    DaysRange = abs((FirstDate-SecondDate).days)

    return DaysRange

# check if the time period is valid and store the date into DateList
def SetDate(event,TimePeriod,DateList,SelectedPeriod,Error,ConfirmButton):

    Date = TimePeriod.get_date()
    # the date will be appended into the DateList when it is a valid selection(less than 2 dates selected and not duplicate)
    if len(DateList) < 2 and not(Date in DateList):
        DateList.append(Date)
        Error.set("")

        if len(DateList) == 1:
            SelectedPeriod.set("Histoical rate between {} and .".format(DateList[0]))
        elif len(DateList) == 2:
            SelectedPeriod.set("Histoical rate between {} and {}.".format(DateList[0],DateList[1]))

    # remove the date in DateList if it has been clicked 2 times
    elif Date in DateList:
        DateList.remove(Date)
        Error.set("")
        if len(DateList) == 1:
            SelectedPeriod.set("Histoical rate between {} and .".format(DateList[0]))
        else:
            SelectedPeriod.set("Histoical rate between  and .")

    else:
        Error.set("Error: more than 2 dates Selected.")
    # check the daysrange
    if len(DateList) == 2:
        
        DaysRange = ParseTime(DateList)

        if DaysRange>366:
            Error.set("Error: Maximum range-366 days.")
            ConfirmButton.config(state=DISABLED)
            Clear(DateList,SelectedPeriod)
        else:
            ConfirmButton.config(state=NORMAL)

# window for date selection
def SelectDate(main_window,SF,ST):

    DateSelectWindow = Toplevel(main_window)
    DateSelectWindow.title("Select Date")
    DateSelectWindow.geometry("500x400")
    DateSelectWindow.maxsize(500,400)
    DateSelectWindow.config(bg="linen")
    InstructionsLable = Label(DateSelectWindow,
                                text = "Select a time period,366 days maximum",
                                bg="grey",
                                fg="white",
                                font=("Arial",15))
    InstructionsLable.pack()
    TimePeriod = Calendar(DateSelectWindow,
                          mindate=datetime.datetime(1999,1,1),
                          maxdate=datetime.datetime.now(),
                          font=("Arial",15),
                          selectmode="day")
    TimePeriod.pack()

    DateList = []

    SelectedPeriod = StringVar()
    Error = StringVar()

    PeriodStr = "Histoical rate between  and ."
    
    DateLabel = Label(DateSelectWindow,
                      textvariable=SelectedPeriod,
                      bg="linen",
                      font=("Arial",15))
    DateLabel.pack()
    
    ErrorLabel = Label(DateSelectWindow,
                      textvariable=Error,
                      bg="linen",
                      fg="dark red",
                      font=("Arial",10))
    ErrorLabel.pack()


    SelectedPeriod.set(PeriodStr)

    # event will be triggered if user has selected a day in the calendar
    TimePeriod.bind("<<CalendarSelected>>",lambda event: SetDate(event,TimePeriod,DateList,SelectedPeriod,Error,ConfirmButton))

    

    ButtonFrame = Frame(DateSelectWindow,
                        bg="linen",
                        padx=10,
                        pady=10)
    ButtonFrame.pack()

    # --------------------------------------------------------------------------------------


    ConfirmButton = Button(ButtonFrame,
                        text="Confirm",
                        font=("Arial",15),
                        activebackground="grey",
                        command=lambda: Graph.yearly_rates_graph(SF,ST,DateList,SelectedPeriod))
    ConfirmButton.grid(row=0,column=0)

    DummyLable = Label(ButtonFrame,
                       width=10,
                       bg="linen")
    DummyLable.grid(row=0,column=1)

    ClearButton = Button(ButtonFrame,
                        text="Clear Selected Dates",
                        font=("Arial",15),
                        activebackground="grey",
                        command=lambda: Clear(DateList,SelectedPeriod))
    ClearButton.grid(row=0,column=2)
    
    DateSelectWindow.mainloop()
















