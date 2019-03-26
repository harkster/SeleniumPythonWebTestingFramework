import xlrd


def get_data(file, sheet_name):
    val = []
    excel_file = xlrd.open_workbook(file)
    sheet = excel_file.sheet_by_name(sheet_name)

    rows = sheet.get_rows()

    for i in range(rows):
        val.append(sheet.cell(i, 0).value)
        val.append(sheet.cell(i, 1).value)
    return val
