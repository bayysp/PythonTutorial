from builtins import print

import pandas
import re
from pandas import ExcelWriter
from pandas import ExcelFile


def main():
    workBook = pandas.read_excel('PendaftarITC2019.xlsx')

    print("Column Headings : ")
    print(workBook.columns)
    delapanBelas = 0
    tujuhBelas = 0
    webDev = 0
    androidDev = 0
    pm = 0
    pr = 0

    for i in workBook.index:
        if workBook['Angkatan'][i] == 2018:
            delapanBelas = delapanBelas + 1;
        else:
            tujuhBelas = tujuhBelas + 1

    for i in workBook.index:
        getDiv = workBook['Divisi'][i]
        if re.search("Web Development", getDiv):
            webDev = webDev+1

        if re.search("Android Development", getDiv):
            androidDev = androidDev+1

        if re.search("Human Resource Project Manager", getDiv):
            pm = pm +1

        if re.search("Human Resource Public Relation", getDiv):
            pr = pr + 1

    print("Delapan Belas : {}".format(delapanBelas))
    print("Tujuh Belas : {}".format(tujuhBelas))
    print("\nAndroid Dev : {}".format(androidDev))
    print("Web Dev : {}".format(webDev))
    print("Project Manager : {}".format(pm))
    print("Public Relation : {}".format(pr))


if __name__ == '__main__':
    main()
