#!/usr/bin/python
# -*- coding: utf-8 -*-

import setctl

from Tkinter import Tk, BOTH, StringVar
from ttk import Frame, Button, Style, OptionMenu


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Finger Putty")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        # Logo text
        # logoText = Text(self)

        # OS drop-down button
        variable = StringVar(self)
        variable.set("Linux")

        osDropdownButton = OptionMenu(self, variable, "Choose your OS", "Linux", "Windows", "Playstation")
        osDropdownButton.pack()
        osDropdownButton.place(x=50, y=50)

        # Set (OS) fingerprint button
        changePrintButton = Button(self, text="Set fingerprint",
            command=self.quit)
        changePrintButton.place(x=50, y=80)

        # Launch browser button
        launchButton = Button(self, text="Launch browser (new user-agent)",
            command=setctl.test)
        launchButton.place(x=50, y=110)



def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  