# Ternary Operator = biasanya disebut dengan conditional expression. Operator ini meng-evaluasi sesuatu berdasarkan pada
# sebuah kondisi menjadi True or not

# sintaks  : condition_if_true if condition else condition_if_false
# contoh

is_nice = True
state = 'nice' if is_nice else 'not nice'
# hasil tergantung dari operator, true / False
print state

print '\n'
# contoh lain yang lebih tidak jelas dan tidak banyak digunakan adalah tuple
# sintaks : (if_test_is_false, if_test_is_true)[test]

nice = True
personality = ('mean', 'nice')[nice]
print 'bagus is a '+ personality + ' person'

# contoh lain
print '\n'
kondisi = True
print (2 if kondisi else 1/0)
