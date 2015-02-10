#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this program, we show various
message boxes.

author: Jan Bodnar
last modified: January 2011
website: www.zetcode.com
"""

from ttk import *
from Tkinter import *
import tkMessageBox as box
import webbrowser


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()


    def initUI(self):

        self.parent.title("Paste to Drive v0.1")
        self.style = Style()
        self.style.theme_use("default")
        self.pack()

        changeUserB = Button(self, text="Change user", command=self.onError)
        changeUserB.grid()
        gotoB = Button(self, text="Goto Drive", command=self.gotoDB)
        gotoB.grid(row=1, column=0)
        question = Button(self, text="Question", command=self.onQuest)
        question.grid(row=0, column=1)
        inform = Button(self, text="Information", command=self.onInfo)
        inform.grid(row=1, column=1)

    def gotoDB(self):
        webbrowser.open_new_tab('https://drive.google.com/drive/')

    def onError(self):
        box.showerror("Error", "Could not open file")

    def onWarn(self):
        box.showwarning("Warning", "Deprecated function call")

    def onQuest(self):
        box.askquestion("Question", "Are you sure to quit?")

    def onInfo(self):
        box.showinfo("Information", "Download completed")


def key(event):
    print "Halla mann:  ", repr(event.char)

def main():

    root = Tk()
    ex = Example(root)
    root.geometry("300x150+300+300")
    root.bind("<Control-h>", key)

    root.mainloop()


if __name__ == '__main__':
    main()
