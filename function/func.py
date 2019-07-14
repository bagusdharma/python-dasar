def fungsi_tanpa_param():
    for i in range(1,10):
        print i

fungsi_tanpa_param()

def fungsi_parameter(batas_akhir):
    for i in range(1, batas_akhir):
        print 'looping ke : ', i

fungsi_parameter(100)


# fungsi dengan return
def fungsi_tanpa_param2():
    temp = 0
    for x in range(1,5):
        temp = temp + x
    return temp

print fungsi_tanpa_param2()


def fungsi_parameter2(batas_akhir):
    temp = 0
    for i in range(1, batas_akhir):
        # print 'looping ke : ', i
        temp += i
    return temp

print fungsi_parameter2(10)

# default argumen pada python -> argumen yg sudah diisi nilainya terlebih dahulu jika argumen tersebut tidak
#     diberikan saat memanggil function
def cetak_biodata(nama, kota, umur=18):
    print 'nama : ', nama
    print 'kota : ', kota
    print 'umur : ', umur
    return

# kalau diisi semua
cetak_biodata('ayu', 'bandung', 90)
# kalau tidak diisi semua
cetak_biodata('gekin', 'bali')

# Variable length arguments -> ketika kita ingin membuat sebuah function yang memiliki argumen yg dinamis
# disebut juga argumen yang tidak utama, pada python ditandai dengan '*' pada argumen terakhir. harus disimpan diakhir
# setelah argumen biasa dan default argument. jika disimpan di awal akan error (sintaks error)
def cetak_nilai(nama, twitter, *scores):
    print 'nama : ', nama
    print 'twitter : ', twitter
    print 'score nya '
    i = 1
    for score in scores:
        print 'nilai ke %d : %d' % (i, score)
        i += 1
    return

# kalau parameter diisi semua
print 'dengan adanya variable length argument, variable sisa akan jadi tuple : '
cetak_nilai('gun', 'gunzzz', 90,80,90,10,1,1,2,2,2,2,2,4)
#argumen utama adalah gun dan gunzzz (nama dan twitter) jika dimasukkan nilai setelahnya akan dikumpulkan ke wadah
# (*scores) dan ditampung menjadi list yang dimasukkan setelah nama dan twitter

# Keyword length argument -> menampung argument berlebih ketika diberikan kepada function yg dipanggil.
# akn diterima dalam bentuk dictionary dengan tanda '**'

def cetak_nilai2(nama, twitter, **data_tambahan):
    print 'nama : ', nama
    print 'twitter : ', twitter
    print 'Data Tambahan : '
    i = 1
    for data in data_tambahan:
        print '%s : %s' %(data, data_tambahan)
    return

# kalau parameter diisi semua
cetak_nilai2('gun', 'gunzzz', email='bogo@boogo', telp='013018301')


