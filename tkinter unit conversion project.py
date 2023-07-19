#Unit coversion
#Ask the user to enter a number in feet and will have an option to get a return value in inches, meters, or miles

import tkinter as tk
import time

window = tk.Tk()
window.title("Unit Conversion")
window.geometry("420x230")

directionsLabel = tk.Label(text="Enter here in feet and choose which unit you want to convert to:")
directionsLabel.pack()

textEntry = tk.Entry()
textEntry.pack()

directions2Label = tk.Label(text="\nChoose the conversion:")
directions2Label.pack()

element = tk.StringVar()

inchesRadioButton = tk.Radiobutton(text="inches          ", variable=element, value="inch")
inchesRadioButton.pack()

milesRadioButton = tk.Radiobutton(text="centimeters ", variable=element, value="cm")
milesRadioButton.pack()

metersRadioButton = tk.Radiobutton(text="meters          ", variable=element, value="meter")
metersRadioButton.pack()


def conversion():
    userChoice = element.get()
    userNumber = float(textEntry.get())
    convertedNumber = 0

    if(userChoice == "inch"):
        convertedNumber = userNumber * 12
        resultLabel.configure(text=f"\n{userNumber} feet is {convertedNumber} inches")

    elif(userChoice == "meter"):
        convertedNumber = userNumber * 0.3048
        resultLabel.configure(text=f"\n{userNumber} feet is {convertedNumber} meters")

    elif (userChoice == "cm"):
        convertedNumber = userNumber * 30.48
        resultLabel.configure(text=f"\n{userNumber} feet is {convertedNumber} centimeters")

    else:
        resultLabel.configure(text="\nSelect a conversion")


submitButton = tk.Button(text="Convert", command=conversion)
submitButton.pack()

resultLabel = tk.Label(text="")
resultLabel.pack()

tk.mainloop()
