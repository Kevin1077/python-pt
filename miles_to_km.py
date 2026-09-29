from tkinter import *

window = Tk()
window.title("Miles to Kilometer convertor")
window.minsize(width=50, height=100)
window.config(padx=150, pady=30)

def calculate():
    km = (float(user_input.get()) * 1.60934)
    my_label3["text"] = f"{round(km, 2)}"


user_input = Entry(width=20)
user_input.grid(row=0, column=1, padx=10)


my_label1 = Label(text="Miles", font=("arial", 15, "bold"))
my_label1.grid(row=0, column=2)

my_label2 = Label(text="is equal to", font=("arial", 15, "bold"))
my_label2.grid(row=1, column=0, padx=20)

my_label3 = Label(text="0", font=("arial", 15, "bold"))
my_label3.grid(row=1, column=1, padx=10)


my_label4 = Label(text="Km", font=("arial", 15, "bold"))
my_label4.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)



window.mainloop()
