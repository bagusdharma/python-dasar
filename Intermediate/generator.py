# 1. Iterable = sebuah objek di python yg mempunyai sebuah method __iter__ atau sebuah __getitem__ yg didefinisikan
#     yang mengembalikan sebuah 'iterator' atau dapat 'mengambil indeks'. Singkatnya iterable adalah objek apapun
#     yg dapat menyediakan kita sebuah 'iterator'.
#
# 2. Iterator = sebuah objek apapun pada python yg memiliki sebuah method next {python2} atau __next__ {python3}
#     yg didefinisikan.
#
# 3. Iteration = proses looping / memproses diri sendiri
#
# 4. Generators = iterator, tapi hanya dapat meng-iterasi sekali. karena mereka tidak menyimpan semua nilai di memory
#     Generators biasanya diimplementasi sebagai sebuah fungsi. tapi tidak mengembalikan nilai, melainkan menghasilkannya
#
# contoh generators

def generator_func():
    for i in range(10):
        yield i

for item in generator_func():
    print item

# generator fibo
def fibo(n):
    a = b = 1
    for i in range(n):
        yield a
        a,b = b,a + b

for x in fibo(10):
    print x

print '\n'
# fungsi next() python
# next() = mengijinkan untuk mengakses next element dalam sebuah sequence / urutan
def generator_func2():
    for i in range(3):
        yield i

gen = generator_func2()
print next(gen)
print next(gen)
print next(gen)
# disini error karena angka hanya sampe element ke 3
# print next(gen)

print '\n'
# fungsi iter() = mengembalikan sebuah objek iterator dari sebuah iterable, ketika sebuah 'int' tidak bisa di iterable
# maka dapat digunakan string

# int_var = 1779
# iter(int_var) #error int tidak bisa di iterable jadi pakai string

string = 'bagus'
my_iter = iter(string)
print next(my_iter)
print next(my_iter)