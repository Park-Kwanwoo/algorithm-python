import re

# 접근: 주어진 입력 값을 1의 구간과 0의 구간으로 분리 후, 적은 구간을 가진 쪽을 리턴
# def find_count_to_turn_out_to_all_zero_or_all_one(string):
#     one_array = re.split(r'[0:]', string)
#     zero_array = re.split(r'[1:]', string)
#
#     one_count = 0
#     zero_count = 0
#     for char in one_array:
#         if char != "":
#             one_count += 1
#     for char in zero_array:
#         if char != "":
#             zero_count += 1
#
#     return min(one_count, zero_count)

# 접근: 0 -> 1 or 1 -> 0 이 되는 경우를 각각 계산 후, 최소 값을 리턴
# def find_count_to_turn_out_to_all_zero_or_all_one(string):
#     zero_count = 0
#     one_count = 0
#
#     for i in range(0, len(string)):
#         if string[i] == "0":
#             continue
#         else:
#             if string[i - 1] == "0":
#                 zero_count += 1
#
#     for i in range(0, len(string)):
#         if string[i] == "1":
#             continue
#         else:
#             if string[i - 1] == "1":
#                 one_count += 1
#
#     return min(zero_count, one_count)

# 개선된 코드
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count = 0
    flag = False

    for i in range(len(string)):
        if i == 0:
            continue
        if string[i] != string[i-1]:
            if flag:
                flag = False
            else:
                count += 1
                flag = True

    return count

result = find_count_to_turn_out_to_all_zero_or_all_one("0001100")
print(result)
result = find_count_to_turn_out_to_all_zero_or_all_one("11111")
print(result)
result = find_count_to_turn_out_to_all_zero_or_all_one("00000001")
print(result)
result = find_count_to_turn_out_to_all_zero_or_all_one("11001100110011000001")
print(result)
result = find_count_to_turn_out_to_all_zero_or_all_one("11101101")
print(result)