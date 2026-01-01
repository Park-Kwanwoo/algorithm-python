from math import sqrt

input = 40


# 소수: 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수
# 풀이: 단순 반복
# def find_prime_list_under_number(number):
#     prime_list = []
#
#     for i in range(2, number + 1):
#         count = 0
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 count += 1
#         if count == 2:
#             prime_list.append(i)
#
#     return prime_list

# 소수: 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수
# 풀이: i의 제곱근보다 크지 않은 어떤 소수로도 나누어 떨어지지 않음
def find_prime_list_under_number(number):
    prime_list = []

    for i in range(2, number + 1):
        for j in prime_list:
            if j * j <= i and i % j == 0:
                break
        else:
            prime_list.append(i)

    return prime_list


result = find_prime_list_under_number(input)
print(result)
