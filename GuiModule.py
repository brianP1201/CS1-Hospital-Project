import tkinter as tk
from Appointment import Appointment
from Patient import Patient


window = tk.Tk()
window.title("Hospital Appointment System")


tk.Label(window, text="Patient Name").grid(row=0)
tk.Label(window, text="Age").grid(row=1)
tk.Label(window, text="Gender").grid(row=2)

e1 = tk.Entry(window)
e2 = tk.Entry(window)
e3 = tk.Entry(window)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)



def show_entry_fields():
    p = Patient(e1.get(), e2.get(), e3.get())
    print(p)
    p.request_appointment()


tk.Button(window, text='Quit', command=window.quit).grid(row=3,  column=0, sticky=tk.W,  pady=4)
tk.Button(window, text='Show', command=show_entry_fields).grid(row=3,  column=1, sticky=tk.W, pady=4)
#button = tk.Button(window,  text="CREATE APPOINTMENT",  fg="blue",command=p.request_appointment())


window.mainloop()