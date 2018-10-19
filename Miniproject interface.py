from tkinter import *
import time

root = Tk()
'Dit is de interface'

root.title('NS Ticketmachine')
root.geometry('1920x1080+0+0')
root.configure(background='#ffac00')

heading = Label(root, text='Welcome to NS', background='#ffac00',  font=('Frutiger', 110, 'bold'), fg='#003373').pack()

label1 = Label(root, text='Please select your option', background='#ffac00', font=('Frutiger', 40, 'bold'), fg='#003373').pack()
label2 = Label(root, text='Utrecht Centraal', background='#ffac00', font=('Frutiger', 20, 'bold'), fg='#003373').place(x=10, y=10)


#logo = PhotoImage(file='NS1.png')
#label3 = Label(root, image=logo).pack()

knop1 = Button(root, text='Route Planner', width=15, height=6, bg='#ffac00', command=print('open scherm'), font=('Frutiger', 30, 'bold'), fg='#003373').place(x=250, y=500)
knop2 = Button(root, text='Leave Now', width=15, height=6, bg='#ffac00', command=print('open scherm'), font=('Frutiger', 30, 'bold'), fg='#003373').place(x=750, y=500)
knop3 = Button(root, text='Travel Abroad', width=15, height=6, bg='#ffac00', command=print('open scherm'), font=('Frutiger', 30, 'bold'), fg='#003373').place(x=1250, y=500)


def tick(time1=''):
    'Dit is onze klok.'
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock_frame.config(text=time2)
    clock_frame.after(200, tick)

clock_frame = Label(root, font=('Futiger', 25, 'bold'), bg='#ffac00', fg='#003373')
clock_frame.place(x=1750, y=10)
tick()
root.mainloop()




