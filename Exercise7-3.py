#3.Char Swap

def swap_and_combine_strings(str1, str2):
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    return new_str1 + ' ' + new_str2

#Example
string1 = "hello"
string2 = "world"
result = swap_and_combine_strings(string1, string2)
print(result)