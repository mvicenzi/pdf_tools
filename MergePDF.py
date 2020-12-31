#!/usr/bin/python
import sys
import os.path
from PyPDF2 import PdfFileMerger

#This function appends all input files into one
#filepaths: list of input files
#output_path: path to output file
def AppendPDFs(filepaths, output_path):

    merger = PdfFileMerger()

    for path in filepaths:
        #bookmark: text of bookmark at the beginning of the appended pages
        #pages: specify range of pages to appended
        #import_bookmarks: bookmarks are kept when appending
        merger.append(path, bookmark=None, pages=None, import_bookmarks=True)

    merger.write(output_path)
    merger.close()

#MAIN FUNCTION
#read filepaths from command line
#(at least two of them are required)
if __name__ == "__main__":

    if len(sys.argv) > 2:
        filepaths = sys.argv[1:]

        #if filename is wrong/not a file stop here
        for filepath in filepaths:
            if os.path.isfile(filepath) == False:
                print ("ERROR:",filepath, "does not exist!")
                exit()

        #take the dir path of the first file
        abs_path_file = os.path.abspath(sys.argv[1])
        file_dir_path, filename = os.path.split(abs_path_file)
        filename, type = os.path.splitext(filename)
        output_path = os.path.join(file_dir_path,filename+"_merged.pdf")

        AppendPDFs(filepaths, output_path)

        print("Success!")
        print("Output written in",output_path)

    else:
        print("WARNING: specify at least 2 PDF filepaths when calling this script!")
