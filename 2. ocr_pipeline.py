# from pdf to img

import pypdfium2 as pdfium # Documentation - (https://pypi.org/project/pypdfium2/)
import os

source_path = "D:\CCI_pdf_orders" # storing source path as a string

files = os.listdir()# returns all the pdf files of the folder in a list.

for i in files:
    file_path = os.path.join(source_path, i) # absolute path to all the files in the folder
    pdf = pdfium.PdfDocument(file_path)
    n_pages = len(pdf) # get the number of the pages in the pdf
    for page_number in range(n_pages):
        page = pdf.get_page(page_number)# get page from the pdf
        pil_image = page.render_topil(scale=1, optimise_mode=pdfium.OptimiseMode.NONE,) # converted that pdf page to img # scale = 1 equals 72 dpi resolution
        pil_image.save("{}_{}.png".format(i, page_number + 1))# saved that page with original name + page number

        
# Pytesseract operations on stored images
# method - pytesseract.image_to_string('image path')

import pytesseract
import os

# need tesseract executable in your PATH
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


source_path = "D:\CCI_orders_img" # contains all the order pages images. in Format: year_snum_onum.pdf_pagenum
##(snum - serial number, onum - order number, pagenumber)

os.chdir(source_path)

cci_img = os.listdir()

#len(cci_img) # total number of pages/images = 20327

output_location = "D:\CCI_OCR\cci_txt_tesseract"
 
# reads in the image file name and use it to create a new text file with modified name.
def convert_img_to_txt(img_name, text):
    output_path = "D:\CCI_OCR\cci_txt_tesseract"
    os.chdir(output_path)
    UID = img_name.split('.pdf')[0] + img_name.split('.pdf')[1][:-4] +".txt"
    fh = open(UID, "w", encoding = "utf=8")
    fh.write(text)
    fh.close()

# run the function on each img file
for i in cci_img:
    UID = i.split('.pdf')[0] + i.split('.pdf')[1][:-4] +".txt" #Format: year_snum_onum.pdf_pagenum
    img_path = os.path.join(source_path,i) # absolute path to the png file.
    txt = pytesseract.image_to_string(img_path)# text extraction from each png in the txt variable
    convert_img_to_txt(i, txt) 
    # create a new text file in a renamed format of :year_snum_onum_pgnum.txt in the  output location
# OCR 20327 pages

