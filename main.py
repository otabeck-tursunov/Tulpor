# n = int(input("n = "))

# 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2 # n = 6
# range(n, 2n + 1)  (6, 7, 8, 9, 10, 11, 12)

# S = 0
# for i in range(n, 2*n + 1):
#     S += i**2
#
# print(S)


# S = 0
# for i in range(1, n + 1):
#     S += 1 / i
# print(S)


# for i in range(1, 6):  # (1, 2, 3, 4, 5)
# for j in range(1, i + 1):
#     print(j, end=" ")
# print()

sonlar = [12, 5, 90, 27, 3]

# for i in range(1, len(sonlar) + 1):
#     print(sonlar[-i])


# n = int(input("n = "))
# tub_son = True
# for i in range(2, n):
#     if n % i == 0:
#         tub_son = False
#         break
# if tub_son:
#     print("tub son")
# else:
#     print("tub son emas")

# for i in range(2, 51):
#     soni = 0
#     for j in range(2, i):
#         if i % j == 0:
#             soni += 1
#     if soni == 0:
#         print(i, end="  ")


f1 = 1
f2 = 1
# 1, 1, 2, 3, 5, 8, 13
# for i in range(1, 11):
#     if i == 1:
#         print(f1, end=" ")
#     elif i == 2:
#         print(f2, end=" ")
#     else:
#         f1, f2 = f2, f1 + f2
#         print(f2, end=" ")


# A = {4, 8, 9, 2, 1, 5, 7, 12, 3}
# B = {7, 5, 8, 1, 13}
#
# for i in B:
#     if i not in A:
#         print("B A ning bo'lagi emas!")
#         break
# else:
#     print("B A ning bo'lagi!")
