# pdf_tools
This repository contains Python scripts that I use to operate on PDFs (merge, extract/split, rotate, ...). They can be use directly from the command terminal or via a user-friendly interactive GUI.

## Requirements
The scripts are based on `PyPDF2`, a Python library to manipulate PDFs (see [https://pypi.org/project/PyPDF2/](https://pypi.org/project/PyPDF2/)). You can install it with:

    pip install PyPDF2

The GUI is based on `PySimpleGUI`, a simple Python interface for several GUI frameworks (see [https://pypi.org/project/PySimpleGUI/](https://pypi.org/project/PySimpleGUI/)). You can install it with:

    pip install pysimplegui

## Usage
### Interactive GUI
The interactive GUI can be launched simply with:

    python run_GUI.py

The user is then guided through the available operations. File browsers and error popups support the user while selecting different options.

The GUI can also be made into a single `.EXE` file for Windows (read more [here](https://pysimplegui.readthedocs.io/en/latest/#creating-a-windows-exe-file)). This file is already available as [dist/PDF_Tools.exe](/dist).

### Scripts via command terminal
#### MergePDF.py
This script merges multiple PDFs by appending them.
It requires at least 2 input files. The output is in the same directory as the first input file with the name <file1>_merged.pdf".

    python MergePDF.py <file1> <file2> ... <fileN>

#### ExtractPDF.py
This script extracts pages from an existing PDF.
It requires an input file and the range of pages to be extracted (start and end page number, to be included). If the end page number is not specified, the pages are extracted from the starting page to the end of the document.

    python ExtractPDF.py <file> <start page number> <end page number (optional)>

#### RotatePDF.py
This script rotates pages in an existing PDF.
It requires an input file, a valid rotation and the list of pages (at least one) to be rotated. Rotations are valid only if multiple of 90 degrees: `90 180 270 ...` are valid counter-clockwise rotations, while `-90 -180 -270 ...` are valid clockwise rotations. The output is in the same directory as the input file with the name "<file>_rotated.pdf".

    python RotatePDF.py <file> <rotation> <page1> <page2> ... <pageN>
