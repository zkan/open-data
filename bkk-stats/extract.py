import pdfplumber

pdf = pdfplumber.open('stat_2559_thai.pdf')

page175 = pdf.pages[196].extract_table()
print(page175)

page294 = pdf.pages[315].extract_table()
print(page294)
