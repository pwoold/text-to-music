def string_to_number(s):

    number_values = []
    for ch in s:
        number_values.append(ord(ch)%40)
        
    return number_values