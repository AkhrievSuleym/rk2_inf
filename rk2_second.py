"""RK_2"""
numbers = ['0','1','2','3','4','5','6','7','8','9']
SUM_NUMBERS = 0
STR_END = ''
with open('stdin.txt', 'w', encoding = 'utf8') as file_first:
    file_first.write(input("Введите строку: "))

with open('stdin.txt', 'r', encoding = 'utf8') as file_first, open('stdout.txt', 'w', encoding = 'utf8') as file_second:
    str_line = file_first.read()
    for item in str_line:
        if item in numbers:
            SUM_NUMBERS += int(item)
        else:
            STR_END += item
    if STR_END == '':
        file_second.write(str(SUM_NUMBERS))
    else:
        file_second.write(STR_END)
