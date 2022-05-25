#!/usr/bin/python
import sys
import os.path
from PyPDF2 import PdfFileReader, PdfFileWriter

#This function extracts pages from a PDF
def ExtractPDFs(filepath, start_page_number, end_page_number, output_path):

    reader = PdfFileReader(filepath, strict=False)
    writer = PdfFileWriter()

    numPages = reader.getNumPages()
    if start_page_number > numPages:
        print("ERROR: start page",start_page_number,"is outside the document range 1 -",numPages)
        exit()

    if end_page_number > numPages:
        print("WARNING: end page",end_page_number,"is outside the document range 1 -",numPages)
        end_page_number = numPages
    elif end_page_number == -1:
        end_page_number = numPages

    #page numbers go to zero to numPages-1
    #pdf readers usually start at 1
    start_page_number = start_page_number-1
    end_page_number = end_page_number-1

    for index in range(start_page_number,end_page_number+1,1):
        page = reader.getPage(index)
        writer.addPage(page)

    with open(output_path,"wb") as output_file:
        writer.write(output_file)

#MAIN FUNCTION
#read filepath and page range from command line
#(at least the start page number is required)
if __name__ == "__main__":

    if len(sys.argv) > 2:
        filepath = sys.argv[1]

        #if filename is wrong/not a file, stop here
        if os.path.isfile(filepath) == False:
            print ("ERROR:",filepath, "does not exist!")
            exit()

        #if the start page number is wrong/not int, stop here
        if not sys.argv[2].isdigit():
            print ("ERROR:",sys.argv[2],"is not a page number!")
            exit()
        start_page_number = int(sys.argv[2])

        #if the end page number is not specified, go on
        #if it is specified but wrong/not int, stop here
        end_page_number = -1
        if len(sys.argv)>3:
            if sys.argv[3].isdigit():
                end_page_number = int(sys.argv[3])
            else:
                print ("ERROR",sys.argv[3],"is not a page number")
                exit()

        #take the dir path of the first file
        abs_path_file = os.path.abspath(sys.argv[1])
        file_dir_path, filename = os.path.split(abs_path_file)
        filename, type = os.path.splitext(filename)
        output_path = os.path.join(file_dir_path,filename+"_extracted.pdf")

        ExtractPDFs(filepath, start_page_number, end_page_number, output_path)

        print("Success!")
        print("Output written in",output_path)

    else:
        print("WARNING: specify the PDF filepath and at least the starting page number!")
