my_dict  = {
  "nama" : "bagus",
  "address" : "bali",
  "status" : "love"
}

print my_dict.keys()
print my_dict.values()

for key in my_dict:
  print key, my_dict[key]


evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x ** 2 for x in range(1, 12) if x % 2 == 0]

print even_squares

# kubik
cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
print cubes_by_four

to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]
# prints ['D', 'E']

print to_five[:2]
# prints ['A', 'B']

print to_five[::2]
# print ['A', 'C', 'E']

to_one_hundred = range(101)
# Add your code below!

backwards_by_tens = to_one_hundred [::-10]
print backwards_by_tens