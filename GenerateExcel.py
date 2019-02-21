import pandas
from pandas import ExcelFile
from pandas import ExcelWriter


def main():
    workBook = pandas.read_csv('data_oprec.csv') #load a source data excel
    namaPendaftar = []
    angkatan = []
    nim = []
    divisi = []
    x=0

    # this loops is use to get a data from ax existing excel and put it into a list
    for i in workBook.index:
        namaPendaftar.append(workBook['Nama'][i])
        angkatan.append(workBook['Angkatan'][i])
        nim.append(workBook['NIM'][i])
        divisi.append(workBook['Pilihan Divisi'][i])

    #that list was contain array which is has a value of data_oprec.csv
    df = pandas.DataFrame(
        {
            'Nama' : namaPendaftar,
            'Angkatan' : angkatan,
            'NIM' : nim,
            'Divisi' : divisi
        }
    )

    writer = ExcelWriter('DataPendaftar.xlsx') #create a new file
    df.to_excel(writer, 'Sheet1', index=False) #put a value into new excel file
    writer.save() #save


if __name__ == '__main__':
    main()
