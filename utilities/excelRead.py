import xlrd
import os


def excelRead(selected_project):
    sp = selected_project
    print(sp)
    workbook = xlrd.open_workbook("d:\Automation\TestAutomationExcel\TestExcel.xls")
    sheet = workbook.sheet_by_name("Sheet1")

    # Get number of rows with data in excel sheet
    rowcount = sheet.nrows
    # Get number of columns with data in each row. Returns highest number
    colcount = sheet.ncols
    # print(rowcount)
    # print(colcount)

    result_data = []
    for curr_row in range(1, rowcount, 1):
        row_data = []
        # print (row_data)
        for curr_col in range(0, colcount, 1):
            # Read the data in the current cell
            # print (curr_col)
            data = sheet.cell_value(curr_row, curr_col)
            # print(data)
            row_data.append(data)
            # print(row_data)

        result_data.append(row_data)

    # print(result_data)

    for d in range(len(result_data)):
        if sp == result_data[d][0]:
            print(d+1,"-", result_data[d][1])