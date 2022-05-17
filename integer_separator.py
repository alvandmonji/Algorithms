def integer_separator(number):
    str_num = str(number)
    num_list = []
    while str_num.isdigit():
        num_list.append(str_num[-3:])
        str_num = str_num[:-3]
    return ",".join(reversed(num_list))


integer_separator(13858124533)
"13,858,124,533"
