# #
# # # print prime number from 1 to 100
# # primeNumlist = []
# # nonPrimelist= []
# # for i in range(2, 100):
# #     count = 0
# #     for j in range(1, i+1):
# #         if (i % j) == 0:
# #             count += 1
# #     if count == 2:
# #         primeNumlist.append(i)
# #     else:
# #         nonPrimelist.append(i)
# # print(nonPrimelist)
# # print(len(primeNumlist))
# #
# # # Factorial number
# # num = 8
# # fact=1
# # if num>0:
# #     for i in range(1, num+1):
# #         fact = fact*i
# #     print(fact)
#
# str1 = ' Hello I am sanju and I love myself'
# str2 = ' this is harhsa, he is stupid'
#
# jnvb = str1.replace(' ', '')
# print(jnvb)
# ist_from_str = list(jnvb)
# print((ist_from_str))
#
# # # join()
# # # separator_string.join(iterable)
# #
# # my_list = ['Hello', 'world', 'Python']
# # result = ' '.join(my_list)  # Joining with a space as separator
# # print(result)      # Hello world Python
# #
# # my_list = ['a', 'b', 'c']
# # result = ''.join(my_list)  # Joining with an empty string as separator
# # print(result)     # abc
#
# reverse_str = ''
# for char in ist_from_str[::-1]:
#     reverse_str += char
# print(reverse_str)
#
# # fibanacci series
# # 0 1 1, 2, 3 5 8 13 21
# a = 0
# b = 1
# sumd = 0  # a =b # a= 1 , b= sum # b= 1, sum = a+b, 2, a= 1 b=2 sum =3, a=2, b=3, sum =5
# for i in range(1, 10):
#     sumd = a + b
#     a = b
#     b =sumd
#     print(sumd)

# progress_perc = '66% complete'
# Val = progress_perc.split()
# numericVal = Val[0].strip('%')
# print(int(numericVal))


# def method(i=0):
#     i += 1
#     return i
#
# temp = []
# temp.append(method(
#        ))
# temp.append(method())
# temp.append(method())
# method(i=4)
# print(temp)

i = 1
