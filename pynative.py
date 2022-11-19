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

num = [12, 75, 243, 281, 9, 31, 790, 901, 1252]
for i in num:
    if i > 790:
        continue
    elif i < 1252:
        break
    elif i % 3 == 0:
        print(i)
    

print(num)