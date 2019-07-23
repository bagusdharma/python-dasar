# Decorators adalah sebuah bagian penting python. simpelnya ada fungsi untuk memodifikasi fungsionalitas dari fungsi
# lainnya. membantu untuk membuat code kita lebih singkat dan baik.
# contoh :

def hi(name='bagus'):
    return 'hai ' + name
print hi()

greet = hi

print greet()

print '\n'
# Mendefinisi Fungsi di dalam Fungsi

def halo(name='bagus'):
    print 'masuk fungsi halo'
    def boy():
        print 'masuk fungsi boy'
    def man():
        print 'masuk fungsi man'
    print boy()
    print man()
    print 'kembali ke fungsi'

halo()
print '\n'
# Mereturn fungsi dari dalam fungsi
def halo(name='bagus'):
    print 'masuk fungsi halo'

    def boy():
        print 'masuk fungsi boy'

    def man():
        print 'masuk fungsi man'

    def girl():
        print 'masuk fungsi girl'

    if name == 'bagus':
        return boy
    elif name == 'nin':
        return girl
    else:
        return man

a = halo()
print a()
print '\n'
print halo()() #cara lain

print '\n'
# Memberikan fungsi sebuah argumen ke fungsi lainnya
def hay():
    print 'nin'

def doSomethingBeforeHay(func):
    print 'will be miss you'
    print func()

doSomethingBeforeHay(hay)
# jadi decorator berfungsi mengubah fungsi sebelum dan sesudah