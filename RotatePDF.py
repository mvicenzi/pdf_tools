#!/usr/bin/python
import sys
import os.path
from PyPDF2 import PdfFileReader, PdfFileWriter

#This function rotates a single page:
#if positive, rotateCounterClockwise
#if negative, rotateClockwise
def RotatePage(page, rotation):

    if rotation < 0:
        rotation = -rotation
        newpage = page.rotateClockwise(rotation)
    else:
        newpage = page.rotateCounterClockwise(rotation)

    return newpage

#This function rotates a selection of PDF pages
def MultiRotate(filepath, rotation, pages, output_path):

    reader = PdfFileReader(filepath, strict=False)
    writer = PdfFileWriter()

    #get total number of pages
    numPages = reader.getNumPages()

    #for each selected page, check if valid
    for page_number in pages:
        if page_number > numPages:
            print("ERROR:",page_number,"is outside the document range 1 -",numPages)
            exit()

    #PDF pages go to 0 to numPages-1
    #pdf readers usually start at 1
    for index in range(0,numPages,1):
        page = reader.getPage(index)
        #check if page was selected to be rotated
        if index+1 in pages:
            page = RotatePage(page,rotation)
        writer.addPage(page)

    with open(output_path,"wb") as output_file:
        writer.write(output_file)

#MAIN FUNCTION
#read filepath, rotation and pages from command line
if __name__ == "__main__":

    if len(sys.argv) > 3:
        filepath = sys.argv[1]

        #if filename is wrong/not a file, stop here
        if os.path.isfile(filepath) == False:
            print ("ERROR:",filepath, "does not exist!")
            exit()

        #if the start page number is wrong/not int, stop here
        #accepts only rotatitions multiple of 90 degres
        if not (sys.argv[2].lstrip("-").isdigit() and int(sys.argv[2]) % 90 == 0):
            print ("ERROR:",sys.argv[2],"is not a valid rotation!")
            exit()
        rotation = int(sys.argv[2])

        #check that all pages are valid
        pages_str = sys.argv[3:]
        pages_num = []
        for page in pages_str:
            if page.isdigit():
                pages_num.append(int(page))
            else:
                print ("ERROR",page,"is not a page number")
                exit()

        #take the dir path of the first file
        abs_path_file = os.path.abspath(sys.argv[1])
        file_dir_path, filename = os.path.split(abs_path_file)
        filename, type = os.path.splitext(filename)
        output_path = os.path.join(file_dir_path,filename+"_rotated.pdf")

        MultiRotate(filepath, rotation, pages_num, output_path)

        print("Success!")
        print("Output written in",output_path)

    else:
        print("WARNING: specify the PDF filepath, a valid rotation (multiple of 90 degrees) and at least one page number!")
