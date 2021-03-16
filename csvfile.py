import csv


# 第一行文件不读取

def getCsvData(filename):
    value_rows = []
    with open(filename, encoding='UTF-8') as file:
        f_csv = csv.reader(file)
        next(f_csv)
        for r in f_csv:
            value_rows.append(r)
    return value_rows


print(getCsvData('username.csv'))
