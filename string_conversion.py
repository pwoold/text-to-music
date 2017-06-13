def string_to_ascii(s):

    ascii_values = []
    for ch in s:
        ascii_values.append(ord(ch)%30)
        
    return ascii_values

print(string_to_ascii("hello"))