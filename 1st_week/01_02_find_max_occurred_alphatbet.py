# def find_max_occurred_alphabet(string):

#     alpha_array = find_alphabet_occurrence_array(string)
    
#     # 1. 첫 번째 인덱스를 최대 값으로 가정
#     max_num = alpha_array[0]
#     idx = 0
#     result_idx = 0
#     # 2. 인덱스 별로 값을 비교하여 최대 값을 찾음
#     for alpha in alpha_array:
#         if max_num < alpha:
#             max_num = alpha
#             result_idx = idx + ord('a')

#         idx += 1
    
#     # 3. 해당 인덱스의 알파벳 값을 리턴
#     return chr(result_idx)


def find_max_occurred_alphabet(string):

    alpha_array = find_alphabet_occurrence_array(string)
    
    # 1. 첫 번째 인덱스를 최대 값으로 가정
    max_num = alpha_array[0]
    max_alphabet_index = 0
    
    # 2. 인덱스 별로 값을 비교하여 최대 값을 찾음
    for i in range(len(alpha_array)):
        if max_num < alpha_array[i]:
            max_num = alpha_array[i]
            max_alphabet_index = i
    
    # 3. 해당 인덱스의 알파벳 값을 리턴
    return chr(max_alphabet_index + ord('a')) 



def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))
