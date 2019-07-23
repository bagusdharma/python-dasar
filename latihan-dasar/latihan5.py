# angka 1-15 yg bisa dibagi 3/5
threes_and_fives = [x for x in range(1,16) if x %3 == 0 or x % 5 == 0]
print threes_and_fives

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-2]
print message

# filter "X"
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x: x!="X", garbled)
print message