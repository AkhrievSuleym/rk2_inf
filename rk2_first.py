"""RK_2"""
str_line = input("Введите строку: ")
numbers = ['0','1','2','3','4','5','6','7','8','9']
SUM_NUMBERS = 0
STR_END = ''
for item in str_line:
    if item in numbers:
        SUM_NUMBERS += int(item)
    else:
        STR_END += item

if STR_END == '':
    print(SUM_NUMBERS)
else:
    print(STR_END)
    