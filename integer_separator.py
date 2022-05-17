def dynamic_integer_separator(number, n):
    str_num = str(number)
    num_list = []
    while str_num.isdigit():
        num_list.append(str_num[-n:])
        str_num = str_num[:-n]
    return ",".join(reversed(num_list))


dynamic_integer_separator(13858124533, 3)
"13,858,124,533"
