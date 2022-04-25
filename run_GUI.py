#!/usr/bin/python
import PySimpleGUI as sg
import sys
import os.path

from MergePDF import AppendPDFs
from ExtractPDF import ExtractPDFs
from RotatePDF import MultiRotate

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
            sys.exit()

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
                sys.exit()
            else:
                sg.popup("Missing inputs: select at least two pdf files and the output name!")

#-------------------------------------------------------------------------------
#EXTRACT WINDOW:

extract_layout = [ [sg.Text('Select PDF file:')],
                 [sg.In(size=(50,10), key="-FILE-"), sg.FileBrowse(key="-brFile-", file_types=(("PDF files", "*.pdf"),))],
                 [sg.Text('A new PDF will be extracted from the interval [start, end], limits are included.\nTo select a single page, set the start and end page equal.\nPage numbering starts from 1.')],
                 [sg.Text('Starting page:')],
                 [sg.Radio("First page", "Radio1", key="-STARTD-", default=True), sg.Radio("Custom:","Radio1", key="-STARTC-"), sg.Input(size=(5,10), key="-START-")],
                 [sg.Text('Ending page:')],
                 [sg.Radio("Last page", "Radio2", key="-ENDD-", default=True), sg.Radio("Custom:","Radio2", key="-ENDC-"), sg.Input(size=(5,10), key="-END-")],
                 [sg.Text('Save output as:')],
                 [sg.In(size=(50,10), key="-OUT-"), sg.FileBrowse(key="-brOUT-", file_types=(("PDF files", "*.pdf"),))],
                 [sg.Button('Extract'), sg.Button('Cancel')] ]

def run_extract():
    extract_window = sg.Window('PDF Tools - Extract/Cut', extract_layout, size=(500,340))

    while True:
        extract_event, extract_values = extract_window.read()

        if extract_event == sg.WIN_CLOSED or extract_event == 'Cancel':
            extract_window.close()
            sys.exit()

        if extract_event == 'Extract':
            ifile = extract_values["-FILE-"]
            ofile = extract_values["-OUT-"]

            start_page_number = 1 #first page by default
            end_page_number = -1 #last page by default

            if extract_values['-STARTC-']:
                if( extract_values['-START-'].isdigit() ):
                    start_page_number = int(extract_values['-START-'])
                else:
                    sg.popup("Missing input: select a valid starting page")
                    continue

            if extract_values['-ENDC-']:
                if( extract_values['-END-'].isdigit() ):
                    end_page_number = int(extract_values['-END-'])
                else:
                    sg.popup("Missing input: select a valid ending page")
                    continue

            if ifile != "" and ofile != "":
                ExtractPDFs(ifile, start_page_number, end_page_number, ofile)
                extract_window.close()
                sg.popup("File extracted in " + ofile)
                sys.exit()
        else:
            sg.popup("Missing inputs: select a valid interval and the output name!")

#-------------------------------------------------------------------------------
#ROTATE WINDOW:

rotate_layout = [ [sg.Text('Select PDF file:')],
                 [sg.In(size=(50,10), key="-FILE-"), sg.FileBrowse(key="-brFile-", file_types=(("PDF files", "*.pdf"),))],
                 [sg.Text('Select rotation:')],
                 [sg.Radio("Clockwise", "Radio1", key="-CLOCK-", default=True), sg.Radio("Counter-clockwise:","Radio1", key="-CCLOCK-"),
                 sg.DropDown(['90','180','270'], size=(5,10), key="-ROTATION-")],
                 [sg.Text('Insert pages to be rotated, separated by commas.\nPage numbering starts from 1.')],
                 [sg.Input(size=(50,10), key="-PAGES-")],
                 [sg.Text('Save output as:')],
                 [sg.In(size=(50,10), key="-OUT-"), sg.FileBrowse(key="-brOUT-", file_types=(("PDF files", "*.pdf"),))],
                 [sg.Button('Rotate'), sg.Button('Cancel')] ]

def run_rotate():
    rotate_window = sg.Window('Rotate - Extract/Cut', rotate_layout, size=(500,300))

    while True:
        rotate_event, rotate_values = rotate_window.read()

        if rotate_event == sg.WIN_CLOSED or rotate_event == 'Cancel':
            rotate_window.close()
            sys.exit()

        if rotate_event == 'Rotate':
            ifile = rotate_values["-FILE-"]
            ofile = rotate_values["-OUT-"]

            rotation = -1 # clockwise by default
            angle = 0
            pages = []

            if rotate_values['-CCLOCK-']:
                rotation = 1

            if( rotate_values['-ROTATION-'].isdigit() ):
                    angle = int(rotate_values['-ROTATION-'])
            else:
                sg.popup("Missing input: select rotation angle!")
                continue

            for page in rotate_values['-PAGES-'].split(","):
                if( page.isdigit() ):
                    pages.append(int(page))
                else:
                    sg.popup("Wrong input: invalid page number")
                    continue

            if ifile != "" and ofile != "" and len(pages)>0:
                MultiRotate(ifile, rotation*angle, pages, ofile)
                rotate_window.close()
                sg.popup("File extracted in " + ofile)
                sys.exit()
        else:
            sg.popup("Missing inputs: select a valid interval and the output name!")

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
            sys.exit()

        #if user clicks ok button
        if event == "Ok":

            # if user has made a choice
            if values["-ACTION-"][0] == "Append/Merge":
                window.close()
                run_merge()

            elif values["-ACTION-"][0] == "Extract/Cut":
                window.close()
                run_extract()

            elif values["-ACTION-"][0] == "Rotate":
                window.close()
                run_rotate()

        #if user made no choice: open a popup,
        #then go back to main window
        else:
            sg.popup("ERROR: no operation specified. Please choose one of the supported operations on PDF files")
