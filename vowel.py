# str  = input("enter the letter:")
# str = str.lower()
# if len(str)<2:
#     if str == 'a' or str == 'e' or str == 'i' or str == 'o' or str == 'u':
#         print("entered letter is vowel")
#         print(f"{str.upper()}")
#     else:
#         print("entered letter is consonant")
# else:
#     print("enter the letter is invalid")

def vow_let(str):
    if len(str)<2:
        if str == 'a' or str == 'e' or str == 'i' or str == 'o' or str == 'u':
            print("entered letter is vowel")
            print(f"{str.upper()}")
        else:
            print("consonent")
    else:
        print("not vowel")

str  = input("enter the letter:")
print(vow_let(str))