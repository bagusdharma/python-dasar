my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

# same as
def by_three(x):
  return x % 3 == 0

# print range 30-70 dari pangkat 2
squares = [x ** 2 for x in range (1,11)]
x= filter(lambda x: x in range(30,70), squares)
print x