
import tkinter as tk
class CustomButton(tk.Button):
    def __init__(self, parent, point,text,option, command=None):
        tk.Button.__init__(self, parent, borderwidth=1,
                           relief="raised", highlightthickness=0)
        self.command = command
        # padding = 4
        parent.create_rectangle(point, outline='green',
                          fill='gray', width=3)
        # (x0, y0, x1, y1) = parent.bbox("all")
        self.button =tk.Button(None, text=text,height = 6, width =7,command=option.Crawl)
        parent.create_window(point[0]+42,point[1]+55,window=self.button)



