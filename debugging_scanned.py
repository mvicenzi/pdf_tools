from PyPDF2 import PdfFileMerger

path1 = "test/test_scanned.pdf"
path2 = "test/file1.pdf"

merger = PdfFileMerger()
merger.append(path1, bookmark=None, pages=None, import_bookmarks=True)
merger.append(path2, bookmark=None, pages=None, import_bookmarks=True)

merger.write("test/output_debug_scanned.pdf")
merger.close()
