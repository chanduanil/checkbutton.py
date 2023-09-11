# def is_num(num):
#     if num % 2 == 0:
#         print("the number is even")
#     else:
#         print("the number is odd")
#
# num = int(input("enter the number"))

#print(is_num(num))
def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return f"{year} is a Leap year"
            else:
                return f"{year} is Not a Leap year"
        else:
            return f"{year} is a Leap year"
    else:
        return f"{year} is Not aaaa Leap year"
my_year = int(input('Enter your Year: '))

print(check_leap_year(my_year))