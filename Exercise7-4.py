#4.Replace Char

def replace_first_char_occurrences(input_string):
    first_char = input_string[0]
    return first_char + input_string[1:].replace(first_char, '$')

# Example usage
input_string = "restart"
output = replace_first_char_occurrences(input_string)
print(output)