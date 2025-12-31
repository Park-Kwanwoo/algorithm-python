def find_max_plus_or_multiply(array):
    plus_or_multipy_sum = array[0]
    for j in range(1, len(array)): # 시간 복잡도: O(N)
        plus_or_multipy_sum = max(plus_or_multipy_sum + array[j], plus_or_multipy_sum * array[j])

    return plus_or_multipy_sum


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))