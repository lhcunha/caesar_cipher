from alphabet import alphabet

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def cypher(text, shift):
  new_text = ""
  for letter in text:
    if letter == " ":
      new_text += " "
    elif letter not in alphabet:
      new_text += letter
    else:
      if direction == "encode":
        new_index = alphabet.index(letter) + shift
      elif direction == "decode":
        new_index = alphabet.index(letter) - shift
      else:
        print(f"{direction} is not a valid option!")
      letter = alphabet[new_index]
      new_text += letter
  print(f"The encoded text is: {new_text}")

cypher(text, shift)
