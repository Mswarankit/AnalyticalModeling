# print 10 numbers in while loop
# i = 1
# while i < 10:
#     print(i)
#     i+=1


# print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5    

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()


# calculate the sum of all numbers from 1 to given numberss
# n = int(input("Enter the number you want whole sum: "))
# sum1 = 0
# for i in range(1, n+1):
#     sum1 += i

# print(sum1)

# Write a program to print multiplication of three numbers in concurrency
# num = [2,3,4,5,6]
# num = [i*x for i in num for x in range(1,11)]

# print(num)

# num = [12, 75, 243, 281, 9, 31, 790, 901, 1252]
# for i in num:
#     if i > 790:
#         continue
#     elif i < 1252:
#         break
#     elif i % 3 == 0:
#         print(i)
    

# # print(num)
# num = int(input())
# counter = 0
# while num != 0:
#     num = num // 10 # floor division of the number so only integer value I will recieve 
#     counter+=1

# print(counter)

# num = (input())
# length = len(num)
# print(length)
# len function only work with str

# let's check that the number is palindrome
# 1. take the input of num 
# 2. get the reverse the len

# reverse the number
# n = int(input())
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
    # print()


# print list in reverse order
# list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# size = len(list1)
# for i in range(size -1, 0, -1):
#     print(list1[i])

list1 = [i*x for i in range(5,2, -1) for x in range(1,11)]
print(list1)
list1.reverse()
print(list1)

# li = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# li.reverse()
# print(li)

