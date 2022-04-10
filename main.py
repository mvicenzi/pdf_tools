#!/usr/bin/python
import PySimpleGUI as sg
import sys
import os.path

from MergePDF import AppendPDFs

#-------------------------------------------------------------------------------
# MERGE WINDOW: allows to select file to needs to be merged
# there needs to be at least two files correctly selected + output path
#-------------------------------------------------------------------------------

merge_layout = [ [sg.Text('Select first PDF file:')],
                 [sg.In(size=(50,10), key="-FILE-"),
                  sg.FileBrowse(key="-brFile-", file_types=(("PDF files", "*.pdf"),))],
                 [sg.Text('Select PDF file(s) to append:')],
                 [sg.Multiline(size=(50,10), key="-FILES-"), sg.Input(key='-HIDDEN-', visible=False, enable_events=True),
                  sg.FilesBrowse(target="-HIDDEN-", key="-brFILES-", file_types=(("PDF files", "*.pdf"),))],
                 [sg.Text('Save output as:')],
                 [sg.In(size=(50,10), key="-OUT-"),
                   sg.FileBrowse(key="-brOUT-", file_types=(("PDF files", "*.pdf"),))],
                 [sg.Button('Merge'), sg.Button('Cancel')] ]

def run_merge():
    merge_window = sg.Window('PDF Tools - Append/Merge', merge_layout, size=(500,350))

    while True:
        merge_event, merge_values = merge_window.read()

        if merge_event == '-HIDDEN-':
            merge_window.Element('-FILES-').Update(merge_values['-HIDDEN-'].split(';'))

        if merge_event == sg.WIN_CLOSED or merge_event == 'Cancel':
            merge_window.close()
            exit()

        if merge_event == 'Merge':
            ifile = merge_values["-FILE-"]
            ofile = merge_values["-OUT-"]
            filepaths = []
            for file in merge_values["-FILES-"].lstrip("[").rstrip("]").split(","):
                filepaths.append(file.lstrip(" '").rstrip("'"))
            filepaths.insert(0,ifile)

            if ifile != "" and ofile != "" and filepaths[1] != "":
                AppendPDFs(filepaths, ofile)
                merge_window.close()
                sg.popup("Files merged in " + ofile)
                exit()
            else:
                sg.popup("Missing inputs: select at least two pdf files and the output name!")

#-------------------------------------------------------------------------------
#EXTRACT WINDOW:

def run_extract():
    sg.popup("Hello here!")

#-------------------------------------------------------------------------------
#ROTATE WINDOW:

def run_rotate():
    sg.popup("Hello sphere!")

#-------------------------------------------------------------------------------
#FIRST WINDOW: choose the operation

choices = ("Append/Merge", "Extract/Cut", "Rotate")

layout = [  [sg.Text('Select an operation on PDF files:')],
            [sg.Listbox(choices, size=(500, len(choices)), key="-ACTION-")],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('PDF Tools', layout, size=(500, 140))

if __name__ == "__main__":
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
            if values["-ACTION-"][0] == "Append/Merge":
                window.close()
                run_merge()

            elif values["operation"][0] == "Extract/Cut":
                window.close()
                run_extract()

            elif values["operation"][0] == "Rotate":
                window.close()
                run_rotate()

        #if user made no choice: open a popup,
        #then go back to main window
        else:
            sg.popup("ERROR: no operation specified. Please choose one of the supported operations on PDF files")
