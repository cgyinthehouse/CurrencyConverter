import tkinter as tk


def convert_currency():
    cur = 28.65
    if usd == '':
        usd.set(round(twd.get() / cur, 2))
    elif twd == '':
        twd.set(round(usd.get() * cur, 2))
def clear():
    usd_box.delete(0, 'end')
    twd_box.delete(0, 'end')


win = tk.Tk()
win.title('Currency Converter')
usd = tk.DoubleVar()
twd = tk.DoubleVar()
btn_conv = tk.Button(win, text='convert', command=convert_currency)
tk.Button(win, text='clear', command=clear).grid(row=1, column=2)

usd_box = tk.Entry(win, textvariable=usd, width=20)
twd_box = tk.Entry(win, textvariable=twd, width=20)
lblusd = tk.Label(win, text='USD：')
lbltwd = tk.Label(win, text='TWD：')
lblusd.grid(row=0, column=0)
lbltwd.grid(row=0, column=3)
usd_box.grid(row=0, column=1)
twd_box.grid(row=0, column=4)
btn_conv.grid(row=0, column=2)

win.mainloop()
