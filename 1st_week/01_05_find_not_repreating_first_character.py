def find_not_repeating_first_character(string):
    not_repeating_char = "_"

    #O(N)
    alphabet_occurrence_array = find_alphabet_occurrence_array(string)

    # O(N)
    for char in string:
        if not char.isalpha():
            continue
        char_index = ord(char) - ord('a')
        if alphabet_occurrence_array[char_index] == 1:
            return chr(char_index + ord('a'))

    return not_repeating_char

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))