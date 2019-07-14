# print 'masukan nama : '
# nama = raw_input('')
#
# print 'kondisi hati sekarang : '
# kondisi = int(raw_input())
#
# if kondisi > 90:
#     print 'senang'
# elif kondisi > 70 and kondisi < 90:
#     print 'biasa'
# else:
#     print 'sedih'


print 'masukan nama : '
nama = raw_input('')

print 'tulis situasi hati anda (senang, biasa, sedih) : '
situasi = raw_input('')

sit_sekarang = 'sedih'
kegiatan = 'dengar musik dan ngoding'

if situasi == sit_sekarang:
    print 'tulis kegiatan yang dilakukan : '
    keg_sekarang = raw_input('')
    if keg_sekarang == kegiatan:
        print 'sabar'
    else:
        print 'ketik lagi'
else:
    print 'anda bahagia dan atau biasa saja'