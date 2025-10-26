# def to_roman(num):
#     answer = ''
#     roman_to_arabic = {
#         'I' :  1,
#         'V' : 5,
#         'X' : 10,
#         'L' : 50,
#         'C' : 100,
#         'D' : 500,
#         'M' : 1000
#     }
#     for key,values in reversed(roman_to_arabic.items()):
#         answer += (nu
#         num = int(num % key)
#     print(answer)
# to_roman(50)


def to_roman(num):
    answer = ''
    roman_to_arabic = {
        1 :  'I',
        4 : 'IV',
        5 : 'V',
        9 : 'IX',
        10 : 'X',
        44 : 'XLIV',
        50 : 'L',
        100 : 'C',
        500 : 'D',
        944 : 'CMXLIV',
        1000 : 'M'
    }
    for key, value in reversed(roman_to_arabic.items()):
        while num >= key:
            answer += value
            num = num - key
        else:
            continue
    return answer

print(to_roman(9))