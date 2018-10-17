from tkinter import *
import time

root = Tk()
root.title('NS Ticketmachine')
root.geometry('1920x1080+0+0')
root.configure(background='#ffac00')

heading = Label(root, text='Welcome to NS', background='#ffac00',  font=('Frutiger', 110, 'bold'), fg='#003373').pack()

label1 = Label(root, text='Please choose your option', background='#ffac00', font=('Frutiger', 40, 'bold'), fg='#003373').pack()
label2 = Label(root, text='Utrecht Centraal', background='#ffac00', font=('Frutiger', 20, 'bold'), fg='#003373').place(x=10, y=10)

class klok:
    def __init__(self):
        self.time1 = ''
        self.time2 = time.strftime('%H:%M:%S')

        self.watch = Label(text=self.time2, background='#ffac00', font=('Times New Roman',25,'bold'), fg='#003373')
        self.watch.place(x=1700, y=10)

        self.changeLabel()

    def changeLabel(self):
        self.time2 = time.strftime('%H:%M:%S')
        self.watch.configure(text=self.time2)
klok()
root.mainloop()




