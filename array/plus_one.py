def plusOne(digits):
    str_int = ""
    for i in range(len(digits)):
        str_int += str(digits[i])
    total_str_int = str(int(str_int) + 1)
    output_int = []
    for i in range(len(total_str_int)):
        output_int.append(int(total_str_int[i]))
    return output_int