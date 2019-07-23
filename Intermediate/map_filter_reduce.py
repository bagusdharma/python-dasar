# 1. Map = fungsi map berlaku ke semua items dalam sebuah input_list
# sintaks = map(function_to_apply, list_input)
# contoh :
# biasanya kita ingin pass semua list elemen ke sebuah fungsi satu-demi-satu dan mengambil output

item = [1,2,3,4,5]
square = []
for i in item:
    square.append(i**2)

print square

print '\n'
# map memperbolehkan kita meng-implement fungsi ini dengan lebih mudah dan lebih baik
items = [1,2,3,4,5]
squared = list(map(lambda x: x**2, items))
print squared #hasil sama

print '\n'
# contoh untuk list_function
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

func = [multiply, add]
for a in range(5):
    value = list(map(lambda x:x(a), func))
    print value

print '\n'

# 2. Filter = membuat sebuah list elemen untuk sebuah fungsi yg mengembalikan nilai True
# contoh
number_list = range(-5,5)
less_than_zero = list(filter(lambda x:x<0, number_list))
print less_than_zero #hasil mengembalikan semua list elemen yg kurang dari 0 (True)

print '\n'
# 3. Reduce = fungsi yg sangat berguna untuk perform beberapa komputasi dalam sebuah list dan mengembalikan hasil.
#             itu berlaku perhitungan bergulir untuk pasangan nilai berurutan dalam daftar. contoh jika ingin mengkomputasi
#             produk dalam sebuah list integer

# normal way
product = 1
my_list = [1,2,3,4]
for num in my_list:
    product *= num
print product

#reduce
from functools import reduce
product = reduce((lambda x, y: x*y), [1,2,3,4])
print product

print '\n'
