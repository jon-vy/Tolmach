from tkinter import *

class View(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.image = PhotoImage(file="img/play1.png")
        b = Button(self, text="Hello, world", image=self.image, compound="left")
        b.pack(side="top")

if __name__ == "__main__":
    root = Tk()
    view = View(root)
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()