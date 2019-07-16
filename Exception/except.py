# angka = 29
#
# # menggunakan ZeroDivisionError
# try:
#     print angka/0
# except:
#     print 'proses kode gagal'
#
# print 'proses cetak masih dapat dijalankan'
#
# print '\n'
# try:
#     print angka/0
# except ZeroDivisionError, e:
#     print 'proses perhitungan gagal karena : ', e
#
# print 'proses cetak masih dapat dijalankan'
#
# # print angka/0 #kalau tidak pakai exception program langsung error tidak bisa jalan
#
# print '\n'
#
# # menggunakan IndexError dan KeyError
# sebuah_list = [1,2,3,4,5]
# sebuah_tuple = (1,2,3,4,5)
# dictionary = {
#     'nama' : 'Mango',
#     'email' : 'mango@mango.com'
# }
#
# try:
#     print sebuah_list[10]
# except IndexError, e:
#     print 'proses gagal karena : ', e
#
# print 'proses cetak masih dapat dijalankan\n'
#
# try:
#     print sebuah_tuple[10]
# except IndexError, e :
#     print 'proses gagal karena : ', e
#
# print 'proses cetak masih dapat dijalankan\n'
#
# try:
#     print dictionary['website']
# except KeyError, e:
#     print 'proses gagal karena : ', e
#
# print 'proses cetak masih dapat dijalankan\n'
#
# # menggunakan AttributeError -> muncul ketika class tidak memiliki attribut (variabel) yg diakses
#
# class PersegiPanjang:
#     panjang = 0
#     lebar = 0
#     def __init__(self, p, l):
#         self.panjang = p
#         self.lebar = l
#
# persegipanjang = PersegiPanjang(10,5)
#
# try:
#     print 'panjang : ', persegipanjang.panjang
#     print 'lebar : ', persegipanjang.lebar
#     print 'tinggi : ', persegipanjang.tinggi
# except AttributeError, e:
#     print 'proses gagal karena : ', e
#     print 'proses masih dapat dijalankan '
#
# # menggunakan exception IOError
# print '\n'
# try:
#     f = open('nilai.txt')
# except IOError, e:
#     print 'error karena : ', e
#
# print 'proses berjalan '
#
# print '\n'
#
# # menyusun multiple except
# try:
#     angka1 = int(raw_input('angka 1 = '))
#     angka2 = int(raw_input('angka 2 = '))
#
#     print 'hasil perhitungan angka = ', angka1/angka2
#
# except ZeroDivisionError, e:
#     print 'proses pembagian gagal karena = ', e
# except ValueError, e:
#     print '\nproses penghitungan gagal karena = ', e
#
# print '\n'
#
# # menggunakan multiple exception
# try:
#     angka3 = float(raw_input('masukkan angka : '))
#     angka4 = float(raw_input('masukkan angka lain : '))
#     print 'hasil = ', angka3/angka4
#
# except (ZeroDivisionError, ValueError, TypeError), e:
#     print 'perhitungan gagal karena error = ',e
#
# print '\n'
# # multiple except bersarang
# try:
#     angka5 = int(raw_input('angka 5 = '))
#     angka6 = int(raw_input('angka 6 = '))
#
#     try:
#         print 'hasil perhitungan angka = ', angka5 / angka6
#     except ZeroDivisionError, e:
#         print 'gagal perhitungan karena = ', e
#
#
# except ValueError, e:
#     print '\nproses gagal karena = ', e

# paling penting ini. membuat exception sendiri
print '\n'

class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value

    #pesan error yg didefinisikan menggunakan function __str__
    def __str__(self):
        s = 'tidak menerima angka kurang dari 0 ' + str(self.value)
        return s

def cekAngka(angka):
    if angka < 0:
        raise NegativeValueError(angka) #untuk memanggil exception menggunakan raise

try:
    sebuah_angka = int(raw_input('masukkan angka : '))
    cekAngka(sebuah_angka)
except(NegativeValueError, TypeError), e:
    print 'gagal karena : ', e


# menggunakan 'finally' pada try-except -> finaly digunakan untuk menentukan penangann apa yg harus dilakukan
# baik ketika exception muncul atau tidak
print '\n'
try:
    angka8 = float(raw_input('angka 8 = '))
    angka9 = float(raw_input('angka 9 = '))

    try:
        print 'hasil perhitungan angka = ', angka8 / angka9
    except ZeroDivisionError, e:
        print '\ngagal perhitungan karena = ', e


except ValueError, e:
    print '\nproses gagal karena = ', e
finally:
    print 'coba perhatikan kembali' #jadi hasilnya ketika program terkena exception atau tidak, tetap disimpan

print 'proses tetap berjalan '