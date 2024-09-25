from tkinter import *



def AutoComplete(Currencies,event):
    # identify the widget users are typing in
    WorkingWidget = event.widget
    # get the input text
    CurrentText = WorkingWidget.get()
    options = Currencies.keys()
    PotentialSelection = {}
    # filter the list by the text
    for key in options:
        if CurrentText.upper() in key.upper():
            PotentialSelection.update({key:Currencies[key]})
    
    if PotentialSelection:
        WorkingWidget["values"] = list(PotentialSelection.keys())


# Add a placeholder for all input bar
def Placeholder(event):
    WorkingWidget = event.widget
    if WorkingWidget.get() == "Select a Currency":
        WorkingWidget.set("")
    


    
    

