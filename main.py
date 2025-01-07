from alpha import alphabet
from logo import main_logo
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here is the {cipher_direction}d result:\n{end_text}")
print(main_logo)
should_end = False
while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("What is the shift number:\n"))
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  restart = input("Type 'yes' if you want to run again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Bye!")
    print(main_logo)
    