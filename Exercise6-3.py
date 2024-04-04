#3.Caeser's Cipher

def rotate_word(word, shift):
  result = ""
  for char in word:
    if char.isalpha():
      # Check uppercase or lowercase
      is_uppercase = char.isupper()
      base = ord('A') if is_uppercase else ord('a')
      # Rotate the character
      new_char = chr((ord(char) - base + shift) % 26 + base)
      result += new_char
    else:
      # Keep non-alphabetic characters
      result += char
  return result

original_word = input("Enter original word :")
shift_amount = int(input("Enter the shift amount :"))
encrypted_word = rotate_word(original_word, shift_amount)
print(f"Original word: {original_word}")
print(f"Encrypted word: {encrypted_word}")