# for i in ['aku','kamu','dia']:
#     print 'data untuk : ', i

for a in 'a,b,c,d,e':
    print a, 'huruf'

for b in range(1,10):
    print b

# untuk jarak space 2 -> sesuai urutan : angka start, angka end, step / jarak
print range(1,10,2)

# tidak bisa maka muncul angka pertama saja
print range(1,10,11)

# print angka menurun
print range(10,1,-1)

# bintang segitiga
for i in range(0,10):
    for j in range(0,i+1):
        if j==i:
            print 'x'
        else:
            print '*',
    print ''

# program mencari bilangan prima
for i in range(1,20):
    counter = 0
    for j in range(1, i+1):
        number = i%j
        # print number
        if number == 0:
            counter += 1
    if counter == 2:
        print i, 'adalah bilangan prima'
    else:
        print i, 'bukan prima'

# while
angka = 0
while (angka < 10):
    print 'aku sudah berjalan sebanyak ', angka, ' langkah'
    angka += 1

terus_tanya = True
while terus_tanya:
    temp = raw_input('masukkan angka kurang dari 10 : ')
    angka = int(temp)
    if angka < 10:
        terus_tanya = False #kenapa False ? karena ketika dia False maka keluar dari perulangan
    else:
        terus_tanya = True #ketika dia masih True akan terus melakukan perulangan

i = 1
count = 0
while i <= 10:
    print 'loop ke %d : %d + %d' % (i,i,count)
    count += i
    i+=1
print 'total angka yg dijumlah : ', count
