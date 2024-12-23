import tkinter as tk
from tkinter import Spinbox
def on_spinbox_changed():
    value = spinbox.get()
    label2.conflig(text = "giá trị đã chọn:"+ value)
root = tk.Tk()
root.Title("SpinBox Example")
root.geometry('300x80')
spinbox = Spinbox(root, from_=1,to=10,increment=1, width=10)
spinbox.grid(row=0)