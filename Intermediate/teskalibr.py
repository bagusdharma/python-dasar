# # def foo(a,b,i,j,x=[]):
# #     k = j
# #     global ct
# #     ct = 0
# #     while k > i-1:
# #         if x[k] <= b and not (x[k] <= a):
# #             ct+=1
# #
# #         k-=1
# #
# # x = [11,10,10,5,10,15,20,10,7,11]
# # print foo(8,18,3,6,x)
# # print foo(x,10,20,0,8)
# # print foo(x,8,18,6,3)
#
# def g(str):
#     i = 0
#     global new_str
#     new_str = ""
#     while i < len(str)-1:
#         new_str = new_str + str[i+1]
#         i+=1
#
# def f(str=""):
#     if len(str) == 0:
#         return ""
#     elif len(str) == 1:
#         return str
#     else:
#         return f(g(str)) + str[0]
#
# def h(n, str):
#     while n != 1:
#         if n%2==0:
#             n = n/2
#         else:
#             n = 3*n + 1
#         str = f(str)
#     return str
#
# def pow(x, y):
#     if y == 0:
#         return 1
#     else:
#         return x * pow(x, y-1)
#
# print h(1,"fruits")
# # print h(2, 'fruits')
# # print h(5, 'fruits')
# print h(pow(2,1000000000000000), "fruits")

# a,b dapat dibagi k
# a = 1
# b = 10
# k = 3 hasil 3,6,9
#
# baris 1 = jumlah kasus T
# tiap kasus ada 3 a,b,k

# input = int(raw_input())
# for i in range(input):
#     a = int(raw_input())
#     b = int(raw_input())
#     k = int(raw_input())
#     hasil = [n**k for n in range(a,b)]
#     # for hasil in range(a,b):
#     #     hasil =
#
# print len(hasil)



