import openpyxl

path = r"C:\New\write.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active

for r in range(1,7):
    for c in range(1,5):
        sheet.cell(row=r,column=c).value = "hello world"

workbook.save(path)

