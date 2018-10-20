import tkinter as tk

root = tk.Tk()

def timeout_cb():
    answer.unbind('<Key-Return>')  # disable answer entry
    print('timed out')

def answer_cb(event):
    root.after_cancel(time_id)  # disable timeout timer
    print('you answered', answer.get())

prompt = tk.Label(root, text='Name?')
answer = tk.Entry(root)
prompt.grid(row=0, column=0)
answer.grid(row=0, column=1)
answer.focus_set()
answer.bind('<Key-Return>', answer_cb)
time_id = root.after(10000, timeout_cb)  # 10 seconds

root.mainloop()