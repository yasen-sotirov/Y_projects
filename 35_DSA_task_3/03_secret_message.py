"Secret Message" #
"""
You want to exchange some secret messages between you and your friends, 
so you decide to encode them using a simple but yet powerful rule: 
n{encoded_text}, where the encoded_text in the curly brackets is 
repeated exactly n times.

Your job is to write a program which decodes the messages. 
Examine the sample tests below.

Input
    Read from the standard input
    On the single line you will find the encoded message

Output
    Print to the standard output
    On the single line print the decoded message

Constraints
    1 <= n <= 100
    encoded_text contains only small letters from "a" to "z"


    Input
4{a}2{xz}

    Output
aaaaxzxz

    Input
2{z10{xy}}

    Output
zxyxyxyxyxyxyxyxyxyxyzxyxyxyxyxyxyxyxyxyxy


    Input
a3{cd2{a}f}ef

    Output
acdaafcdaafcdaafef
"""

# a3{cd2{a}f}ef
# input_str = input()

def recursion(sequence, multiplier):
    letters = ""

    if not sequence:
        return letters

    for index, el in enumerate(sequence):
        if el.isnumeric():
            multiplier_ind = index
            return letters + recursion(sequence[multiplier_ind + 2:], int(el))

        elif el.isalpha():
            letters += el

        elif el == "}":
            letters *= multiplier
            return letters

input_str = "a3{cd2{abc}f}ef"
print(recursion(input_str, 1))




# def flatten(lst):
#     output = []
#     # проверява дали елемента е число или списък
#     for el in lst:
#         if isinstance(el, int):
#             output.append(el)
#         else:
#             output.extend(flatten(el))
#     return output
#
# values = [1, [2, [[[3, [4, [5, [6]]]], 7], 8], 9]]
# print(flatten(values))





