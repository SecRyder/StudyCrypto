# from Crypto.Util.number import *
# """
# x ≡ 2 mod 5
# x ≡ 3 mod 11
# x ≡ 5 mod 17
# """
# print((2*11*17*inverse(11*17,5) + 3*5*17*inverse(5*17,11) + 5*5*11*inverse(5*11,17)) % 935)# Dữ liệu
a = [2, 3, 5]       # các số dư
n = [5, 11, 17]     # các mô-đun (pairwise coprime)

# Chinese Remainder Theorem
N = 1
for ni in n:
    N *= ni

x = 0
for ai, ni in zip(a, n):
    Ni = N // ni
    # Tìm nghịch đảo của Ni mod ni
    inv = pow(Ni, -1, ni)
    x += ai * Ni * inv

result = x % N
print("Nghiệm a =", result)

