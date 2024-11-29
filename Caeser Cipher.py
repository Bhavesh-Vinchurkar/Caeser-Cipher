import art
print(art.logo)
import string
alphabet=list(string.ascii_lowercase)

def caeser(original_text,shift_amount,task):
    output_text=""
    if task=="decode":
                shift_amount*=-1
    for letter in original_text:
        if letter not in alphabet:
            output_text+=letter
        else:    
            shifted_position=alphabet.index(letter)+shift_amount    #else
            shifted_position%=26
            output_text+=alphabet[shifted_position]
    print(f"Here's the {task}d message : {output_text}")
    
should_continue=True
while should_continue:
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    caeser(original_text=text,shift_amount=shift,task=direction)

    restart=input("Type 'yes' if you want to go again, otherwise type 'no' :\n").lower()
    if restart=="no":
        should_continue=False
        print("Goodbye")
    

#def encrypt(original_text,shift_amount):
#    cipher_text=""
#    for letter in original_text:
#        shifted_position=alphabet.index(letter)+shift_amount
#        shifted_position%=26
#        cipher_text+=alphabet[shifted_position]
#def decrypt(original_text,shift_amount):
#    output_text=""
#    for letter in original_text:
#        shifted_position=alphabet.index(letter)-shift_amount
#        shifted_position%=26
#        output_text+=alphabet[shifted_position]

