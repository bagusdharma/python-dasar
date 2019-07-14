# struktur data python ada 3 yaitu
# 1. list -> [] = bisa berupa string, angka, object, dan lainnya. bahkan bisa terdapat list di dalam list.
#                 list dapat ditambah, dirubah data pada elemennya, hapus elemen dan hapus seluruh list.
# 2. dictionary -> {} = Pada dictionary terdapat 2 utama : key (pengenal), dan value (datanya). Key pada dictionary
#                         harus berupa tipe data yg tidak dapat diganti seperti tuple, string dan number
# 3. tuple -> () = elemen pada tuple tidak dapat diubah atau dihapus

list = ['adi','ugi','agi']

tuple = (0,1,2,3,4,5,6)

dictionary = {
    'nama' : ['bowo', 'agus', 'ajuns'],
    'email' : 'bowo@bow.id',
    'web' : 'bowo.id'
}

print list, tuple, dictionary

# akses elemen lewat indeks
print list[0]
print tuple[0]
print dictionary['nama']

# slicing indeks (akses beberapa elemen) [x:x] x pertama : start indeks, x kedua : end indeks
print list[1:1]
print tuple[0:6]

for x in list:
    print x

for i in dictionary:
    print i,':',dictionary[i],


print '\n'

# mengubah isi list, tuple, dan dictionary
list [0] = 'Dogi'
# tuple [0] = 28 -> tuple tidak dapat dirubah elemennya
dictionary['web'] = 'bowoselalu.id'
print list,  dictionary

print '\n'

# tambah data list, tuple, dictionary
tambah_list = list + ['blabar','goku','oke']
print tambah_list

tambah_tuple = tuple + (900,800,700)
print tambah_tuple

tambah_dictionary = {
    'telp' : '801821210',
    'alamat' : 'oekokeodke'
}
dictionary.update(tambah_dictionary)
print dictionary

print '\n'

# hapus data list, tuple, dictionary
del list [0]
# tuple tidak bisa dihapus
del dictionary['web']

print  list, dictionary

# fungsi-fungsi pada list, tuple, dictionary
# 1. max() = mencari nilai max
# 2. min() = mencari nilai min
# 3. cmp() = menghasilkan 3 nilai :
#             1. (-1) jika list pertama < list kedua
#             2. (0) jika list pertama = list kedua
#             3. (1) jika list pertama > list kedua
# 4. len() = menhitung jumlah elemen
# 5. tuple() = pengubahan dari list ke tuple
# 6. list() = pengubahan dari tuple ke list

list2 = list + ['aku', 'bahagia']
tuple2 = tuple + (100,200)
dictionary2 = {
    'alamat' : 'gunung juga',
    'web' : 'bowo.id'
}
dictionary.update(dictionary2)

# membandingkan yang lama dan baru
print '\n'
print 'list 1 :', list, '\nlist 2 : ', list2
print 'perbandingan list : ', cmp(list,list2)

# mengetahui panjang list, tuple, dictionary
print '\n'
print 'list :', len(list), '\ntuple : ', len(tuple), '\ndictionary : ', len(dictionary)

# mengubah list, tuple, dictionary menjadi string
print '\n'
print str(list), 'memiliki panjang karakter : ', str(len(list))
print str(tuple), '\nmemiliki panjang karakter : ', str(len(tuple))
print str(dictionary), '\nmemiliki panjang karakter : ', str(len(dictionary))


