from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
want_to_continue = True

print(logo)

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    shift_amount %= len(alphabet)

    if encode_or_decode == "decode":
        shift_amount = -shift_amount

    for letter in original_text:
        if letter in alphabet:
            original_index = alphabet.index(letter)
            new_index = (original_index + shift_amount)
            output_text += alphabet[new_index]
        else:
            output_text += letter

    print(f"Here is the {encode_or_decode}d result: {output_text}")

while want_to_continue :

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    answer = input("To continue type \"yes\" and to stop type \"no\" :")
    if answer == "no":
        want_to_continue = False
        print("Goodbye")

