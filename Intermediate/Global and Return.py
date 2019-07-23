def add (value1, value2):
    return value1 + value2

result = add(3,5)
print result

# bisa dengan global
def add2(value1, value2):
    global hasil
    hasil = value1+value2

add2(3,5)
print hasil

print '\n'
# Multiple return value
def profile():
    global name
    global age
    name = 'bagus'
    age = 21
#jangan pakai seperti ini
profile()
print name, age

# solusi
def profile2():
    name='bagus'
    age = 21
    return name, age

profile_data = profile2()
print profile_data[0]