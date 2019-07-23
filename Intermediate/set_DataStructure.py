# Set Data Structure berguna untuk check dalam list apakah ada yg duplikat atau tidak. bisa dengan 2 cara, yaitu:
# 1. Dengan Loop For

some_list = ['a','b','b','c','a','f']
duplicate = []
for value in some_list:
    # jadi ketika ada value yg berjumlah lebih dari 1 / duplikat
    if some_list.count(value) > 1:
        # kemudian jika valuenya tidak ada sebelumnya pada list 'duplicate', maka element itu di append ke list
        if value not in duplicate:
            duplicate.append(value)
print duplicate

# 2. dengan Set
print '\n'
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print duplicates

print '\n'
# Method lainnya pada Set -> Intersection = mencari yg valid / sama
valid = set(['yellow', 'red', 'green', 'black'])
input_set = set(['red', 'brown'])
print input_set.intersection(valid)

print '\n'
# Method lainnya pada Set -> Difference = mencari yg invalid
valid = set(['yellow', 'red', 'green', 'black'])
input_set = set(['red', 'brown'])
print input_set.difference(valid)

print '\n'

