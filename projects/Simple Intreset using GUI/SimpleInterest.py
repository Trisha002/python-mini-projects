from tkinter import *


# defining the reset function
def reset():
    # deleting the entries in all entry fields
    principalField.delete(0, END)
    rateField.delete(0, END)
    numberField.delete(0, END)
    timeField.delete(0, END)
    resultField.delete(0, END)

    # setting the focus to the principal field
    principalField.focus_set()


# defining the function to calculate the compound interest
def simple_interest():
    # getting the values from the entry fields
    principal = float(principalField.get())
    rate_of_interest = float(rateField.get())
    time = int(timeField.get())

    # calculating the compound interest
    si = (principal * rate_of_interest * time ) / 100

    resultField.insert(10, si)


# main function
if __name__ == "__main__":
    # creating an instance of the Tk() class
    guiWindow = Tk()
    # defining the title for the GUI window
    guiWindow.title("Simple Interest Calculator")
    # defining the geometry for the window
    guiWindow.geometry("640x500+600+350")
    # disabling the resizable option
    guiWindow.resizable(1, 1)
    # setting the background color for the window
    guiWindow.configure(bg="#2ECC71")

    # heading on the window
    guiLabel = Label(
        guiWindow,
        text="Calculate the Simple Interest",
        font=("Courier New", 20),
        fg="#211600",
        bg="#f0c33c"
    )
    # placing the label on the window
    guiLabel.place(
        x=60,
        y=10
    )

    # creating a 'Principal Amount' label
    labelOne = Label(
        guiWindow,
        text="Principal Amount (₹):",
        bg="#f0c33c",
        fg="#4a3200"
    )
    # creating a 'Rate of Interest' label
    labelTwo = Label(
        guiWindow,
        text="Rate of Interest (%):",
        bg="#f0c33c",
        fg="#4a3200"
    )

    # creating a 'Time Period' label
    labelThree = Label(
        guiWindow,
        text="Time Period (Years):",
        bg="#f0c33c",
        fg="#4a3200"
    )
    # creating a 'Compound Interest' label
    labelFour = Label(
        guiWindow,
        text="Simple Interest (S.I.):",
        bg="#f0c33c",
        fg="#4a3200"
    )

    # using the place() method to place
    # the above labels on the window
    labelOne.place(x=72, y=120)
    labelTwo.place(x=72, y=160)
    labelThree.place(x=72, y=200)
    labelFour.place(x=72, y=300)

    # entry field for the principal amount
    principalField = Entry(
        guiWindow,
        bg="#fcf9e8",
        fg="#211600"
    )
    # entry field for the rate of interest
    rateField = Entry(
        guiWindow,
        bg="#fcf9e8",
        fg="#211600"
    )
    # entry field for the number
    numberField = Entry(
        guiWindow,
        bg="#fcf9e8",
        fg="#211600"
    )
    # entry field for the time period
    timeField = Entry(
        guiWindow,
        bg="#fcf9e8",
        fg="#211600"
    )
    # entry field for the result
    resultField = Entry(
        guiWindow,
        bg="#fcf9e8",
        fg="#211600"
    )

    # using the place() method to place
    # the above fields on the window
    principalField.place(x=250, y=120)
    rateField.place(x=250, y=160)
    timeField.place(x=250, y=200)
    resultField.place(x=250, y=300)

    # creating a Result button
    resultButton = Button(
        guiWindow,
        text="CALCULATE",
        bg="#135e96",
        fg="#fcf9e8",
        command=simple_interest
    )
    # creating a Reset button
    resetButton = Button(
        guiWindow,
        text="RESET",
        bg="#d63638",
        fg="#fcf0f1",
        command=reset
    )
    # using the place() method to place
    # the above buttons on the window
    resultButton.place(x=280, y=240)
    resetButton.place(x=300, y=340)

    # running the window
    guiWindow.mainloop()
