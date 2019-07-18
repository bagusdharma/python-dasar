# mode manipulasi pada python :
# 1. r = membuka file dan hanya untuk pembacaan saja. pointer file akan ditempatkan di awal file.
# 2. w = membuka file dan hanya untuk penulisan saja. jika file yg dibuka sudah ada dan menggunakan mode 'w'
#         file akan ditimpa (rewrite). kalau tidak ada akan di buat
# 3. a = membuka file untuk penambahan isi file. pointer file akan ditempatkan di akhir file. jika file
#         tidak ada akan dibuat baru
# 4. b = mode ini akan ditambahkan masing-masing pada mode r,w,a menjadi 'rb', 'wb', 'ab'. maka pembacaan file dalam biner
# 5. + = mode ini juga ditambahkan pada masing-masing mode menjadi :
#         r+ = baca dan tulis
#         w+ = tulis dan baca
#         a+ = tambah dan baca

# Membuat file baru
try:
    sebuah_file = open('absen.txt', 'w')

    print 'nama file yg dibuat : ', sebuah_file.name
    print 'mode pembacaan : ', sebuah_file.mode
    print 'apakah file sudah ditutup : ', sebuah_file.closed

    sebuah_file.close()
    print 'apakah file sudah ditutup sekarang ? ', sebuah_file.closed
except IOError, e:
    print 'proses gagal karena : ', e

print '\n'

# Mengisi file
try:
    sebuah_file = open('absen.txt', 'w')
    print 'nama file yg dibuat : ', sebuah_file.name
    print 'mode pembacaan : ', sebuah_file.mode
    print 'apakah file sudah ditutup : ', sebuah_file.closed

    sebuah_file.write('1. Jajang dan Udin bersama \n')
    sebuah_file.write('2. aku dan kamu bersama \n')
    sebuah_file.write('3. namun terhalang ijin orang tua\n')

    sebuah_file.close()
    print 'apa file sudah tertutup ? ', sebuah_file.closed
except IOError, e:
    print 'gagal karena apa ? ', e

print '\n'

# Membaca File
try:
    sebuah_file = open('absen.txt', 'rb')
    print 'nama file yg dibuat : ', sebuah_file.name
    print 'mode pembacaan : ', sebuah_file.mode

    # fungsi read() melihat isi secara keseluruhan sekaligus, tapi ruang memori yg digunakan akan banyak
    print 'isi file : \n', sebuah_file.read()
    print 'posisi pointer pada file : ', sebuah_file.tell()

    sebuah_file.close()
except IOError, e :
    print 'gagal :', e

print '\n'
# untuk menghemat ruang memori dilakukan pembacaan file baris per baris
try:
    sebuah_file = open('absen.txt', 'rb')
    print 'nama file yg dibuat : ', sebuah_file.name
    print 'mode pembacaan : ', sebuah_file.mode

    print 'isi file : \n'

    for line in sebuah_file:
        print line

    print 'posisi pointer pada file : ', sebuah_file.tell()

    sebuah_file.close()
except IOError, e:
    print 'gagal karena ', e

print '\n'
# Mengatur posisi pointer file
try:
    sebuah_file = open('absen.txt', 'rb')
    print 'nama file yg dibuat : ', sebuah_file.name
    print 'mode pembacaan : ', sebuah_file.mode

    print 'isi file : \n'

    for line in sebuah_file:
        print line

    print 'posisi pointer pada file : ', sebuah_file.tell()

    # jika paramater pertama diisi 15 akan membaca dari pointter ke 15 ke kanan, jika -15 akan sebaliknya
    # jika parameter kedua diisi 0 : patokan berada di awal file
    #                            1 : patokan berada di tempat pointer berada
    #                            2 : patokan berada di akhir file
    print 'kembali lagi ke awal : ', sebuah_file.seek(10,0)

    print 'isi file : \n'

    # pada hasil nanti terlihat hasil dari pembacaan pointer akan mulai membaca dari point ke 10 kekanan
    for line in sebuah_file:
        print line

    print 'posisi pointer pada file : ', sebuah_file.tell()

    sebuah_file.close()
except IOError, e:
    print 'gagal karena ', e


print '\n'

# Mengganti nama file
import os

try:
    os.rename('absen.txt', 'rindu.txt')
    print 'nama sudah berubah'
except(IOError,OSError), e:
    print 'error',e

print '\n'

# menghapus file
import os

try:
    os.remove('absen.txt')
    print 'File sudah dihapus'
except(IOError, OSError), e:
    print 'gagal', e