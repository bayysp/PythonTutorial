class Aritmatika():
    def tambah(self, n1, n2):
        hasilTambah = n1 + n2
        print("Hasil Tambah", hasilTambah)

    def kurang(self, n1, n2):
        hasilKurang = n1 - n2
        print("Hasil Kurang", hasilKurang)


class OperasiAritmatika(Aritmatika):
    def kali(self, n1, n2):
        hasilKali = n1 * n2
        print("Hasil Kali,", hasilKali)

    def kurang(self, n1, n2):
        super().kurang(n1, n2)  # super class of kurang() is Aritmatika.kurang() , send value to it


def main():
    aritmatika = OperasiAritmatika()

    aritmatika.kurang(10, 5)
    aritmatika.kali(2, 5)
    aritmatika.tambah(5, 5)


if __name__ == '__main__':
    main()
