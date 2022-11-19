# a = [3, 4, 6, 10, 11, 18]
# b = [1, 5, 7, 12, 13, 19, 21]

# c = []

# while a and b:
#     if a[0] < b[0]:
#         c.append(a.pop(0))
#     else:
#         c.append(b.pop(0))

# print(c+b)
# a = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# b = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# a.extend(b)
# c = sorted(a)
# print(c)

# even = [num for num in range(20) if num%2==0]
# odd = [num for num in range(20) if num%2!=0]

# even.extend(odd)
# number = sorted(even)
# print(number)

# def fancy_generator():
#     my_list = [1,2, 3, 4, 5, 6]
#     for i in my_list:
#         yield i**2

# gen = fancy_generator()
# next(gen)
# print(str(next(gen))+" is 1st Number")
# print(str(next(gen))+" is 2nd Number")
# print(str(next(gen))+" is 3rd Number")
# print(str(next(gen))+" is 4th Number")
# print(str(next(gen))+" is 5th Number")
