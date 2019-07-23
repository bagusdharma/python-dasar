# Penggunaan *args
# *args dan **kwargs memperbolehkanmu untuk pass argumen variabel angka ke sebuah fungsi.
# variabel yang dimaksud disini adalah kita tidak tau sebelumnya berapa banyak argumen yg dapat di pass ke fungsi oleh
# user jadi disini menggunakan *args atau **kwargs. *args digunakan untuk mengirim sebuah list argumen variabel panjang
# non-keyword ke fungsi
# contoh :
def test_var_args(f_arg, *argv):
    print 'first normal arg : ', f_arg
    for arg in argv:
        print 'another arg through *argv : ', arg

test_var_args('yassoob', 'pthon', 'eggs', 'test')

print '\n'
# Penggunaan **kwargs
# **kwargs memperbolehkanmu untuk pass panjang argumen variabel keyworded ke sebuah fungsi. harus menggunakan **kwargs
# jika ingin menghandle named arguments dalam sebuah fungsi. contoh:
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print '{0} = {1}'.format(key,value)

greet_me(name="bagus") #harus memasukkan keyword dulu contoh disini memasukkan key -> name, valuenya -> bagus

print '\n'
# Penggunaan *args dan **kwargs untuk memanggil sebuah fungsi
def tes_args_kwargs(arg1, arg2, arg3):
    print 'arg 1 : ', arg1
    print 'arg 2 : ', arg2
    print 'arg 3 : ', arg3

# with *args
args = ('aku', 'dan', 'kamu')
tes_args_kwargs(*args)
print '\n'

# with kwargs
kwargs = {'arg1' : 'sangat', 'arg2' : 'rindu', 'arg3' : 'kamu'} #harus sesuai dengan parameternya
tes_args_kwargs(**kwargs)

# Debug
# bisa dengan cara python -m pdb namafile.py
import pdb
def make_bread():
    pdb.set_trace()
    return 'dont have you'

print make_bread()

# command pdb :
# 1. c = continue execution
# 2. w = shows the context of the current line it is executing
# 3. a = print list argument pada fungsi sekaraang
# 4. s = execute curent line and stop at the first possible occasion
# 5. n = continue execute sampai line berikutnya yg dicari dalam fungsi sekarang atau akan mereturn
