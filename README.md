# pdf_tools
This repository contains Python scripts that I use to operate on PDFs (merge, cut, extract, insert, ..). 
Since my PDF reader doesn't allow these operations and I don't want to relay on online tools, I decided to write some scripts myself.

The implementation is based on `PyPDF2`, a Python library to manipulate PDFs (see [https://pypi.org/project/PyPDF2/](https://pypi.org/project/PyPDF2/)).
It is a pure-Python library, which means that it doesn't depend on any external libraries.
You can install it with:

    pip install PyPDF2

## MergePDF.py
This script merges multiple PDFs by appending them.
It requires at least 2 input files. The output is in the same directory as the first input file with the name "merge_output.pdf".
To call the script:

    python MergePDF.py <file1> <file2> ... <fileN>
    
For example, using the `test` folder, `python MergePDF.py test/file1.pdf test/file2.pdf test/file3.pdf` outputs in `test/merge_output.pdf`.
