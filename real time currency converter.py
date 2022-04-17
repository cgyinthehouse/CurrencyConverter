import tkinter as tk
from tkinter import ttk
import requests


def convert_currency(*event):
    cur = real_time_currency_conversion()
    value2.set(round(value1.get() * cur, 2))


def clear():
    box1.delete(0, 'end')
    box2.delete(0, 'end')


def real_time_currency_conversion():
    # currency code
    from_currency = combo1.get()
    to_currency = combo2.get()
    pair = from_currency + to_currency

    if pair not in cur_pairs:
        with open('apikey.txt', 'r') as f:
            api_key = f.readline()
        url = r'https://v6.exchangerate-api.com/v6/' + api_key + '/latest/' + from_currency
        req_ob = requests.get(url)
        result = req_ob.json()
        exchange_rate = float(result['conversion_rates'][to_currency])
        cur_pairs[pair] = exchange_rate
        print(pair,exchange_rate, cur_pairs)
        return exchange_rate
    else:
        exchange_rate = cur_pairs[pair]
        return exchange_rate


cur_pairs = {}
currencies = ['USD', 'TWD', 'EUR', 'GBP', 'CAD', 'CNY', 'JPY', 'CHF', 'HKD', 'MYR', 'NZD', 'RUB', 'KRW']
win = tk.Tk()
win.title('Currency Converter')
value1 = tk.DoubleVar()
value2 = tk.DoubleVar()
btn_conv = tk.Button(win, text='convert', command=convert_currency, font='Arial',fg='green')
tk.Button(win, text='clear', command=clear, font='Arial').grid(row=0, column=1)
box1 = tk.Entry(win, textvariable=value1, width=20, font=('Helvetica', 15), justify='right')
box2 = tk.Entry(win, textvariable=value2, width=20, font=('Helvetica', 15), justify='right')
combo1 = ttk.Combobox(win, values=currencies, width=5, font=('Arial', 12))
combo2 = ttk.Combobox(win, values=currencies, width=5, font=('Arial', 12))
combo1.grid(row=0, column=0)
combo2.grid(row=0, column=2)
box1.grid(row=1, column=0)
box2.grid(row=1, column=2)
btn_conv.grid(row=1, column=1)
combo1.set(value='USD')
combo2.set(value='TWD')
box2.config(state='disabled')
box1.bind('<Return>',convert_currency)
box2.bind('<Return>',convert_currency)
clear()

win.mainloop()
