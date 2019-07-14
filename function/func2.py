# Pass by Reference dan Pass by Value
# by reference = jika mengubah argumen dalam fungsi maka nilai argumen yg direfrensi akan ikut berubah
def fungsi(sebuah_list):
    sebuah_list = [1,2,3,4,5]
    print sebuah_list

def fungsi2(sebuah_list):
    sebuah_list.append([10,20,30])
    print sebuah_list

ini_list = [10,20,30]
sebuah_list = [100,200,300]

# untuk ini_list perubahan hanya pada fungsi2
print ini_list
fungsi(ini_list)
print ini_list
print '\n'
print ini_list
print fungsi2(ini_list)
print ini_list


print '\n'

print sebuah_list
fungsi(sebuah_list) #ketika list diganti nilainya maka list yg ada diluar function tidak akan terpengaruh
print sebuah_list

print '\n'
print sebuah_list #sebelum fungsi dipanggil data nya masih sama
fungsi2(sebuah_list) #ketika fungsi dipanggil data pada sebuah_list mulai berubah dan berpengaruh ke selanjutnya
                     #tapi ketika menambah data baru dengan method pada function nilai diluar akan berubah
print sebuah_list

print '\n'

# Variable Scope Python
# Variabel Lokal = kondisi dimana variabel diakses secara lokal pada blok kode tertentu / bersifat universal jadi variabel bisa
# diakses dari blok kode manapun . untuk menjadikan global ada keyword bernama global untuk merujuk kode diluar blok

def sebuah_fungsi():
    angka = 10
    print 'angka pada func sebuah_fungsi bernilai : ', angka

def sebuah_fungsi2():
    global angka
    angka = 14
    print 'angka pada func sebuah_fungsi2 bernilai : ', angka

angka = 900
print 'sebelum panggil func sebuah_fungsi : ', angka
sebuah_fungsi()
print 'sesudah panggil func : ', angka

print '\n'

print 'sebelum panggil func sebuah_fungsi2 : ', angka
sebuah_fungsi2()
print 'sesudah panggil func : ', angka #angka sudah berubah setelah dipanggil fungsi karena angka diberika var global
                                        # jadi ketika angka diubah nilainya, nilai pada variabel angka yg berada diluar
                                        # blok function juga ikut berubah (berubah untuk seterusnya)
