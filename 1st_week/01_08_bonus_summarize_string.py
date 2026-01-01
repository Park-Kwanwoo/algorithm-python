# 문자열 요약하기
# EX)
# abc      a1/b1/c1
# aaabbbc  a3/b3/c1
# abbbc	   a1/b3/c1
# ahhhhz   a1/h4/z1
# acccdeee a1/c3/d1/e3
from itertools import count


# 풀이: 앞의 값과 비교 후 다르면 문자 + count 후, count 초기화 및 반복
def summarize_string(string):
    answer = ""
    n = len(string)
    count = 1

    for i in range(n - 1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            answer += string[i]
            answer += str(count)
            answer += '/'
            count = 1
    answer += string[n - 1] + str(count)
    return answer

result = summarize_string("abc")
print("정답 = a1/b1/c1", result)
result = summarize_string("aaabbbc")
print("정답 = a3/b3/c1", result)
result = summarize_string("ahhhhz")
print("정답 = a1/h4/z1", result)
result = summarize_string("acccdeee")
print("정답 = a1/c3/d1/e3", result)
