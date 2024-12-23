import tkinter as tk
class LisBoxExample:
    def __init__(self, root):
        self.root = root
        self.root.title("ListBox Example")
        self.root.geometry('300x250')
        self.create_widgets()
    def create_widgets(self):
        self.lbl = tk.Label(root, text="Học phần:")