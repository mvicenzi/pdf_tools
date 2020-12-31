# pdf_tools
This repository contains Python scripts that I use to operate on PDFs (merge, cut, extract, insert, ..).
Since my PDF reader doesn't allow these operations and I don't want to relay on online tools, I decided to write some scripts myself.

The implementation is based on `PyPDF2`, a Python library to manipulate PDFs (see [https://pypi.org/project/PyPDF2/](https://pypi.org/project/PyPDF2/)).
It is a pure-Python library, which means that it doesn't depend on any external libraries.
You can install it with:

    pip install PyPDF2

## MergePDF.py
This script merges multiple PDFs by appending them.
It requires at least 2 input files. The output is in the same directory as the first input file with the name <file1>_merged.pdf".
To call the script:

    python MergePDF.py <file1> <file2> ... <fileN>

For example, using the `test` folder, `python MergePDF.py test/file1.pdf test/file2.pdf test/file3.pdf` outputs in `test/file1_merged.pdf`.

## ExtractPDF.py
This script extracts pages from an existing PDF.
It requires an input file and the range of pages to be extracted (start and end page number). If the end page number is not specified, the pages are extracted from the staring page to the end of the document.
The output is in the same directory as the input file with the name "<file>_extracted.pdf".
To call the script:

    python ExtractPDF.py <file> <start page number> <end page number (optional)>

For example, using the `test` folder, `python ExtractPDF.py test/file1.pdf 12 15` outputs in `test/file1_extracted.pdf` pages from 12 to 15 included. While `python ExtractPDF.py test/file1.pdf 12` outputs pages from 12 to the end of the document.

## RotatePDF.py
This script rotates pages in an existing PDF.
It requires an input file, a valid rotation and the list of pages (at least one) to be rotated. Rotations are valid only if multiple of 90 degrees: `90 180 270 ...` are valid counter-clockwise rotations, while `-90 -180 -270` are valid clockwise rotations. The output is in the same directory as the input file with the name "<file>_rotated.pdf".
To call the script:

    python RotatePDF.py <file> <rotation> <page1> <page2> ... <pageN>

For example, using the `test` folder, `python RoatePDF.py test/file1.pdf -180 12 15` outputs in `test/file1_rotated.pdf` with pages 12 and 15 rotated clockwise of 180 degrees.
