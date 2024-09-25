import csv
from tkinter import *
from tkinter import messagebox
import os 
path = ".\\RecordFile\\Record.csv"

def Write(Amount ,Base ,ConversionResult ,Target ,Rate ,SaveTime):
    try:
        
        if os.path.exists(path):
            with open(path, "a",newline="") as csvfile:
                csv_writer = csv.writer(csvfile)
                
                
                csv_writer.writerow([str(Amount) ,Base ,str(ConversionResult) ,Target ,str(Rate),SaveTime])
            csvfile.close()

            messagebox.showinfo("Record saved")
        else:
            with open(path, "w",newline="") as csvfile:
                csv_writer = csv.writer(csvfile)
                
                
                csv_writer.writerow([str(Amount) ,Base ,str(ConversionResult) ,Target ,str(Rate),SaveTime])
            csvfile.close()
        
            messagebox.showinfo("Record saved")

    except FileNotFoundError:
        messagebox.showerror("File not found")
    except PermissionError:
        messagebox.showerror("Permission error")
    except TypeError:
        messagebox.showerror("Data Type error")
    except Exception:
        messagebox.showerror("Save failed")

# disable the button if there is no record selected
def ActiveButton(event,DeleteButton):
    Widget = event.widget
    Widget.curselection()
    if Widget.curselection():
        DeleteButton.config(state=ACTIVE)
    else:
        DeleteButton.config(state=DISABLED)

#Delete functions ---------------------------------------------------------------------------------------------------------------

def Delete(Recordlist,ReadWindow):
    # curselection returns a tuple of selected elements' indexes
    Record = list(Recordlist.get(0,END))
    Selected = Recordlist.curselection()
    SelectedList = []
    for i in Selected:
        SelectedList.append(Recordlist.get(i))

    # delete the selected record from the Record list
    for i in list(Recordlist.get(0,END)):
        if i in SelectedList:
            Record.remove(i)
    
    #GUI ------------------------------------------------------------
    # clear the GUI listbox
    Recordlist.delete(0,END)
    # Insert the record into the listbox one by one
    for i in Record:
        Recordlist.insert(END,i)

    # open the file and override the origin record with new data
    
    #File ---------------------------------------------------------------
    with open(path, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        # write the records in Record list one by one
        
        for i in range(len(Recordlist.get(0,END))):
            # use split to make a list with each record for writerow ,writerow will accept a string but it will identify a string as a list(because write row can only accept iterables) and separate each character with a comma so we need a list to make sure the new data will be written and separated into the csv correctly.
            csv_writer.writerow(Recordlist.get(i).split(","))
        csvfile.close()



# Delete all records
def DeleteAll(Recordlist,DeleteAllButton):
    if messagebox.askyesno("Delete All Records"):
        # "w" will override all data and write new data, opening a file with "w" and write nothing will delete the old data
        with open(path,"w") as csvfile:

            csvfile.close()
        Recordlist.delete(0,END)
        DeleteAllButton.config(state=DISABLED)


# ------------------------------------------------------------------------------------------------------------------
# window for showing records
def Read(main_window):
    try:
        if os.path.exists(path):
            with open(path, "r") as csvfile:
                csv_reader = csv.reader(csvfile)

                ReadWindow = Toplevel(main_window)
                ReadWindow.geometry("800x300")
                ReadWindow.maxsize(800,300)
                ReadWindow.config(bg="linen")

                Recordlist = Listbox(ReadWindow,
                                    bg="linen",
                                    font=("Arial",15),
                                    width=500,
                                    selectmode=MULTIPLE)
                Recordlist.pack()

                # read all the records and add them into the listbox
                for line in csv_reader:
                    Base_Amount = str(line[0])
                    Base = line[1]
                    Target_Amount = str(line[2])
                    Target = line[3]
                    Rate = str(line[4])
                    Time = line[5]

                    if line:
                        Recordlist.insert(END,Base_Amount + "," + Base + "," + Target_Amount + "," + Target + "," + Rate + "," + Time)
                csvfile.close()
                
                ButtonFrame = Frame(ReadWindow,
                                    width=800,
                                    height=300,
                                    bg="linen")
                
                DeleteButton = Button(ButtonFrame,
                                    padx=10,
                                    font=("Arial",10),
                                    state="disabled",
                                    text="Delete Selected Records",
                                    command=lambda:Delete(Recordlist,ReadWindow))
                
                DeleteAllButton = Button(ButtonFrame,
                                        padx=10,
                                        font=("Arial",10),
                                        text="Delete All Records",
                                        command=lambda:DeleteAll(Recordlist,DeleteAllButton))
                
                if not(Recordlist.get(0,END)):
                    DeleteAllButton.config(state=DISABLED)

                Recordlist.bind("<<ListboxSelect>>",lambda event, args=DeleteButton: ActiveButton(event,DeleteButton))

                DummyLable = Label(ButtonFrame,
                                   bg="linen",
                                   width=10)

                DeleteButton.grid(row=0,column=0)
                DummyLable.grid(row=0,column=1)
                DeleteAllButton.grid(row=0,column=2)
                ButtonFrame.pack()



                ReadWindow.propagate(0)
                ReadWindow.mainloop()
        else:
            messagebox.showerror("File not found")
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission error")
    except IsADirectoryError:
        print("Is a directory error")
    except UnicodeDecodeError:
        print("Decoding error")
    except Exception as e:
        messagebox.showerror(e)


