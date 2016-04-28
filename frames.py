from Tkinter import *
import ttk

root = Tk()

button1 = Button(root, text='Button1')
button2 = Button(root, text='Button2')
button3 = Button(root, text='Button3')
entry1 = Entry(root, width=6)
aTimeCombo = ttk.Combobox(root, state='readonly', width=6, values=['year', 'month', 'week'])

button1.pack(side=TOP)
button2.pack(side=TOP)
button3.pack(side=RIGHT)
entry1.pack(side=RIGHT)
aTimeCombo.pack()

mainloop()
