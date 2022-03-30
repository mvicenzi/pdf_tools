#!/usr/bin/python

import PySimpleGUI as sg
import sys
import os.path

# FIRST WINDOW: choose the operation
choices = ("Append/Merge", "Extract/Cut", "Rotate")

layout = [  [sg.Text('Select an operation on PDF files:')],
            [sg.Listbox(choices, size=(500, len(choices)), key="-ACTION-")],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('PDF TOOLS', layout, size=(500, 140))

# process the input
while True:
    event, values = window.read()

    #if user closes the window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        window.close()
        exit()

    #if user clicks ok button
    if event == "Ok":
        # if user has made a choice
        if values["-ACTION-"]:

            ### TO DO...: according to choice, open a new windows
            ### different windows depending on choice
            ### each window allow to set parameters
            window.close()
            sg.popup("Hello there!")

        #if user made no choice: open a popup,
        #then go back to main window
        else:
            sg.popup("ERROR: no operation specified. Please choose one of the supported operations on PDF files")
